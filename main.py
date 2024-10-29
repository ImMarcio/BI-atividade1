import pandas as pd


fornecedores = pd.read_csv('csvs/Fornecedores.csv')
transportadoras = pd.read_csv('csvs/Transportadoras.csv')
vendas_globais = pd.read_csv('csvs/Vendas Globais.csv')
vendedores = pd.read_csv('csvs/Vendedores.csv')

print(fornecedores.head())
print(vendedores.head())