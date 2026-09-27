# MVP - Pipeline de Análise de Risco de Crédito na Nuvem

## 1. Contexto de Negócios e Perguntas (Etapa 2 e 4.1)

### Contexto do Problema
Uma instituição financeira necessita aprimorar seu processo de concessão de crédito para minimizar a taxa de inadimplência sem comprometer a aprovação de bons clientes. O objetivo deste projeto é construir um pipeline de dados de ponta a ponta na nuvem para analisar os fatores socioeconômicos e comportamentais de solicitantes de empréstimo, identificando padrões associados ao risco de não pagamento.

### Fonte dos Dados e Licença
- **Dataset:** Loan Approval Dataset
- **Origem:** Kaggle (`amineipad/loan-approval-dataset`)
- **Licença:** CC0: Public Domain (Uso acadêmico e comercial livre)
- **Resumo da Estrutura:** Arquivo tabular (CSV) contendo atributos demográficos e financeiros dos clientes (como idade, renda anual, tempo de emprego, valor do empréstimo, taxa de juros, histórico de crédito, pontuação de crédito/Score) e o status final do empréstimo (`loan_status`).

### Perguntas de Negócio
1. Qual é a relação entre o comprometimento de renda (valor do empréstimo/renda anual) e o status de inadimplência do cliente?
2. Clientes com menor histórico de crédito ou menores pontuações de Score apresentam uma taxa proporcionalmente maior de não pagamento?
3. Existe uma combinação crítica entre a intenção/motivo do empréstimo (ex: pessoal, educação, consolidação de dívidas) e a taxa de juros aplicada que resulta em maior risco de inadimplência?

---

## 2. Carga dos Dados (Etapa 4.2)

### Descrição da Carga
A ingestão dos dados brutos foi realizada via código Python dentro do ambiente **Databricks Free Edition**, utilizando a biblioteca `kagglehub` para baixar os arquivos originais do Kaggle e persisti-los na camada de volumes do **Unity Catalog** (`/Volumes/meu_catalogo/default/raw_loans/`).

**Código de Ingestão Utilizado:**
```python
import kagglehub

# Download da última versão do dataset
path = kagglehub.dataset_download("amineipad/loan-approval-dataset")

print("Path to dataset files:", path)

# Movendo/Salvando os arquivos para o Volume do Unity Catalog no Databricks
dbutils.fs.cp(f"file:{path}/loan_approval_dataset.csv", "/Volumes/meu_catalogo/default/raw_loans/loan_approval.csv")
