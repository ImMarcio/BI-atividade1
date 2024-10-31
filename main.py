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


# 5. Quais são os principais clientes (vendas $) do segmento “Calçados Masculinos” (Men ́s Footwear) na Alemanha?

def calcular_principais_clientes_calcados_alemanha(vendas_globais):

    print(vendas_globais['CategoriaNome'].unique())
    print(vendas_globais['ClientePaís'].unique())
    print("\nPrincipais clientes (vendas $) do segmento 'Calçados Masculinos' na Alemanha:")
    filtros = (vendas_globais['CategoriaNome'] == "Men´s Footwear") & (vendas_globais['ClientePaís'] == 'Germany')
    top_clientes = vendas_globais[filtros].groupby('ClienteNome')['Vendas'].sum().nlargest(10).reset_index()
    
    top_clientes_console = top_clientes.copy()
    top_clientes_console['Vendas'] = top_clientes_console['Vendas'].apply(lambda x: f'R$ {x:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))
    print(top_clientes_console)

    ax5 = plt.subplot(3, 3, 5)
    ax5.bar(top_clientes["ClienteNome"], top_clientes["Vendas"], color='lightblue')
    ax5.set_xlabel('Cliente')
    ax5.set_ylabel('Vendas (R$)')
    ax5.set_title("Principais Clientes de 'Calçados Masculinos' na Alemanha")
    ax5.tick_params(axis='x', rotation=45)


# 6. Quais os vendedores que mais dão descontos nos Estados Unidos?

def calcular_vendedores_top_descontos_usa(vendas_globais, vendedores):
    print("\nVendedores que mais dão descontos nos Estados Unidos:")
    descontos_usa = vendas_globais[vendas_globais['ClientePaís'] == 'USA']
    top_vendedores = descontos_usa.groupby('VendedorID')['Desconto'].sum().nlargest(10).reset_index()
    
    resultado = pd.merge(top_vendedores, vendedores, on="VendedorID")
    resultado.rename(columns={"VendedorNome": "Vendedor", "Desconto": "Total Desconto"}, inplace=True)
    
    resultado_console = resultado.copy()
    resultado_console['Total Desconto'] = resultado_console['Total Desconto'].apply(lambda x: f'R$ {x:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))
    print(resultado_console[["Vendedor", "Total Desconto"]])

    ax6 = plt.subplot(3, 3, 6)
    ax6.bar(resultado["Vendedor"], resultado["Total Desconto"], color='lightgreen')
    ax6.set_xlabel('Vendedor')
    ax6.set_ylabel('Total Desconto (R$)')
    ax6.set_title("Top Vendedores em Descontos nos EUA")
    ax6.tick_params(axis='x', rotation=45)


# 7. Quais os fornecedores que dão a maior margem de lucro ($) no segmento de “Vestuário Feminino” (Womens wear)?

def calcular_fornecedores_top_margem_lucro_vestuario(vendas_globais, fornecedores):
    print("\nFornecedores que dão a maior margem de lucro ($) no segmento 'Vestuário Feminino':")
    filtros = (vendas_globais['CategoriaNome'] == "Womens wear")
    top_fornecedores = vendas_globais[filtros].groupby('FornecedorID')['Margem Bruta'].sum().nlargest(10).reset_index()
    
    resultado = pd.merge(top_fornecedores, fornecedores, on="FornecedorID")
    resultado.rename(columns={"FornecedorNome": "Fornecedor", "Margem Bruta": "Margem Lucro Total"}, inplace=True)
    
    resultado_console = resultado.copy()
    resultado_console['Margem Lucro Total'] = resultado_console['Margem Lucro Total'].apply(lambda x: f'R$ {x:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))
    print(resultado_console[["Fornecedor", "Margem Lucro Total"]])

    ax7 = plt.subplot(3, 3, 7)
    ax7.bar(resultado["Fornecedor"], resultado["Margem Lucro Total"], color='lightcoral')
    ax7.set_xlabel('Fornecedor')
    ax7.set_ylabel('Margem Lucro Total (R$)')
    ax7.set_title("Top Fornecedores em Margem de Lucro no Vestuário Feminino")
    ax7.tick_params(axis='x', rotation=45)




plt.figure(figsize=(14, 6))

top_10_clientes(vendas_globais)
top_paises(vendas_globais)
categorias_maior_faturamento_brasil(vendas_globais)
calcular_despesa_frete_transportadora(vendas_globais, transportadoras)
calcular_principais_clientes_calcados_alemanha(vendas_globais)
calcular_vendedores_top_descontos_usa(vendas_globais, vendedores)
calcular_fornecedores_top_margem_lucro_vestuario(vendas_globais, fornecedores)


plt.tight_layout()
plt.show()