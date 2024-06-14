import pandas as pd  
import matplotlib.pyplot as plt
import streamlit as st
import ipeadatapy as ip

st.set_page_config(
    
page_title="Receita Mensal de 5 projetos", 
) 

st.header("Dados")

arquivo = "https://github.com/joseagnaldo26/Prova4/blob/main/projetos-1.csv" 
dfe = pd.read_csv(arquivo, sep=';') 
st.dataframe(dfe.head(23))

df1 = pd.DataFrame({'mes': [12], 'ano': [2023], 'Projeto1': [29376], 'Projeto2': [40392], 'Projeto3': [63648], 'Projeto4': [29376], 'Projeto5': [25704] })
df = pd.concat([df, df1])
print(df.tail())

colunas = ['Projeto1', 'Projeto2', 'Projeto3', 'Projeto4', 'Projeto5']
df.groupby('ano')[colunas].sum()

fig, ax = plt.subplots()
df.plot( ax=ax)
st.pyplot(fig)

fig, ax = plt.subplots()
df.plot["Projeto1"].plot(kind = 'hist')
df.plot["Projeto4"].plot(kind = 'hist')
st.pyplot(fig)

ip.list_series('Selic')

selic = ip.timeseries('BM12_TJOVER12', yearGreaterThan=2021, yearSmallerThan=2024)
selic

fig, ax = plt.subplots()
ip.timeseries('BM12_TJOVER12', year=2021).plot("MONTH", "VALUE ((% a.m.))")
ip.timeseries('BM12_TJOVER12', year=2022).plot("MONTH", "VALUE ((% a.m.))")
st.pyplot(fig)
