import streamlit as st
import pandas as pd
import plotly.express as px
car_data = pd.read_csv(
    r'C:\Users\Alfredo Díaz J\Desktop\proyecto_final_sprin_7\proyecto_sprint_7\vehicles_us.csv')
st.header('Análisis de Datos de Vehículos')
st.write('Visualización de datos de vehículos usados en Estados Unidos')

filtrar_por_año = st.checkbox('Filtrar modelos del año 2015 en adelante')
if filtrar_por_año:
    filtro_año = car_data[car_data['model_year'] >= 2015]
    st.write('Carros del año 2015 en adelante')
    st.write(filtro_año)
else:
    st.write('Todos los carros')
    st.write(car_data)

build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    st.write('Construir un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
build_dispersion = st.checkbox('Construir un gráfico de dispersión')
if build_dispersion:
    st.write('Construir un gráfico de dispersión para las columnas odómetro y precio')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
