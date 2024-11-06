# EXEMPLO 3

# Conectando no Python
from sqlalchemy import create_engine
import pandas as pd

host = "localhost"
user = "root"
password = "root"
database = "bd_vendas"
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")

# carregar dados da tabela "tb_clientes" do banco bd_vendas MYSQL
query_clientes = "SELECT id_cliente, nome, email FROM tb_clientes"
df_clientes = pd.read_sql(query_clientes,engine)

# Carregar dados da tabela "pedidos" do arquivo Excel
df_pedidos = pd.read_excel("tb_pedidos.xlsx")

print(df_clientes)

# Relacionar os dados usando merge
df_relacionado = pd.merge(df_pedidos, df_clientes, on="id_cliente", how="inner")

# Ordenar o Dataframe relacionado pela coluna "id_cliente"
df_relacionado = df_relacionado.sort_values(by="nome")

# Exibir o resultado
print(f"\n{df_relacionado}")
