import streamlit as st
import pandas as pd
import plotly.express as px
car_data = pd.read_csv('C:\Users\Alfredo Díaz J\Desktop\proyecto_final_sprin_7\proyecto_sprint_7\vehicles_us.csv')
hist_button = st.button('Construir histograma')
if hist_button:
    st.write(
        'Creacion de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    st.write('Construir un histograma para la columna odómetro')
