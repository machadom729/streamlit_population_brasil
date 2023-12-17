import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(layout='wide')

df = pd.read_csv('brazil_population_2019.csv', sep=',')
df = df[df['region'].eq('Sudeste')].reset_index(drop=True)

estado = st.sidebar.selectbox("Estado", df['state'].unique())

df_filtrado = df[df['state'].eq(estado)]

col1, col2 = st.columns(2)
# col3, col4, col5 = st.columns(3)

df_agrupado = df.groupby(by='state', as_index=False).agg({
    'population': 'sum',
    'city': 'nunique'
})

estado_populacao = px.pie(
    df_agrupado,
    values='population',
    names='state',
    color='state',
    title='População por estado',
    labels={
        'population': 'População',
        "state": 'Estado'
    },
)
with col1:
    st.plotly_chart(estado_populacao, use_container_width=True)
    
cidade_populacao = px.bar(
    df_agrupado,
    x='state',
    y='city',
    color='state',
    title='Cidades por estado',
    labels={
        'city': 'Cidade',
        "state": 'Estado'
    },
    text_auto='.2s'
)
cidade_populacao.update_layout(showlegend=False)
# estado_populacao = px.bar(
#     df_agrupado,
#     x='state',
#     y='population',
#     color='state',
#     title='População por estado',
#     labels={
#         'population': 'População',
#         "state": 'Estado'
#     },
#     text_auto='.2s'
# )
# estado_populacao.update_layout(showlegend=False)
with col2:
    st.plotly_chart(cidade_populacao, use_container_width=True)
    
st.dataframe(data=df_filtrado, use_container_width=True)