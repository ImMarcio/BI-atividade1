import pandas as pd


fornecedores = pd.read_csv('csvs/Fornecedores.csv')
transportadoras = pd.read_csv('csvs/Transportadoras.csv')
vendas_globais = pd.read_csv('csvs/Vendas Globais.csv')
vendedores = pd.read_csv('csvs/Vendedores.csv')




#Questões

#1. Quem são os meus 10 maiores clientes, em termos de vendas ($)?

top_clientes = vendas_globais.groupby('ClienteNome')['Vendas'].sum().nlargest(10)
print("\nTop 10 clientes: " )
print(top_clientes)


# 2. Quais os três maiores países, em termos de vendas ($)?

print("\nTrês maiores países " )
top_paises = vendas_globais.groupby('ClientePaís')['Vendas'].sum().nlargest(3)
print(top_paises)


# 3. Quais as categorias de produtos que geram maior faturamento (vendas $) no Brasil?

def categorias_maior_faturamento_brasil(vendas_globais):
    print("\nCategorias de produtos com maior faturamento no Brasil:")
    vendas_brasil = vendas_globais[vendas_globais["ClientePaísID"] == "BRA"]
    top_categorias_brasil = vendas_brasil.groupby("CategoriaNome")["Vendas"].sum()
    top_categorias_brasil = top_categorias_brasil.sort_values(ascending=False)
    resultado = top_categorias_brasil.reset_index()
    resultado.columns = ['Categoria', 'Faturamento']
    resultado['Faturamento'] = resultado['Faturamento'].apply(lambda x: f'R$ {x:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))
    print(resultado)


# 4. Qual a despesa com frete envolvendo cada transportadora?

def calcular_despesa_frete_transportadora(vendas_globais, transportadoras):
    print("\nDespesa com frete envolvendo cada transportadora:")
    frete_por_transportadora = vendas_globais.groupby("TransportadoraID")["Frete"].sum().reset_index()
    frete_por_transportadora.rename(columns={"Frete": "Custo Frete Total"}, inplace=True)
    resultado = pd.merge(frete_por_transportadora, transportadoras, on="TransportadoraID")
    resultado.rename(columns={"TransportadoraNome": "Transportadora"}, inplace=True)
    resultado = resultado.sort_values(by="Custo Frete Total", ascending=False)
    resultado['Custo Frete Total'] = resultado['Custo Frete Total'].apply(lambda x: f'R$ {x:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))
    print(resultado[["Transportadora", "Custo Frete Total"]])


categorias_maior_faturamento_brasil(vendas_globais)
calcular_despesa_frete_transportadora(vendas_globais, transportadoras)