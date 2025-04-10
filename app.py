import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Análisis de Anuncios de Vehículos en EE.UU.')

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: 
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Mostrar gráfico de dispersión (odómetro vs precio)')

if scatter_button:
    st.write('Creación de un gráfico de dispersión: odómetro vs precio')
    fig2 = px.scatter(car_data, x="odometer", y="price", title="Kilometraje vs Precio")
    st.plotly_chart(fig2, use_container_width=True)