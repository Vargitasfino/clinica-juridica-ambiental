import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# Configuración de página
st.set_page_config(
    page_title="Marco Normativo del Aire - Perú",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Ultra Profesional - VERSIÓN MEJORADA CON MEJOR VISIBILIDAD
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Variables de color corporativas */
    :root {
        --primary-blue: #0052CC;
        --secondary-blue: #0065FF;
        --accent-teal: #00B8D9;
        --dark-bg: #0A1929;
        --card-bg: #132F4C;
        --text-primary: #E3E8EF;
        --text-secondary: #B2BAC2;
        --success: #00C853;
        --warning: #FFB300;
        --danger: #D32F2F;
    }
    
    /* MEJORA CRÍTICA: Componentes nativos de Streamlit más visibles */
    div[data-testid="stMarkdownContainer"] > div[data-testid="stAlert"] {
        background-color: rgba(96, 165, 250, 0.3) !important;
        border: 1px solid rgba(96, 165, 250, 0.5) !important;
        border-left: 4px solid #60A5FA !important;
    }
    
    div[data-testid="stAlert"] p,
    div[data-testid="stAlert"] strong,
    div[data-testid="stAlert"] span {
        color: #FFFFFF !important;
        font-weight: 500 !important;
    }
    
    /* Background principal */
    .stApp {
        background: linear-gradient(135deg, #0A1929 0%, #132F4C 50%, #1A3A52 100%);
        background-attachment: fixed;
    }
    
    .main {
        background: transparent;
        padding-top: 0 !important;
    }
    
    .block-container {
        padding-top: 1rem !important;
    }
    
    header {
        background: transparent !important;
    }
    
    [data-testid="stHeader"] {
        background: transparent !important;
    }
    
    /* Sidebar profesional */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #132F4C 0%, #0A1929 100%);
        border-right: 1px solid rgba(255, 255, 255, 0.12);
    }
    
    [data-testid="stSidebar"] .element-container {
        padding: 0.5rem 1rem;
    }
    
    button[kind="header"],
    button[kind="headerNoPadding"],
    [data-testid="collapsedControl"] {
        background-color: rgba(255, 255, 255, 0.2) !important;
        border-radius: 8px !important;
    }
    
    button[kind="header"] svg,
    button[kind="headerNoPadding"] svg,
    [data-testid="collapsedControl"] svg {
        filter: brightness(0) invert(1) !important;
        -webkit-filter: brightness(0) invert(1) !important;
    }
    
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label {
        color: #FFFFFF !important;
        text-shadow: 0 2px 4px rgba(0,0,0,0.5);
    }
    
    [data-testid="stSidebar"] input {
        background: rgba(255, 255, 255, 0.15) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
    }
    
    [data-testid="stSidebar"] input::placeholder {
        color: rgba(255, 255, 255, 0.7) !important;
    }
    /* Header institucional */
    .institutional-header {
        background: linear-gradient(135deg, rgba(0, 82, 204, 0.95) 0%, rgba(0, 101, 255, 0.9) 100%);
        backdrop-filter: blur(20px) saturate(180%);
        padding: 2rem 3rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 20px 60px rgba(0, 82, 204, 0.3), 0 0 0 1px rgba(255, 255, 255, 0.05) inset;
        position: relative;
        overflow: hidden;
    }
    
    .institutional-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.6), transparent);
    }
    
    .institutional-header h1 {
        font-size: 2.5rem;
        font-weight: 800;
        color: white !important;
        margin: 0 0 0.5rem 0;
        letter-spacing: -0.02em;
        line-height: 1.2;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    
    .institutional-header .subtitle {
        font-size: 1.1rem;
        color: rgba(255, 255, 255, 0.95) !important;
        font-weight: 500;
        margin: 0.5rem 0;
        text-shadow: 0 1px 2px rgba(0,0,0,0.2);
    }
    
    .institutional-header .metadata {
        font-size: 0.9rem;
        color: rgba(255, 255, 255, 0.85) !important;
        margin-top: 1rem;
        padding-top: 1rem;
        border-top: 1px solid rgba(255, 255, 255, 0.15);
        text-shadow: 0 1px 2px rgba(0,0,0,0.2);
    }
    
    .breadcrumb {
        background: rgba(19, 47, 76, 0.8);
        backdrop-filter: blur(10px);
        padding: 0.75rem 1.5rem;
        border-radius: 8px;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        font-size: 0.9rem;
        color: rgba(255, 255, 255, 0.95) !important;
    }
    
    .breadcrumb a {
        color: #60A5FA !important;
        text-decoration: none;
        transition: color 0.2s;
        font-weight: 600;
    }
    
    .breadcrumb a:hover {
        color: #00B8D9 !important;
    }
    
    .breadcrumb-separator {
        margin: 0 0.5rem;
        color: rgba(255, 255, 255, 0.5);
    }
    
    .corporate-card {
        background: linear-gradient(135deg, rgba(19, 47, 76, 0.85) 0%, rgba(26, 58, 82, 0.75) 100%);
        backdrop-filter: blur(20px) saturate(180%);
        padding: 2rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3), 0 0 0 1px rgba(255, 255, 255, 0.03) inset;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
    }
    
    .corporate-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, var(--primary-blue), var(--accent-teal));
        border-radius: 12px 12px 0 0;
        opacity: 0;
        transition: opacity 0.3s;
    }
    
    .corporate-card:hover {
        transform: translateY(-4px);
        border-color: rgba(0, 101, 255, 0.3);
        box-shadow: 0 16px 48px rgba(0, 82, 204, 0.25), 0 0 0 1px rgba(255, 255, 255, 0.05) inset;
    }
    
    .corporate-card:hover::before {
        opacity: 1;
    }
    
    .corporate-card h2, .corporate-card h3 {
        color: white !important;
        font-weight: 700;
        margin-top: 0;
        letter-spacing: -0.01em;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    
    .corporate-card h2 {
        font-size: 1.75rem;
        margin-bottom: 1rem;
    }
    
    .corporate-card h3 {
        font-size: 1.4rem;
        margin-bottom: 0.75rem;
    }
    
    .corporate-card h4 {
        color: white !important;
        font-weight: 600;
        font-size: 1.2rem;
        margin-top: 1rem;
        text-shadow: 0 1px 2px rgba(0,0,0,0.2);
    }
    
    .corporate-card p, .corporate-card li {
        color: var(--text-secondary);
        line-height: 1.7;
        font-size: 1rem;
    }
    .normative-card {
        background: linear-gradient(135deg, rgba(19, 47, 76, 0.9) 0%, rgba(26, 58, 82, 0.85) 100%);
        backdrop-filter: blur(20px) saturate(180%);
        padding: 2rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        border-left: 4px solid var(--primary-blue);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .normative-card::after {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 100px;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0, 101, 255, 0.05));
        pointer-events: none;
    }
    
    .normative-card:hover {
        transform: translateX(8px);
        border-left-color: var(--accent-teal);
        box-shadow: 0 16px 48px rgba(0, 82, 204, 0.3);
    }
    
    .normative-card.vigente {
        border-left-color: var(--success);
    }
    
    .normative-card.modificatoria {
        border-left-color: var(--warning);
    }
    
    .normative-card.referencia {
        border-left-color: var(--text-secondary);
    }
    
    .normative-card h3 {
        color: white !important;
        font-weight: 700;
        font-size: 1.35rem;
        margin: 0 0 1rem 0;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    
    .normative-card p {
        color: rgba(255, 255, 255, 0.95) !important;
        line-height: 1.7;
        margin: 0.75rem 0;
    }
    
    .normative-card strong {
        color: white !important;
        font-weight: 600;
    }
    
    .status-badge {
        display: inline-flex;
        align-items: center;
        padding: 0.4rem 1rem;
        border-radius: 6px;
        font-size: 0.8rem;
        font-weight: 600;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }
    
    .status-badge.vigente {
        background: linear-gradient(135deg, var(--success) 0%, #00E676 100%);
        color: white;
    }
    
    .status-badge.modificatoria {
        background: linear-gradient(135deg, var(--warning) 0%, #FFC107 100%);
        color: #000;
    }
    
    .status-badge.referencia {
        background: linear-gradient(135deg, #546E7A 0%, #78909C 100%);
        color: white;
    }
    
    .status-badge.internacional {
        background: linear-gradient(135deg, var(--accent-teal) 0%, #26C6DA 100%);
        color: white;
    }
    
    .status-badge.ntp {
        background: linear-gradient(135deg, #FF6F00 0%, #FF9
        800 100%);
        color: white;
    }
    
    .corporate-button {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.875rem 1.75rem;
        background: linear-gradient(135deg, var(--primary-blue) 0%, var(--secondary-blue) 100%);
        color: white;
        text-decoration: none;
        border-radius: 8px;
        font-weight: 600;
        font-size: 0.95rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 4px 12px rgba(0, 82, 204, 0.3);
        margin: 0.5rem 0.5rem 0.5rem 0;
    }
    
    .corporate-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(0, 82, 204, 0.4);
        background: linear-gradient(135deg, var(--secondary-blue) 0%, var(--accent-teal) 100%);
    }
    
    .dataframe {
        background: rgba(19, 47, 76, 0.6) !important;
        backdrop-filter: blur(10px);
        border-radius: 12px !important;
        overflow: hidden !important;
        border: 1px solid rgba(255, 255, 255, 0.06) !important;
    }
    
    .dataframe thead tr th {
        background: linear-gradient(135deg, var(--primary-blue) 0%, var(--secondary-blue) 100%) !important;
        color: white !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        font-size: 0.85rem !important;
        letter-spacing: 0.05em !important;
        padding: 1rem !important;
        border: none !important;
    }
    
    .dataframe tbody tr {
        border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important;
        transition: background 0.2s !important;
    }
    
    .dataframe tbody tr:hover {
        background: rgba(0, 101, 255, 0.08) !important;
    }
    
    .dataframe tbody tr td {
        color: var(--text-secondary) !important;
        padding: 0.875rem 1rem !important;
        border: none !important;
    }
    
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, rgba(0, 82, 204, 0.15) 0%, rgba(0, 101, 255, 0.15) 100%);
        backdrop-filter: blur(10px);
        color: var(--text-primary);
        border: 1px solid rgba(0, 101, 255, 0.3);
        border-radius: 8px;
        padding: 0.75rem 1.25rem;
        font-weight: 600;
        font-size: 0.95rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, rgba(0, 82, 204, 0.3) 0%, rgba(0, 101, 255, 0.3) 100%);
        border-color: var(--secondary-blue);
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(0, 82, 204, 0.3);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        background: rgba(19, 47, 76, 0.6);
        backdrop-filter: blur(10px);
        padding: 0.5rem;
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.06);
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        color: var(--text-secondary);
        border-radius: 6px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        border: 1px solid transparent;
        transition: all 0.2s;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(0, 101, 255, 0.1);
        color: var(--text-primary);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, var(--primary-blue) 0%, var(--secondary-blue) 100%);
        color: white;
        border-color: rgba(255, 255, 255, 0.1);
        box-shadow: 0 4px 12px rgba(0, 82, 204, 0.3);
    }
    
    [data-testid="stMetricValue"] {
        font-size: 2.5rem;
        font-weight: 800;
        color: #60A5FA !important;
        letter-spacing: -0.02em;
        text-shadow: 0 2px 8px rgba(96, 165, 250, 0.4);
    }
    
    [data-testid="stMetricLabel"] {
        color: rgba(255, 255, 255, 0.95) !important;
        font-weight: 600;
        text-transform: uppercase;
        font-size: 0.85rem;
        letter-spacing: 0.05em;
    }
    
    [data-testid="stMetricDelta"] {
        color: rgba(255, 255, 255, 0.85) !important;
    }
    .streamlit-expanderHeader {
        background: rgba(19, 47, 76, 0.6);
        backdrop-filter: blur(10px);
        border-radius: 8px;
        border: 1px solid rgba(255, 255, 255, 0.06);
        color: var(--text-primary);
        font-weight: 600;
    }
    
    .stSelectbox > div > div,
    .stTextInput > div > div {
        background: rgba(19, 47, 76, 0.6);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 8px;
        color: var(--text-primary);
    }
    
    .warning-box {
        background: linear-gradient(135deg, rgba(255, 179, 0, 0.2) 0%, rgba(255, 152, 0, 0.15) 100%);
        border-left: 4px solid var(--warning);
        padding: 1.25rem;
        border-radius: 8px;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
    }
    
    .warning-box p {
        color: rgba(255, 255, 255, 0.95) !important;
        margin: 0;
        line-height: 1.6;
    }
    
    .warning-box strong {
        color: white !important;
    }
    
    .warning-box h4 {
        color: white !important;
        margin-top: 0;
    }
    
    .corporate-footer {
        text-align: center;
        background: linear-gradient(135deg, rgba(19, 47, 76, 0.95) 0%, rgba(10, 25, 41, 0.98) 100%);
        backdrop-filter: blur(20px);
        padding: 3rem 2rem;
        border-radius: 12px;
        margin-top: 4rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 -4px 24px rgba(0, 0, 0, 0.3);
    }
    
    .corporate-footer h2, .corporate-footer h3, .corporate-footer h4 {
        color: white !important;
        font-weight: 700;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    
    .corporate-footer p {
        color: rgba(255, 255, 255, 0.9) !important;
        margin: 0.5rem 0;
        line-height: 1.6;
    }
    
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(19, 47, 76, 0.3);
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, var(--primary-blue), var(--secondary-blue));
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, var(--secondary-blue), var(--accent-teal));
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .fade-in {
        animation: fadeInUp 0.6s ease-out;
    }
    
    @media (max-width: 768px) {
        .institutional-header h1 {
            font-size: 1.75rem;
        }
        
        .corporate-card {
            padding: 1.5rem;
        }
        
        .normative-card {
            padding: 1.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Estado de sesión
if 'pagina' not in st.session_state:
    st.session_state.pagina = "Inicio"
if 'busqueda' not in st.session_state:
    st.session_state.busqueda = ""
    # Sidebar profesional
with st.sidebar:
    st.markdown("""
    <h3 style='color: white; font-weight: 700; font-size: 1.2rem; margin-bottom: 0.25rem; margin-top: 0; text-shadow: 0 2px 4px rgba(0,0,0,0.5);'>
        🔍 NAVEGACIÓN RÁPIDA
    </h3>
    """, unsafe_allow_html=True)
    
    busqueda = st.text_input("🔎 Buscar normativa...", placeholder="Ej: PM2.5, ECA, protocolo...", key="search_input")
    
    if busqueda:
        busqueda_lower = busqueda.lower()
        
        keywords = {
            "ECA": ["eca", "estándar", "estandar", "calidad ambiental", "pm2.5", "pm10", "no2", "so2", "co", "o3", "ozono", "003-2017", "010-2019", "074-2001"],
            "LMP": ["lmp", "límite", "limite", "máximo permisible", "maximo permisible", "emisión", "emision", "termoeléctrica", "termoelectrica", "vehicular", "minería", "mineria", "003-2010", "011-2009", "010-2010"],
            "Protocolo": ["protocolo", "monitoreo", "digesa", "medición", "medicion", "muestreo", "1404-2005", "026-2000", "195-2010"],
            "Lineamiento": ["lineamiento", "inventario", "alerta", "estado de alerta", "181-2016", "009-2003", "1278"],
            "Medidas": ["medida", "control", "tecnología", "tecnologia", "filtro", "precipitador", "scrubber", "fgd", "scr", "nox", "28611"],
            "Normativas": ["internacional", "oms", "who", "epa", "usa", "canadá", "canada", "naaqs", "caaqs", "guía", "guia"]
        }
        
        mejor_match = None
        max_coincidencias = 0
        
        for pagina, palabras in keywords.items():
            coincidencias = sum(1 for palabra in palabras if palabra in busqueda_lower)
            if coincidencias > max_coincidencias:
                max_coincidencias = coincidencias
                mejor_match = pagina
        
        if mejor_match and max_coincidencias > 0:
            st.success(f"✓ Encontrado en: **{mejor_match}**")
            if st.button(f"Ir a {mejor_match}", use_container_width=True, type="primary", key="search_go"):
                st.session_state.pagina = mejor_match
                st.rerun()
        else:
            st.warning("⚠️ No se encontraron resultados. Intenta con: ECA, LMP, Protocolo, PM2.5, etc.")
    
    st.markdown("---")
    
    st.markdown("""
    <h4 style='color: white; font-weight: 700; font-size: 1rem; margin-bottom: 0.75rem; margin-top: 0.5rem; text-shadow: 0 2px 4px rgba(0,0,0,0.5);'>
        📋 SECCIONES
    </h4>
    """, unsafe_allow_html=True)
    
    if st.button("🏠 Inicio", use_container_width=True, key="nav_inicio"):
        st.session_state.pagina = "Inicio"
    
    if st.button("📋 Estándares ECA", use_container_width=True, key="nav_eca"):
        st.session_state.pagina = "ECA"
    
    if st.button("🏭 Límites LMP", use_container_width=True, key="nav_lmp"):
        st.session_state.pagina = "LMP"
    
    if st.button("📖 Protocolos", use_container_width=True, key="nav_protocolo"):
        st.session_state.pagina = "Protocolo"
    
    if st.button("📐 Lineamientos", use_container_width=True, key="nav_lineamiento"):
        st.session_state.pagina = "Lineamiento"
    
    if st.button("🛡️ Control de Emisiones", use_container_width=True, key="nav_medidas"):
        st.session_state.pagina = "Medidas"
    
    if st.button("🌍 Normativas Internacionales", use_container_width=True, key="nav_normativas"):
        st.session_state.pagina = "Normativas"
    
    st.markdown("---")
    
    st.markdown("""
    <h4 style='color: white; font-weight: 700; font-size: 1rem; margin-bottom: 0.5rem; margin-top: 0.5rem; text-shadow: 0 2px 4px rgba(0,0,0,0.5);'>
        📊 ESTADÍSTICAS
    </h4>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Normativas", "18+")
    with col2:
        st.metric("Países", "4")
    
    st.markdown("---")
    
    st.markdown("""
    <h4 style='color: white; font-weight: 700; font-size: 1rem; margin-bottom: 0.5rem; margin-top: 0.5rem; text-shadow: 0 2px 4px rgba(0,0,0,0.5);'>
        ℹ️ INFORMACIÓN
    </h4>
    """, unsafe_allow_html=True)
    
    st.info("**Última actualización:** Octubre 2024")
    
    with st.expander("📞 Contacto"):
        st.markdown("""
        <p style='color: rgba(255,255,255,0.95); line-height: 1.8;'>
        <strong style='color: white;'>Universidad Nacional de Moquegua</strong><br>
        Facultad de Ingeniería y Arquitectura<br><br>
        
        📧 contacto@unam.edu.pe<br>
        📱 +51 961 854 041
        </p>
        """, unsafe_allow_html=True)
        # Header institucional premium con secciones
st.markdown(f"""
<div class='institutional-header fade-in'>
    <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;'>
        <div>
            <h1 style='margin: 0;'>🌍 Marco Normativo de Calidad del Aire</h1>
            <p class='subtitle' style='margin: 0.5rem 0 0 0;'>Sistema Integral de Consulta de Normativas Ambientales</p>
        </div>
        <div style='text-align: right;'>
            <div style='background: rgba(255,255,255,0.15); backdrop-filter: blur(10px); padding: 0.75rem 1.5rem; border-radius: 8px; border: 1px solid rgba(255,255,255,0.2);'>
                <div style='font-size: 0.85rem; color: rgba(255,255,255,0.8); margin-bottom: 0.25rem;'>Última actualización</div>
                <div style='font-size: 1.1rem; font-weight: 700; color: white;'>{datetime.now().strftime('%d/%m/%Y')}</div>
            </div>
        </div>
    </div>
    
    <div style='display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; margin-top: 1.5rem; padding-top: 1.5rem; border-top: 1px solid rgba(255,255,255,0.2);'>
        <div style='text-align: center; padding: 1rem; background: rgba(255,255,255,0.1); border-radius: 8px; transition: all 0.3s;' 
             onmouseover="this.style.background='rgba(255,255,255,0.2)'; this.style.transform='translateY(-4px)';" 
             onmouseout="this.style.background='rgba(255,255,255,0.1)'; this.style.transform='translateY(0)';">
            <div style='font-size: 0.8rem; color: rgba(255,255,255,0.85); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.5rem;'>Normativas Nacionales</div>
            <div style='font-size: 2.5rem; font-weight: 800; color: white; line-height: 1;'>12</div>
            <div style='font-size: 0.75rem; color: rgba(255,255,255,0.7); margin-top: 0.5rem;'>↑ Vigentes</div>
        </div>
        
        <div style='text-align: center; padding: 1rem; background: rgba(255,255,255,0.1); border-radius: 8px; transition: all 0.3s;'
             onmouseover="this.style.background='rgba(255,255,255,0.2)'; this.style.transform='translateY(-4px)';" 
             onmouseout="this.style.background='rgba(255,255,255,0.1)'; this.style.transform='translateY(0)';">
            <div style='font-size: 0.8rem; color: rgba(255,255,255,0.85); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.5rem;'>Estándares Internacionales</div>
            <div style='font-size: 2.5rem; font-weight: 800; color: white; line-height: 1;'>6</div>
            <div style='font-size: 0.75rem; color: rgba(255,255,255,0.7); margin-top: 0.5rem;'>↑ OMS, EPA, Canadá</div>
        </div>
        
        <div style='text-align: center; padding: 1rem; background: rgba(255,255,255,0.1); border-radius: 8px; transition: all 0.3s;'
             onmouseover="this.style.background='rgba(255,255,255,0.2)'; this.style.transform='translateY(-4px)';" 
             onmouseout="this.style.background='rgba(255,255,255,0.1)'; this.style.transform='translateY(0)';">
            <div style='font-size: 0.8rem; color: rgba(255,255,255,0.85); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.5rem;'>Contaminantes Regulados</div>
            <div style='font-size: 2.5rem; font-weight: 800; color: white; line-height: 1;'>8</div>
            <div style='font-size: 0.75rem; color: rgba(255,255,255,0.7); margin-top: 0.5rem;'>↑ Criterio</div>
        </div>
        
        <div style='text-align: center; padding: 1rem; background: rgba(255,255,255,0.1); border-radius: 8px; transition: all 0.3s;'
             onmouseover="this.style.background='rgba(255,255,255,0.2)'; this.style.transform='translateY(-4px)';" 
             onmouseout="this.style.background='rgba(255,255,255,0.1)'; this.style.transform='translateY(0)';">
            <div style='font-size: 0.8rem; color: rgba(255,255,255,0.85); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.5rem;'>Protocolos Activos</div>
            <div style='font-size: 2.5rem; font-weight: 800; color: white; line-height: 1;'>5</div>
            <div style='font-size: 0.75rem; color: rgba(255,255,255,0.7); margin-top: 0.5rem;'>↑ Monitoreo</div>
        </div>
    </div>
    
    <div class='metadata' style='margin-top: 1.5rem; padding-top: 1.5rem; border-top: 1px solid rgba(255, 255, 255, 0.15);'>
        <div style='display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;'>
            <div>
                <strong>Universidad Nacional de Moquegua</strong> • 
                Facultad de Ingeniería y Arquitectura
            </div>
            <div>
                <strong>Prof. Dr. José Antonio Valeriano Zapana</strong>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Breadcrumb mejorado con navegación
breadcrumb_map = {
    "Inicio": "🏠 Inicio",
    "ECA": "📋 Estándares ECA",
    "LMP": "🏭 Límites LMP",
    "Protocolo": "📖 Protocolos",
    "Lineamiento": "📐 Lineamientos",
    "Medidas": "🛡️ Control de Emisiones",
    "Normativas": "🌍 Normativas Internacionales"
}

pagina_actual = breadcrumb_map.get(st.session_state.pagina, st.session_state.pagina)

st.markdown(f"""
<div class='breadcrumb fade-in' style='display: flex; justify-content: space-between; align-items: center;'>
    <div>
        <a href='#' onclick='return false;' style='font-size: 0.9rem;'>🏠 Inicio</a>
        <span class='breadcrumb-separator'>›</span>
        <span style='font-weight: 600; color: #60A5FA;'>{pagina_actual}</span>
    </div>
    <div style='display: flex; gap: 0.5rem; align-items: center;'>
        <span style='font-size: 0.85rem; color: rgba(255,255,255,0.7);'>Vista:</span>
        <div style='background: rgba(96, 165, 250, 0.15); padding: 0.25rem 0.75rem; border-radius: 6px; font-size: 0.85rem; font-weight: 600;'>
            {st.session_state.pagina}
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
# ===================== PÁGINA INICIO =====================
if st.session_state.pagina == "Inicio":
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(label="Normativas Nacionales", value="12", delta="Vigentes")
    
    with col2:
        st.metric(label="Estándares Internacionales", value="6", delta="OMS, EPA, Canadá")
    
    with col3:
        st.metric(label="Contaminantes Regulados", value="8", delta="Criterio")
    
    with col4:
        st.metric(label="Protocolos Activos", value="5", delta="Monitoreo")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class='corporate-card fade-in'>
            <h2>📚 Evolución del Marco Normativo Peruano</h2>
            <p style='font-size: 1.05rem; margin-bottom: 2rem;'>
                Recorrido histórico de las principales normativas de calidad del aire en Perú
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        timeline_data = [
            {'año': 1996, 'titulo': 'R.M. N° 315-96-EM/VMM', 'categoria': 'LMP', 'descripcion': 'Primeros límites para fundiciones y refinerías mineras', 'url': 'https://sinia.minam.gob.pe/normas/niveles-maximos-permisibles-elementos-compuestos-presentes-emisiones'},
            {'año': 2000, 'titulo': 'R.M. N° 026-2000-ITINCI/DM', 'categoria': 'Protocolo', 'descripcion': 'Protocolo de monitoreo industrial', 'url': 'https://sinia.minam.gob.pe/normas/protocolo-monitoreo-calidad-aire-emisiones-para-actividades'},
            {'año': 2001, 'titulo': 'D.S. N° 074-2001-PCM', 'categoria': 'ECA', 'descripcion': 'Primeros Estándares de Calidad Ambiental para Aire', 'url': 'https://sinia.minam.gob.pe/normas/reglamento-estandares-nacionales-calidad-ambiental-aire'},
            {'año': 2003, 'titulo': 'D.S. N° 009-2003-SA', 'categoria': 'Lineamiento', 'descripcion': 'Niveles de Estados de Alerta Nacional', 'url': 'https://sinia.minam.gob.pe/normas/reglamento-niveles-estados-alerta-nacionales-contaminantes-del-aire'},
            {'año': 2005, 'titulo': 'R.D. N° 1404-2005/DIGESA', 'categoria': 'Protocolo', 'descripcion': 'Protocolo de Monitoreo de Calidad del Aire', 'url': 'https://sinia.minam.gob.pe/documentos/protocolo-monitoreo-calidad-aire-gestion-datos'},
            {'año': 2005, 'titulo': 'Ley N° 28611', 'categoria': 'Marco Legal', 'descripcion': 'Ley General del Ambiente', 'url': 'https://www.minam.gob.pe/wp-content/uploads/2017/04/Ley-N%C2%B0-28611.pdf'},
            {'año': 2009, 'titulo': 'D.S. N° 011-2009-MINAM', 'categoria': 'LMP', 'descripcion': 'Límites para vehículos automotores', 'url': 'https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_011-2009-minam.pdf'},
            {'año': 2010, 'titulo': 'D.S. N° 003-2010-MINAM', 'categoria': 'LMP', 'descripcion': 'Límites para centrales termoeléctricas', 'url': 'https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_003-2010-minam.pdf'},
            {'año': 2010, 'titulo': 'D.S. N° 010-2010-MINAM', 'categoria': 'LMP', 'descripcion': 'Límites para industrias manufactureras', 'url': 'https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_010-2010-minam.pdf'},
            {'año': 2016, 'titulo': 'R.M. N° 181-2016-MINAM', 'categoria': 'Lineamiento', 'descripcion': 'Lineamientos para Inventario de Emisiones', 'url': 'https://www.minam.gob.pe/wp-content/uploads/2016/07/RM-N%C2%B0-181-2016-MINAM.pdf'},
            {'año': 2017, 'titulo': 'D.S. N° 003-2017-MINAM', 'categoria': 'ECA', 'descripcion': 'Actualización de Estándares de Calidad Ambiental', 'url': 'https://www.minam.gob.pe/wp-content/uploads/2017/06/DS-003-2017-MINAM.pdf'},
            {'año': 2018, 'titulo': 'Ley N° 30754', 'categoria': 'Marco Legal', 'descripcion': 'Ley Marco sobre Cambio Climático', 'url': 'https://www.minam.gob.pe/wp-content/uploads/2018/07/Ley-N%C2%B0-30754.pdf'},
            {'año': 2019, 'titulo': 'D.S. N° 010-2019-MINAM', 'categoria': 'ECA', 'descripcion': 'Modificatoria de ECA para Aire', 'url': 'https://busquedas.elperuano.pe/download/url/decreto-supremo-que-modifica-el-decreto-supremo-n-003-2017-decreto-supremo-n-010-2019-minam-1792823-1'}
        ]
        
        df_timeline = pd.DataFrame(timeline_data)
        
        # Crear figura con subplots
        fig_timeline = go.Figure()
        
        # Colores mejorados por categoría
        colores_cat = {
            'ECA': '#00E676',
            'LMP': '#FF9800',
            'Protocolo': '#BA68C8',
            'Lineamiento': '#42A5F5',
            'Marco Legal': '#EF5350'
        }
        
        # Símbolos diferentes por categoría
        simbolos_cat = {
            'ECA': 'star',
            'LMP': 'diamond',
            'Protocolo': 'hexagon',
            'Lineamiento': 'circle',
            'Marco Legal': 'square'
        }
        
        # Añadir línea de tiempo base
        fig_timeline.add_trace(go.Scatter(
            x=[1995, 2020],
            y=[0, 0],
            mode='lines',
            line=dict(color='rgba(96, 165, 250, 0.3)', width=3),
            showlegend=False,
            hoverinfo='skip'
        ))
        
        # Añadir marcadores por categoría
        categorias = df_timeline['categoria'].unique()
        
        # Calcular posiciones Y para evitar superposición
        posiciones_y = {}
        contador = {}
        
        for cat in categorias:
            contador[cat] = 0
        
        for idx, row in df_timeline.iterrows():
            cat = row['categoria']
            año = row['año']
            
            # Alternar posición vertical por categoría
            if año < 2005:
                y_pos = contador[cat] % 3 + 1
            elif año < 2012:
                y_pos = -(contador[cat] % 3 + 1)
            else:
                y_pos = contador[cat] % 3 + 1
                
            posiciones_y[idx] = y_pos
            contador[cat] += 1
            # Añadir trazas por categoría con animación
        for cat in categorias:
            df_cat = df_timeline[df_timeline['categoria'] == cat]
            
            x_vals = []
            y_vals = []
            textos = []
            urls = []
            
            for idx, row in df_cat.iterrows():
                x_vals.append(row['año'])
                y_vals.append(posiciones_y[idx])
                textos.append(f"<b>{row['año']}</b>")
                urls.append(row['url'])
            
            # Añadir líneas verticales desde la base
            for i, (x, y) in enumerate(zip(x_vals, y_vals)):
                fig_timeline.add_trace(go.Scatter(
                    x=[x, x],
                    y=[0, y],
                    mode='lines',
                    line=dict(color=colores_cat[cat], width=2, dash='dot'),
                    showlegend=False,
                    hoverinfo='skip',
                    opacity=0.6
                ))
            
            # Añadir marcadores principales con enlaces
            fig_timeline.add_trace(go.Scatter(
                x=x_vals,
                y=y_vals,
                mode='markers+text',
                name=cat,
                marker=dict(
                    size=22,
                    color=colores_cat[cat],
                    symbol=simbolos_cat[cat],
                    line=dict(color='white', width=3),
                    opacity=0.95
                ),
                text=textos,
                textposition='top center',
                textfont=dict(size=11, color='white', family='Inter', weight='bold'),
                hovertemplate='<b style="font-size:14px">%{customdata[0]}</b><br>' +
                              '<span style="font-size:12px">%{customdata[1]}</span><br>' +
                              '<i style="font-size:11px; color:#60A5FA">📄 Año: %{x}</i><br>' +
                              '<b style="font-size:11px; color:#00E676">🔗 Click para abrir documento</b><extra></extra>',
                customdata=df_cat[['titulo', 'descripcion']].values,
                customurl=urls
            ))
        
        # Layout mejorado
        fig_timeline.update_layout(
            height=600,
            showlegend=True,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#E3E8EF', size=13, family='Inter'),
            xaxis=dict(
                showgrid=True,
                gridcolor='rgba(255,255,255,0.08)',
                title=dict(text='<b>Año de Publicación</b>', font=dict(size=14)),
                dtick=2,
                range=[1994, 2021],
                tickfont=dict(size=12, weight='bold'),
                zeroline=False
            ),
            yaxis=dict(
                showgrid=False,
                showticklabels=False,
                title='',
                range=[-4, 4],
                zeroline=False
            ),
            legend=dict(
                title=dict(text='<b>Tipo de Normativa</b>', font=dict(size=14)),
                orientation="h",
                yanchor="bottom",
                y=-0.25,
                xanchor="center",
                x=0.5,
                bgcolor='rgba(19, 47, 76, 0.9)',
                bordercolor='rgba(96, 165, 250, 0.3)',
                borderwidth=2,
                font=dict(size=12)
            ),
            hovermode='closest',
            margin=dict(l=60, r=60, t=40, b=100),
            hoverlabel=dict(
                bgcolor='rgba(19, 47, 76, 0.95)',
                bordercolor='rgba(96, 165, 250, 0.5)',
                font=dict(size=12, color='white', family='Inter')
            )
        )
        
        st.plotly_chart(fig_timeline, use_container_width=True, config={'displayModeBar': False})
        
        # Añadir JavaScript para hacer los puntos clicables
        st.markdown("""
        <script>
        document.addEventListener('DOMContentLoaded', function() {
            setTimeout(function() {
                const plot = document.querySelector('.js-plotly-plot');
                if (plot) {
                    plot.on('plotly_click', function(data) {
                        const point = data.points[0];
                        if (point.customurl) {
                            window.open(point.customurl, '_blank');
                        }
                    });
                }
            }, 1000);
        });
        </script>
        """, unsafe_allow_html=True)
        
        # Mensaje informativo
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(96, 165, 250, 0.15), rgba(0, 184, 217, 0.1)); 
                    padding: 1rem 1.5rem; border-radius: 8px; border-left: 4px solid #60A5FA; margin-top: 1rem;'>
            <p style='color: rgba(255,255,255,0.95); margin: 0; font-size: 0.95rem;'>
                <strong style='color: #60A5FA;'>💡 Tip:</strong> Haz <strong>click en cualquier punto</strong> de la línea de tiempo para abrir el documento oficial completo en una nueva pestaña.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
st.markdown("""
        <div class='corporate-card' style='margin-top: 2rem;'>
            <h3 style='text-align: center; margin-bottom: 1.5rem;'>📂 Categorías del Sistema Normativo</h3>
            <p style='text-align: center; color: var(--text-secondary); margin-bottom: 2rem;'>
                Haz click en cualquier categoría para explorar las normativas
            </p>
        </div>
        """, unsafe_allow_html=True)
        
      st.markdown("""
        <div class='corporate-card' style='margin-top: 2rem;'>
            <h3 style='text-align: center; margin-bottom: 1.5rem;'>📂 Categorías del Sistema Normativo</h3>
            <p style='text-align: center; color: var(--text-secondary); margin-bottom: 2rem;'>
                Haz click en cualquier categoría para explorar las normativas
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            if st.button("📋 ECA\nEstándares de Calidad Ambiental del Aire\n\n3 Normativas", key="cat_eca", use_container_width=True):
                st.session_state.pagina = "ECA"
                st.rerun()
            
            st.markdown("""
            <style>
            button[key="cat_eca"] {
                background: linear-gradient(135deg, rgba(0, 200, 83, 0.2), rgba(0, 230, 118, 0.1)) !important;
                border: 2px solid #00C853 !important;
                border-radius: 12px !important;
                padding: 2rem 1.5rem !important;
                min-height: 180px !important;
                text-align: center !important;
                transition: all 0.3s !important;
            }
            button[key="cat_eca"]:hover {
                background: linear-gradient(135deg, rgba(0, 200, 83, 0.35), rgba(0, 230, 118, 0.2)) !important;
                transform: translateY(-8px) !important;
                box-shadow: 0 12px 32px rgba(0, 200, 83, 0.4) !important;
            }
            </style>
            """, unsafe_allow_html=True)
            
            if st.button("📖 Protocolos\nProcedimientos de Monitoreo\n\n4 Protocolos", key="cat_proto", use_container_width=True):
                st.session_state.pagina = "Protocolo"
                st.rerun()
            
            st.markdown("""
            <style>
            button[key="cat_proto"] {
                background: linear-gradient(135deg, rgba(142, 36, 170, 0.2), rgba(156, 39, 176, 0.1)) !important;
                border: 2px solid #8E24AA !important;
                border-radius: 12px !important;
                padding: 2rem 1.5rem !important;
                min-height: 180px !important;
                margin-top: 1rem !important;
                transition: all 0.3s !important;
            }
            button[key="cat_proto"]:hover {
                background: linear-gradient(135deg, rgba(142, 36, 170, 0.35), rgba(156, 39, 176, 0.2)) !important;
                transform: translateY(-8px) !important;
                box-shadow: 0 12px 32px rgba(142, 36, 170, 0.4) !important;
            }
            </style>
            """, unsafe_allow_html=True)
        
        with col_b:
            if st.button("🏭 LMP\nLímites Máximos Permisibles\n\n4 Normativas", key="cat_lmp", use_container_width=True):
                st.session_state.pagina = "LMP"
                st.rerun()
            
            st.markdown("""
            <style>
            button[key="cat_lmp"] {
                background: linear-gradient(135deg, rgba(255, 111, 0, 0.2), rgba(255, 152, 0, 0.1)) !important;
                border: 2px solid #FF6F00 !important;
                border-radius: 12px !important;
                padding: 2rem 1.5rem !important;
                min-height: 180px !important;
                transition: all 0.3s !important;
            }
            button[key="cat_lmp"]:hover {
                background: linear-gradient(135deg, rgba(255, 111, 0, 0.35), rgba(255, 152, 0, 0.2)) !important;
                transform: translateY(-8px) !important;
                box-shadow: 0 12px 32px rgba(255, 111, 0, 0.4) !important;
            }
            </style>
            """, unsafe_allow_html=True)
            
            if st.button("⚖️ Marco Legal\nLeyes y Decretos Base\n\n2 Leyes", key="cat_legal", use_container_width=True):
                st.session_state.pagina = "Medidas"
                st.rerun()
            
            st.markdown("""
            <style>
            button[key="cat_legal"] {
                background: linear-gradient(135deg, rgba(211, 47, 47, 0.2), rgba(229, 57, 53, 0.1)) !important;
                border: 2px solid #D32F2F !important;
                border-radius: 12px !important;
                padding: 2rem 1.5rem !important;
                min-height: 180px !important;
                margin-top: 1rem !important;
                transition: all 0.3s !important;
            }
            button[key="cat_legal"]:hover {
                background: linear-gradient(135deg, rgba(211, 47, 47, 0.35), rgba(229, 57, 53, 0.2)) !important;
                transform: translateY(-8px) !important;
                box-shadow: 0 12px 32px rgba(211, 47, 47, 0.4) !important;
            }
            </style>
            """, unsafe_allow_html=True)
        
        with col_c:
            if st.button("📐 Lineamientos\nGuías Técnicas\n\n3 Lineamientos", key="cat_linea", use_container_width=True):
                st.session_state.pagina = "Lineamiento"
                st.rerun()
            
            st.markdown("""
            <style>
            button[key="cat_linea"] {
                background: linear-gradient(135deg, rgba(0, 145, 234, 0.2), rgba(3, 169, 244, 0.1)) !important;
                border: 2px solid #0091EA !important;
                border-radius: 12px !important;
                padding: 2rem 1.5rem !important;
                min-height: 180px !important;
                transition: all 0.3s !important;
            }
            button[key="cat_linea"]:hover {
                background: linear-gradient(135deg, rgba(0, 145, 234, 0.35), rgba(3, 169, 244, 0.2)) !important;
                transform: translateY(-8px) !important;
                box-shadow: 0 12px 32px rgba(0, 145, 234, 0.4) !important;
            }
            </style>
            """, unsafe_allow_html=True)
            
            if st.button("🌍 Internacional\nOMS, EPA, Canadá\n\n6 Estándares", key="cat_inter", use_container_width=True):
                st.session_state.pagina = "Normativas"
                st.rerun()
            
            st.markdown("""
            <style>
            button[key="cat_inter"] {
                background: linear-gradient(135deg, rgba(0, 184, 217, 0.2), rgba(0, 188, 212, 0.1)) !important;
                border: 2px solid #00B8D9 !important;
                border-radius: 12px !important;
                padding: 2rem 1.5rem !important;
                min-height: 180px !important;
                margin-top: 1rem !important;
                transition: all 0.3s !important;
            }
            button[key="cat_inter"]:hover {
                background: linear-gradient(135deg, rgba(0, 184, 217, 0.35), rgba(0, 188, 212, 0.2)) !important;
                transform: translateY(-8px) !important;
                box-shadow: 0 12px 32px rgba(0, 184, 217, 0.4) !important;
            }
            </style>
            """, unsafe_allow_html=True)
            <style>
            button[key="cat_eca"] {
                background: linear-gradient(135deg, rgba(0, 200, 83, 0.2), rgba(0, 230, 118, 0.1)) !important;
                border: 2px solid #00C853 !important;
                border-radius: 12px !important;
                padding: 2rem 1.5rem !important;
                min-height: 180px !important;
                text-align: center !important;
                transition: all 0.3s !important;
            }
            button[key="cat_eca"]:hover {
                background: linear-gradient(135deg, rgba(0, 200, 83, 0.35), rgba(0, 230, 118, 0.2)) !important;
                transform: translateY(-8px) !important;
                box-shadow: 0 12px 32px rgba(0, 200, 83, 0.4) !important;
            }
            </style>
            """, unsafe_allow_html=True)
            
            if st.button("📖 Protocolos\nProcedimientos de Monitoreo\n\n4 Protocolos", key="cat_proto", use_container_width=True):
                st.session_state.pagina = "Protocolo"
                st.rerun()
            
            st.markdown("""
            <style>
            button[key="cat_proto"] {
                background: linear-gradient(135deg, rgba(142, 36, 170, 0.2), rgba(156, 39, 176, 0.1)) !important;
                border: 2px solid #8E24AA !important;
                border-radius: 12px !important;
                padding: 2rem 1.5rem !important;
                min-height: 180px !important;
                margin-top: 1rem !important;
                transition: all 0.3s !important;
            }
            button[key="cat_proto"]:hover {
                background: linear-gradient(135deg, rgba(142, 36, 170, 0.35), rgba(156, 39, 176, 0.2)) !important;
                transform: translateY(-8px) !important;
                box-shadow: 0 12px 32px rgba(142, 36, 170, 0.4) !important;
            }
            </style>
            """, unsafe_allow_html=True)
        
        with col_b:
            if st.button("🏭 LMP\nLímites Máximos Permisibles\n\n4 Normativas", key="cat_lmp", use_container_width=True):
                st.session_state.pagina = "LMP"
                st.rerun()
            
            st.markdown("""
            <style>
            button[key="cat_lmp"] {
                background: linear-gradient(135deg, rgba(255, 111, 0, 0.2), rgba(255, 152, 0, 0.1)) !important;
                border: 2px solid #FF6F00 !important;
                border-radius: 12px !important;
                padding: 2rem 1.5rem !important;
                min-height: 180px !important;
                transition: all 0.3s !important;
            }
            button[key="cat_lmp"]:hover {
                background: linear-gradient(135deg, rgba(255, 111, 0, 0.35), rgba(255, 152, 0, 0.2)) !important;
                transform: translateY(-8px) !important;
                box-shadow: 0 12px 32px rgba(255, 111, 0, 0.4) !important;
            }
            </style>
            """, unsafe_allow_html=True)
            
            if st.button("⚖️ Marco Legal\nLeyes y Decretos Base\n\n2 Leyes", key="cat_legal", use_container_width=True):
                st.session_state.pagina = "Medidas"
                st.rerun()
            
            st.markdown("""
            <style>
            button[key="cat_legal"] {
                background: linear-gradient(135deg, rgba(211, 47, 47, 0.2), rgba(229, 57, 53, 0.1)) !important;
                border: 2px solid #D32F2F !important;
                border-radius: 12px !important;
                padding: 2rem 1.5rem !important;
                min-height: 180px !important;
                margin-top: 1rem !important;
                transition: all 0.3s !important;
            }
            button[key="cat_legal"]:hover {
                background: linear-gradient(135deg, rgba(211, 47, 47, 0.35), rgba(229, 57, 53, 0.2)) !important;
                transform: translateY(-8px) !important;
                box-shadow: 0 12px 32px rgba(211, 47, 47, 0.4) !important;
            }
            </style>
            """, unsafe_allow_html=True)
        
        with col_c:
            if st.button("📐 Lineamientos\nGuías Técnicas\n\n3 Lineamientos", key="cat_linea", use_container_width=True):
                st.session_state.pagina = "Lineamiento"
                st.rerun()
            
            st.markdown("""
            <style>
            button[key="cat_linea"] {
                background: linear-gradient(135deg, rgba(0, 145, 234, 0.2), rgba(3, 169, 244, 0.1)) !important;
                border: 2px solid #0091EA !important;
                border-radius: 12px !important;
                padding: 2rem 1.5rem !important;
                min-height: 180px !important;
                transition: all 0.3s !important;
            }
            button[key="cat_linea"]:hover {
                background: linear-gradient(135deg, rgba(0, 145, 234, 0.35), rgba(3, 169, 244, 0.2)) !important;
                transform: translateY(-8px) !important;
                box-shadow: 0 12px 32px rgba(0, 145, 234, 0.4) !important;
            }
            </style>
            """, unsafe_allow_html=True)
            
            if st.button("🌍 Internacional\nOMS, EPA, Canadá\n\n6 Estándares", key="cat_inter", use_container_width=True):
                st.session_state.pagina = "Normativas"
                st.rerun()
            
            st.markdown("""
            <style>
            button[key="cat_inter"] {
                background: linear-gradient(135deg, rgba(0, 184, 217, 0.2), rgba(0, 188, 212, 0.1)) !important;
                border: 2px solid #00B8D9 !important;
                border-radius: 12px !important;
                padding: 2rem 1.5rem !important;
                min-height: 180px !important;
                margin-top: 1rem !important;
                transition: all 0.3s !important;
            }
            button[key="cat_inter"]:hover {
                background: linear-gradient(135deg, rgba(0, 184, 217, 0.35), rgba(0, 188, 212, 0.2)) !important;
                transform: translateY(-8px) !important;
                box-shadow: 0 12px 32px rgba(0, 184, 217, 0.4) !important;
            }
            </style>
            """, unsafe_allow_html=True)
        
        with col_a:
            if st.button("📋 ECA\nEstándares de Calidad Ambiental del Aire\n\n3 Normativas", 
                        key="cat_eca", 
                        use_container_width=True):
                st.session_state.pagina = "ECA"
                st.rerun()
            
            st.markdown("""
            <style>
            button[key="cat_eca"] {
                background: linear-gradient(135deg, rgba(0, 200, 83, 0.2), rgba(0, 230, 118, 0.1)) !important;
                border: 2px solid #00C853 !important;
                border-radius: 12px !important;
                padding: 2rem 1.5rem !important;
                min-height: 180px !important;
                text-align: center !important;
                transition: all 0.3s !important;
            }
            button[key="cat_eca"]:hover {
                background: linear-gradient(135deg, rgba(0, 200, 83, 0.35), rgba(0, 230, 118, 0.2)) !important;
                transform: translateY(-8px) !important;
                box-shadow: 0 12px 32px rgba(0, 200, 83, 0.4) !important;
            }
            </style>
            """, unsafe_allow_html=True)
            
            if st.button("📖 Protocolos\nProcedimientos de Monitoreo\n\n4 Protocolos", 
                        key="cat_proto", 
                        use_container_width=True):
                st.session_state.pagina = "Protocolo"
                st.rerun()
            
            st.markdown("""
            <style>
            button[key="cat_proto"] {
                background: linear-gradient(135deg, rgba(142, 36, 170, 0.2), rgba(156, 39, 176, 0.1)) !important;
                border: 2px solid #8E24AA !important;
                border-radius: 12px !important;
                padding: 2rem 1.5rem !important;
                min-height: 180px !important;
                margin-top: 1rem !important;
                transition: all 0.3s !important;
            }
            button[key="cat_proto"]:hover {
                background: linear-gradient(135deg, rgba(142, 36, 170, 0.35), rgba(156, 39, 176, 0.2)) !important;
                transform: translateY(-8px) !important;
                box-shadow: 0 12px 32px rgba(142, 36, 170, 0.4) !important;
            }
            </style>
            """, unsafe_allow_html=True)
            with col_b:
            if st.button("🏭 LMP\nLímites Máximos Permisibles\n\n4 Normativas", 
                        key="cat_lmp", 
                        use_container_width=True):
                st.session_state.pagina = "LMP"
                st.rerun()
            
            st.markdown("""
            <style>
            button[key="cat_lmp"] {
                background: linear-gradient(135deg, rgba(255, 111, 0, 0.2), rgba(255, 152, 0, 0.1)) !important;
                border: 2px solid #FF6F00 !important;
                border-radius: 12px !important;
                padding: 2rem 1.5rem !important;
                min-height: 180px !important;
                transition: all 0.3s !important;
            }
            button[key="cat_lmp"]:hover {
                background: linear-gradient(135deg, rgba(255, 111, 0, 0.35), rgba(255, 152, 0, 0.2)) !important;
                transform: translateY(-8px) !important;
                box-shadow: 0 12px 32px rgba(255, 111, 0, 0.4) !important;
            }
            </style>
            """, unsafe_allow_html=True)
            
            if st.button("⚖️ Marco Legal\nLeyes y Decretos Base\n\n2 Leyes", 
                        key="cat_legal", 
                        use_container_width=True):
                st.session_state.pagina = "Medidas"
                st.rerun()
            
            st.markdown("""
            <style>
            button[key="cat_legal"] {
                background: linear-gradient(135deg, rgba(211, 47, 47, 0.2), rgba(229, 57, 53, 0.1)) !important;
                border: 2px solid #D32F2F !important;
                border-radius: 12px !important;
                padding: 2rem 1.5rem !important;
                min-height: 180px !important;
                margin-top: 1rem !important;
                transition: all 0.3s !important;
            }
            button[key="cat_legal"]:hover {
                background: linear-gradient(135deg, rgba(211, 47, 47, 0.35), rgba(229, 57, 53, 0.2)) !important;
                transform: translateY(-8px) !important;
                box-shadow: 0 12px 32px rgba(211, 47, 47, 0.4) !important;
            }
            </style>
            """, unsafe_allow_html=True)
        
        with col_c:
            if st.button("📐 Lineamientos\nGuías Técnicas\n\n3 Lineamientos", 
                        key="cat_linea", 
                        use_container_width=True):
                st.session_state.pagina = "Lineamiento"
                st.rerun()
            
            st.markdown("""
            <style>
            button[key="cat_linea"] {
                background: linear-gradient(135deg, rgba(0, 145, 234, 0.2), rgba(3, 169, 244, 0.1)) !important;
                border: 2px solid #0091EA !important;
                border-radius: 12px !important;
                padding: 2rem 1.5rem !important;
                min-height: 180px !important;
                transition: all 0.3s !important;
            }
            button[key="cat_linea"]:hover {
                background: linear-gradient(135deg, rgba(0, 145, 234, 0.35), rgba(3, 169, 244, 0.2)) !important;
                transform: translateY(-8px) !important;
                box-shadow: 0 12px 32px rgba(0, 145, 234, 0.4) !important;
            }
            </style>
            """, unsafe_allow_html=True)
            
            if st.button("🌍 Internacional\nOMS, EPA, Canadá\n\n6 Estándares", 
                        key="cat_inter", 
                        use_container_width=True):
                st.session_state.pagina = "Normativas"
                st.rerun()
            
            st.markdown("""
            <style>
            button[key="cat_inter"] {
                background: linear-gradient(135deg, rgba(0, 184, 217, 0.2), rgba(0, 188, 212, 0.1)) !important;
                border: 2px solid #00B8D9 !important;
                border-radius: 12px !important;
                padding: 2rem 1.5rem !important;
                min-height: 180px !important;
                margin-top: 1rem !important;
                transition: all 0.3s !important;
            }
            button[key="cat_inter"]:hover {
                background: linear-gradient(135deg, rgba(0, 184, 217, 0.35), rgba(0, 188, 212, 0.2)) !important;
                transform: translateY(-8px) !important;
                box-shadow: 0 12px 32px rgba(0, 184, 217, 0.4) !important;
            }
            </style>
            """, unsafe_allow_html=True)
        
        st.success("""
        **✓ Beneficios del Sistema**
        
        **📄 Acceso Directo:** Enlaces actualizados a documentos oficiales
        
        **📊 Visualizaciones:** Gráficos interactivos para análisis comparativo
        
        **✅ Información Validada:** Datos técnicos verificados y referencias completas
        """)
    
    with col2:
        st.markdown("""
        <div class='corporate-card fade-in'>
            <h2>⚡ Acceso Directo</h2>
            <p style='color: rgba(255,255,255,0.95); margin-bottom: 1.5rem;'>
                Navegue rápidamente a las secciones principales
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("📋 Estándares ECA", use_container_width=True, type="primary", key="quick_eca"):
            st.session_state.pagina = "ECA"
            st.rerun()
        
        if st.button("🏭 Límites LMP", use_container_width=True, key="quick_lmp"):
            st.session_state.pagina = "LMP"
            st.rerun()
        
        if st.button("📖 Protocolos", use_container_width=True, key="quick_protocolo"):
            st.session_state.pagina = "Protocolo"
            st.rerun()
        
        if st.button("📐 Lineamientos", use_container_width=True, key="quick_lineamiento"):
            st.session_state.pagina = "Lineamiento"
            st.rerun()
        
        if st.button("🛡️ Control Emisiones", use_container_width=True, key="quick_medidas"):
            st.session_state.pagina = "Medidas"
            st.rerun()
        
        if st.button("🌍 Normativas Mundial", use_container_width=True, key="quick_normativas"):
            st.session_state.pagina = "Normativas"
            st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.info("**Sugerencia:** Utilice el buscador del menú lateral para encontrar normativas específicas.")
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>📊 Análisis Comparativo: PM2.5 Anual</h2>
        <p style='color: var(--text-secondary); margin-bottom: 1.5rem;'>
            Comparación de estándares internacionales vs. normativa peruana vigente
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    datos_comp = pd.DataFrame([
        {'Entidad': 'OMS 2021', 'Valor': 5, 'Tipo': 'Internacional'},
        {'Entidad': 'EPA USA 2024', 'Valor': 9, 'Tipo': 'Internacional'},
        {'Entidad': 'Canadá 2025', 'Valor': 8, 'Tipo': 'Internacional'},
        {'Entidad': 'OEFA Perú', 'Valor': 25, 'Tipo': 'Nacional'}
    ])
    
    fig = go.Figure()
    
    internacional = datos_comp[datos_comp['Tipo'] == 'Internacional']
    nacional = datos_comp[datos_comp['Tipo'] == 'Nacional']
    
    fig.add_trace(go.Bar(
        name='Internacional',
        x=internacional['Entidad'],
        y=internacional['Valor'],
        marker_color='#00B8D9',
        text=internacional['Valor'],
        texttemplate='%{text} μg/m³',
        textposition='outside'
    ))
    
    fig.add_trace(go.Bar(
        name='Nacional',
        x=nacional['Entidad'],
        y=nacional['Valor'],
        marker_color='#FFB300',
        text=nacional['Valor'],
        texttemplate='%{text} μg/m³',
        textposition='outside'
    ))
    
    fig.update_layout(
        height=500,
        showlegend=True,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#E3E8EF', size=13, family='Inter'),
        xaxis=dict(showgrid=False, title=''),
        yaxis=dict(
            showgrid=True, 
            gridcolor='rgba(255,255,255,0.06)',
            title='Concentración (μg/m³)',
            range=[0, 30]
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            bgcolor='rgba(19, 47, 76, 0.8)',
            bordercolor='rgba(255,255,255,0.1)',
            borderwidth=1
        ),
        margin=dict(t=40, b=60, l=60, r=40)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.warning("**⚠️ Análisis:** El estándar peruano de PM2.5 anual (25 μg/m³) es 5 veces más permisivo que la recomendación de la OMS (5 μg/m³) y 2.8 veces más alto que el estándar de EPA USA (9 μg/m³). Se recomienda evaluar una actualización gradual de los ECA nacionales para mejor protección de la salud pública.")
    # ===================== PÁGINA ECA =====================
elif st.session_state.pagina == "ECA":
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>📋 Estándares de Calidad Ambiental (ECA)</h2>
        <p style='font-size: 1.05rem;'>
            Los ECA establecen los <strong>niveles de concentración de contaminantes en el aire ambiente</strong> 
            que no deben superarse para proteger la salud de la población. Se miden en estaciones de monitoreo 
            de calidad del aire y son de cumplimiento obligatorio en todo el territorio nacional.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("**Diferencia clave:** ECA se mide en aire ambiente (lo que respiramos), mientras que LMP se mide en la fuente de emisión (chimeneas, ductos).")
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>● VIGENTE</span>
        <h3>D.S. N° 003-2017-MINAM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Estándares de Calidad Ambiental (ECA) para Aire</strong>
        </p>
        <p>
            Norma principal que establece los valores de concentración máxima de contaminantes del aire 
            que no deben superarse para proteger la salud humana y el ambiente. Incluye PM2.5, PM10, SO2, 
            NO2, O3, CO, Pb, H2S y BaP. Establece períodos de cumplimiento y métodos de referencia.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 07 de junio de 2017 | 
            <strong>Vigencia:</strong> Desde junio 2017
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2017/06/DS-003-2017-MINAM.pdf' 
           target='_blank' class='corporate-button'>
            📄 Descargar D.S. 003-2017-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card modificatoria fade-in'>
        <span class='status-badge modificatoria'>● MODIFICATORIA</span>
        <h3>D.S. N° 010-2019-MINAM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Modificatoria del D.S. N° 003-2017-MINAM</strong>
        </p>
        <p>
            Actualiza parámetros y períodos de evaluación de los ECA para aire. Modifica las formas de 
            cumplimiento de algunos estándares adaptándose a nueva evidencia científica sobre efectos en 
            la salud pública y capacidades de monitoreo nacional.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 12 de julio de 2019 | 
            <strong>Vigencia:</strong> Desde julio 2019
        </p>
        <a href='https://busquedas.elperuano.pe/download/url/decreto-supremo-que-modifica-el-decreto-supremo-n-003-2017-decreto-supremo-n-010-2019-minam-1792823-1' 
           target='_blank' class='corporate-button'>
            📄 Descargar D.S. 010-2019-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card referencia fade-in'>
        <span class='status-badge referencia'>● REFERENCIA HISTÓRICA</span>
        <h3>D.S. N° 074-2001-PCM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Reglamento de Estándares Nacionales de Calidad Ambiental del Aire (Derogado)</strong>
        </p>
        <p>
            Primera norma que estableció los ECA para aire en Perú. Estuvo vigente durante 16 años hasta 
            su reemplazo por el D.S. 003-2017-MINAM. Importante para contexto histórico y análisis de la 
            evolución normativa nacional en materia de calidad del aire.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 24 de junio de 2001 | 
            <strong>Derogación:</strong> Junio 2017
        </p>
        <a href='https://sinia.minam.gob.pe/normas/reglamento-estandares-nacionales-calidad-ambiental-aire' 
           target='_blank' class='corporate-button'>
            📄 Ver D.S. 074-2001-PCM (Histórico)
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>📊 Valores de ECA Vigentes (D.S. 003-2017-MINAM)</h2>
        <p style='color: var(--text-secondary); margin-bottom: 1.5rem;'>
            Concentraciones máximas permitidas en aire ambiente para protección de salud pública
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    eca_valores = pd.DataFrame([
        ['PM2.5', '24 horas', 50, 'μg/m³', 'No exceder más de 7 veces al año'],
        ['PM2.5', 'Anual', 25, 'μg/m³', 'Media aritmética anual'],
        ['PM10', '24 horas', 100, 'μg/m³', 'No exceder más de 7 veces al año'],
        ['PM10', 'Anual', 50, 'μg/m³', 'Media aritmética anual'],
        ['NO2', '1 hora', 200, 'μg/m³', 'No exceder más de 24 veces al año'],
        ['NO2', 'Anual', 100, 'μg/m³', 'Media aritmética anual'],
        ['SO2', '24 horas', 250, 'μg/m³', 'No exceder más de 7 veces al año'],
        ['O3', '8 horas', 100, 'μg/m³', 'Máximas diarias de promedios móviles'],
        ['CO', '8 horas', 10000, 'μg/m³', 'Promedio móvil'],
        ['CO', '1 hora', 30000, 'μg/m³', 'No exceder más de 1 vez al año'],
        ['Pb', 'Mensual', 1.5, 'μg/m³', 'Media aritmética mensual'],
        ['Pb', 'Anual', 0.5, 'μg/m³', 'Media aritmética anual'],
        ['H2S', '24 horas', 150, 'μg/m³', 'Media aritmética'],
        ['BaP', 'Anual', 0.0012, 'μg/m³', 'Media aritmética anual']
    ], columns=['Contaminante', 'Período', 'Valor', 'Unidad', 'Forma del Estándar'])
    
    st.dataframe(eca_valores, use_container_width=True, hide_index=True, height=550)
    
    with st.expander("ℹ️ Ver información adicional sobre contaminantes criterio"):
        st.markdown("""
        <div style='color: rgba(255,255,255,0.95); line-height: 1.8;'>
        
        <h4 style='color: #60A5FA; margin-top: 0; margin-bottom: 1.5rem;'>Contaminantes Criterio Regulados</h4>
        
        <p style='color: #00C853; font-weight: 700; font-size: 1.1rem; margin-top: 1.5rem; margin-bottom: 0.5rem;'>Material Particulado (PM2.5 y PM10)</p>
        <ul style='color: #FFFFFF; margin-left: 1.5rem; line-height: 1.8;'>
            <li>Partículas sólidas o líquidas suspendidas en el aire</li>
            <li>PM2.5: diámetro ≤ 2.5 μm (penetran profundamente en pulmones)</li>
            <li>PM10: diámetro ≤ 10 μm (afectan vías respiratorias superiores)</li>
            <li>Fuentes: combustión, polvo, actividades industriales</li>
        </ul>
        
        <p style='color: #00C853; font-weight: 700; font-size: 1.1rem; margin-top: 1.5rem; margin-bottom: 0.5rem;'>Dióxido de Nitrógeno (NO2)</p>
        <ul style='color: #FFFFFF; margin-left: 1.5rem; line-height: 1.8;'>
            <li>Gas irritante de color marrón rojizo</li>
            <li>Fuentes: combustión vehicular e industrial</li>
            <li>Efectos: irritación respiratoria, reducción función pulmonar</li>
        </ul>
        
        <p style='color: #00C853; font-weight: 700; font-size: 1.1rem; margin-top: 1.5rem; margin-bottom: 0.5rem;'>Dióxido de Azufre (SO2)</p>
        <ul style='color: #FFFFFF; margin-left: 1.5rem; line-height: 1.8;'>
            <li>Gas incoloro con olor penetrante</li>
            <li>Fuentes: combustión de combustibles fósiles con azufre</li>
            <li>Efectos: irritación respiratoria, enfermedades cardiovasculares</li>
        </ul>
        
        <p style='color: #00C853; font-weight: 700; font-size: 1.1rem; margin-top: 1.5rem; margin-bottom: 0.5rem;'>Ozono Troposférico (O3)</p>
        <ul style='color: #FFFFFF; margin-left: 1.5rem; line-height: 1.8;'>
            <li>Contaminante secundario (no se emite directamente)</li>
            <li>Se forma por reacción fotoquímica de NOx y COVs</li>
            <li>Efectos: daño pulmonar, reducción función respiratoria</li>
        </ul>
        
        <p style='color: #00C853; font-weight: 700; font-size: 1.1rem; margin-top: 1.5rem; margin-bottom: 0.5rem;'>Monóxido de Carbono (CO)</p>
        <ul style='color: #FFFFFF; margin-left: 1.5rem; line-height: 1.8;'>
            <li>Gas incoloro e inodoro</li>
            <li>Fuentes: combustión incompleta</li>
            <li>Efectos: reduce capacidad de transporte de oxígeno en sangre</li>
        </ul>
        
        <p style='color: #00C853; font-weight: 700; font-size: 1.1rem; margin-top: 1.5rem; margin-bottom: 0.5rem;'>Plomo (Pb)</p>
        <ul style='color: #FFFFFF; margin-left: 1.5rem; line-height: 1.8;'>
            <li>Metal pesado tóxico</li>
            <li>Fuentes: históricamente gasolina con plomo, industrias</li>
            <li>Efectos: neurotoxicidad, afecta desarrollo infantil</li>
        </ul>
        
        <p style='color: #00C853; font-weight: 700; font-size: 1.1rem; margin-top: 1.5rem; margin-bottom: 0.5rem;'>Sulfuro de Hidrógeno (H2S)</p>
        <ul style='color: #FFFFFF; margin-left: 1.5rem; line-height: 1.8;'>
            <li>Gas con olor a huevo podrido</li>
            <li>Fuentes: actividades petroleras, descomposición materia orgánica</li>
            <li>Efectos: irritación ocular y respiratoria</li>
        </ul>
        
        <p style='color: #00C853; font-weight: 700; font-size: 1.1rem; margin-top: 1.5rem; margin-bottom: 0.5rem;'>Benzo(a)pireno (BaP)</p>
        <ul style='color: #FFFFFF; margin-left: 1.5rem; line-height: 1.8;'>
            <li>Hidrocarburo aromático policíclico (HAP)</li>
            <li>Fuentes: combustión incompleta de materia orgánica</li>
            <li>Efectos: cancerígeno, mutagénico</li>
        </ul>
        
        </div>
        """, unsafe_allow_html=True)
        # ===================== PÁGINA LMP =====================
elif st.session_state.pagina == "LMP":
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>🏭 Límites Máximos Permisibles (LMP)</h2>
        <p style='font-size: 1.05rem;'>
            Los LMP son <strong>valores de concentración máxima de contaminantes</strong> que pueden 
            ser emitidos al ambiente desde una fuente puntual de emisión (chimeneas, ductos). Son 
            específicos por sector productivo y tipo de actividad, estableciendo obligaciones para 
            el cumplimiento ambiental de las empresas.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("**Diferencia clave:** Los LMP se aplican a la fuente emisora y son medidos en el punto de descarga, mientras que los ECA se miden en el aire ambiente que respira la población.")
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>● VIGENTE</span>
        <h3>D.S. N° 003-2010-MINAM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>LMP de Emisiones Atmosféricas para Centrales Termoeléctricas</strong>
        </p>
        <p>
            Establece límites de emisión de NOx, SO2 y Material Particulado para plantas de generación 
            termoeléctrica. Los límites varían según el tipo de combustible utilizado (gas natural, diesel, 
            residual). Mediciones en condiciones normalizadas: 25°C, 1 atm, base seca, 15% O2.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 17 de enero de 2010 | 
            <strong>Sector:</strong> Energía
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_003-2010-minam.pdf' 
           target='_blank' class='corporate-button'>
            📄 Descargar D.S. 003-2010-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>● VIGENTE</span>
        <h3>D.S. N° 011-2009-MINAM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>LMP de Emisiones para Vehículos Automotores</strong>
        </p>
        <p>
            Regula las emisiones de gases contaminantes de vehículos automotores que circulan por la red 
            vial. Incluye límites para CO, HC, NOx y Material Particulado según categoría vehicular 
            (ligeros, pesados) y tipo de combustible. Establece procedimientos de verificación técnica vehicular.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 13 de marzo de 2009 | 
            <strong>Sector:</strong> Transporte
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_011-2009-minam.pdf' 
           target='_blank' class='corporate-button'>
            📄 Descargar D.S. 011-2009-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>● VIGENTE</span>
        <h3>D.S. N° 010-2010-MINAM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>LMP de Emisiones para Industrias de Cemento, Papel, Cerveza y Curtiembre</strong>
        </p>
        <p>
            Establece límites de emisión atmosférica para industrias de cemento, papel, cerveza y curtiembre. 
            Regula emisiones de Material Particulado, SO2, NOx y otros contaminantes específicos según el 
            proceso industrial. Define métodos de muestreo y análisis, así como plazos de cumplimiento.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 17 de agosto de 2010 | 
            <strong>Sector:</strong> Industria Manufacturera
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_010-2010-minam.pdf' 
           target='_blank' class='corporate-button'>
            📄 Descargar D.S. 010-2010-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>● VIGENTE</span>
        <h3>R.M. N° 315-96-EM/VMM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Niveles Máximos Permisibles para Fundiciones y Refinerías</strong>
        </p>
        <p>
            Establece los niveles máximos permisibles de emisiones de gases y partículas para las actividades 
            minero-metalúrgicas de fundición y refinación. Regula emisiones de SO2, Material Particulado, 
            plomo, arsénico y otros metales pesados específicos de procesos metalúrgicos.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 19 de julio de 1996 | 
            <strong>Sector:</strong> Minería y Metalurgia
        </p>
        <a href='https://sinia.minam.gob.pe/normas/niveles-maximos-permisibles-elementos-compuestos-presentes-emisiones' 
           target='_blank' class='corporate-button'>
            📄 Ver R.M. 315-96-EM/VMM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>📊 LMP para Centrales Termoeléctricas por Tipo de Combustible</h2>
        <p style='color: var(--text-secondary); margin-bottom: 1rem;'>
            D.S. 003-2010-MINAM | Condiciones: 25°C, 1 atm, base seca, 15% O2
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    lmp_termo = pd.DataFrame([
        ['Óxidos de Nitrógeno (NOx)', 320, 850, 2000, 'mg/Nm³'],
        ['Dióxido de Azufre (SO2)', 0, 1700, 3500, 'mg/Nm³'],
        ['Material Particulado (MP)', 50, 150, 350, 'mg/Nm³']
    ], columns=['Contaminante', 'Gas Natural', 'Diesel', 'Residual', 'Unidad'])
    
    st.dataframe(lmp_termo, use_container_width=True, hide_index=True, height=200)
    
    fig_lmp = go.Figure()
    
    contaminantes = lmp_termo['Contaminante'].tolist()
    
    fig_lmp.add_trace(go.Bar(
        name='Gas Natural',
        x=contaminantes,
        y=lmp_termo['Gas Natural'],
        marker_color='#00C853',
        text=lmp_termo['Gas Natural'],
        texttemplate='%{text}',
        textposition='outside'
    ))
    
    fig_lmp.add_trace(go.Bar(
        name='Diesel',
        x=contaminantes,
        y=lmp_termo['Diesel'],
        marker_color='#FFB300',
        text=lmp_termo['Diesel'],
        texttemplate='%{text}',
        textposition='outside'
    ))
    
    fig_lmp.add_trace(go.Bar(
        name='Residual',
        x=contaminantes,
        y=lmp_termo['Residual'],
        marker_color='#D32F2F',
        text=lmp_termo['Residual'],
        texttemplate='%{text}',
        textposition='outside'
    ))
    
    fig_lmp.update_layout(
        barmode='group',
        height=500,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#E3E8EF', size=13, family='Inter'),
        xaxis=dict(showgrid=False, title=''),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(255,255,255,0.06)',
            title='Concentración (mg/Nm³)',
            type='log'
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            bgcolor='rgba(19, 47, 76, 0.8)',
            bordercolor='rgba(255,255,255,0.1)',
            borderwidth=1
        )
    )
    
    st.plotly_chart(fig_lmp, use_container_width=True)
    
    st.info("**Nota técnica:** Los límites son más estrictos para combustibles más limpios. El gas natural tiene los LMP más bajos debido a su menor contenido de azufre y mejor eficiencia de combustión, mientras que el residual (combustóleo) tiene los límites más permisivos debido a su mayor contenido de impurezas.")
    # ===================== PÁGINA PROTOCOLO =====================
elif st.session_state.pagina == "Protocolo":
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>📖 Protocolos de Monitoreo y Medición</h2>
        <p style='font-size: 1.05rem;'>
            Los protocolos establecen <strong>procedimientos técnicos estandarizados</strong> para el 
            monitoreo de calidad del aire y la medición de emisiones atmosféricas. Garantizan que las 
            mediciones sean comparables, confiables y válidas a nivel nacional, cumpliendo con estándares 
            internacionales de calidad analítica.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("**Importancia:** Los protocolos aseguran la trazabilidad, precisión y validez legal de las mediciones ambientales realizadas por laboratorios acreditados y empresas consultoras.")
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>● VIGENTE</span>
        <h3>R.D. N° 1404-2005/DIGESA/SA</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Protocolo de Monitoreo de Calidad del Aire y Gestión de Datos</strong>
        </p>
        <p>
            Define los procedimientos técnicos para el monitoreo de calidad del aire ambiente en todo el 
            territorio nacional. Incluye métodos de muestreo, ubicación de estaciones, calibración de 
            equipos, análisis de laboratorio, aseguramiento y control de calidad, y gestión de datos. 
            Aplicable a redes de monitoreo públicas y privadas.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 11 de noviembre de 2005 | 
            <strong>Entidad:</strong> DIGESA-MINSA
        </p>
        <a href='https://sinia.minam.gob.pe/documentos/protocolo-monitoreo-calidad-aire-gestion-datos' 
           target='_blank' class='corporate-button'>
            📄 Descargar Protocolo DIGESA
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>● VIGENTE</span>
        <h3>R.M. N° 026-2000-ITINCI/DM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Protocolo de Monitoreo de Calidad de Aire y Emisiones - Sector Industrial</strong>
        </p>
        <p>
            Aprueba protocolos específicos de monitoreo de calidad de aire y emisiones atmosféricas para 
            actividades industriales manufactureras. Establece metodologías de muestreo isocinético, análisis 
            de gases, y determinación de caudales en fuentes fijas industriales.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 28 de febrero de 2000 | 
            <strong>Sector:</strong> Industria - PRODUCE
        </p>
        <a href='https://sinia.minam.gob.pe/normas/protocolo-monitoreo-calidad-aire-emisiones-para-actividades' 
           target='_blank' class='corporate-button'>
            📄 Ver R.M. 026-2000-ITINCI/DM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>● VIGENTE</span>
        <h3>R.D. N° 195-2010-MEM/AAM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Protocolo de Monitoreo de Calderos y Hornos Industriales</strong>
        </p>
        <p>
            Establece procedimientos estandarizados para el monitoreo de emisiones atmosféricas en calderos 
            y hornos industriales de diversos sectores. Incluye métodos isocinéticos para material particulado, 
            análisis instrumental de gases (SO2, NOx, CO), y determinación de parámetros de proceso.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 12 de agosto de 2010 | 
            <strong>Sector:</strong> Energía y Minas
        </p>
        <a href='https://sinia.minam.gob.pe/normas/aprueban-lineamientos-emision-opiniones-tecnicas-protocolos' 
           target='_blank' class='corporate-button'>
            📄 Ver Legislación MINEM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>● VIGENTE</span>
        <h3>R.M. N° 247-2009-MEM/DM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Protocolo de Monitoreo de Calidad de Agua y Aire - Minería</strong>
        </p>
        <p>
            Protocolo específico para actividades minero-metalúrgicas que establece procedimientos de monitoreo 
            de calidad de aire en zonas de influencia minera. Define ubicación de estaciones, frecuencias de 
            muestreo, parámetros a evaluar y procedimientos de reporte ante autoridades sectoriales.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 14 de mayo de 2009 | 
            <strong>Sector:</strong> Minería
        </p>
        <a href='https://sinia.minam.gob.pe/normas/protocolo-monitoreo-calidad-agua-aire-subsector-mineria' 
           target='_blank' class='corporate-button'>
            📄 Ver R.M. 247-2009-MEM/DM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>🔬 Métodos de Referencia EPA Adoptados en Perú</h2>
        <p style='color: var(--text-secondary); margin-bottom: 1rem;'>
            Métodos estandarizados de la Agencia de Protección Ambiental de EE.UU. (EPA) 
            reconocidos en normativa peruana para asegurar calidad analítica
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    metodos = pd.DataFrame([
        ['PM10', 'EPA Method 40 CFR Part 50, Appendix J', 'Muestreo gravimétrico con separador inercial', 'Alto volumen (Hi-Vol)'],
        ['PM2.5', 'EPA Method 40 CFR Part 50, Appendix L', 'Muestreo gravimétrico con separador inercial', 'Bajo volumen (Low-Vol)'],
        ['SO2', 'EPA Method 40 CFR Part 50, Appendix A-1', 'Fluorescencia UV pulsada', 'Analizador continuo'],
        ['NO2', 'EPA Method 40 CFR Part 50, Appendix F', 'Quimioluminiscencia', 'Analizador continuo'],
        ['CO', 'EPA Method 40 CFR Part 50, Appendix C', 'Espectrometría infrarroja no dispersiva (NDIR)', 'Analizador continuo'],
        ['O3', 'EPA Method 40 CFR Part 50, Appendix D', 'Fotometría de absorción UV', 'Analizador continuo'],
        ['Pb', 'EPA Method 40 CFR Part 50, Appendix G', 'Espectrometría de absorción atómica', 'Filtros PM10'],
        ['H2S', 'EPA Method 11', 'Tren de muestreo con solución absorbente', 'Método manual']
    ], columns=['Contaminante', 'Método EPA', 'Técnica Analítica', 'Tipo de Equipo'])
    
    st.dataframe(metodos, use_container_width=True, hide_index=True, height=380)

# ===================== PÁGINA LINEAMIENTO =====================
elif st.session_state.pagina == "Lineamiento":
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>📐 Lineamientos y Guías Técnicas</h2>
        <p style='font-size: 1.05rem;'>
            Los lineamientos son <strong>instrumentos técnico-normativos complementarios</strong> que 
            proporcionan guías operativas para la implementación de normativas ambientales. Establecen 
            metodologías, procedimientos y criterios técnicos específicos para la gestión de calidad del aire.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("**Función:** Los lineamientos facilitan la aplicación práctica de la normativa legal, proporcionando herramientas técnicas para su cumplimiento efectivo por parte de autoridades, empresas y consultores.")
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>● VIGENTE</span>
        <h3>R.M. N° 181-2016-MINAM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Lineamientos para la Elaboración del Inventario de Emisiones Atmosféricas</strong>
        </p>
        <p>
            Establece la metodología estandarizada para elaborar inventarios de emisiones de contaminantes 
            atmosféricos a nivel nacional, regional y local. Incluye factores de emisión, procedimientos de 
            cálculo, categorización de fuentes, y formatos de reporte. Aplicable a autoridades ambientales 
            y titulares de actividades productivas.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 13 de julio de 2016 | 
            <strong>Ámbito:</strong> Nacional
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2016/07/RM-N%C2%B0-181-2016-MINAM.pdf' 
           target='_blank' class='corporate-button'>
            📄 Descargar R.M. 181-2016-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>● VIGENTE</span>
        <h3>D.S. N° 009-2003-SA</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Reglamento de Niveles de Estados de Alerta Nacionales para Contaminantes del Aire</strong>
        </p>
        <p>
            Define los niveles de alerta ambiental (Cuidado, Peligro y Emergencia) ante episodios críticos 
            de contaminación del aire. Establece umbrales de concentración que activan protocolos de emergencia, 
            acciones obligatorias para autoridades y población, y mecanismos de comunicación pública del riesgo.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 25 de junio de 2003 | 
            <strong>Entidad:</strong> MINSA
        </p>
        <a href='https://sinia.minam.gob.pe/normas/reglamento-niveles-estados-alerta-nacionales-contaminantes-del-aire' 
           target='_blank' class='corporate-button'>
            📄 Descargar D.S. 009-2003-SA
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>● VIGENTE</span>
        <h3>Decreto Legislativo N° 1278</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Ley de Gestión Integral de Residuos Sólidos</strong>
        </p>
        <p>
            Establece lineamientos para el control de emisiones atmosféricas de instalaciones de tratamiento, 
            valorización e incineración de residuos sólidos. Define obligaciones de monitoreo continuo de 
            emisiones (CEMS), límites operativos y procedimientos de reporte ante autoridades sanitarias y ambientales.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 23 de diciembre de 2016 | 
            <strong>Vigencia:</strong> Desde diciembre 2017
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2017/04/Decreto-Legislativo-N%C2%B0-1278.pdf' 
           target='_blank' class='corporate-button'>
            📄 Ver Decreto Legislativo 1278
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>⚠️ Niveles de Estados de Alerta Nacional (D.S. 009-2003-SA)</h2>
        <p style='color: var(--text-secondary); margin-bottom: 1rem;'>
            Umbrales de concentración que activan protocolos de emergencia ambiental
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    niveles = pd.DataFrame([
        ['PM10', '🟡 Cuidado', 250, 350, 'μg/m³', 'Información a grupos sensibles'],
        ['PM10', '🟠 Peligro', 350, 420, 'μg/m³', 'Alerta general a población'],
        ['PM10', '🔴 Emergencia', '> 420', '---', 'μg/m³', 'Emergencia sanitaria regional'],
        ['SO2', '🟡 Cuidado', 500, 1000, 'μg/m³', 'Advertencia a grupos sensibles'],
        ['SO2', '🟠 Peligro', 1000, 1600, 'μg/m³', 'Restricción actividades al aire libre'],
        ['SO2', '🔴 Emergencia', '> 1600', '---', 'μg/m³', 'Suspensión actividades productivas'],
        ['NO2', '🟡 Cuidado', 600, 1200, 'μg/m³', 'Alerta a grupos de riesgo'],
        ['NO2', '🟠 Peligro', 1200, 1600, 'μg/m³', 'Reducción tráfico vehicular'],
        ['NO2', '🔴 Emergencia', '> 1600', '---', 'μg/m³', 'Cierre de vías principales'],
        ['CO', '🟡 Cuidado', 15000, 30000, 'μg/m³', 'Información preventiva'],
        ['CO', '🟠 Peligro', 30000, 40000, 'μg/m³', 'Restricción circulación vehicular'],
        ['CO', '🔴 Emergencia', '> 40000', '---', 'μg/m³', 'Estado de emergencia sanitaria']
    ], columns=['Contaminante', 'Nivel de Alerta', 'Límite Inferior', 'Límite Superior', 'Unidad', 'Acción Requerida'])
    
    st.dataframe(niveles, use_container_width=True, hide_index=True, height=500)
    
    st.warning("**⚠️ Protocolo de activación:** Las autoridades ambientales y de salud deben activar los niveles de alerta cuando se registren o pronostiquen concentraciones en los rangos establecidos. Las medidas incluyen difusión masiva de información, restricción de actividades, y en casos de emergencia, la declaratoria de estado de emergencia ambiental.")
    # ===================== PÁGINA MEDIDAS =====================
elif st.session_state.pagina == "Medidas":
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>🛡️ Medidas de Control y Marco Legal</h2>
        <p style='font-size: 1.05rem;'>
            Conjunto de <strong>tecnologías, normativas y políticas públicas</strong> implementadas para 
            reducir y controlar las emisiones atmosféricas. Incluye tanto el marco legal fundamental como 
            las principales tecnologías de control de emisiones industriales.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>● VIGENTE - LEY MARCO</span>
        <h3>Ley N° 28611</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Ley General del Ambiente</strong>
        </p>
        <p>
            Norma ordenadora del marco normativo legal para la gestión ambiental en el Perú. Establece los 
            principios y normas básicas para asegurar el derecho constitucional a un ambiente saludable. 
            Define instrumentos de gestión ambiental, responsabilidades, fiscalización y régimen de incentivos. 
            Base legal de todos los ECA y LMP vigentes.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 15 de octubre de 2005 | 
            <strong>Vigencia:</strong> Desde octubre 2005
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2017/04/Ley-N%C2%B0-28611.pdf' 
           target='_blank' class='corporate-button'>
            📄 Descargar Ley 28611
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>● VIGENTE - LEY MARCO</span>
        <h3>Ley N° 30754</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Ley Marco sobre Cambio Climático</strong>
        </p>
        <p>
            Establece el marco institucional, principios, obligaciones, procesos, mecanismos e instrumentos 
            para la gestión integral, participativa y transparente de las medidas de adaptación y mitigación 
            al cambio climático. Vincula el control de emisiones atmosféricas con los compromisos nacionales 
            de reducción de gases de efecto invernadero (NDC).
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 18 de abril de 2018 | 
            <strong>Vigencia:</strong> Desde abril 2018
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2018/07/Ley-N%C2%B0-30754.pdf' 
           target='_blank' class='corporate-button'>
            📄 Descargar Ley 30754
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>⚙️ Principales Tecnologías de Control de Emisiones</h2>
        <p style='color: var(--text-secondary); margin-bottom: 1.5rem;'>
            Sistemas de abatimiento más utilizados en industrias para cumplir con LMP
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    tabs = st.tabs(["💨 Material Particulado", "🌫️ Gases Ácidos", "⚗️ NOx y VOCs", "📊 Comparación"])
    
    with tabs[0]:
        st.markdown("""
        <div class='corporate-card'>
            <h3>Tecnologías para Control de Material Particulado</h3>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **🔷 Precipitador Electrostático (ESP)**
            
            - **Principio:** Ionización y captura por campo eléctrico
            - **Eficiencia:** 99-99.9% para PM >0.1 μm
            - **Aplicación:** Termoeléctricas, cementeras, metalurgia
            - **Ventajas:** Alta eficiencia, bajo costo operativo
            - **Desventajas:** Alta inversión inicial, requiere espacio
            """)
            
            st.markdown("""
            **🔷 Filtros de Mangas (Baghouse)**
            
            - **Principio:** Filtración mecánica por medio poroso
            - **Eficiencia:** 99.5-99.9% para PM >0.5 μm
            - **Aplicación:** Cemento, minería, fundiciones
            - **Ventajas:** Muy alta eficiencia, versátil
            - **Desventajas:** Requiere cambio periódico de mangas
            """)
        
        with col2:
            st.markdown("""
            **🔷 Ciclones**
            
            - **Principio:** Separación centrífuga
            - **Eficiencia:** 50-90% para PM >10 μm
            - **Aplicación:** Pre-tratamiento, industrias pesadas
            - **Ventajas:** Bajo costo, robusto
            - **Desventajas:** Baja eficiencia en partículas finas
            """)
            
            st.markdown("""
            **🔷 Scrubbers Húmedos**
            
            - **Principio:** Lavado con agua o solución química
            - **Eficiencia:** 80-99% según diseño
            - **Aplicación:** Gases con alta temperatura/humedad
            - **Ventajas:** Enfría gases, captura gases y partículas
            - **Desventajas:** Genera efluentes líquidos
            """)
    
    with tabs[1]:
        st.markdown("""
        <div class='corporate-card'>
            <h3>Tecnologías para Control de Gases Ácidos (SO2, HCl, HF)</h3>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **🔷 Desulfuración de Gases (FGD) - Vía Húmeda**
            
            - **Principio:** Absorción en suspensión de caliza/cal
            - **Eficiencia:** 95-98% remoción de SO2
            - **Aplicación:** Termoeléctricas a carbón/petróleo
            - **Reacción:** CaCO3 + SO2 → CaSO3 + CO2
            - **Ventajas:** Muy alta eficiencia, tecnología probada
            - **Desventajas:** Alto consumo de agua y reactivos
            """)
            
            st.markdown("""
            **🔷 Inyección de Sorbente en Ducto (DSI)**
            
            - **Principio:** Inyección de cal o bicarbonato sódico
            - **Eficiencia:** 50-90% según configuración
            - **Aplicación:** Instalaciones medianas, incineradoras
            - **Ventajas:** Menor inversión que FGD húmedo
            - **Desventajas:** Mayor consumo de reactivos
            """)
        
        with col2:
            st.markdown("""
            **🔷 FGD Semiseco (Spray Dryer)**
            
            - **Principio:** Atomización de lechada de cal
            - **Eficiencia:** 85-95% remoción de SO2
            - **Aplicación:** Termoeléctricas, cementeras
            - **Ventajas:** No genera efluentes líquidos
            - **Desventajas:** Genera residuos sólidos a disponer
            """)
            
            st.markdown("""
            **🔷 Absorción con Aminas**
            
            - **Principio:** Lavado con soluciones alcalinas
            - **Eficiencia:** >99% para gases ácidos
            - **Aplicación:** Plantas químicas, refinerías
            - **Ventajas:** Regeneración del absorbente
            - **Desventajas:** Complejidad operativa
            """)
    
    with tabs[2]:
        st.markdown("""
        <div class='corporate-card'>
            <h3>Tecnologías para Control de NOx y Compuestos Orgánicos Volátiles</h3>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **🔷 Reducción Catalítica Selectiva (SCR)**
            
            - **Principio:** Reducción de NOx con NH3 y catalizador
            - **Eficiencia:** 80-95% remoción de NOx
            - **Temperatura:** 300-400°C
            - **Aplicación:** Termoeléctricas, grandes calderos
            - **Reacción:** 4NO + 4NH3 + O2 → 4N2 + 6H2O
            - **Ventajas:** Máxima eficiencia disponible
            - **Desventajas:** Requiere catalizador costoso, NH3
            """)
            
            st.markdown("""
            **🔷 Reducción No Catalítica Selectiva (SNCR)**
            
            - **Principio:** Inyección de urea o NH3 a alta temperatura
            - **Eficiencia:** 40-70% remoción de NOx
            - **Temperatura:** 850-1100°C
            - **Aplicación:** Calderos, incineradores
            - **Ventajas:** Menor inversión que SCR
            - **Desventajas:** Menor eficiencia, ventana térmica crítica
            """)
        
        with col2:
            st.markdown("""
            **🔷 Oxidación Catalítica**
            
            - **Principio:** Oxidación de VOCs con catalizador
            - **Eficiencia:** >95% destrucción de VOCs
            - **Temperatura:** 250-500°C
            - **Aplicación:** Emisiones con VOCs, pinturas, químicos
            - **Ventajas:** Baja temperatura de operación
            - **Desventajas:** Sensible a envenenamiento de catalizador
            """)
            
            st.markdown("""
            **🔷 Oxidación Térmica (Incineración)**
            
            - **Principio:** Combustión completa a alta temperatura
            - **Eficiencia:** >99% destrucción de VOCs
            - **Temperatura:** 760-1000°C
            - **Aplicación:** Corrientes de alta concentración
            - **Ventajas:** Destrucción completa, robusto
            - **Desventajas:** Alto consumo energético
            """)
    
    with tabs[3]:
        st.markdown("""
        <div class='corporate-card'>
            <h3>📊 Comparación de Eficiencias y Costos</h3>
        </div>
        """, unsafe_allow_html=True)
        
        comparacion = pd.DataFrame([
            ['Precipitador Electrostático', 'Material Particulado', '99-99.9%', 'Alta', 'Bajo', 'Termoeléctricas, cementeras'],
            ['Filtros de Mangas', 'Material Particulado', '99.5-99.9%', 'Media', 'Medio', 'Minería, cemento, metalurgia'],
            ['FGD Húmedo', 'SO2', '95-98%', 'Muy Alta', 'Alto', 'Termoeléctricas a carbón'],
            ['FGD Semiseco', 'SO2', '85-95%', 'Alta', 'Medio', 'Cementeras, termoeléctricas'],
            ['SCR', 'NOx', '80-95%', 'Muy Alta', 'Alto', 'Termoeléctricas, grandes calderos'],
            ['SNCR', 'NOx', '40-70%', 'Media', 'Bajo', 'Calderos industriales'],
            ['Oxidación Catalítica', 'VOCs', '>95%', 'Alta', 'Medio', 'Industria química, pinturas'],
            ['Ciclones', 'Material Particulado', '50-90%', 'Baja', 'Muy Bajo', 'Pre-tratamiento industrial']
        ], columns=['Tecnología', 'Contaminante Objetivo', 'Eficiencia', 'Inversión', 'Costo Operativo', 'Aplicación Principal'])
        
        st.dataframe(comparacion, use_container_width=True, hide_index=True, height=380)
        
        st.info("""
        **💡 Criterios de Selección de Tecnología:**
        
        1. **Regulación aplicable:** LMP del sector y contaminante específico
        2. **Características del gas:** Temperatura, humedad, concentración de contaminantes
        3. **Espacio disponible:** Algunas tecnologías requieren grandes instalaciones
        4. **Presupuesto:** Balance entre inversión inicial y costos operativos
        5. **Generación de residuos:** Considerar tratamiento de subproductos
        6. **Integración con proceso:** Compatibilidad con operación existente
        """)
        # ===================== PÁGINA NORMATIVAS INTERNACIONALES =====================
elif st.session_state.pagina == "Normativas":
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>🌍 Estándares Internacionales de Calidad del Aire</h2>
        <p style='font-size: 1.05rem;'>
            Comparativa de los principales <strong>estándares de calidad del aire a nivel mundial</strong> 
            establecidos por organizaciones internacionales y países de referencia. Estos estándares representan 
            el consenso científico sobre niveles seguros de contaminantes para protección de la salud pública.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("**Nota:** Los estándares internacionales sirven de referencia para la actualización de normativas nacionales y reflejan los avances en investigación sobre efectos de contaminantes en la salud.")
    
    tabs = st.tabs(["🏥 OMS", "🇺🇸 EPA USA", "🇨🇦 Canadá", "📊 Comparación"])
    
    with tabs[0]:
        st.markdown("""
        <div class='normative-card internacional fade-in'>
            <span class='status-badge internacional'>● GUÍAS INTERNACIONALES</span>
            <h3>Organización Mundial de la Salud (OMS/WHO) 2021</h3>
            <p style='font-size: 1.05rem; margin: 1rem 0;'>
                <strong>WHO Global Air Quality Guidelines</strong>
            </p>
            <p>
                Las Guías de Calidad del Aire de la OMS representan el <strong>consenso científico más actualizado</strong> 
                sobre los efectos de la contaminación del aire en la salud. Actualizadas en 2021 después de 15 años, 
                estas guías establecen niveles recomendados para proteger la salud pública basados en evidencia 
                epidemiológica y toxicológica robusta.
            </p>
            <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
                <strong>Última actualización:</strong> Septiembre 2021 | 
                <strong>Alcance:</strong> Global
            </p>
            <a href='https://www.who.int/news-room/feature-stories/detail/what-are-the-who-air-quality-guidelines' 
               target='_blank' class='corporate-button'>
                📄 Ver Guías OMS 2021
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        oms_data = pd.DataFrame([
            ['PM2.5', '24 horas', 15, 'μg/m³', 'Percentil 99'],
            ['PM2.5', 'Anual', 5, 'μg/m³', 'Media anual'],
            ['PM10', '24 horas', 45, 'μg/m³', 'Percentil 99'],
            ['PM10', 'Anual', 15, 'μg/m³', 'Media anual'],
            ['NO2', '24 horas', 25, 'μg/m³', 'Percentil 99'],
            ['NO2', 'Anual', 10, 'μg/m³', 'Media anual'],
            ['SO2', '24 horas', 40, 'μg/m³', 'Percentil 99'],
            ['O3', '8 horas', 100, 'μg/m³', 'Máximo diario promedio 8h'],
            ['CO', '24 horas', 4000, 'μg/m³', 'Media 24 horas']
        ], columns=['Contaminante', 'Período', 'Valor OMS 2021', 'Unidad', 'Forma del Estándar'])
        
        st.dataframe(oms_data, use_container_width=True, hide_index=True, height=420)
        
        st.warning("**🔬 Evidencia científica:** La OMS determinó que NO existe un umbral seguro para PM2.5 por debajo del cual no haya efectos adversos en salud. Los valores guía representan niveles donde el riesgo es mínimo basado en estudios epidemiológicos globales.")
    
    with tabs[1]:
        st.markdown("""
        <div class='normative-card internacional fade-in'>
            <span class='status-badge internacional'>● ESTÁNDARES NACIONALES USA</span>
            <h3>Agencia de Protección Ambiental de EE.UU. (EPA)</h3>
            <p style='font-size: 1.05rem; margin: 1rem 0;'>
                <strong>National Ambient Air Quality Standards (NAAQS)</strong>
            </p>
            <p>
                Los NAAQS son <strong>estándares federales de obligatorio cumplimiento</strong> en todo el territorio 
                estadounidense, establecidos bajo la Ley de Aire Limpio (Clean Air Act). EPA revisa periódicamente 
                estos estándares basándose en la mejor ciencia disponible. Incluyen estándares primarios (protección 
                de salud) y secundarios (protección de bienestar público).
            </p>
            <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
                <strong>Última revisión PM2.5:</strong> Febrero 2024 | 
                <strong>Jurisdicción:</strong> Estados Unidos
            </p>
            <a href='https://www.epa.gov/criteria-air-pollutants/naaqs-table' 
               target='_blank' class='corporate-button'>
                📄 Ver NAAQS EPA
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        epa_data = pd.DataFrame([
            ['PM2.5', '24 horas', 35, 'μg/m³', 'Percentil 98, promedio 3 años'],
            ['PM2.5', 'Anual', 9, 'μg/m³', 'Media anual, promedio 3 años'],
            ['PM10', '24 horas', 150, 'μg/m³', 'No exceder más de 1 vez al año'],
            ['NO2', '1 hora', 188, 'μg/m³', 'Percentil 98, promedio 3 años'],
            ['NO2', 'Anual', 100, 'μg/m³', 'Media aritmética anual'],
            ['SO2', '1 hora', 196, 'μg/m³', 'Percentil 99, promedio 3 años'],
            ['O3', '8 horas', 140, 'μg/m³', 'Máximo 4to más alto, promedio 3 años'],
            ['CO', '8 horas', 10000, 'μg/m³', 'No exceder más de 1 vez al año'],
            ['CO', '1 hora', 40000, 'μg/m³', 'No exceder más de 1 vez al año'],
            ['Pb', 'Trimestral', 0.15, 'μg/m³', 'Promedio móvil 3 meses']
        ], columns=['Contaminante', 'Período', 'Valor EPA 2024', 'Unidad', 'Forma del Estándar'])
        
        st.dataframe(epa_data, use_container_width=True, hide_index=True, height=450)
        
        st.success("**✅ Actualización 2024:** EPA redujo el estándar anual de PM2.5 de 12 a 9 μg/m³ en febrero 2024, basándose en nueva evidencia científica sobre efectos cardiovasculares y respiratorios a largo plazo.")
    
    with tabs[2]:
        st.markdown("""
        <div class='normative-card internacional fade-in'>
            <span class='status-badge internacional'>● ESTÁNDARES NACIONALES CANADÁ</span>
            <h3>Environment and Climate Change Canada</h3>
            <p style='font-size: 1.05rem; margin: 1rem 0;'>
                <strong>Canadian Ambient Air Quality Standards (CAAQS)</strong>
            </p>
            <p>
                Los CAAQS son <strong>estándares nacionales establecidos por el Consejo Canadiense de Ministros 
                del Ambiente</strong> (CCME) bajo el marco del Sistema de Gestión de Calidad del Aire (AQMS). 
                Son de aplicación en todas las provincias y territorios. Se actualizan periódicamente con objetivos 
                progresivos de mejoramiento continuo.
            </p>
            <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
                <strong>Estándares 2025:</strong> Vigentes | 
                <strong>Jurisdicción:</strong> Canadá (federal y provincial)
            </p>
            <a href='https://www.canada.ca/en/environment-climate-change/services/air-quality-health-index/about.html' 
               target='_blank' class='corporate-button'>
                📄 Ver CAAQS Canadá
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        canada_data = pd.DataFrame([
            ['PM2.5', '24 horas', 27, 'μg/m³', 'Percentil 98, promedio 3 años'],
            ['PM2.5', 'Anual', 8.0, 'μg/m³', 'Media anual, promedio 3 años'],
            ['PM10', '24 horas', 50, 'μg/m³', 'Percentil 98'],
            ['NO2', '1 hora', 114, 'μg/m³', 'Percentil 98, promedio 3 años'],
            ['NO2', 'Anual', 40, 'μg/m³', 'Media anual'],
            ['SO2', '1 hora', 172, 'μg/m³', 'Percentil 99, promedio 3 años'],
            ['O3', '8 horas', 126, 'μg/m³', 'Percentil 4to más alto, promedio 3 años']
        ], columns=['Contaminante', 'Período', 'Valor CAAQS 2025', 'Unidad', 'Forma del Estándar'])
        
        st.dataframe(canada_data, use_container_width=True, hide_index=True, height=350)
        
        st.info("**📅 Progresividad:** Los CAAQS se establecen con objetivos a 2020, 2025 y 2030, volviéndose progresivamente más estrictos para incentivar la mejora continua de la calidad del aire.")
    
    with tabs[3]:
        st.markdown("""
        <div class='corporate-card fade-in'>
            <h2>📊 Comparación Internacional PM2.5 Anual</h2>
            <p style='color: var(--text-secondary); margin-bottom: 1.5rem;'>
                Análisis comparativo de estándares más relevantes para salud pública
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        comp_data = pd.DataFrame([
            {'País/Organismo': 'OMS 2021', 'PM2.5 Anual': 5, 'PM2.5 24h': 15, 'NO2 Anual': 10, 'SO2 24h': 40},
            {'País/Organismo': 'EPA USA 2024', 'PM2.5 Anual': 9, 'PM2.5 24h': 35, 'NO2 Anual': 100, 'SO2 24h': None},
            {'País/Organismo': 'Canadá 2025', 'PM2.5 Anual': 8, 'PM2.5 24h': 27, 'NO2 Anual': 40, 'SO2 24h': None},
            {'País/Organismo': 'Perú 2017', 'PM2.5 Anual': 25, 'PM2.5 24h': 50, 'NO2 Anual': 100, 'SO2 24h': 250}
        ])
        
        fig_comp = go.Figure()
        
        fig_comp.add_trace(go.Bar(
            name='PM2.5 Anual (μg/m³)',
            x=comp_data['País/Organismo'],
            y=comp_data['PM2.5 Anual'],
            marker_color='#00E676',
            text=comp_data['PM2.5 Anual'],
            textposition='outside'
        ))
        
        fig_comp.add_trace(go.Bar(
            name='PM2.5 24h (μg/m³)',
            x=comp_data['País/Organismo'],
            y=comp_data['PM2.5 24h'],
            marker_color='#FFB300',
            text=comp_data['PM2.5 24h'],
            textposition='outside'
        ))
        
        fig_comp.update_layout(
            barmode='group',
            height=500,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#E3E8EF', size=13, family='Inter'),
            xaxis=dict(showgrid=False, title=''),
            yaxis=dict(
                showgrid=True,
                gridcolor='rgba(255,255,255,0.06)',
                title='Concentración (μg/m³)'
            ),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1,
                bgcolor='rgba(19, 47, 76, 0.8)',
                bordercolor='rgba(255,255,255,0.1)',
                borderwidth=1
            )
        )
        
        st.plotly_chart(fig_comp, use_container_width=True)
        
        st.warning("""
        **⚠️ Análisis Comparativo:**
        
        - **PM2.5 Anual:** Perú (25 μg/m³) tiene un estándar **5 veces más permisivo** que la recomendación OMS (5 μg/m³)
        - **PM2.5 24h:** El estándar peruano (50 μg/m³) es **3.3 veces mayor** que la guía OMS (15 μg/m³)
        - **Tendencia global:** Los países desarrollados están actualizando sus estándares para alinearse con las guías OMS 2021
        - **Recomendación:** Se sugiere evaluar actualización gradual de los ECA nacionales hacia estándares más protectivos
        """)
        
        st.dataframe(comp_data, use_container_width=True, hide_index=True)

# Footer institucional
st.markdown("""
<div class='corporate-footer fade-in'>
    <h2>🌍 Marco Normativo de Calidad del Aire - Perú</h2>
    <h4>Sistema Integral de Consulta de Normativas Ambientales</h4>
    
    <p style='margin: 2rem 0 1rem 0; font-size: 1.05rem;'>
        <strong>Universidad Nacional de Moquegua</strong><br>
        Facultad de Ingeniería y Arquitectura<br>
        Escuela Profesional de Ingeniería Ambiental
    </p>
    
    <p style='margin: 1.5rem 0;'>
        <strong>Responsable Académico:</strong><br>
        Prof. Dr. José Antonio Valeriano Zapana
    </p>
    
    <p style='margin: 1.5rem 0; font-size: 0.9rem; color: rgba(255,255,255,0.8)'>
        <strong>📧 Contacto:</strong> contacto@unam.edu.pe | 
        <strong>📱 Teléfono:</strong> +51 961 854 041<br>
        <strong>🌐 Web:</strong> www.unam.edu.pe
    </p>
    
    <p style='margin-top: 2rem; padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.15); font-size: 0.85rem; color: rgba(255,255,255,0.7);'>
        © 2024 Universidad Nacional de Moquegua. Todos los derechos reservados.<br>
        Última actualización: Octubre 2024 | Versión 2.0
    </p>
    
    <p style='margin-top: 1rem; font-size: 0.8rem; color: rgba(255,255,255,0.6);'>
        <em>Este sistema fue desarrollado con fines académicos y de consulta técnica. 
        La información presentada se basa en normativas oficiales vigentes del Estado Peruano 
        y organismos internacionales reconocidos.</em>
    </p>
</div>
""", unsafe_allow_html=True)
        
