import pandas as pd
import matplotlib.pyplot as plt


fornecedores = pd.read_csv('csvs/Fornecedores.csv')
transportadoras = pd.read_csv('csvs/Transportadoras.csv')
vendas_globais = pd.read_csv('csvs/Vendas Globais.csv')
vendedores = pd.read_csv('csvs/Vendedores.csv')




#Questões

#1. Quem são os meus 10 maiores clientes, em termos de vendas ($)?

def top_10_clientes(vendas_globais):
    top_clientes = (vendas_globais.groupby('ClienteNome')['Vendas'].sum().nlargest(10).reset_index(name='Total Vendas'))
    print("\nTop 10 clientes: " )
    print(top_clientes)

    ax1 = plt.subplot(3, 3, 1)
    ax1.bar(top_clientes['ClienteNome'], top_clientes['Total Vendas'], color='lightgreen')
    ax1.set_xlabel('Cliente')
    ax1.set_ylabel('Vendas (R$)')
    ax1.set_title('Top 10 Clientes por Faturamento')
    ax1.tick_params(axis='x', rotation=45)


# 2. Quais os três maiores países, em termos de vendas ($)?

def top_paises(vendas_globais):
    print("\nTrês maiores países " )
    top_paises = (vendas_globais.groupby('ClientePaís')['Vendas'].sum().nlargest(3).reset_index(name='Total Vendas'))
    print(top_paises)

    ax2 = plt.subplot(3, 3, 2)
    ax2.bar(top_paises['ClientePaís'], top_paises['Total Vendas'], color='orange')
    ax2.set_xlabel('País')
    ax2.set_ylabel('Vendas (R$)')
    ax2.set_title('Top 3 Maiores Países em Vendas')
    ax2.tick_params(axis='x', rotation=45)


# 3. Quais as categorias de produtos que geram maior faturamento (vendas $) no Brasil?

def categorias_maior_faturamento_brasil(vendas_globais):
    print("\nCategorias de produtos com maior faturamento no Brasil:")
    vendas_brasil = vendas_globais[vendas_globais["ClientePaísID"] == "BRA"]
    top_categorias_brasil = (vendas_brasil.groupby("CategoriaNome")["Vendas"].sum().reset_index(name="Faturamento"))
    top_categorias_brasil = top_categorias_brasil.sort_values(by="Faturamento", ascending=False)
    print(top_categorias_brasil)

    ax3 = plt.subplot(3, 3, 3)
    ax3.bar(top_categorias_brasil["CategoriaNome"], top_categorias_brasil["Faturamento"], color='skyblue')
    ax3.set_xlabel('Categoria')
    ax3.set_ylabel('Faturamento (R$)')
    ax3.set_title('Faturamento por Categoria no Brasil')
    ax3.tick_params(axis='x', rotation=45)


# 4. Qual a despesa com frete envolvendo cada transportadora?

def calcular_despesa_frete_transportadora(vendas_globais, transportadoras):
    print("\nDespesa com frete envolvendo cada transportadora:")
    frete_por_transportadora = vendas_globais.groupby("TransportadoraID")["Frete"].sum().reset_index()
    frete_por_transportadora.rename(columns={"Frete": "Custo Frete Total"}, inplace=True)
    resultado = pd.merge(frete_por_transportadora, transportadoras, on="TransportadoraID")
    resultado.rename(columns={"TransportadoraNome": "Transportadora"}, inplace=True)
    resultado = resultado.sort_values(by="Custo Frete Total", ascending=False)
    
    resultado_console = resultado.copy()
    resultado_console['Custo Frete Total'] = resultado_console['Custo Frete Total'].apply(lambda x: f'R$ {x:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))
    print(resultado_console[["Transportadora", "Custo Frete Total"]])

    ax4 = plt.subplot(3, 3, 4)
    ax4.bar(resultado["Transportadora"], resultado["Custo Frete Total"], color='salmon')
    ax4.set_xlabel('Transportadora')
    ax4.set_ylabel('Custo Frete Total (R$)')
    ax4.set_title('Despesa com Frete por Transportadora')
    ax4.tick_params(axis='x', rotation=45)


plt.figure(figsize=(14, 6))

top_10_clientes(vendas_globais)
top_paises(vendas_globais)
categorias_maior_faturamento_brasil(vendas_globais)
calcular_despesa_frete_transportadora(vendas_globais, transportadoras)

plt.tight_layout()
plt.show()