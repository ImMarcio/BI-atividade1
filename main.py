import pandas as pd


fornecedores = pd.read_csv('csvs/Fornecedores.csv')
transportadoras = pd.read_csv('csvs/Transportadoras.csv')
vendas_globais = pd.read_csv('csvs/Vendas Globais.csv')
vendedores = pd.read_csv('csvs/Vendedores.csv')




#Questões

#1. Quem são os meus 10 maiores clientes, em termos de vendas ($)?

top_clientes = vendas_globais.groupby('ClienteNome')['Vendas'].sum().nlargest(10)
print("Top 10 clientes: " )
print(top_clientes)



# 2. Quais os três maiores países, em termos de vendas ($)?
print("Três maiores países " )
top_paises = vendas_globais.groupby('ClientePaís')['Vendas'].sum().nlargest(3)
print(top_paises)




# 10. Quais os países nos quais mais se tiram pedidos (qtde total de pedidos)?
total_pedidos_pais = vendas_globais['ClientePaís'].value_counts()
print(total_pedidos_pais)