import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from datetime import datetime

st.set_page_config(
    page_title="Clínica Jurídica-Ambiental",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    h1, h2, h3 {
        color: #667eea !important;
    }
    .stAlert {
        background-color: rgba(102, 126, 234, 0.1);
        border-left: 4px solid #667eea;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("⚖️ Clínica Jurídica-Ambiental: Calidad del Aire")
st.markdown("### Normativas y Estándares Internacionales de Calidad del Aire")

st.sidebar.title("📑 Navegación")
pagina = st.sidebar.radio(
    "Selecciona una sección:",
    ["🏠 Introducción",
     "🇵🇪 OEFA Perú",
     "🌐 OMS",
     "🇺🇸 EPA (USA)",
     "🇨🇦 Canadá",
     "📊 Comparación Normativas",
     "⏳ Línea de Tiempo",
     "📚 Recursos"]
)

datos_normativas = {
    'Contaminante': ['PM2.5', 'PM2.5', 'PM10', 'PM10', 'SO₂', 'NO₂', 'NO₂', 'O₃', 'CO'],
    'Período': ['24h', 'Anual', '24h', 'Anual', '24h', '1h', 'Anual', '8h', '8h'],
    'OEFA Perú': [50, 25, 100, 50, 250, 200, 100, 100, 10000],
    'OMS 2021': [15, 5, 45, 15, 40, 25, 10, 100, 4000],
    'EPA USA': [35, 12, 150, None, None, 100, 53, 70, 9000],
    'Canadá': [27, 8.8, 50, None, 70, 60, None, 62, 13000],
}

df_normativas = pd.DataFrame(datos_normativas)

timeline_data = [
    {"fecha": "2001-06", "evento": "Perú: D.S. N° 074-2001-PCM establece primeros ECA para aire", "entidad": "OEFA"},
    {"fecha": "2005-10", "evento": "OMS publica Guías de Calidad del Aire", "entidad": "OMS"},
    {"fecha": "2008-08", "evento": "Perú: Se crea el MINAM (Ministerio del Ambiente)", "entidad": "OEFA"},
    {"fecha": "2013-01", "evento": "EPA actualiza estándares de PM2.5 (reducción a 12 μg/m³ anual)", "entidad": "EPA"},
    {"fecha": "2017-06", "evento": "Perú: D.S. N° 003-2017-MINAM establece nuevos ECA más estrictos", "entidad": "OEFA"},
    {"fecha": "2019-12", "evento": "Perú: D.S. N° 010-2019-MINAM modifica ECA para aire", "entidad": "OEFA"},
    {"fecha": "2020-09", "evento": "EPA fortalece estándares de PM2.5", "entidad": "EPA"},
    {"fecha": "2021-09", "evento": "OMS actualiza Directrices Globales con estándares más estrictos", "entidad": "OMS"},
    {"fecha": "2022-03", "evento": "Canadá: Actualización de Objetivos de Calidad del Aire", "entidad": "Canadá"},
    {"fecha": "2023-05", "evento": "Perú: OEFA intensifica fiscalización en zonas mineras", "entidad": "OEFA"},
    {"fecha": "2024-02", "evento": "EPA propone nuevos estándares más estrictos para PM2.5", "entidad": "EPA"},
    {"fecha": "2024-08", "evento": "Perú: Implementación de nuevas estaciones de monitoreo en Lima y Arequipa", "entidad": "OEFA"},
]

timeline_df = pd.DataFrame(timeline_data)
timeline_df['fecha'] = pd.to_datetime(timeline_df['fecha'])

if pagina == "🏠 Introducción":
    st.header("🌍 Calidad del Aire: Un Derecho Fundamental")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.info("""
        **¿Por qué es importante?**
        
        La calidad del aire es esencial para la salud pública y el medio ambiente. Según la OMS, 
        la contaminación del aire causa aproximadamente **7 millones de muertes prematuras** cada año 
        en todo el mundo. Las normativas ambientales establecen límites máximos permisibles para 
        proteger la salud de la población.
        """)
    
    with col2:
        st.metric("Muertes anuales por contaminación", "7 millones", "Según OMS")
        st.metric("Población mundial afectada", "99%", "Respira aire contaminado")
    
    st.subheader("📊 Principales Contaminantes del Aire")
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["PM2.5 & PM10", "NO₂", "SO₂", "O₃", "CO", "Pb"])
    
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 🔴 Material Particulado PM2.5")
            st.markdown("""
            - **Tamaño:** ≤ 2.5 micrómetros
            - **Fuentes:** Combustión de combustibles fósiles, industria, vehículos
            - **Efectos en salud:** 
                - Penetra profundamente en los pulmones
                - Enfermedades cardiovasculares
                - Cáncer de pulmón
                - Muerte prematura
            - **Más peligroso:** Por su tamaño microscópico
            """)
        with col2:
            st.markdown("#### 🟠 Material Particulado PM10")
            st.markdown("""
            - **Tamaño:** ≤ 10 micrómetros
            - **Fuentes:** Polvo de caminos, construcción, agricultura
            - **Efectos en salud:**
                - Irritación de vías respiratorias
                - Agravamiento de asma
                - Bronquitis crónica
                - Reducción de función pulmonar
            - **Visible:** A veces como neblina o polvo
            """)
    
    with tab2:
        st.markdown("#### 💨 Dióxido de Nitrógeno (NO₂)")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Fuentes principales:**
            - Tráfico vehicular (principal)
            - Plantas de energía
            - Procesos industriales
            - Calefacción doméstica
            """)
        with col2:
            st.markdown("""
            **Efectos en la salud:**
            - Irritación del sistema respiratorio
            - Aumento de susceptibilidad a infecciones
            - Agravamiento del asma
            - Precursor del ozono troposférico
            """)
    
    with tab3:
        st.markdown("#### ☁️ Dióxido de Azufre (SO₂)")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Fuentes principales:**
            - Quema de carbón
            - Refinación de petróleo
            - Fundición de metales
            - Industria química
            """)
        with col2:
            st.markdown("""
            **Efectos:**
            - Causa lluvia ácida
            - Irritante respiratorio severo
            - Daño a vegetación
            - Corrosión de materiales
            """)
    
    with tab4:
        st.markdown("#### 🌤️ Ozono Troposférico (O₃)")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Características:**
            - Contaminante secundario
            - Se forma por reacción fotoquímica
            - Niveles más altos en días soleados
            - No emitido directamente
            """)
        with col2:
            st.markdown("""
            **Efectos en la salud:**
            - Daña tejido pulmonar
            - Reduce función pulmonar
            - Agrava enfermedades respiratorias
            - Afecta cultivos y ecosistemas
            """)
    
    with tab5:
        st.markdown("#### ⚠️ Monóxido de Carbono (CO)")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Características:**
            - Gas inodoro e incoloro
            - Combustión incompleta
            - Muy tóxico
            - Difícil de detectar sin instrumentos
            """)
        with col2:
            st.markdown("""
            **Efectos en la salud:**
            - Reduce oxígeno en sangre
            - Daño cardiovascular
            - Afecta sistema nervioso
            - Puede ser letal en altas concentraciones
            """)
    
    with tab6:
        st.markdown("#### 🏭 Plomo (Pb)")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Fuentes:**
            - Fundiciones de metales
            - Baterías
            - Pinturas antiguas
            - Combustibles con plomo (prohibidos en muchos países)
            """)
        with col2:
            st.markdown("""
            **Efectos en la salud:**
            - Daño neurológico permanente
            - Retraso en el desarrollo (niños)
            - Problemas de aprendizaje
            - Daño renal y cardiovascular
            """)

elif pagina == "🇵🇪 OEFA Perú":
    st.header("🇵🇪 OEFA - Organismo de Evaluación y Fiscalización Ambiental")
    
    st.info("""
    **¿Qué es la OEFA?**
    
    El Organismo de Evaluación y Fiscalización Ambiental (OEFA) es el ente rector del Sistema Nacional 
    de Evaluación y Fiscalización Ambiental en el Perú.
    """)
    
    eca_peru = pd.DataFrame({
        'Contaminante': ['PM2.5', 'PM2.5', 'PM10', 'PM10', 'SO₂', 'NO₂', 'NO₂', 'O₃', 'CO', 'CO'],
        'Período': ['24 horas', 'Anual', '24 horas', 'Anual', '24 horas', '1 hora', 'Anual', '8 horas', '8 horas', '1 hora'],
        'Valor ECA (μg/m³)': [50, 25, 100, 50, 250, 200, 100, 100, 10000, 30000],
    })
    
    st.dataframe(eca_peru, use_container_width=True)

elif pagina == "🌐 OMS":
    st.header("🌐 OMS - Organización Mundial de la Salud")
    
    oms_comp = pd.DataFrame({
        'Contaminante': ['PM2.5', 'PM2.5', 'PM10', 'PM10', 'SO₂', 'NO₂', 'NO₂', 'O₃'],
        'Período': ['24h', 'Anual', '24h', 'Anual', '24h', '24h', 'Anual', '8h'],
        'OMS 2005 (μg/m³)': [25, 10, 50, 20, 20, 25, 40, 100],
        'OMS 2021 (μg/m³)': [15, 5, 45, 15, 40, 25, 10, 100],
    })
    
    st.dataframe(oms_comp, use_container_width=True)

elif pagina == "🇺🇸 EPA (USA)":
    st.header("🇺🇸 EPA - Agencia de Protección Ambiental de Estados Unidos")
    
    epa_standards = pd.DataFrame({
        'Contaminante': ['PM2.5', 'PM2.5', 'PM10', 'O₃', 'SO₂', 'NO₂', 'CO'],
        'Período': ['24h', 'Anual', '24h', '8h', '1h', '1h', '8h'],
        'Estándar': ['35 μg/m³', '12 μg/m³', '150 μg/m³', '70 ppb', '75 ppb', '100 ppb', '9 ppm'],
    })
    
    st.dataframe(epa_standards, use_container_width=True)

elif pagina == "🇨🇦 Canadá":
    st.header("🇨🇦 Estándares Canadienses de Calidad del Aire")
    
    canada_standards = pd.DataFrame({
        'Contaminante': ['PM2.5', 'PM2.5', 'O₃', 'NO₂', 'SO₂'],
        'Período': ['24h', 'Anual', '8h', '1h', '1h'],
        'Estándar 2020 (μg/m³)': [27, 8.8, 62, 60, 70],
    })
    
    st.dataframe(canada_standards, use_container_width=True)

elif pagina == "📊 Comparación Normativas":
    st.header("📊 Comparación de Normativas Internacionales")
    st.dataframe(df_normativas, use_container_width=True)

elif pagina == "⏳ Línea de Tiempo":
    st.header("⏳ Línea de Tiempo de Cambios Normativos")
    
    fig = px.scatter(timeline_df, 
                     x='fecha', 
                     y='entidad',
                     color='entidad',
                     hover_data=['evento'],
                     title='Eventos Clave en Normativas de Calidad del Aire')
    
    st.plotly_chart(fig, use_container_width=True)

elif pagina == "📚 Recursos":
    st.header("📚 Recursos y Enlaces Oficiales")
    
    st.subheader("🇵🇪 OEFA - Perú")
    st.markdown("""
    - [Portal OEFA](https://www.oefa.gob.pe/)
    - Central telefónica: (01) 717-6000
    """)
    
    st.subheader("🌐 OMS")
    st.markdown("""
    - [Directrices OMS 2021](https://www.who.int/)
    """)

st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <h3>⚖️ Clínica Jurídica-Ambiental</h3>
    <p>© 2024 - Información basada en fuentes oficiales de OEFA, OMS, EPA y Canadá</p>
</div>
""", unsafe_allow_html=True)
