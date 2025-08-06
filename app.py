import streamlit as st
import pandas as pd
import plotly.express as px
car_data = pd.read_csv(
    r'C:\Users\Alfredo Díaz J\Desktop\proyecto_final_sprin_7\proyecto_sprint_7\vehicles_us.csv')

# eliminar filas con valores NaN en 'model_year'
car_data.dropna(subset=['model_year'], inplace=True)
car_data['model_year'] = car_data['model_year'].astype(
    int)  # convertir a tipo int
st.title('Análisis de Datos de Vehículos')
st.write('Visualización de datos de vehículos usados en Estados Unidos')

# mostrar las primeras filas del DataFrame con los fabricantes extraídos
print(car_data.head(10))
filtrar_por_año = st.checkbox('Filtrar modelos del año 2015 en adelante')
if filtrar_por_año:
    filtro_año = car_data[car_data['model_year'] >= 2015]
    st.write('Carros del año 2015 en adelante')
    st.write(filtro_año)
else:
    st.write('Todos los carros')
    st.write(car_data)

st.header('Grafico de vehiculos en venta agrupados por fabricante')
fabricantes = ['bmw', 'ford', 'hyundai', 'chrysler', 'toyota', 'honda', 'kia', 'chevrolet', 'ram', 'gmc', 'jeep',
               'dodge', 'nissan', 'volkswagen', 'subaru', 'mazda', 'buick', 'cadillac', 'mitsubishi', 'acura', 'lincoln', 'infiniti']


def extraer_fabricantes(model_name):
    # convertir a minúsculas
    model_name_lower = str(model_name).lower()
    for fabricante in fabricantes:
        if fabricante in model_name_lower:
            return fabricante.capitalize()
    return 'Otro'


car_data['fabricante'] = car_data['model'].apply(
    extraer_fabricantes)  # aplicar la función para extraer fabricantes

data_bar = car_data.groupby(['fabricante', 'type']).size().reset_index(
    name='counts')  # agrupar por tipo de vehículo y contar
print(data_bar)  # mostrar el DataFrame agrupado
# crear un gráfico de barras # mostrar el gráfico de barras
fig = px.bar(data_bar, x='fabricante', y='counts',
             color='type', title='Vehiculos por fabricante')
st.plotly_chart(fig, use_container_width=True)

build_histogram = st.checkbox(
    'Construir un histograma de los odometros de los vehiculos')

if build_histogram:
    st.write('Construir un histograma para los odómetros de los vehículos')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

build_dispersion = st.checkbox(
    'Construir un gráfico de dispersión de los odometros y precios de los vehículos')
if build_dispersion:
    st.write('Construir un gráfico de dispersión para las columnas odómetro y precio')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

st.header('Histograma de las condiciones de los vehículos vs modelo')
fig2 = px.histogram(car_data, x="model_year", color="condition",
                    title='Histograma de condiciones vs modelo')
st.plotly_chart(fig2, use_container_width=True)
