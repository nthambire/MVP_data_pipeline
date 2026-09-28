# Databricks notebook source
# Imstalando o kaggle
%pip install kagglehub

import kagglehub

# Download latest version
path = kagglehub.dataset_download("amineipad/loan-approval-dataset")

print("Path to dataset files:", path)

# COMMAND ----------

# correção do bug acima
dbutils.library.restartPython()

# COMMAND ----------

#Carregar os dados para o Spark
import kagglehub
import os

# Baixar dataset do Kaggle
path = kagglehub.dataset_download("amineipad/loan-approval-dataset")

# Localizar o arquivo CSV baixado
files = os.listdir(path)
csv_file = [f for f in files if f.endswith('.csv')][0]
full_path = os.path.join(path, csv_file)

# Ler o CSV com pandas (acesso ao filesystem local) e converter para Spark DataFrame
import pandas as pd
pdf = pd.read_csv(full_path)
df_raw = spark.createDataFrame(pdf)

# Visualizar o resultado
display(df_raw)

# COMMAND ----------

# Célula 3: Análise de Qualidade dos Dados
from pyspark.sql.functions import col, count, when

# Contar valores nulos por coluna
df_raw.select([count(when(col(c).isNull(), c)).alias(c) for c in df_raw.columns]).show()

# Verificar quantidade total de registros
print(f"Total de registros: {df_raw.count()}")

# COMMAND ----------

# Célula 4: Limpeza e Criação de Regras de Risco
# Registrar o DataFrame como uma Tabela Temporária SQL
df_raw.createOrReplaceTempView("loan_data")

# Consulta SQL para categorizar o risco com base no Credit Score e Renda
df_gold = spark.sql("""
    SELECT 
        loan_approved,
        CASE 
            WHEN credit_score >= 750 THEN '1. Risco Baixo (Excelente Score)'
            WHEN credit_score >= 650 THEN '2. Risco Médio (Score Bom)'
            ELSE '3. Risco Alto (Score Baixo)'
        END AS faixa_risco_credito,
        COUNT(*) AS total_pedidos,
        ROUND(AVG(annual_income), 2) AS media_renda_anual,
        ROUND(AVG(loan_amount), 2) AS media_valor_emprestimo
    FROM loan_data
    GROUP BY loan_approved, faixa_risco_credito
    ORDER BY faixa_risco_credito, loan_approved
""")

display(df_gold)
