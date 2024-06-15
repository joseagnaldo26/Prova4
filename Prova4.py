import pandas as pd  
import matplotlib.pyplot as plt
import streamlit as st
import ipeadatapy as ip

st.set_page_config(
    
page_title="Receita Mensal de 5 projetos", 
) 

st.header("Dados")

arquivo = "https://raw.githubusercontent.com/joseagnaldo26/Prova4/main/projetos-1.csv" 
df = pd.read_csv(arquivo, sep=';') 
st.dataframe(df.head(23))

df1 = pd.DataFrame({'mes': [12], 'ano': [2023], 'Projeto1': [29376], 'Projeto2': [40392], 'Projeto3': [63648], 'Projeto4': [29376], 'Projeto5': [25704] })
df = pd.concat([df, df1])
st.dataframe(df.tail())

colunas = ['Projeto1', 'Projeto2', 'Projeto3', 'Projeto4', 'Projeto5']
df.groupby('ano')[colunas].sum()

fig, ax = plt.subplots()
df.plot(kind = 'scatter', x = 'Projeto1', y = 'Projeto2', color='darkgreen', marker='*', ax=ax)
st.pyplot(fig)

fig, ax = plt.subplots()
df["Projeto1"].plot(kind = 'hist')
df["Projeto4"].plot(kind = 'hist')
st.pyplot(fig)

ip.list_series('Selic')
