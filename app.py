import streamlit as st
import pandas as pd
import plotly.express as px
car_data = pd.read_csv(
    r'vehicles_us.csv')  # leer el archivo CSV
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

st.title('Comparación de Distribución de Precios')
st.write('Selecciona dos fabricantes para comparar la distribución de precios de sus vehículos.')
todos_fabricantes = sorted(car_data['fabricante'].unique())
# Seleccionar el primer fabricante con un valor predeterminado
fabricante_1 = st.selectbox(
    'Selecciona fabricante 1',
    options=todos_fabricantes,
    index=todos_fabricantes.index('chevrolet') if 'chevrolet' in todos_fabricantes else 0)
# Seleccionar el segundo fabricante con un valor predeterminado
fabricante_2 = st.selectbox(
    'Selecciona fabricante 2',
    options=todos_fabricantes,
    index=todos_fabricantes.index('ford') if 'ford' in todos_fabricantes else 0)
# checkbox para normalizar el histograma
normalizar_hist = st.checkbox('Normalizar el histograma', value=True)
# Filtrar los datos para los fabricantes seleccionados
fabricantes_filtrados = car_data[car_data['fabricante'].isin(
    [fabricante_1, fabricante_2])]
# Crear el histograma
if not fabricantes_filtrados.empty:
    histnorm_value = 'percent' if normalizar_hist else None
    fig_4 = px.histogram(
        fabricantes_filtrados,
        x='price',
        color='fabricante',
        barmode='overlay',
        nbins=25,  # Puedes ajustar el número de barras (bins)
        title=f'Distribución de precios entre {fabricante_1} y {fabricante_2}',
        histnorm=histnorm_value,
        opacity=0.7  # Añadimos opacidad para ver ambas distribuciones
    )
    if normalizar_hist:
        fig_4.update_yaxes(title_text='Porcentaje')
    else:
        fig_4.update_yaxes(title_text='Conteo')

    fig_4.update_layout(xaxis_title='Precio')

    # Mostramos el gráfico en Streamlit
    st.plotly_chart(fig_4, use_container_width=True)
else:
    st.warning('No hay datos suficientes para los fabricantes seleccionados.')
