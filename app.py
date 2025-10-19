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

# CSS Ultra Profesional
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
    
    /* Background principal */
    .stApp {
        background: linear-gradient(135deg, #0A1929 0%, #132F4C 50%, #1A3A52 100%);
        background-attachment: fixed;
    }
    
    .main {
        background: transparent;
        padding-top: 0 !important;
    }
    
    /* Ocultar espacio superior blanco */
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
    
    /* ÚLTIMO INTENTO - MÁXIMA FUERZA BRUTA */
    button[kind="header"],
    button[kind="headerNoPadding"],
    [data-testid="collapsedControl"] {
        background-color: rgba(255, 255, 255, 0.2) !important;
        border-radius: 8px !important;
    }
    
    /* INVERTIR COLORES DEL SVG COMPLETO */
    button[kind="header"] svg,
    button[kind="headerNoPadding"] svg,
    [data-testid="collapsedControl"] svg {
        filter: brightness(0) invert(1) !important;
        -webkit-filter: brightness(0) invert(1) !important;
    }
    
    /* Texto del sidebar MÁS VISIBLE */
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label {
        color: #FFFFFF !important;
        text-shadow: 0 2px 4px rgba(0,0,0,0.5);
    }
    
    /* Input de búsqueda más visible */
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
    
    /* Breadcrumbs profesionales */
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
    
    /* Cards corporativas premium */
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
    
    /* Normative cards de nivel premium */
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
    
    /* Status badges profesionales */
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
        background: linear-gradient(135deg, #FF6F00 0%, #FF9800 100%);
        color: white;
    }
    
    /* Botones corporativos premium */
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
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
    /* Tablas profesionales */
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
    
    /* Botones de Streamlit mejorados */
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
    
    /* Tabs corporativos */
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
    
    /* Métricas profesionales */
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
    
    /* Expanders mejorados */
    .streamlit-expanderHeader {
        background: rgba(19, 47, 76, 0.6);
        backdrop-filter: blur(10px);
        border-radius: 8px;
        border: 1px solid rgba(255, 255, 255, 0.06);
        color: var(--text-primary);
        font-weight: 600;
    }
    
    /* Selectbox y inputs */
    .stSelectbox > div > div,
    .stTextInput > div > div {
        background: rgba(19, 47, 76, 0.6);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 8px;
        color: var(--text-primary);
    }
    
    /* Info boxes */
    .info-box {
        background: linear-gradient(135deg, rgba(0, 184, 217, 0.2) 0%, rgba(0, 101, 255, 0.15) 100%);
        border-left: 4px solid var(--accent-teal);
        padding: 1.25rem;
        border-radius: 8px;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
    }
    
    .info-box p {
        color: rgba(255, 255, 255, 0.95) !important;
        margin: 0;
        line-height: 1.6;
    }
    
    .info-box strong {
        color: white !important;
    }
    
    /* Warning boxes */
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
    
    /* Success boxes */
    .success-box {
        background: linear-gradient(135deg, rgba(0, 200, 83, 0.2) 0%, rgba(0, 230, 118, 0.15) 100%);
        border-left: 4px solid var(--success);
        padding: 1.25rem;
        border-radius: 8px;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
    }
    
    .success-box p {
        color: rgba(255, 255, 255, 0.95) !important;
        margin: 0;
        line-height: 1.6;
    }
    
    .success-box strong {
        color: white !important;
    }
    
    .success-box h4 {
        color: white !important;
        margin-top: 0;
    }
    
    .success-box ol, .success-box ul {
        color: rgba(255, 255, 255, 0.95) !important;
    }
    
    /* Footer corporativo */
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
    
    .corporate-footer h3, .corporate-footer h4 {
        color: white !important;
        font-weight: 700;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    
    .corporate-footer h3 {
        font-size: 1.5rem;
        margin: 0 0 0.5rem 0;
    }
    
    .corporate-footer p {
        color: rgba(255, 255, 255, 0.9) !important;
        margin: 0.5rem 0;
        line-height: 1.6;
    }
    
    .corporate-footer .divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
        margin: 1.5rem 0;
    }
    
    /* Scrollbar */
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
    
    /* Animaciones sutiles */
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
    
    /* Responsive */
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
    
    # Búsqueda con funcionalidad
    busqueda = st.text_input("🔎 Buscar normativa...", placeholder="Ej: PM2.5, ECA, protocolo...", key="search_input")
    
    # Sistema de búsqueda inteligente
    if busqueda:
        busqueda_lower = busqueda.lower()
        
        # Diccionario de palabras clave por página
        keywords = {
            "ECA": ["eca", "estándar", "estandar", "calidad ambiental", "pm2.5", "pm10", "no2", "so2", "co", "o3", "ozono", "003-2017", "010-2019", "074-2001"],
            "LMP": ["lmp", "límite", "limite", "máximo permisible", "maximo permisible", "emisión", "emision", "termoeléctrica", "termoelectrica", "vehicular", "minería", "mineria", "003-2010", "011-2009", "010-2010"],
            "Protocolo": ["protocolo", "monitoreo", "digesa", "medición", "medicion", "muestreo", "1404-2005", "026-2000", "195-2010"],
            "Lineamiento": ["lineamiento", "inventario", "alerta", "estado de alerta", "181-2016", "009-2003", "1278"],
            "Medidas": ["medida", "control", "tecnología", "tecnologia", "filtro", "precipitador", "scrubber", "fgd", "scr", "nox", "28611"],
            "Normativas": ["internacional", "oms", "who", "epa", "usa", "canadá", "canada", "naaqs", "caaqs", "guía", "guia"]
        }
        
        # Buscar coincidencias
        mejor_match = None
        max_coincidencias = 0
        
        for pagina, palabras in keywords.items():
            coincidencias = sum(1 for palabra in palabras if palabra in busqueda_lower)
            if coincidencias > max_coincidencias:
                max_coincidencias = coincidencias
                mejor_match = pagina
        
        # Si encuentra coincidencia, mostrar sugerencia
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
    st.markdown("""
    <div class='info-box'>
        <p style='font-size: 0.85rem;'><strong>Última actualización:</strong><br>Octubre 2024</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("📞 Contacto"):
        st.markdown("""
        <p style='color: rgba(255,255,255,0.95); line-height: 1.8;'>
        <strong style='color: white;'>Universidad Nacional de Moquegua</strong><br>
        Facultad de Ingeniería y Arquitectura<br><br>
        
        📧 contacto@unam.edu.pe<br>
        📱 +51 XXX XXX XXX
        </p>
        """, unsafe_allow_html=True)

# Header institucional premium
st.markdown(f"""
<div class='institutional-header fade-in'>
    <h1>🌍 Marco Normativo de Calidad del Aire</h1>
    <p class='subtitle'>Sistema Integral de Consulta de Normativas Ambientales</p>
    <div class='metadata'>
        <strong>Universidad Nacional de Moquegua</strong> | 
        Facultad de Ingeniería y Arquitectura | 
        Prof. Dr. José Antonio Valeriano Zapana | 
        <span style='opacity: 0.7;'>{datetime.now().strftime('%d/%m/%Y')}</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Breadcrumb
breadcrumb_map = {
    "Inicio": "🏠 Inicio",
    "ECA": "📋 Estándares ECA",
    "LMP": "🏭 Límites LMP",
    "Protocolo": "📖 Protocolos",
    "Lineamiento": "📐 Lineamientos",
    "Medidas": "🛡️ Control de Emisiones",
    "Normativas": "🌍 Normativas Internacionales"
}

st.markdown(f"""
<div class='breadcrumb fade-in'>
    <a href='#' onclick='return false;'>Inicio</a>
    <span class='breadcrumb-separator'>›</span>
    <span>{breadcrumb_map.get(st.session_state.pagina, st.session_state.pagina)}</span>
</div>
""", unsafe_allow_html=True)
# ===================== PÁGINA INICIO =====================
if st.session_state.pagina == "Inicio":
    
    # Métricas principales
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Normativas Nacionales",
            value="12",
            delta="Vigentes"
        )
    
    with col2:
        st.metric(
            label="Estándares Internacionales",
            value="6",
            delta="OMS, EPA, Canadá"
        )
    
    with col3:
        st.metric(
            label="Contaminantes Regulados",
            value="8",
            delta="Criterio"
        )
    
    with col4:
        st.metric(
            label="Protocolos Activos",
            value="5",
            delta="Monitoreo"
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # NUEVA SECCIÓN: Línea del Tiempo
        st.markdown("""
        <div class='corporate-card fade-in'>
            <h2>📚 Evolución del Marco Normativo Peruano</h2>
            <p style='font-size: 1.05rem; margin-bottom: 2rem;'>
                Recorrido histórico de las principales normativas de calidad del aire en Perú
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Timeline interactiva - Datos
        timeline_data = [
            {'año': 1996, 'titulo': 'R.M. N° 315-96-EM/VMM', 'categoria': 'LMP', 'descripcion': 'Primeros límites para fundiciones y refinerías mineras'},
            {'año': 2000, 'titulo': 'R.M. N° 026-2000-ITINCI/DM', 'categoria': 'Protocolo', 'descripcion': 'Protocolo de monitoreo industrial'},
            {'año': 2001, 'titulo': 'D.S. N° 074-2001-PCM', 'categoria': 'ECA', 'descripcion': 'Primeros Estándares de Calidad Ambiental para Aire'},
            {'año': 2003, 'titulo': 'D.S. N° 009-2003-SA', 'categoria': 'Lineamiento', 'descripcion': 'Niveles de Estados de Alerta Nacional'},
            {'año': 2005, 'titulo': 'R.D. N° 1404-2005/DIGESA', 'categoria': 'Protocolo', 'descripcion': 'Protocolo de Monitoreo de Calidad del Aire'},
            {'año': 2005, 'titulo': 'Ley N° 28611', 'categoria': 'Marco Legal', 'descripcion': 'Ley General del Ambiente'},
            {'año': 2009, 'titulo': 'D.S. N° 011-2009-MINAM', 'categoria': 'LMP', 'descripcion': 'Límites para vehículos automotores'},
            {'año': 2010, 'titulo': 'D.S. N° 003-2010-MINAM', 'categoria': 'LMP', 'descripcion': 'Límites para centrales termoeléctricas'},
            {'año': 2010, 'titulo': 'D.S. N° 010-2010-MINAM', 'categoria': 'LMP', 'descripcion': 'Límites para industrias manufactureras'},
            {'año': 2016, 'titulo': 'R.M. N° 181-2016-MINAM', 'categoria': 'Lineamiento', 'descripcion': 'Lineamientos para Inventario de Emisiones'},
            {'año': 2017, 'titulo': 'D.S. N° 003-2017-MINAM', 'categoria': 'ECA', 'descripcion': 'Actualización de Estándares de Calidad Ambiental'},
            {'año': 2018, 'titulo': 'Ley N° 30754', 'categoria': 'Marco Legal', 'descripcion': 'Ley Marco sobre Cambio Climático'},
            {'año': 2019, 'titulo': 'D.S. N° 010-2019-MINAM', 'categoria': 'ECA', 'descripcion': 'Modificatoria de ECA para Aire'}
        ]
        
        df_timeline = pd.DataFrame(timeline_data)
        
        # Gráfico de timeline con Plotly
        fig_timeline = go.Figure()
        
        categorias = df_timeline['categoria'].unique()
        colores_cat = {
            'ECA': '#00C853',
            'LMP': '#FF6F00',
            'Protocolo': '#8E24AA',
            'Lineamiento': '#0091EA',
            'Marco Legal': '#D32F2F'
        }
        
        for i, cat in enumerate(categorias):
            df_cat = df_timeline[df_timeline['categoria'] == cat]
            
            fig_timeline.add_trace(go.Scatter(
                x=df_cat['año'],
                y=[i] * len(df_cat),
                mode='markers+text',
                name=cat,
                marker=dict(
                    size=20,
                    color=colores_cat[cat],
                    symbol='diamond',
                    line=dict(color='white', width=2)
                ),
                text=df_cat['año'],
                textposition='top center',
                textfont=dict(size=10, color='white'),
                hovertemplate='<b>%{customdata[0]}</b><br>' +
                              '%{customdata[1]}<br>' +
                              '<i>Año: %{x}</i><extra></extra>',
                customdata=df_cat[['titulo', 'descripcion']].values
            ))
        
        fig_timeline.update_layout(
            height=450,
            showlegend=True,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#E3E8EF', size=12, family='Inter'),
            xaxis=dict(
                showgrid=True,
                gridcolor='rgba(255,255,255,0.1)',
                title='Año',
                dtick=2,
                range=[1995, 2020]
            ),
            yaxis=dict(
                showgrid=False,
                showticklabels=False,
                title=''
            ),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.2,
                xanchor="center",
                x=0.5,
                bgcolor='rgba(19, 47, 76, 0.8)',
                bordercolor='rgba(255,255,255,0.1)',
                borderwidth=1
            ),
            hovermode='closest',
            margin=dict(l=50, r=50, t=30, b=80)
        )
        
        st.plotly_chart(fig_timeline, use_container_width=True)
        
        # Cards de categorías con iconos
        st.markdown("""
        <div class='corporate-card' style='margin-top: 2rem;'>
            <h3 style='text-align: center; margin-bottom: 1.5rem;'>📂 Categorías del Sistema Normativo</h3>
        </div>
        """, unsafe_allow_html=True)
        
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            st.markdown("""
            <div style='background: linear-gradient(135deg, rgba(0, 200, 83, 0.2), rgba(0, 230, 118, 0.1)); 
                        padding: 1.5rem; border-radius: 12px; border-left: 4px solid #00C853; text-align: center;'>
                <div style='font-size: 3rem; margin-bottom: 0.5rem;'>📋</div>
                <h4 style='color: #00C853; margin: 0.5rem 0;'>ECA</h4>
                <p style='color: var(--text-secondary); font-size: 0.9rem; margin: 0;'>
                    Estándares de Calidad Ambiental del Aire
                </p>
                <div style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
                    <span style='font-size: 1.5rem; font-weight: 700; color: #00C853;'>3</span>
                    <p style='font-size: 0.8rem; color: var(--text-secondary); margin: 0.25rem 0 0 0;'>Normativas</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div style='background: linear-gradient(135deg, rgba(142, 36, 170, 0.2), rgba(156, 39, 176, 0.1)); 
                        padding: 1.5rem; border-radius: 12px; border-left: 4px solid #8E24AA; text-align: center; margin-top: 1rem;'>
                <div style='font-size: 3rem; margin-bottom: 0.5rem;'>📖</div>
                <h4 style='color: #8E24AA; margin: 0.5rem 0;'>Protocolos</h4>
                <p style='color: var(--text-secondary); font-size: 0.9rem; margin: 0;'>
                    Procedimientos de Monitoreo
                </p>
                <div style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
                    <span style='font-size: 1.5rem; font-weight: 700; color: #8E24AA;'>4</span>
                    <p style='font-size: 0.8rem; color: var(--text-secondary); margin: 0.25rem 0 0 0;'>Protocolos</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col_b:
            st.markdown("""
            <div style='background: linear-gradient(135deg, rgba(255, 111, 0, 0.2), rgba(255, 152, 0, 0.1)); 
                        padding: 1.5rem; border-radius: 12px; border-left: 4px solid #FF6F00; text-align: center;'>
                <div style='font-size: 3rem; margin-bottom: 0.5rem;'>🏭</div>
                <h4 style='color: #FF6F00; margin: 0.5rem 0;'>LMP</h4>
                <p style='color: var(--text-secondary); font-size: 0.9rem; margin: 0;'>
                    Límites Máximos Permisibles
                </p>
                <div style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
                    <span style='font-size: 1.5rem; font-weight: 700; color: #FF6F00;'>4</span>
                    <p style='font-size: 0.8rem; color: var(--text-secondary); margin: 0.25rem 0 0 0;'>Normativas</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div style='background: linear-gradient(135deg, rgba(211, 47, 47, 0.2), rgba(229, 57, 53, 0.1)); 
                        padding: 1.5rem; border-radius: 12px; border-left: 4px solid #D32F2F; text-align: center; margin-top: 1rem;'>
                <div style='font-size: 3rem; margin-bottom: 0.5rem;'>⚖️</div>
                <h4 style='color: #D32F2F; margin: 0.5rem 0;'>Marco Legal</h4>
                <p style='color: var(--text-secondary); font-size: 0.9rem; margin: 0;'>
                    Leyes y Decretos Base
                </p>
                <div style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
                    <span style='font-size: 1.5rem; font-weight: 700; color: #D32F2F;'>2</span>
                    <p style='font-size: 0.8rem; color: var(--text-secondary); margin: 0.25rem 0 0 0;'>Leyes</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col_c:
            st.markdown("""
            <div style='background: linear-gradient(135deg, rgba(0, 145, 234, 0.2), rgba(3, 169, 244, 0.1)); 
                        padding: 1.5rem; border-radius: 12px; border-left: 4px solid #0091EA; text-align: center;'>
                <div style='font-size: 3rem; margin-bottom: 0.5rem;'>📐</div>
                <h4 style='color: #0091EA; margin: 0.5rem 0;'>Lineamientos</h4>
                <p style='color: var(--text-secondary); font-size: 0.9rem; margin: 0;'>
                    Guías Técnicas
                </p>
                <div style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
                    <span style='font-size: 1.5rem; font-weight: 700; color: #0091EA;'>3</span>
                    <p style='font-size: 0.8rem; color: var(--text-secondary); margin: 0.25rem 0 0 0;'>Lineamientos</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div style='background: linear-gradient(135deg, rgba(0, 184, 217, 0.2), rgba(0, 188, 212, 0.1)); 
                        padding: 1.5rem; border-radius: 12px; border-left: 4px solid #00B8D9; text-align: center; margin-top: 1rem;'>
                <div style='font-size: 3rem; margin-bottom: 0.5rem;'>🌍</div>
                <h4 style='color: #00B8D9; margin: 0.5rem 0;'>Internacional</h4>
                <p style='color: var(--text-secondary); font-size: 0.9rem; margin: 0;'>
                    OMS, EPA, Canadá
                </p>
                <div style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
                    <span style='font-size: 1.5rem; font-weight: 700; color: #00B8D9;'>6</span>
                    <p style='font-size: 0.8rem; color: var(--text-secondary); margin: 0.25rem 0 0 0;'>Estándares</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Beneficios del sistema
        st.markdown("""
        <div class='success-box' style='margin-top: 2rem;'>
            <h4 style='margin-top: 0; color: white;'>✓ Beneficios del Sistema</h4>
            <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;'>
                <div>
                    <strong style='color: white;'>📄 Acceso Directo</strong><br>
                    <span style='color: rgba(255,255,255,0.9); font-size: 0.95rem;'>
                        Enlaces actualizados a documentos oficiales
                    </span>
                </div>
                <div>
                    <strong style='color: white;'>📊 Visualizaciones</strong><br>
                    <span style='color: rgba(255,255,255,0.9); font-size: 0.95rem;'>
                        Gráficos interactivos para análisis comparativo
                    </span>
                </div>
                <div>
                    <strong style='color: white;'>✅ Información Validada</strong><br>
                    <span style='color: rgba(255,255,255,0.9); font-size: 0.95rem;'>
                        Datos técnicos verificados y referencias completas
                    </span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
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
        
        st.markdown("""
        <div class='info-box'>
            <p style='font-size: 0.9rem;'>
                <strong>💡 Sugerencia:</strong> Utilice el buscador del menú lateral para encontrar 
                normativas específicas rápidamente.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Gráfico comparativo mejorado
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
    
    fig = px.bar(
        datos_comp, 
        x='Entidad', 
        y='Valor',
        color='Tipo',
        color_discrete_map={'Internacional': '#00B8D9', 'Nacional': '#FFB300'},
        text='Valor',
        title=''
    )
    
    fig.update_traces(
        texttemplate='%{text} μg/m³', 
        textposition='outside',
        marker=dict(
            line=dict(color='rgba(255,255,255,0.2)', width=1),
            pattern=dict(shape="")
        )
    )
    
    fig.update_layout(
        height=500,
        showlegend=True,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#E3E8EF', size=13, family='Inter'),
        xaxis=dict(
            showgrid=False,
            title='',
            tickfont=dict(size=12)
        ),
        yaxis=dict(
            showgrid=True, 
            gridcolor='rgba(255,255,255,0.06)',
            title='Concentración (μg/m³)',
            titlefont=dict(size=12)
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
    
    st.markdown("""
    <div class='warning-box'>
        <p><strong>⚠️ Análisis:</strong> El estándar peruano de PM2.5 anual (25 μg/m³) es 5 veces más 
        permisivo que la recomendación de la OMS (5 μg/m³) y 2.8 veces más alto que el estándar de EPA USA (9 μg/m³). 
        Se recomienda evaluar una actualización gradual de los ECA nacionales para una mejor protección de la salud pública.</p>
    </div>
    """, unsafe_allow_html=True)
