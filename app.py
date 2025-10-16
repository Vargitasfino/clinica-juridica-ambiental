import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Marco Normativo del Aire - Perú",
    page_icon="🌬️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS ULTRA PREMIUM (Tu diseño original, es excelente) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600;700;800;900&display=swap');
    
    * { font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] {display: none;}
    
    .main {
        background: linear-gradient(180deg, #0a0f1e 0%, #050810 100%);
        position: relative;
        overflow: hidden;
    }
    
    .main::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            radial-gradient(circle at 15% 20%, rgba(34, 211, 238, 0.15) 0%, transparent S45%),
            radial-gradient(circle at 85% 10%, rgba(14, 165, 233, 0.18) 0%, transparent 45%),
            radial-gradient(circle at 50% 80%, rgba(6, 182, 212, 0.12) 0%, transparent 50%);
        z-index: 0;
        animation: breathe 8s ease-in-out infinite;
    }
    
    @keyframes breathe { 0%, 100% { opacity: 1; } 50% { opacity: 0.8; } }
    @keyframes fadeInUp { from { opacity: 0; transform: translateY(50px); } to { opacity: 1; transform: translateY(0); } }
    
    .mega-header {
        text-align: center;
        padding: 60px 40px;
        background: linear-gradient(135deg, rgba(6, 182, 212, 0.08) 0%, rgba(14, 165, 233, 0.12) 50%, rgba(6, 78, 59, 0.08) 100%);
        backdrop-filter: blur(30px) saturate(200%);
        border-radius: 24px;
        margin-bottom: 40px;
        border: 1px solid rgba(34, 211, 238, 0.25);
        box-shadow: 0 30px 90px rgba(0, 0, 0, 0.9), inset 0 1px 0 rgba(34, 211, 238, 0.15), 0 0 100px rgba(6, 182, 212, 0.2);
        animation: fadeInUp 1s ease-out;
        position: relative;
        z-index: 1;
    }
    
    .mega-header h1 {
        font-size: 4em !important;
        font-weight: 900 !important;
        background: linear-gradient(135deg, #06b6d4 0%, #22d3ee 25%, #67e8f9 50%, #22d3ee 75%, #06b6d4 100%);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0 !important;
        position: relative;
        z-index: 2;
        letter-spacing: -0.03em;
        animation: shimmer 3s linear infinite;
    }
    
    @keyframes shimmer { 0% { background-position: 0% center; } 100% { background-position: 200% center; } }
    
    .mega-header .subtitle { color: #a5f3fc; font-size: 1.4em; font-weight: 700; margin-top: 20px; }
    
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, rgba(31, 41, 55, 0.9) 0%, rgba(17, 24, 39, 0.95) 100%);
        color: #06b6d4;
        border: 1.5px solid rgba(6, 182, 212, 0.3);
        border-radius: 12px;
        padding: 14px 20px;
        font-weight: 700;
        transition: all 0.3s;
        text-transform: uppercase;
        font-size: 0.9em;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%);
        color: #000;
        transform: translateY(-2px);
        box-shadow: 0 10px 30px rgba(6, 182, 212, 0.4);
    }
    
    .stButton > button:focus {
        background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%) !important;
        color: #000 !important;
        box-shadow: 0 10px 30px rgba(6, 182, 212, 0.4) !important;
    }
    
    .card {
        background: linear-gradient(135deg, rgba(17, 24, 39, 0.95) 0%, rgba(31, 41, 55, 0.9) 100%);
        backdrop-filter: blur(20px);
        padding: 30px;
        border-radius: 20px;
        border: 1px solid rgba(6, 182, 212, 0.25);
        margin: 15px 0;
        box-shadow: 0 25px 70px rgba(0, 0, 0, 0.8), inset 0 1px 0 rgba(6, 182, 212, 0.15);
        transition: all 0.4s;
        z-index: 1;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 35px 100px rgba(0, 0, 0, 0.9), 0 0 80px rgba(6, 182, 212, 0.25);
    }
    
    .card h2 {
        font-size: 1.8em;
        font-weight: 800;
        background: linear-gradient(135deg, #06b6d4 0%, #22d3ee 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0 0 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# --- CARGA DE DATOS ---
@st.cache_data
def load_data():
    # Datos de Estándares de Calidad Ambiental (ECA) para Aire en Perú - D.S. N° 003-2017-MINAM
    data_eca = {
        'Contaminante': ['Dióxido de Azufre (SO₂)', 'Dióxido de Azufre (SO₂)', 'Material Particulado (PM₁₀)', 'Material Particulado (PM₁₀)', 'Material Particulado (PM₂.₅)', 'Material Particulado (PM₂.₅)', 'Monóxido de Carbono (CO)', 'Monóxido de Carbono (CO)', 'Ozono (O₃)', 'Dióxido de Nitrógeno (NO₂)', 'Plomo (Pb)', 'Sulfuro de Hidrógeno (H₂S)'],
        'Periodo': ['24 horas', '1 hora', '24 horas', 'Anual', '24 horas', 'Anual', '8 horas', '1 hora', '8 horas', '1 hora', 'Mensual', '24 horas'],
        'Valor': [80, 250, 100, 50, 50, 25, 10000, 30000, 100, 200, 1.5, 150],
        'Unidad': ['µg/m³', 'µg/m³', 'µg/m³', 'µg/m³', 'µg/m³', 'µg/m³', 'µg/m³', 'µg/m³', 'µg/m³', 'µg/m³', 'µg/m³', 'µg/m³'],
        'Base Legal': ['D.S. N° 003-2017-MINAM'] * 12
    }
    df_eca = pd.DataFrame(data_eca)

    # Datos de las Guías de Calidad del Aire de la OMS (2021)
    data_oms = {
        'Contaminante': ['Dióxido de Azufre (SO₂)', 'Material Particulado (PM₁₀)', 'Material Particulado (PM₂.₅)', 'Material Particulado (PM₂.₅)', 'Monóxido de Carbono (CO)', 'Ozono (O₃)', 'Dióxido de Nitrógeno (NO₂)','Dióxido de Nitrógeno (NO₂)'],
        'Periodo': ['24 horas', '24 horas', '24 horas', 'Anual', '24 horas', '8 horas (pico)', '24 horas', 'Anual'],
        'Valor': [40, 45, 15, 5, 4000, 100, 25, 10],
        'Unidad': ['µg/m³', 'µg/m³', 'µg/m³', 'µg/m³', 'µg/m³', 'µg/m³', 'µg/m³', 'µg/m³'],
        'Base Legal': ['Guía OMS 2021'] * 8
    }
    df_oms = pd.DataFrame(data_oms)
    return df_eca, df_oms

df_eca, df_oms = load_data()

# --- FUNCIONES DE PÁGINA ---
def pagina_inicio():
    st.markdown("<div class='card'><h2>Bienvenido al Dashboard Interactivo</h2></div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("Esta herramienta permite explorar, comparar y entender el marco normativo que rige la calidad del aire en el Perú, contrastándolo con los estándares internacionales más exigentes.")
    with col2:
        st.warning("Navegue por las diferentes secciones utilizando los botones superiores para acceder a los Estándares de Calidad Ambiental (ECA), Límites Máximos Permisibles (LMP), y más.")
    with col3:
        st.error("Utilice los filtros en cada sección para analizar los datos de contaminantes específicos y visualizar comparativas clave.")

def pagina_eca():
    st.markdown("<div class='card'><h2>Explorador de Estándares de Calidad Ambiental (ECA)</h2></div>", unsafe_allow_html=True)
    
    contaminantes_unicos = df_eca['Contaminante'].unique()
    contaminante_seleccionado = st.selectbox(
        'Seleccione un contaminante para analizar:',
        options=contaminantes_unicos,
        index=2 # PM10 por defecto
    )

    st.markdown("---")
    
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader(f"Valores para {contaminante_seleccionado}")
        data_filtrada_eca = df_eca[df_eca['Contaminante'] == contaminante_seleccionado]
        st.dataframe(data_filtrada_eca, use_container_width=True)

        with st.expander("Ver Base Legal y Detalles"):
            st.markdown("""
            - **Decreto Supremo N° 003-2017-MINAM:** Aprueba los Estándares de Calidad Ambiental (ECA) para Aire y establece Disposiciones Complementarias.
            - **Vigencia:** Los valores presentados son los vigentes a la fecha.
            - **Finalidad:** Los ECA son el referente obligatorio para el diseño y aplicación de los instrumentos de gestión ambiental a nivel nacional. Miden la concentración de elementos en el aire en su condición de cuerpo receptor, y no sobre la fuente que los emite.
            """)
    
    with col2:
        st.subheader("Comparativa: Norma Peruana vs. Guía OMS")
        
        # Filtrar datos de OMS y ECA para el contaminante y un periodo comparable (ej. 24h)
        data_oms_comp = df_oms[(df_oms['Contaminante'] == contaminante_seleccionado) & (df_oms['Periodo'].str.contains('24 horas'))]
        data_eca_comp = df_eca[(df_eca['Contaminante'] == contaminante_seleccionado) & (df_eca['Periodo'].str.contains('24 horas'))]
        
        if not data_eca_comp.empty and not data_oms_comp.empty:
            valor_eca = data_eca_comp['Valor'].iloc[0]
            valor_oms = data_oms_comp['Valor'].iloc[0]
            
            fig = go.Figure(data=[
                go.Bar(name='ECA Perú (D.S. 003-2017)', x=['Valor Límite (24h)'], y=[valor_eca], marker_color='#06b6d4', text=f"{valor_eca} µg/m³", textposition='auto'),
                go.Bar(name='Guía OMS (2021)', x=['Valor Límite (24h)'], y=[valor_oms], marker_color='#ef4444', text=f"{valor_oms} µg/m³", textposition='auto')
            ])
            
            fig.update_layout(
                title=f'Comparativa de {contaminante_seleccionado} (24h)',
                yaxis_title='Valor (µg/m³)',
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='#e0f2fe',
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning(f"No se encontró un estándar comparable de 24 horas en la guía de la OMS para {contaminante_seleccionado} en esta base de datos.")


def pagina_en_desarrollo(titulo):
    st.markdown(f"<div class='card'><h2>{titulo}</h2></div>", unsafe_allow_html=True)
    st.info("Esta sección se encuentra actualmente en desarrollo. Próximamente encontrará aquí herramientas interactivas y datos detallados.")
    with st.expander("¿Qué contenido habrá en esta sección?"):
        if "LMP" in titulo:
            st.markdown("- Buscador de Límites Máximos Permisibles por sector industrial (Minería, Pesca, Hidrocarburos, etc.).\n- Comparativas entre los LMP de diferentes actividades.")
        elif "Protocolo" in titulo:
            st.markdown("- Guías descargables de los Protocolos Nacionales de Monitoreo de Calidad del Aire.\n- Checklists interactivos para asegurar el cumplimiento de los procedimientos.")
        elif "Internacional" in titulo:
            st.markdown("- Comparativas detalladas con normativas de la Unión Europea, EPA (EE.UU.), y otros países de la región.\n- Mapas interactivos de la calidad del aire a nivel global.")

# --- CUERPO PRINCIPAL DE LA APLICACIÓN ---

# Estado de la sesión para navegación
if 'pagina' not in st.session_state:
    st.session_state.pagina = "Inicio"

# Header
st.markdown("""
<div class='mega-header'>
    <h1>Marco Normativo de Calidad del Aire</h1>
    <p class='subtitle'>Herramienta Interactiva de Consulta | Normativas Peruanas e Internacionales</p>
</div>
""", unsafe_allow_html=True)

# Barra de Navegación
cols = st.columns(5)
botones = ["INICIO", "ECA", "LMP", "PROTOCOLO", "INTERNACIONAL"]
paginas = ["Inicio", "ECA", "LMP", "Protocolo", "Internacional"]

for col, boton, pagina in zip(cols, botones, paginas):
    with col:
        if st.button(boton, use_container_width=True):
            st.session_state.pagina = pagina

st.markdown("<br>", unsafe_allow_html=True)

# Renderizado de la página seleccionada
if st.session_state.pagina == "Inicio":
    pagina_inicio()
elif st.session_state.pagina == "ECA":
    pagina_eca()
elif st.session_state.pagina == "LMP":
    pagina_en_desarrollo("Límites Máximos Permisibles (LMP)")
elif st.session_state.pagina == "Protocolo":
    pagina_en_desarrollo("Protocolos de Monitoreo")
elif st.session_state.pagina == "Internacional":
    pagina_en_desarrollo("Normativas Internacionales")
