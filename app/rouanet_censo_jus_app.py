import streamlit as st
import pandas as pd

def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

st.title('Desafio de Data Engineering')
st.markdown("""
Clique abaixo para gerar o arquivo dados_tratados.csv
""")

df_rouanet = pd.read_csv("rouanet.csv")
df_censo = pd.read_csv("censo_estado.csv")

df_rouanet_censo = df_rouanet.merge(df_censo, left_on='estado_ibge', right_on='codigo')

df_rouanet_censo['nk_estado_ibge_valor_em_reais'] = df_rouanet_censo.estado_ibge.astype(str) + df_rouanet_censo.valor_em_reais.astype(str)

df_rouanet_censo.drop_duplicates(subset=['nk_estado_ibge_valor_em_reais'], inplace=True)

df_rouanet_censo_sem_zero = df_rouanet_censo[(df_rouanet_censo["valor_em_reais"] != 0) & (df_rouanet_censo["quantidade"] != 0)]

url_estados = 'https://raw.githubusercontent.com/kelvins/Municipios-Brasileiros/main/csv/estados.csv'
df_estados = pd.read_csv(url_estados, usecols=['uf','nome'])
estados_nomes_ufs = dict(zip(df_estados['nome'], df_estados['uf']))
df_rouanet_censo_sem_zero['estado'].replace(estados_nomes_ufs, inplace=True)

df_rouanet_censo_sem_zero.to_csv('dados_tratados.csv', index=False)

csv = convert_df(df_rouanet_censo_sem_zero)

st.download_button(
    "Fazer download",
    csv,
    "dados_tratados.csv",
    "text/csv",
    key='download-csv'
    )