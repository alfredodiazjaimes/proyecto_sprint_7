import streamlit as st
import pandas as pd
import plotly.express as px
car_data = pd.read_csv(
    r'C:\Users\Alfredo Díaz J\Desktop\proyecto_final_sprin_7\proyecto_sprint_7\vehicles_us.csv')

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
