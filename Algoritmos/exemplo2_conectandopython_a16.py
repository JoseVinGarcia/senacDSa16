# EXEMPLO 1 - CONECTANDO AO PYTHON

# pip install pandas sqlalchemy pymysql

from sqlalchemy import create_engine
import pandas as pd

host = "localhost"
user = "root"
password = "root"
database = "bd_loja"

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")

# leitura dos dados da tabela de produtos
df_estoque = pd.read_sql("tb_produtos",engine)

# printando somente os 5 primeiros
print(df_estoque.head())

# calcula o valor do estoque por linha
df_estoque["TotalEstoque"] = df_estoque["QuantidadeEstoque"] * df_estoque["Valor"]

print("\n")
print(df_estoque[["NomeProduto","TotalEstoque"]])

# Calcula o valor total do estoque
print(f"\nTotal geral em estoque: R${df_estoque['TotalEstoque'].sum()}")
