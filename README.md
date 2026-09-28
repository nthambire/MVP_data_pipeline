# MVP: Pipeline de Dados de Análise de Risco de Crédito na Nuvem

## 1. Descrição do problema a ser resolvido
O objetivo deste trabalho é a construção de  um pipeline de dados na nuvem para analisar a concessão de empréstimos bancários e identificar os fatores determinantes do risco de inadimplência.

**Perguntas a serem respondidas:**
- Qual o impacto do *Credit Score* no status de aprovação do empréstimo?
- Existe relação direta entre a renda anual do cliente e a taxa de concessão?
- Como o valor solicitado se comporta em cada faixa de risco?


## 2. Definição da Base de Dados
- **Fonte:** Kaggle - [Loan Approval Prediction Dataset](https://www.kaggle.com/datasets/amineipad/loan-approval-dataset)
- **Licença de Uso:** Open Database License / Uso Acadêmico e Público.


## 3. Coleta dos Dados e adição na Nuvem
A adição dos dados foi realizada na plataforma **Databricks Community Edition**. O download do conjunto de dados foi automatizado através da biblioteca `kagglehub` e carregado em um DataFrame PySpark no ambiente de nuvem.


## 4. Análise de Qualidade dos Dados
Durante a fase de inspeção e validação do dataset:
- Verificou-se a presença e integridade dos campos estruturais.
- O esquema de tipos dos dados foi validado (`inferSchema`).
- Não foram identificadas anomalias críticas de valores nulos que inviabilizassem as análises.


## 5. Modelagem e Catálogo de Dados
Os dados foram organizados segundo um fluxo simplificado de arquitetura Medallion:
- **Bronze:** Dados brutos ingeridos diretamente do Kaggle em formato tabular. <img width="1045" height="670" alt="Screenshot 2026-09-27 at 22 41 28" src="https://github.com/user-attachments/assets/ed857c90-87ae-484a-99e3-efa7af05c708" />

- **Silver / Gold:** Tabela tratada e agregada criando faixas categorizadas de risco baseadas no score de crédito (`credit_score`).
<img width="1036" height="262" alt="Screenshot 2026-09-27 at 22 45 31" src="https://github.com/user-attachments/assets/e6b4f0ed-1eb6-407c-9767-29fe299ce330" />
<img width="1036" height="558" alt="Screenshot 2026-09-27 at 22 45 48" src="https://github.com/user-attachments/assets/983342cb-7e12-487f-9aaf-84e0604f4758" />

### Dicionário de Dados principais:
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `applicant_id` | bigint | Identificador único do cliente |
| `age` | bigint | Idade do cliente |
| `gender` | string | Gênero do cliente |
| `marital_status` | string | Estado civil do cliente |
| `annual_income` | bigint | Renda anual declarada |
| `loan_amount` | bigint | Valor total do empréstimo solicitado |
| `credit_score` | bigint | Score do cliente |
| `num_dependents` | bigint | Número de dependentes do cliente |
| `existing_loans_count` | bigint | Quantidade de empréstimos atualmente ativos |
| `employment_status` | string | Situação empregatícia do cliente |
| `loan_approved` | bigint | Status de aprovação do empréstimo |

## 6. Análise de Resultados & Discussão
1. Clientes com `credit_score` abaixo de 650 apresentam a maior risco de inadimplência.
2. Clientes com `credit_score` acima de 750 apresentam maior taxa de aprovação, indicando um grupo de maior segurança.
3. Um nível elevado de renda não garante a aprovação do empréstimo, o score tem um peso maior.


## 7. Autoavaliação
O objetivo de construir um pipeline funcional para analisar a concessão de empréstimos bancários e identificar os fatores determinantes do risco de inadimplência foi concluído de forma satisfatória.
A utilização do Databricks facilitou a integração do processamento distribuído com PySpark/SQL sem necessidade de infraestrutura local complexa. 
Como melhoria futura, pode ser implementadas rotinas automáticas para adição de dados de forma contínua para aprimoramento do pipeline e melhor acurácia nos resultados.
