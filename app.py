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
        background: linear-gradient(135deg, #FF6F00 0%, #FF9800 100%);
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
        Navegacion Rapida
    </h3>
    """, unsafe_allow_html=True)
    
    busqueda = st.text_input("Buscar normativa...", placeholder="Ej: PM2.5, ECA, protocolo...", key="search_input")
    
    if busqueda:
        busqueda_lower = busqueda.lower()
        
        keywords = {
            "ECA": ["eca", "estandar", "calidad ambiental", "pm2.5", "pm10", "no2", "so2", "co", "o3", "ozono", "003-2017", "010-2019", "074-2001"],
            "LMP": ["lmp", "limite", "maximo permisible", "emision", "termoelectrica", "vehicular", "mineria", "003-2010", "011-2009", "010-2010"],
            "Protocolo": ["protocolo", "monitoreo", "digesa", "medicion", "muestreo", "1404-2005", "026-2000", "195-2010"],
            "Lineamiento": ["lineamiento", "inventario", "alerta", "estado de alerta", "181-2016", "009-2003", "1278"],
            "Medidas": ["medida", "control", "tecnologia", "filtro", "precipitador", "scrubber", "fgd", "scr", "nox", "28611"],
            "Normativas": ["internacional", "oms", "who", "epa", "usa", "canada", "naaqs", "caaqs", "guia"]
        }
        
        mejor_match = None
        max_coincidencias = 0
        
        for pagina, palabras in keywords.items():
            coincidencias = sum(1 for palabra in palabras if palabra in busqueda_lower)
            if coincidencias > max_coincidencias:
                max_coincidencias = coincidencias
                mejor_match = pagina
        
        if mejor_match and max_coincidencias > 0:
            st.success(f"Encontrado en: **{mejor_match}**")
            if st.button(f"Ir a {mejor_match}", use_container_width=True, type="primary", key="search_go"):
                st.session_state.pagina = mejor_match
                st.rerun()
        else:
            st.warning("No se encontraron resultados. Intenta con: ECA, LMP, Protocolo, PM2.5, etc.")
    
    st.markdown("---")
    
    st.markdown("""
    <h4 style='color: white; font-weight: 700; font-size: 1rem; margin-bottom: 0.75rem; margin-top: 0.5rem; text-shadow: 0 2px 4px rgba(0,0,0,0.5);'>
        Secciones
    </h4>
    """, unsafe_allow_html=True)
    
    if st.button("Inicio", use_container_width=True, key="nav_inicio"):
        st.session_state.pagina = "Inicio"
    
    if st.button("Estandares ECA", use_container_width=True, key="nav_eca"):
        st.session_state.pagina = "ECA"
    
    if st.button("Limites LMP", use_container_width=True, key="nav_lmp"):
        st.session_state.pagina = "LMP"
    
    if st.button("Protocolos", use_container_width=True, key="nav_protocolo"):
        st.session_state.pagina = "Protocolo"
    
    if st.button("Lineamientos", use_container_width=True, key="nav_lineamiento"):
        st.session_state.pagina = "Lineamiento"
    
    if st.button("Control de Emisiones", use_container_width=True, key="nav_medidas"):
        st.session_state.pagina = "Medidas"
    
    if st.button("Normativas Internacionales", use_container_width=True, key="nav_normativas"):
        st.session_state.pagina = "Normativas"
    
    st.markdown("---")
    
    st.markdown("""
    <h4 style='color: white; font-weight: 700; font-size: 1rem; margin-bottom: 0.5rem; margin-top: 0.5rem; text-shadow: 0 2px 4px rgba(0,0,0,0.5);'>
        Estadisticas
    </h4>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Normativas", "18+")
    with col2:
        st.metric("Paises", "4")
    
    st.markdown("---")
    
    st.markdown("""
    <h4 style='color: white; font-weight: 700; font-size: 1rem; margin-bottom: 0.5rem; margin-top: 0.5rem; text-shadow: 0 2px 4px rgba(0,0,0,0.5);'>
        Informacion
    </h4>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class='info-box'>
        <p style='font-size: 0.85rem;'><strong>Ultima actualizacion:</strong><br>Octubre 2024</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("Contacto"):
        st.markdown("""
        <p style='color: rgba(255,255,255,0.95); line-height: 1.8;'>
        <strong style='color: white;'>Universidad Nacional de Moquegua</strong><br>
        Facultad de Ingenieria y Arquitectura<br><br>
        
        contacto@unam.edu.pe<br>
        +51 XXX XXX XXX
        </p>
        """, unsafe_allow_html=True)

# Header institucional premium
st.markdown(f"""
<div class='institutional-header fade-in'>
    <h1>Marco Normativo de Calidad del Aire</h1>
    <p class='subtitle'>Sistema Integral de Consulta de Normativas Ambientales</p>
    <div class='metadata'>
        <strong>Universidad Nacional de Moquegua</strong> | 
        Facultad de Ingenieria y Arquitectura | 
        Prof. Dr. Jose Antonio Valeriano Zapana | 
        <span style='opacity: 0.7;'>{datetime.now().strftime('%d/%m/%Y')}</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Breadcrumb
breadcrumb_map = {
    "Inicio": "Inicio",
    "ECA": "Estandares ECA",
    "LMP": "Limites LMP",
    "Protocolo": "Protocolos",
    "Lineamiento": "Lineamientos",
    "Medidas": "Control de Emisiones",
    "Normativas": "Normativas Internacionales"
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
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(label="Normativas Nacionales", value="12", delta="Vigentes")
    
    with col2:
        st.metric(label="Estandares Internacionales", value="6", delta="OMS, EPA, Canada")
    
    with col3:
        st.metric(label="Contaminantes Regulados", value="8", delta="Criterio")
    
    with col4:
        st.metric(label="Protocolos Activos", value="5", delta="Monitoreo")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class='corporate-card fade-in'>
            <h2>Evolucion del Marco Normativo Peruano</h2>
            <p style='font-size: 1.05rem; margin-bottom: 2rem;'>
                Recorrido historico de las principales normativas de calidad del aire en Peru
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        timeline_data = [
            {'año': 1996, 'titulo': 'R.M. N 315-96-EM/VMM', 'categoria': 'LMP', 'descripcion': 'Primeros limites para fundiciones y refinerias mineras'},
            {'año': 2000, 'titulo': 'R.M. N 026-2000-ITINCI/DM', 'categoria': 'Protocolo', 'descripcion': 'Protocolo de monitoreo industrial'},
            {'año': 2001, 'titulo': 'D.S. N 074-2001-PCM', 'categoria': 'ECA', 'descripcion': 'Primeros Estandares de Calidad Ambiental para Aire'},
            {'año': 2003, 'titulo': 'D.S. N 009-2003-SA', 'categoria': 'Lineamiento', 'descripcion': 'Niveles de Estados de Alerta Nacional'},
            {'año': 2005, 'titulo': 'R.D. N 1404-2005/DIGESA', 'categoria': 'Protocolo', 'descripcion': 'Protocolo de Monitoreo de Calidad del Aire'},
            {'año': 2005, 'titulo': 'Ley N 28611', 'categoria': 'Marco Legal', 'descripcion': 'Ley General del Ambiente'},
            {'año': 2009, 'titulo': 'D.S. N 011-2009-MINAM', 'categoria': 'LMP', 'descripcion': 'Limites para vehiculos automotores'},
            {'año': 2010, 'titulo': 'D.S. N 003-2010-MINAM', 'categoria': 'LMP', 'descripcion': 'Limites para centrales termoelectricas'},
            {'año': 2010, 'titulo': 'D.S. N 010-2010-MINAM', 'categoria': 'LMP', 'descripcion': 'Limites para industrias manufactureras'},
            {'año': 2016, 'titulo': 'R.M. N 181-2016-MINAM', 'categoria': 'Lineamiento', 'descripcion': 'Lineamientos para Inventario de Emisiones'},
            {'año': 2017, 'titulo': 'D.S. N 003-2017-MINAM', 'categoria': 'ECA', 'descripcion': 'Actualizacion de Estandares de Calidad Ambiental'},
            {'año': 2018, 'titulo': 'Ley N 30754', 'categoria': 'Marco Legal', 'descripcion': 'Ley Marco sobre Cambio Climatico'},
            {'año': 2019, 'titulo': 'D.S. N 010-2019-MINAM', 'categoria': 'ECA', 'descripcion': 'Modificatoria de ECA para Aire'}
        ]
        
        df_timeline = pd.DataFrame(timeline_data)
        
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
                              '<i>Ano: %{x}</i><extra></extra>',
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
                title='Ano',
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
        
        st.markdown("""
        <div class='corporate-card' style='margin-top: 2rem;'>
            <h3 style='text-align: center; margin-bottom: 1.5rem;'>Categorias del Sistema Normativo</h3>
        </div>
        """, unsafe_allow_html=True)
        
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            st.markdown("""
            <div style='background: linear-gradient(135deg, rgba(0, 200, 83, 0.2), rgba(0, 230, 118, 0.1)); 
                        padding: 1.5rem; border-radius: 12px; border-left: 4px solid #00C853; text-align: center;'>
                <div style='font-size: 3rem; margin-bottom: 0.5rem;'>&#128203;</div>
                <h4 style='color: #00C853; margin: 0.5rem 0;'>ECA</h4>
                <p style='color: var(--text-secondary); font-size: 0.9rem; margin: 0;'>
                    Estandares de Calidad Ambiental del Aire
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
                <div style='font-size: 3rem; margin-bottom: 0.5rem;'>&#128214;</div>
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
                <div style='font-size: 3rem; margin-bottom: 0.5rem;'>&#127981;</div>
                <h4 style='color: #FF6F00; margin: 0.5rem 0;'>LMP</h4>
                <p style='color: var(--text-secondary); font-size: 0.9rem; margin: 0;'>
                    Limites Maximos Permisibles
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
                <div style='font-size: 3rem; margin-bottom: 0.5rem;'>&#9878;</div>
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
                <div style='font-size: 3rem; margin-bottom: 0.5rem;'>&#128208;</div>
                <h4 style='color: #0091EA; margin: 0.5rem 0;'>Lineamientos</h4>
                <p style='color: var(--text-secondary); font-size: 0.9rem; margin: 0;'>
                    Guias Tecnicas
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
                <div style='font-size: 3rem; margin-bottom: 0.5rem;'>&#127757;</div>
                <h4 style='color: #00B8D9; margin: 0.5rem 0;'>Internacional</h4>
                <p style='color: var(--text-secondary); font-size: 0.9rem; margin: 0;'>
                    OMS, EPA, Canada
                </p>
                <div style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
                    <span style='font-size: 1.5rem; font-weight: 700; color: #00B8D9;'>6</span>
                    <p style='font-size: 0.8rem; color: var(--text-secondary); margin: 0.25rem 0 0 0;'>Estandares</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='success-box' style='margin-top: 2rem;'>
            <h4 style='margin-top: 0; color: white;'>Beneficios del Sistema</h4>
            <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;'>
                <div>
                    <strong style='color: white;'>Acceso Directo</strong><br>
                    <span style='color: rgba(255,255,255,0.9); font-size: 0.95rem;'>
                        Enlaces actualizados a documentos oficiales
                    </span>
                </div>
                <div>
                    <strong style='color: white;'>Visualizaciones</strong><br>
                    <span style='color: rgba(255,255,255,0.9); font-size: 0.95rem;'>
                        Graficos interactivos para analisis comparativo
                    </span>
                </div>
                <div>
                    <strong style='color: white;'>Informacion Validada</strong><br>
                    <span style='color: rgba(255,255,255,0.9); font-size: 0.95rem;'>
                        Datos tecnicos verificados y referencias completas
                    </span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='corporate-card fade-in'>
            <h2>Acceso Directo</h2>
            <p style='color: rgba(255,255,255,0.95); margin-bottom: 1.5rem;'>
                Navegue rapidamente a las secciones principales
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Estandares ECA", use_container_width=True, type="primary", key="quick_eca"):
            st.session_state.pagina = "ECA"
            st.rerun()
        
        if st.button("Limites LMP", use_container_width=True, key="quick_lmp"):
            st.session_state.pagina = "LMP"
            st.rerun()
        
        if st.button("Protocolos", use_container_width=True, key="quick_protocolo"):
            st.session_state.pagina = "Protocolo"
            st.rerun()
        
        if st.button("Lineamientos", use_container_width=True, key="quick_lineamiento"):
            st.session_state.pagina = "Lineamiento"
            st.rerun()
        
        if st.button("Control Emisiones", use_container_width=True, key="quick_medidas"):
            st.session_state.pagina = "Medidas"
            st.rerun()
        
        if st.button("Normativas Mundial", use_container_width=True, key="quick_normativas"):
            st.session_state.pagina = "Normativas"
            st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class='info-box'>
            <p style='font-size: 0.9rem;'>
                <strong>Sugerencia:</strong> Utilice el buscador del menu lateral para encontrar 
                normativas especificas rapidamente.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>Analisis Comparativo: PM2.5 Anual</h2>
        <p style='color: var(--text-secondary); margin-bottom: 1.5rem;'>
            Comparacion de estandares internacionales vs. normativa peruana vigente
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    datos_comp = pd.DataFrame([
        {'Entidad': 'OMS 2021', 'Valor': 5, 'Tipo': 'Internacional'},
        {'Entidad': 'EPA USA 2024', 'Valor': 9, 'Tipo': 'Internacional'},
        {'Entidad': 'Canada 2025', 'Valor': 8, 'Tipo': 'Internacional'},
        {'Entidad': 'OEFA Peru', 'Valor': 25, 'Tipo': 'Nacional'}
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
        marker=dict(line=dict(color='rgba(255,255,255,0.2)', width=1))
    )
    
    fig.update_layout(
        height=500,
        showlegend=True,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#E3E8EF', size=13, family='Inter'),
        xaxis=dict(showgrid=False, title='', tickfont=dict(size=12)),
        yaxis=dict(
            showgrid=True, 
            gridcolor='rgba(255,255,255,0.06)',
            title='Concentracion (μg/m³)',
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
        <p><strong>Analisis:</strong> El estandar peruano de PM2.5 anual (25 μg/m³) es 5 veces mas 
        permisivo que la recomendacion de la OMS (5 μg/m³) y 2.8 veces mas alto que el estandar de EPA USA (9 μg/m³). 
        Se recomienda evaluar una actualizacion gradual de los ECA nacionales para una mejor proteccion de la salud publica.</p>
    </div>
    """, unsafe_allow_html=True)
    # ===================== PÁGINA ECA =====================
elif st.session_state.pagina == "ECA":
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>Estandares de Calidad Ambiental (ECA)</h2>
        <p style='font-size: 1.05rem;'>
            Los ECA establecen los <strong>niveles de concentracion de contaminantes en el aire ambiente</strong> 
            que no deben superarse para proteger la salud de la poblacion. Se miden en estaciones de monitoreo 
            de calidad del aire y son de cumplimiento obligatorio en todo el territorio nacional.
        </p>
        
        <div class='info-box' style='margin-top: 1.5rem;'>
            <p><strong>Diferencia clave:</strong> ECA se mide en aire ambiente (lo que respiramos), 
            mientras que LMP se mide en la fuente de emision (chimeneas, ductos).</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>VIGENTE</span>
        <h3>D.S. N 003-2017-MINAM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Estandares de Calidad Ambiental (ECA) para Aire</strong>
        </p>
        <p>
            Norma principal que establece los valores de concentracion maxima de contaminantes del aire 
            que no deben superarse para proteger la salud humana y el ambiente. Incluye PM2.5, PM10, SO2, 
            NO2, O3, CO, Pb, H2S y BaP. Establece periodos de cumplimiento y metodos de referencia.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicacion:</strong> 07 de junio de 2017 | 
            <strong>Vigencia:</strong> Desde junio 2017
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2017/06/DS-003-2017-MINAM.pdf' 
           target='_blank' class='corporate-button'>
            Descargar D.S. 003-2017-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card modificatoria fade-in'>
        <span class='status-badge modificatoria'>MODIFICATORIA</span>
        <h3>D.S. N 010-2019-MINAM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Modificatoria del D.S. N 003-2017-MINAM</strong>
        </p>
        <p>
            Actualiza parametros y periodos de evaluacion de los ECA para aire. Modifica las formas de 
            cumplimiento de algunos estandares adaptandose a nueva evidencia cientifica sobre efectos en 
            la salud publica y capacidades de monitoreo nacional.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicacion:</strong> 12 de julio de 2019 | 
            <strong>Vigencia:</strong> Desde julio 2019
        </p>
        <a href='https://busquedas.elperuano.pe/download/url/decreto-supremo-que-modifica-el-decreto-supremo-n-003-2017-decreto-supremo-n-010-2019-minam-1792823-1' 
           target='_blank' class='corporate-button'>
            Descargar D.S. 010-2019-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card referencia fade-in'>
        <span class='status-badge referencia'>REFERENCIA HISTORICA</span>
        <h3>D.S. N 074-2001-PCM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Reglamento de Estandares Nacionales de Calidad Ambiental del Aire (Derogado)</strong>
        </p>
        <p>
            Primera norma que establecio los ECA para aire en Peru. Estuvo vigente durante 16 anos hasta 
            su reemplazo por el D.S. 003-2017-MINAM. Importante para contexto historico y analisis de la 
            evolucion normativa nacional en materia de calidad del aire.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicacion:</strong> 24 de junio de 2001 | 
            <strong>Derogacion:</strong> Junio 2017
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_074-2001-pcm.pdf' 
           target='_blank' class='corporate-button'>
            Ver D.S. 074-2001-PCM (Historico)
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>Valores de ECA Vigentes (D.S. 003-2017-MINAM)</h2>
        <p style='color: var(--text-secondary); margin-bottom: 1.5rem;'>
            Concentraciones maximas permitidas en aire ambiente para proteccion de salud publica
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    eca_valores = pd.DataFrame([
        ['PM2.5', '24 horas', 50, 'μg/m³', 'No exceder mas de 7 veces al ano'],
        ['PM2.5', 'Anual', 25, 'μg/m³', 'Media aritmetica anual'],
        ['PM10', '24 horas', 100, 'μg/m³', 'No exceder mas de 7 veces al ano'],
        ['PM10', 'Anual', 50, 'μg/m³', 'Media aritmetica anual'],
        ['NO2', '1 hora', 200, 'μg/m³', 'No exceder mas de 24 veces al ano'],
        ['NO2', 'Anual', 100, 'μg/m³', 'Media aritmetica anual'],
        ['SO2', '24 horas', 250, 'μg/m³', 'No exceder mas de 7 veces al ano'],
        ['O3', '8 horas', 100, 'μg/m³', 'Maximas diarias de promedios moviles'],
        ['CO', '8 horas', 10000, 'μg/m³', 'Promedio movil'],
        ['CO', '1 hora', 30000, 'μg/m³', 'No exceder mas de 1 vez al ano'],
        ['Pb', 'Mensual', 1.5, 'μg/m³', 'Media aritmetica mensual'],
        ['Pb', 'Anual', 0.5, 'μg/m³', 'Media aritmetica anual'],
        ['H2S', '24 horas', 150, 'μg/m³', 'Media aritmetica'],
        ['BaP', 'Anual', 0.0012, 'μg/m³', 'Media aritmetica anual']
    ], columns=['Contaminante', 'Periodo', 'Valor', 'Unidad', 'Forma del Estandar'])
    
    st.dataframe(eca_valores, use_container_width=True, hide_index=True, height=550)
    
    with st.expander("Ver informacion adicional sobre contaminantes criterio"):
        st.markdown("""
        #### Contaminantes Criterio Regulados
        
        **Material Particulado (PM2.5 y PM10)**
        - Particulas solidas o liquidas suspendidas en el aire
        - PM2.5: diametro ≤ 2.5 μm (penetran profundamente en pulmones)
        - PM10: diametro ≤ 10 μm (afectan vias respiratorias superiores)
        - Fuentes: combustion, polvo, actividades industriales
        
        **Dioxido de Nitrogeno (NO2)**
        - Gas irritante de color marron rojizo
        - Fuentes: combustion vehicular e industrial
        - Efectos: irritacion respiratoria, reduccion funcion pulmonar
        
        **Dioxido de Azufre (SO2)**
        - Gas incoloro con olor penetrante
        - Fuentes: combustion de combustibles fosiles con azufre
        - Efectos: irritacion respiratoria, enfermedades cardiovasculares
        
        **Ozono Troposferico (O3)**
        - Contaminante secundario (no se emite directamente)
        - Se forma por reaccion fotoquimica de NOx y COVs
        - Efectos: dano pulmonar, reduccion funcion respiratoria
        
        **Monoxido de Carbono (CO)**
        - Gas incoloro e inodoro
        - Fuentes: combustion incompleta
        - Efectos: reduce capacidad de transporte de oxigeno en sangre
        
        **Plomo (Pb)**
        - Metal pesado toxico
        - Fuentes: historicamente gasolina con plomo, industrias
        - Efectos: neurotoxicidad, afecta desarrollo infantil
        
        **Sulfuro de Hidrogeno (H2S)**
        - Gas con olor a huevo podrido
        - Fuentes: actividades petroleras, descomposicion materia organica
        - Efectos: irritacion ocular y respiratoria
        
        **Benzo(a)pireno (BaP)**
        - Hidrocarburo aromatico policiclico (HAP)
        - Fuentes: combustion incompleta de materia organica
        - Efectos: cancerigeno, mutagenico
        """)

# ===================== PÁGINA LMP =====================
elif st.session_state.pagina == "LMP":
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>Limites Maximos Permisibles (LMP)</h2>
        <p style='font-size: 1.05rem;'>
            Los LMP son <strong>valores de concentracion maxima de contaminantes</strong> que pueden 
            ser emitidos al ambiente desde una fuente puntual de emision (chimeneas, ductos). Son 
            especificos por sector productivo y tipo de actividad, estableciendo obligaciones para 
            el cumplimiento ambiental de las empresas.
        </p>
        
        <div class='info-box' style='margin-top: 1.5rem;'>
            <p><strong>Diferencia clave:</strong> Los LMP se aplican a la fuente emisora y son 
            medidos en el punto de descarga, mientras que los ECA se miden en el aire ambiente 
            que respira la poblacion.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>VIGENTE</span>
        <h3>D.S. N 003-2010-MINAM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>LMP de Emisiones Atmosfericas para Centrales Termoelectricas</strong>
        </p>
        <p>
            Establece limites de emision de NOx, SO2 y Material Particulado para plantas de generacion 
            termoelectrica. Los limites varian segun el tipo de combustible utilizado (gas natural, diesel, 
            residual). Mediciones en condiciones normalizadas: 25°C, 1 atm, base seca, 15% O2.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicacion:</strong> 17 de enero de 2010 | 
            <strong>Sector:</strong> Energia
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_003-2010-minam.pdf' 
           target='_blank' class='corporate-button'>
            Descargar D.S. 003-2010-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>VIGENTE</span>
        <h3>D.S. N 011-2009-MINAM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>LMP de Emisiones para Vehiculos Automotores</strong>
        </p>
        <p>
            Regula las emisiones de gases contaminantes de vehiculos automotores que circulan por la red 
            vial. Incluye limites para CO, HC, NOx y Material Particulado segun categoria vehicular 
            (ligeros, pesados) y tipo de combustible. Establece procedimientos de verificacion tecnica vehicular.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicacion:</strong> 13 de marzo de 2009 | 
            <strong>Sector:</strong> Transporte
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_011-2009-minam.pdf' 
           target='_blank' class='corporate-button'>
            Descargar D.S. 011-2009-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>VIGENTE</span>
        <h3>D.S. N 010-2010-MINAM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>LMP de Emisiones para Industrias de Cemento, Papel, Cerveza y Curtiembre</strong>
        </p>
        <p>
            Establece limites de emision atmosferica para industrias de cemento, papel, cerveza y curtiembre. 
            Regula emisiones de Material Particulado, SO2, NOx y otros contaminantes especificos segun el 
            proceso industrial. Define metodos de muestreo y analisis, asi como plazos de cumplimiento.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicacion:</strong> 17 de agosto de 2010 | 
            <strong>Sector:</strong> Industria Manufacturera
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_010-2010-minam.pdf' 
           target='_blank' class='corporate-button'>
            Descargar D.S. 010-2010-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>VIGENTE</span>
        <h3>R.M. N 315-96-EM/VMM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Niveles Maximos Permisibles para Fundiciones y Refinerias</strong>
        </p>
        <p>
            Establece los niveles maximos permisibles de emisiones de gases y particulas para las actividades 
            minero-metalurgicas de fundicion y refinacion. Regula emisiones de SO2, Material Particulado, 
            plomo, arsenico y otros metales pesados especificos de procesos metalurgicos.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicacion:</strong> 19 de julio de 1996 | 
            <strong>Sector:</strong> Mineria y Metalurgia
        </p>
        <a href='http://www.minem.gob.pe/minem/archivos/file/DGAAM/legislacion/resolucion/RM-315-96.pdf' 
           target='_blank' class='corporate-button'>
            Ver R.M. 315-96-EM/VMM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>LMP para Centrales Termoelectricas por Tipo de Combustible</h2>
        <p style='color: var(--text-secondary); margin-bottom: 1rem;'>
            D.S. 003-2010-MINAM | Condiciones: 25°C, 1 atm, base seca, 15% O2
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    lmp_termo = pd.DataFrame([
        ['Oxidos de Nitrogeno (NOx)', 320, 850, 2000, 'mg/Nm³'],
        ['Dioxido de Azufre (SO2)', 0, 1700, 3500, 'mg/Nm³'],
        ['Material Particulado (MP)', 50, 150, 350, 'mg/Nm³']
    ], columns=['Contaminante', 'Gas Natural', 'Diesel', 'Residual', 'Unidad'])
    
    st.dataframe(lmp_termo, use_container_width=True, hide_index=True, height=200)
    
    fig = go.Figure()
    
    contaminantes = lmp_termo['Contaminante'].tolist()
    
    fig.add_trace(go.Bar(
        name='Gas Natural',
        x=contaminantes,
        y=lmp_termo['Gas Natural'],
        marker_color='#00C853',
        text=lmp_termo['Gas Natural'],
        texttemplate='%{text}',
        textposition='outside'
    ))
    
    fig.add_trace(go.Bar(
        name='Diesel',
        x=contaminantes,
        y=lmp_termo['Diesel'],
        marker_color='#FFB300',
        text=lmp_termo['Diesel'],
        texttemplate='%{text}',
        textposition='outside'
    ))
    
    fig.add_trace(go.Bar(
        name='Residual',
        x=contaminantes,
        y=lmp_termo['Residual'],
        marker_color='#D32F2F',
        text=lmp_termo['Residual'],
        texttemplate='%{text}',
        textposition='outside'
    ))
    
    fig.update_layout(
        barmode='group',
        height=500,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#E3E8EF', size=13, family='Inter'),
        xaxis=dict(showgrid=False, title=''),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(255,255,255,0.06)',
            title='Concentracion (mg/Nm³)',
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
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    <div class='info-box'>
        <p><strong>Nota tecnica:</strong> Los limites son mas estrictos para combustibles mas limpios. 
        El gas natural tiene los LMP mas bajos debido a su menor contenido de azufre y mejor eficiencia 
        de combustion, mientras que el residual (combustoleo) tiene los limites mas permisivos debido 
        a su mayor contenido de impurezas.</p>
    </div>
    """, unsafe_allow_html=True)

# ===================== PÁGINA PROTOCOLO =====================
elif st.session_state.pagina == "Protocolo":
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>Protocolos de Monitoreo y Medicion</h2>
        <p style='font-size: 1.05rem;'>
            Los protocolos establecen <strong>procedimientos tecnicos estandarizados</strong> para el 
            monitoreo de calidad del aire y la medicion de emisiones atmosfericas. Garantizan que las 
            mediciones sean comparables, confiables y validas a nivel nacional, cumpliendo con estandares 
            internacionales de calidad analitica.
        </p>
        
        <div class='info-box' style='margin-top: 1.5rem;'>
            <p><strong>Importancia:</strong> Los protocolos aseguran la trazabilidad, precision y 
            validez legal de las mediciones ambientales realizadas por laboratorios acreditados y 
            empresas consultoras.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>VIGENTE</span>
        <h3>R.D. N 1404-2005/DIGESA/SA</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Protocolo de Monitoreo de Calidad del Aire y Gestion de Datos</strong>
        </p>
        <p>
            Define los procedimientos tecnicos para el monitoreo de calidad del aire ambiente en todo el 
            territorio nacional. Incluye metodos de muestreo, ubicacion de estaciones, calibracion de 
            equipos, analisis de laboratorio, aseguramiento y control de calidad, y gestion de datos. 
            Aplicable a redes de monitoreo publicas y privadas.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicacion:</strong> 11 de noviembre de 2005 | 
            <strong>Entidad:</strong> DIGESA-MINSA
        </p>
        <a href='http://www.digesa.minsa.gob.pe/DEPA/protocolo_calidad_aire.pdf' 
           target='_blank' class='corporate-button'>
            Descargar Protocolo DIGESA
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>VIGENTE</span>
        <h3>R.M. N 026-2000-ITINCI/DM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Protocolo de Monitoreo de Calidad de Aire y Emisiones - Sector Industrial</strong>
        </p>
        <p>
            Aprueba protocolos especificos de monitoreo de calidad de aire y emisiones atmosfericas para 
            actividades industriales manufactureras. Establece metodologias de muestreo isocinetico, analisis 
            de gases, y determinacion de caudales en fuentes fijas industriales.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicacion:</strong> 28 de febrero de 2000 | 
            <strong>Sector:</strong> Industria - PRODUCE
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2017/04/RM-026-2000-ITINCI.pdf' 
           target='_blank' class='corporate-button'>
            Ver R.M. 026-2000-ITINCI/DM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>VIGENTE</span>
        <h3>R.D. N 195-2010-MEM/AAM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Protocolo de Monitoreo de Calderos y Hornos Industriales</strong>
        </p>
        <p>
            Establece procedimientos estandarizados para el monitoreo de emisiones atmosfericas en calderos 
            y hornos industriales de diversos sectores. Incluye metodos isocineticos para material particulado, 
            analisis instrumental de gases (SO2, NOx, CO), y determinacion de parametros de proceso.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicacion:</strong> 12 de agosto de 2010 | 
            <strong>Sector:</strong> Energia y Minas
        </p>
        <a href='http://www.minem.gob.pe/minem/archivos/RD%20195-2010-AAM.pdf' 
           target='_blank' class='corporate-button'>
            Descargar R.D. 195-2010-MEM/AAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>VIGENTE</span>
        <h3>R.M. N 247-2009-MEM/DM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Protocolo de Monitoreo de Calidad de Agua y Aire - Mineria</strong>
        </p>
        <p>
            Protocolo especifico para actividades minero-metalurgicas que establece procedimientos de monitoreo 
            de calidad de aire en zonas de influencia minera. Define ubicacion de estaciones, frecuencias de 
            muestreo, parametros a evaluar y procedimientos de reporte ante autoridades sectoriales.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicacion:</strong> 14 de mayo de 2009 | 
            <strong>Sector:</strong> Mineria
        </p>
        <a href='http://www.minem.gob.pe/minem/archivos/file/DGAAM/guias/protocmonitoreoaire.pdf' 
           target='_blank' class='corporate-button'>
            Ver R.M. 247-2009-MEM/DM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>Metodos de Referencia EPA Adoptados en Peru</h2>
        <p style='color: var(--text-secondary); margin-bottom: 1rem;'>
            Metodos estandarizados de la Agencia de Proteccion Ambiental de EE.UU. (EPA) 
            reconocidos en normativa peruana para asegurar calidad analitica
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    metodos = pd.DataFrame([
        ['PM10', 'EPA Method 40 CFR Part 50, Appendix J', 'Muestreo gravimetrico con separador inercial', 'Alto volumen (Hi-Vol)'],
        ['PM2.5', 'EPA Method 40 CFR Part 50, Appendix L', 'Muestreo gravimetrico con separador inercial', 'Bajo volumen (Low-Vol)'],
        ['SO2', 'EPA Method 40 CFR Part 50, Appendix A-1', 'Fluorescencia UV pulsada', 'Analizador continuo'],
        ['NO2', 'EPA Method 40 CFR Part 50, Appendix F', 'Quimioluminiscencia', 'Analizador continuo'],
        ['CO', 'EPA Method 40 CFR Part 50, Appendix C', 'Espectrometria infrarroja no dispersiva (NDIR)', 'Analizador continuo'],
        ['O3', 'EPA Method 40 CFR Part 50, Appendix D', 'Fotometria de absorcion UV', 'Analizador continuo'],
        ['Pb', 'EPA Method 40 CFR Part 50, Appendix G', 'Espectrometria de absorcion atomica', 'Filtros PM10'],
        ['H2S', 'EPA Method 11', 'Tren de muestreo con solucion absorbente', 'Metodo manual']
    ], columns=['Contaminante', 'Metodo EPA', 'Tecnica Analitica', 'Tipo de Equipo'])
    
    st.dataframe(metodos, use_container_width=True, hide_index=True, height=380)
    
    with st.expander("Ver flujo de proceso de monitoreo de calidad del aire"):
        st.markdown("""
        #### Proceso Completo de Monitoreo
        
        **1. Planificacion**
        - Definicion de objetivos del monitoreo
        - Seleccion de ubicacion de estaciones (criterios de macro y microescala)
        - Determinacion de parametros y frecuencias de muestreo
        - Elaboracion de Plan de Monitoreo
        
        **2. Implementacion**
        - Instalacion y configuracion de equipos
        - Calibracion inicial con gases y patrones certificados
        - Verificacion de condiciones ambientales del sitio
        - Inicio de operacion segun protocolo
        
        **3. Operacion y Mantenimiento**
        - Calibraciones periodicas (diarias, semanales, mensuales)
        - Mantenimiento preventivo de equipos
        - Verificacion de flujos y condiciones operativas
        - Registro de eventos y anomalias
        
        **4. Aseguramiento de Calidad**
        - Auditorias internas y externas
        - Analisis de blancos y duplicados
        - Control de precision y exactitud
        - Validacion de datos
        
        **5. Analisis de Laboratorio**
        - Analisis gravimetrico (PM)
        - Analisis quimico (metales, iones)
        - Control de calidad analitico
        - Certificados de analisis
        
        **6. Gestion de Datos**
        - Transferencia y almacenamiento de datos
        - Validacion estadistica
        - Calculo de promedios segun ECA
        - Identificacion de excedencias
        
        **7. Reporte**
        - Informes tecnicos periodicos
        - Reportes a autoridades competentes
        - Publicacion de resultados (cuando aplique)
        - Acciones correctivas si hay excedencias
        """)

# ===================== PÁGINA LINEAMIENTO =====================
elif st.session_state.pagina == "Lineamiento":
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>Lineamientos y Guias Tecnicas</h2>
        <p style='font-size: 1.05rem;'>
            Los lineamientos son <strong>instrumentos tecnico-normativos complementarios</strong> que 
            proporcionan guias operativas para la implementacion de normativas ambientales. Establecen 
            metodologias, procedimientos y criterios tecnicos especificos para la gestion de calidad del aire.
        </p>
        
        <div class='info-box' style='margin-top: 1.5rem;'>
            <p><strong>Funcion:</strong> Los lineamientos facilitan la aplicacion practica de la normativa 
            legal, proporcionando herramientas tecnicas para su cumplimiento efectivo por parte de autoridades, 
            empresas y consultores.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>VIGENTE</span>
        <h3>R.M. N 181-2016-MINAM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Lineamientos para la Elaboracion del Inventario de Emisiones Atmosfericas</strong>
        </p>
        <p>
            Establece la metodologia estandarizada para elaborar inventarios de emisiones de contaminantes 
            atmosfericos a nivel nacional, regional y local. Incluye factores de emision, procedimientos de 
            calculo, categorizacion de fuentes, y formatos de reporte. Aplicable a autoridades ambientales 
            y titulares de actividades productivas.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicacion:</strong> 13 de julio de 2016 | 
            <strong>Ambito:</strong> Nacional
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2016/07/RM-N%C2%B0-181-2016-MINAM.pdf' 
           target='_blank' class='corporate-button'>
            Descargar R.M. 181-2016-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>VIGENTE</span>
        <h3>D.S. N 009-2003-SA</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Reglamento de Niveles de Estados de Alerta Nacionales para Contaminantes del Aire</strong>
        </p>
        <p>
            Define los niveles de alerta ambiental (Cuidado, Peligro y Emergencia) ante episodios criticos 
            de contaminacion del aire. Establece umbrales de concentracion que activan protocolos de emergencia, 
            acciones obligatorias para autoridades y poblacion, y mecanismos de comunicacion publica del riesgo.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicacion:</strong> 25 de junio de 2003 | 
            <strong>Entidad:</strong> MINSA
        </p>
        <a href='http://www.digesa.minsa.gob.pe/NormasLegales/Normas/DS_009-2003-SA.pdf' 
           target='_blank' class='corporate-button'>
            Descargar D.S. 009-2003-SA
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>VIGENTE</span>
        <h3>Decreto Legislativo N 1278</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Ley de Gestion Integral de Residuos Solidos</strong>
        </p>
        <p>
            Establece lineamientos para el control de emisiones atmosfericas de instalaciones de tratamiento, 
            valorizacion e incineracion de residuos solidos. Define obligaciones de monitoreo continuo de 
            emisiones (CEMS), limites operativos y procedimientos de reporte ante autoridades sanitarias y ambientales.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicacion:</strong> 23 de diciembre de 2016 | 
            <strong>Vigencia:</strong> Desde diciembre 2017
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2017/04/Decreto-Legislativo-N%C2%B0-1278.pdf' 
           target='_blank' class='corporate-button'>
            Ver Decreto Legislativo 1278
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>VIGENTE</span>
        <h3>Ley N 30754</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Ley Marco sobre Cambio Climatico - Componente Calidad del Aire</strong>
        </p>
        <p>
            Establece el marco institucional para la gestion integral del cambio climatico en el pais. 
            Incluye lineamientos para la reduccion de contaminantes climaticos de vida corta (CCVC) como 
            el carbono negro, considerando sus efectos simultaneos en calidad del aire y clima.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicacion:</strong> 18 de abril de 2018 | 
            <strong>Ambito:</strong> Nacional
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2018/10/Ley-N%C2%B0-30754.pdf' 
           target='_blank' class='corporate-button'>
            Ver Ley 30754
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>Niveles de Estados de Alerta Nacional (D.S. 009-2003-SA)</h2>
        <p style='color: var(--text-secondary); margin-bottom: 1rem;'>
            Umbrales de concentracion que activan protocolos de emergencia ambiental
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    niveles = pd.DataFrame([
        ['PM10', 'Cuidado', 250, 350, 'μg/m³', 'Informacion a grupos sensibles'],
        ['PM10', 'Peligro', 350, 420, 'μg/m³', 'Alerta general a poblacion'],
        ['PM10', 'Emergencia', '> 420', '---', 'μg/m³', 'Emergencia sanitaria regional'],
        ['SO2', 'Cuidado', 500, 1000, 'μg/m³', 'Advertencia a grupos sensibles'],
        ['SO2', 'Peligro', 1000, 1600, 'μg/m³', 'Restriccion actividades al aire libre'],
        ['SO2', 'Emergencia', '> 1600', '---', 'μg/m³', 'Suspension actividades productivas'],
        ['NO2', 'Cuidado', 600, 1200, 'μg/m³', 'Alerta a grupos de riesgo'],
        ['NO2', 'Peligro', 1200, 1600, 'μg/m³', 'Reduccion trafico vehicular'],
        ['NO2', 'Emergencia', '> 1600', '---', 'μg/m³', 'Cierre de vias principales'],
        ['CO', 'Cuidado', 15000, 30000, 'μg/m³', 'Informacion preventiva'],
        ['CO', 'Peligro', 30000, 40000, 'μg/m³', 'Restriccion circulacion vehicular'],
        ['CO', 'Emergencia', '> 40000', '---', 'μg/m³', 'Estado de emergencia sanitaria']
    ], columns=['Contaminante', 'Nivel de Alerta', 'Limite Inferior', 'Limite Superior', 'Unidad', 'Accion Requerida'])
    
    st.dataframe(niveles, use_container_width=True, hide_index=True, height=500)
    
    st.markdown("""
    <div class='warning-box'>
        <p><strong>Protocolo de activacion:</strong> Las autoridades ambientales y de salud deben 
        activar los niveles de alerta cuando se registren o pronostiquen concentraciones en los rangos 
        establecidos. Las medidas incluyen difusion masiva de informacion, restriccion de actividades, 
        y en casos de emergencia, la declaratoria de estado de emergencia ambiental.</p>
    </div>
    """, unsafe_allow_html=True)

# ===================== PÁGINA MEDIDAS =====================
elif st.session_state.pagina == "Medidas":
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>Medidas y Tecnologias de Control de Emisiones</h2>
        <p style='font-size: 1.05rem;'>
            Las tecnologias de control son <strong>sistemas y equipos disenados para reducir las emisiones</strong> 
            de contaminantes atmosfericos desde fuentes puntuales. Su implementacion es obligatoria para cumplir 
            con los LMP establecidos y representan la mejor tecnologia disponible economicamente viable (BATEA).
        </p>
        
        <div class='info-box' style='margin-top: 1.5rem;'>
            <p><strong>Marco legal:</strong> La Ley General del Ambiente (Ley 28611) establece la obligacion 
            de implementar medidas de prevencion y control de la contaminacion del aire, priorizando tecnologias 
            limpias y sistemas de reduccion de emisiones.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>VIGENTE</span>
        <h3>Ley N 28611 - Ley General del Ambiente</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Titulo II, Capitulo 3: De la Calidad Ambiental</strong>
        </p>
        <p>
            Establece la obligacion legal de implementar medidas de prevencion, control y remediacion de la 
            contaminacion del aire. Define responsabilidades de titulares de actividades productivas para 
            adoptar tecnologias limpias, sistemas de tratamiento de emisiones y programas de monitoreo continuo.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicacion:</strong> 15 de octubre de 2005 | 
            <strong>Ambito:</strong> Marco general ambiental
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2017/04/Ley-N%C2%B0-28611.pdf' 
           target='_blank' class='corporate-button'>
            Ver Ley 28611
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>VIGENTE</span>
        <h3>D.S. N 012-2005-EM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Reglamento de Plan de Cierre de Minas - Control de Emisiones</strong>
        </p>
        <p>
            Incluye obligaciones especificas de implementacion y mantenimiento de sistemas de control de 
            emisiones atmosfericas durante las fases de operacion, cierre progresivo y cierre final de 
            operaciones mineras. Define responsabilidades tecnicas y financieras para asegurar el cumplimiento 
            a largo plazo.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicacion:</strong> 05 de agosto de 2005 | 
            <strong>Sector:</strong> Mineria
        </p>
        <a href='http://www.minem.gob.pe/minem/archivos/file/Mineria/LEGISLACION/2005/agosto/DS012-2005.pdf' 
           target='_blank' class='corporate-button'>
            Ver D.S. 012-2005-EM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card ntp fade-in'>
        <span class='status-badge ntp'>NORMAS TECNICAS</span>
        <h3>Normas Tecnicas Peruanas (NTP) - INACAL</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Gestion Ambiental del Aire - Metodologias y Terminologia</strong>
        </p>
        <p>
            <strong>NTP 900.058:2019</strong> - Gestion Ambiental. Calidad del Aire. Metodos de muestreo<br>
            <strong>NTP 900.030:2003</strong> - Gestion Ambiental. Calidad del Aire. Terminologia<br>
            <strong>NTP-ISO 9169:2014</strong> - Calidad del aire. Determinacion de caracteristicas de funcionamiento<br><br>
            Normas tecnicas que establecen procedimientos estandarizados para evaluacion de eficiencia de 
            sistemas de control, metodos de medicion de emisiones, y terminologia tecnica normalizada.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Entidad emisora:</strong> Instituto Nacional de Calidad (INACAL)
        </p>
        <a href='https://www.inacal.gob.pe/repositorioaps/data/1/1/1/jer/ctnprocedimiento/files/Catalogo_NTP_Vigentes_2023.pdf' 
           target='_blank' class='corporate-button'>
            Ver Catalogo NTP INACAL
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>Tecnologias de Control de Emisiones por Contaminante</h2>
        <p style='color: var(--text-secondary); margin-bottom: 1rem;'>
            Principales sistemas utilizados en la industria peruana para cumplimiento de LMP
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    tecnologias = pd.DataFrame([
        ['Material Particulado', 'Filtros de mangas (Baghouse)', '>99%', 'Captacion por filtracion textil', 'Media-Alta', 'Alto', 'Industria general'],
        ['Material Particulado', 'Precipitadores electrostaticos (ESP)', '95-99%', 'Carga electrica y coleccion', 'Alta', 'Medio', 'Termoelectricas, cemento'],
        ['Material Particulado', 'Ciclones', '70-90%', 'Separacion por fuerza centrifuga', 'Baja', 'Bajo', 'Pre-tratamiento'],
        ['Material Particulado', 'Lavadores humedos (Scrubbers)', '85-95%', 'Absorcion liquido-gas', 'Media', 'Medio', 'Industria quimica'],
        ['SO2', 'Desulfuracion humeda (FGD)', '>95%', 'Absorcion con caliza/cal + agua', 'Muy Alta', 'Alto', 'Termoelectricas, fundiciones'],
        ['SO2', 'Desulfuracion seca (SDA)', '80-95%', 'Inyeccion de sorbente seco', 'Alta', 'Medio-Alto', 'Industria general'],
        ['SO2', 'Scrubber de doble alcali', '90-98%', 'Absorcion NaOH regenerativo', 'Alta', 'Alto', 'Metalurgia'],
        ['NOx', 'Reduccion Catalitica Selectiva (SCR)', '>90%', 'Reduccion con NH3/urea + catalizador', 'Muy Alta', 'Muy Alto', 'Termoelectricas, cemento'],
        ['NOx', 'Reduccion No Catalitica (SNCR)', '40-60%', 'Inyeccion termica de urea', 'Media', 'Medio', 'Calderos, hornos'],
        ['NOx', 'Quemadores Low-NOx', '30-50%', 'Control de combustion (T y O2)', 'Media', 'Bajo-Medio', 'Calderos industriales'],
        ['NOx', 'Recirculacion de gases (FGR)', '20-40%', 'Reduccion T de llama', 'Baja-Media', 'Bajo', 'Calderos pequenos'],
        ['COVs', 'Oxidacion termica', '>95%', 'Combustion 700-850°C', 'Alta', 'Alto', 'Quimica, pinturas'],
        ['COVs', 'Oxidacion catalitica', '>90%', 'Combustion catalitica 350-450°C', 'Alta', 'Medio-Alto', 'Imprentas, recubrimientos'],
        ['COVs', 'Adsorcion carbon activado', '85-95%', 'Captura en microporos', 'Media', 'Medio', 'Baja concentracion'],
        ['COVs', 'Condensacion criogenica', '80-90%', 'Enfriamiento bajo punto rocio', 'Alta', 'Alto', 'Recuperacion solventes'],
        ['CO', 'Oxidacion catalitica', '>98%', 'Conversion CO a CO2', 'Media-Alta', 'Medio', 'Escape vehicular, hornos']
    ], columns=['Contaminante', 'Tecnologia', 'Eficiencia', 'Principio de Operacion', 'Complejidad', 'Costo', 'Aplicacion Principal'])
    
    st.dataframe(tecnologias, use_container_width=True, hide_index=True, height=650)
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>Comparacion de Eficiencias de Remocion</h2>
        <p style='color: var(--text-secondary); margin-bottom: 1rem;'>
            Eficiencia tipica de principales tecnologias de control
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    eficiencias_data = pd.DataFrame([
        {'Tecnologia': 'Filtros mangas', 'Eficiencia': 99.5, 'Tipo': 'Material Particulado'},
        {'Tecnologia': 'ESP', 'Eficiencia': 97, 'Tipo': 'Material Particulado'},
        {'Tecnologia': 'Ciclones', 'Eficiencia': 80, 'Tipo': 'Material Particulado'},
        {'Tecnologia': 'FGD Humedo', 'Eficiencia': 97, 'Tipo': 'SO2'},
        {'Tecnologia': 'SDA Seco', 'Eficiencia': 87.5, 'Tipo': 'SO2'},
        {'Tecnologia': 'SCR', 'Eficiencia': 92, 'Tipo': 'NOx'},
        {'Tecnologia': 'SNCR', 'Eficiencia': 50, 'Tipo': 'NOx'},
        {'Tecnologia': 'Low-NOx', 'Eficiencia': 40, 'Tipo': 'NOx'},
        {'Tecnologia': 'Oxidacion termica', 'Eficiencia': 97, 'Tipo': 'COVs'},
        {'Tecnologia': 'Carbon activado', 'Eficiencia': 90, 'Tipo': 'COVs'}
    ])
    
    fig2 = px.bar(
        eficiencias_data,
        x='Tecnologia',
        y='Eficiencia',
        color='Tipo',
        color_discrete_map={
            'Material Particulado': '#00B8D9',
            'SO2': '#FFB300',
            'NOx': '#00C853',
            'COVs': '#D32F2F'
        },
        text='Eficiencia'
    )
    
    fig2.update_traces(
        texttemplate='%{text}%',
        textposition='outside',
        marker=dict(line=dict(color='rgba(255,255,255,0.2)', width=1))
    )
    
    fig2.update_layout(
        height=500,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#E3E8EF', size=12, family='Inter'),
        xaxis=dict(showgrid=False, title='', tickangle=-45),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(255,255,255,0.06)',
            title='Eficiencia de Remocion (%)',
            range=[0, 105]
        ),
        legend=dict(
            title='Tipo de Contaminante',
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
    
    st.plotly_chart(fig2, use_container_width=True)
    # ===================== PÁGINA NORMATIVAS INTERNACIONALES =====================
elif st.session_state.pagina == "Normativas":
    
    st.markdown("<h1 style='text-align: center; margin-bottom: 2rem;'>Normativas Internacionales de Calidad del Aire</h1>", unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["OMS", "EPA USA", "Canada", "Analisis Comparativo"])
    
    with tab1:
        st.markdown("""
        <div class='corporate-card fade-in'>
            <h2>Organizacion Mundial de la Salud (OMS)</h2>
            <p style='font-size: 1.05rem;'>
                La OMS establece las <strong>directrices globales mas estrictas</strong> para proteger 
                la salud publica de la contaminacion del aire basandose en la mejor evidencia cientifica disponible.
            </p>
            
            <div class='success-box' style='margin-top: 1.5rem;'>
                <p><strong>Referencia mundial:</strong> Las guias OMS son reconocidas internacionalmente como 
                la mejor evidencia cientifica disponible sobre efectos de la contaminacion del aire en la salud.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='normative-card internacional fade-in'>
            <span class='status-badge internacional'>GUIAS 2021</span>
            <h3>WHO Global Air Quality Guidelines 2021</h3>
            <p style='font-size: 1.05rem; margin: 1rem 0;'>
                <strong>Directrices Mundiales de Calidad del Aire</strong>
            </p>
            <p>
                Primera actualizacion mayor desde 2005. Reduce niveles recomendados en 50% para PM2.5 basandose en 
                mas de 500 estudios cientificos que demuestran efectos adversos en salud incluso a concentraciones 
                muy bajas. Establece guias para PM2.5, PM10, O3, NO2, SO2 y CO, con metas intermedias para 
                implementacion gradual en paises en desarrollo.
            </p>
            <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
                <strong>Publicacion:</strong> 22 de septiembre de 2021 | 
                <strong>Impacto:</strong> Referencia mundial
            </p>
            <a href='https://www.who.int/publications/i/item/9789240034228' 
               target='_blank' class='corporate-button'>
                Ver Directrices OMS 2021 (Ingles)
            </a>
            <a href='https://www.who.int/es/news-room/feature-stories/detail/what-are-the-who-air-quality-guidelines' 
               target='_blank' class='corporate-button'>
                Resumen Ejecutivo en Espanol
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        oms_tabla = pd.DataFrame([
            ['PM2.5', 5, 15, 'μg/m³', 'Media anual / 24h'],
            ['PM10', 15, 45, 'μg/m³', 'Media anual / 24h'],
            ['NO2', 10, 25, 'μg/m³', 'Media anual / 24h'],
            ['SO2', None, 40, 'μg/m³', '24 horas'],
            ['O3', None, 100, 'μg/m³', 'Pico estacional (8h)'],
            ['CO', None, 4, 'mg/m³', '24 horas']
        ], columns=['Contaminante', 'Anual', '24 horas', 'Unidad', 'Periodo'])
        
        st.markdown("<h3 style='text-align: center; color: #00B8D9; margin-top: 2rem;'>Valores Guia OMS 2021</h3>", unsafe_allow_html=True)
        st.dataframe(oms_tabla, use_container_width=True, hide_index=True, height=280)
        
        st.markdown("""
        <div class='info-box' style='margin-top: 1.5rem;'>
            <p><strong>Metas Intermedias:</strong> La OMS tambien establece 4 niveles intermedios (IT-1 a IT-4) 
            para paises que no pueden alcanzar inmediatamente las guias finales, permitiendo una mejora progresiva 
            de la calidad del aire.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("""
        <div class='corporate-card fade-in'>
            <h2>Environmental Protection Agency (EPA)</h2>
            <p style='font-size: 1.05rem;'>
                La EPA de Estados Unidos establece los <strong>National Ambient Air Quality Standards (NAAQS)</strong>, 
                estandares vinculantes de cumplimiento obligatorio que se revisan cada 5 anos basandose en la mejor 
                ciencia disponible.
            </p>
            
            <div class='success-box' style='margin-top: 1.5rem;'>
                <p><strong>Sistema dual:</strong> La EPA establece estandares primarios (proteccion de salud) 
                y secundarios (proteccion de bienestar publico, incluyendo vegetacion, visibilidad, edificios).</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='normative-card internacional fade-in'>
            <span class='status-badge internacional'>NAAQS 2024</span>
            <h3>National Ambient Air Quality Standards</h3>
            <p style='font-size: 1.05rem; margin: 1rem 0;'>
                <strong>Estandares Nacionales de Calidad del Aire Ambiente</strong>
            </p>
            <p>
                Ultima actualizacion: PM2.5 anual reducido de 12 a 9.0 μg/m³ (febrero 2024), el cambio mas 
                significativo desde 2012. Los NAAQS son legalmente vinculantes y su cumplimiento es monitoreado 
                en todo el territorio estadounidense. Estados que no cumplen deben implementar State Implementation 
                Plans (SIPs) con medidas correctivas.
            </p>
            <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
                <strong>Base legal:</strong> Clean Air Act (1970, enmendado 1990) | 
                <strong>Revision:</strong> Cada 5 anos
            </p>
            <a href='https://www.epa.gov/criteria-air-pollutants/naaqs-table' 
               target='_blank' class='corporate-button'>
                Ver Tabla Completa NAAQS
            </a>
            <a href='https://www.epa.gov/pm-pollution/national-ambient-air-quality-standards-naaqs-pm' 
               target='_blank' class='corporate-button'>
                Estandares PM Detallados
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        epa_tabla = pd.DataFrame([
            ['PM2.5', '9.0 (P)', '35 (P)', 'μg/m³', '2024', 'Anual / 24h'],
            ['PM2.5', '15.0 (S)', '35 (S)', 'μg/m³', '2012', 'Anual / 24h (secundario)'],
            ['PM10', None, '150 (P,S)', 'μg/m³', '2012', '24 horas'],
            ['NO2', '53 (P,S)', '100 (P)', 'ppb', '2010', 'Anual / 1h'],
            ['SO2', None, '75 (P)', 'ppb', '2010', '1 hora (percentil 99)'],
            ['O3', None, '70 (P,S)', 'ppb', '2015', '8h (4to maximo anual)'],
            ['CO', None, '9 ppm (P)', 'ppm', '1971', '8 horas'],
            ['CO', None, '35 ppm (P)', 'ppm', '1971', '1 hora'],
            ['Pb', '0.15 (P,S)', None, 'μg/m³', '2008', 'Promedio movil 3 meses']
        ], columns=['Contaminante', 'Anual', 'Corto Plazo', 'Unidad', 'Ultima Actualizacion', 'Forma del Estandar'])
        
        st.markdown("<h3 style='text-align: center; color: #00B8D9; margin-top: 2rem;'>Estandares EPA (NAAQS)</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: var(--text-secondary); margin-bottom: 1rem;'>(P) = Primario (salud) | (S) = Secundario (bienestar)</p>", unsafe_allow_html=True)
        st.dataframe(epa_tabla, use_container_width=True, hide_index=True, height=400)
        
        st.markdown("""
        <div class='warning-box' style='margin-top: 1.5rem;'>
            <p><strong>Designaciones de no cumplimiento:</strong> Areas que exceden NAAQS son designadas como 
            "nonattainment" y deben desarrollar planes de mejora con cronograma especifico. El incumplimiento 
            persistente puede resultar en sanciones federales.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("""
        <div class='corporate-card fade-in'>
            <h2>Canadian Ambient Air Quality Standards (CAAQS)</h2>
            <p style='font-size: 1.05rem;'>
                Canada utiliza un <strong>sistema de mejora continua</strong> con estandares que se actualizan 
                progresivamente cada 5 anos. La gestion se realiza por Air Zones con sistema de clasificacion 
                por colores que determina las acciones requeridas.
            </p>
            
            <div class='success-box' style='margin-top: 1.5rem;'>
                <p><strong>Enfoque innovador:</strong> Sistema de "Management Levels" (Verde, Amarillo, Naranja, Rojo) 
                que vincula automaticamente el nivel de calidad del aire con acciones de gestion obligatorias.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='normative-card internacional fade-in'>
            <span class='status-badge internacional'>CAAQS 2020-2025</span>
            <h3>Canadian Ambient Air Quality Standards</h3>
            <p style='font-size: 1.05rem; margin: 1rem 0;'>
                <strong>Estandares Canadienses de Calidad del Aire Ambiente</strong>
            </p>
            <p>
                Sistema de gestion por Air Zones implementado nacionalmente. Los estandares 2020 estan en vigor 
                y los estandares 2025 entraran en vigencia proximamente. El sistema incluye objetivos a 2030. 
                Cada provincia y territorio gestiona sus Air Zones con obligacion de reportar anualmente al 
                Canadian Council of Ministers of the Environment (CCME).
            </p>
            <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
                <strong>Base legal:</strong> Canadian Environmental Protection Act | 
                <strong>Coordinacion:</strong> CCME
            </p>
            <a href='https://www.ccme.ca/en/air-quality-report' 
               target='_blank' class='corporate-button'>
                Ver Reporte CAAQS Anual
            </a>
            <a href='https://www.canada.ca/en/environment-climate-change/services/air-quality-health-index.html' 
               target='_blank' class='corporate-button'>
                Indice de Calidad del Aire
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        canada_tabla = pd.DataFrame([
            ['PM2.5', 8.8, 8.0, 6.0, 'μg/m³', 'Anual (percentil 98 de promedios diarios)'],
            ['PM2.5', 27, 25, 20, 'μg/m³', '24h (percentil 98)'],
            ['O3', 62, 60, 56, 'ppb', '8h (4to valor maximo anual)'],
            ['NO2', 60, 50, 42, 'ppb', '1h (percentil 98 anual)'],
            ['SO2', 70, 65, 50, 'ppb', '1h (percentil 99 anual)']
        ], columns=['Contaminante', 'Estandar 2020', 'Meta 2025', 'Objetivo 2030', 'Unidad', 'Forma del Estandar'])
        
        st.markdown("<h3 style='text-align: center; color: #00B8D9; margin-top: 2rem;'>Evolucion de Estandares CAAQS</h3>", unsafe_allow_html=True)
        st.dataframe(canada_tabla, use_container_width=True, hide_index=True, height=250)
        
        st.markdown("""
        <div class='corporate-card' style='margin-top: 2rem;'>
            <h3>Sistema de Gestion por Air Zones</h3>
            <p style='color: var(--text-secondary); margin-bottom: 1.5rem;'>
                Clasificacion por niveles de gestion segun cumplimiento de CAAQS
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div style='background: linear-gradient(135deg, rgba(0, 200, 83, 0.15), rgba(0, 230, 118, 0.1)); 
                        padding: 1.5rem; border-radius: 10px; border-left: 4px solid #00C853; margin: 0.5rem 0;'>
                <h4 style='color: #00C853; margin: 0 0 0.5rem 0;'>Verde - Buena Gestion</h4>
                <p style='color: var(--text-secondary); font-size: 0.95rem; margin: 0;'>
                    Cumple todos los CAAQS. Mantener acciones actuales de gestion.
                </p>
            </div>
            
            <div style='background: linear-gradient(135deg, rgba(255, 179, 0, 0.15), rgba(255, 152, 0, 0.1)); 
                        padding: 1.5rem; border-radius: 10px; border-left: 4px solid #FFB300; margin: 0.5rem 0;'>
                <h4 style='color: #FFB300; margin: 0 0 0.5rem 0;'>Amarillo - Gestion Activa</h4>
                <p style='color: var(--text-secondary); font-size: 0.95rem; margin: 0;'>
                    Se acerca a exceder CAAQS. Implementar medidas preventivas.
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style='background: linear-gradient(135deg, rgba(255, 87, 34, 0.15), rgba(244, 67, 54, 0.1)); 
                        padding: 1.5rem; border-radius: 10px; border-left: 4px solid #FF5722; margin: 0.5rem 0;'>
                <h4 style='color: #FF5722; margin: 0 0 0.5rem 0;'>Naranja - Accion Obligatoria</h4>
                <p style='color: var(--text-secondary); font-size: 0.95rem; margin: 0;'>
                    Excede CAAQS. Plan de gestion obligatorio con metas y cronograma.
                </p>
            </div>
            
            <div style='background: linear-gradient(135deg, rgba(211, 47, 47, 0.15), rgba(198, 40, 40, 0.1)); 
                        padding: 1.5rem; border-radius: 10px; border-left: 4px solid #D32F2F; margin: 0.5rem 0;'>
                <h4 style='color: #D32F2F; margin: 0 0 0.5rem 0;'>Rojo - Intervencion Urgente</h4>
                <p style='color: var(--text-secondary); font-size: 0.95rem; margin: 0;'>
                    Excede significativamente CAAQS. Plan de accion inmediato y estricto.
                </p>
            </div>
            """, unsafe_allow_html=True)
    
    with tab4:
        st.markdown("<h2 style='text-align: center; margin-bottom: 2rem;'>Analisis Comparativo Internacional</h2>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class='corporate-card fade-in'>
            <h3>Comparacion PM2.5 - Estandar Mas Critico para Salud</h3>
            <p style='color: var(--text-secondary); margin-bottom: 1rem;'>
                Valores anuales y de 24 horas segun cada jurisdiccion
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        comparacion = pd.DataFrame([
            {'Entidad': 'OMS 2021', 'Anual': 5, '24h': 15, 'Region': 'Global'},
            {'Entidad': 'EPA USA 2024', 'Anual': 9, '24h': 35, 'Region': 'America'},
            {'Entidad': 'Canada 2025', 'Anual': 8, '24h': 25, 'Region': 'America'},
            {'Entidad': 'OEFA Peru', 'Anual': 25, '24h': 50, 'Region': 'America'}
        ])
        
        fig3 = go.Figure()
        
        fig3.add_trace(go.Bar(
            name='Anual',
            x=comparacion['Entidad'],
            y=comparacion['Anual'],
            marker=dict(
                color=['#00C853', '#0065FF', '#8b5cf6', '#FFB300'],
                line=dict(color='rgba(255,255,255,0.2)', width=1)
            ),
            text=comparacion['Anual'],
            texttemplate='%{text} μg/m³',
            textposition='outside'
        ))
        
        fig3.add_trace(go.Bar(
            name='24 horas',
            x=comparacion['Entidad'],
            y=comparacion['24h'],
            marker=dict(
                color=['#66BB6A', '#42A5F5', '#BA68C8', '#FFA726'],
                line=dict(color='rgba(255,255,255,0.2)', width=1)
            ),
            text=comparacion['24h'],
            texttemplate='%{text} μg/m³',
            textposition='outside'
        ))
        
        fig3.update_layout(
            barmode='group',
            height=550,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#E3E8EF', size=13, family='Inter'),
            xaxis=dict(showgrid=False, title=''),
            yaxis=dict(
                showgrid=True,
                gridcolor='rgba(255,255,255,0.06)',
                title='Concentracion (μg/m³)',
                range=[0, 60]
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
        
        st.plotly_chart(fig3, use_container_width=True)
        
        st.markdown("""
        <div class='corporate-card' style='margin-top: 2rem;'>
            <h3>Tabla Comparativa Completa de Estandares</h3>
            <p style='color: var(--text-secondary); margin-bottom: 1rem;'>
                Comparacion de todos los contaminantes criterio
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        tabla_completa = pd.DataFrame([
            ['PM2.5 Anual', '5 μg/m³', '9 μg/m³', '8 μg/m³', '25 μg/m³', 'Peru 5x mas permisivo'],
            ['PM2.5 24h', '15 μg/m³', '35 μg/m³', '25 μg/m³', '50 μg/m³', 'Peru 3.3x mas permisivo'],
            ['PM10 Anual', '15 μg/m³', 'No establece', 'No establece', '50 μg/m³', 'Peru 3.3x mas permisivo'],
            ['PM10 24h', '45 μg/m³', '150 μg/m³', 'No establece', '100 μg/m³', 'Peru mas estricto que EPA'],
            ['NO2 Anual', '10 μg/m³', '100 μg/m³', '113 μg/m³', '100 μg/m³', 'Peru 10x mas permisivo'],
            ['NO2 1h', '25 μg/m³', '188 μg/m³', '113 μg/m³', '200 μg/m³', 'Peru 8x mas permisivo'],
            ['SO2 24h', '40 μg/m³', 'No establece', 'No establece', '250 μg/m³', 'Peru 6.25x mas permisivo'],
            ['O3 8h', '100 μg/m³', '137 μg/m³', '120 μg/m³', '100 μg/m³', 'Peru igual a OMS'],
            ['CO 8h', '4 mg/m³', '10 mg/m³', 'No establece', '10 mg/m³', 'Peru 2.5x mas permisivo']
        ], columns=['Contaminante/Periodo', 'OMS 2021', 'EPA USA', 'Canada 2025', 'Peru (ECA)', 'Evaluacion'])
        
        st.dataframe(tabla_completa, use_container_width=True, hide_index=True, height=400)
        
        st.markdown("""
        <div class='corporate-card' style='margin-top: 2rem;'>
            <h3>Analisis Comparativo y Recomendaciones</h3>
            
            <div style='margin-top: 1.5rem;'>
                <h4 style='color: #00B8D9; font-size: 1.1rem;'>Principales Hallazgos:</h4>
                <ul style='color: var(--text-secondary); line-height: 1.8; margin-top: 1rem;'>
                    <li><strong>Material Particulado Fino (PM2.5):</strong> El estandar peruano anual (25 μg/m³) 
                    es 5 veces mas permisivo que la recomendacion OMS (5 μg/m³) y 2.8 veces mas alto que EPA USA (9 μg/m³). 
                    Esta brecha representa el mayor desafio normativo nacional.</li>
                    
                    <li><strong>Dioxido de Nitrogeno (NO2):</strong> Peru tiene uno de los estandares mas permisivos 
                    internacionalmente. La OMS 2021 redujo su recomendacion a 10 μg/m³ anual, 10 veces mas estricto 
                    que el ECA peruano.</li>
                    
                    <li><strong>Dioxido de Azufre (SO2):</strong> El estandar peruano de 24h (250 μg/m³) contrasta con 
                    la guia OMS (40 μg/m³). EPA elimino el estandar de 24h y usa uno de 1h mas estricto.</li>
                    
                    <li><strong>Ozono (O3):</strong> Peru mantiene un estandar alineado con OMS (100 μg/m³ en 8h), 
                    siendo uno de los pocos parametros donde la normativa nacional es competitiva internacionalmente.</li>
                    
                    <li><strong>PM10:</strong> Paradojicamente, el estandar peruano de 24h para PM10 (100 μg/m³) es 
                    mas estricto que el de EPA (150 μg/m³), aunque menos que OMS (45 μg/m³).</li>
                </ul>
            </div>
            
            <div class='warning-box' style='margin-top: 2rem;'>
                <h4 style='margin-top: 0;'>Implicaciones para Salud Publica</h4>
                <p>
                    La evidencia cientifica revisada por la OMS en 2021 demuestra que <strong>no existe un umbral seguro</strong> 
                    para material particulado: incluso concentraciones bajas causan efectos adversos en salud. Los estandares 
                    mas permisivos implican mayor carga de enfermedad y mortalidad prematura en la poblacion peruana.
                </p>
            </div>
            
            <div class='success-box' style='margin-top: 1.5rem;'>
                <h4 style='margin-top: 0;'>Recomendaciones Estrategicas</h4>
                <ol style='color: var(--text-secondary); line-height: 1.8; padding-left: 1.2rem;'>
                    <li><strong>Actualizacion Gradual de ECA:</strong> Implementar una hoja de ruta de 10 anos con 
                    metas intermedias progresivas hacia estandares similares a EPA y eventualmente OMS.</li>
                    
                    <li><strong>Priorizacion de PM2.5:</strong> Enfocar esfuerzos iniciales en reducir el estandar 
                    de PM2.5 anual, el contaminante con mayor impacto en salud publica.</li>
                    
                    <li><strong>Fortalecimiento de Redes de Monitoreo:</strong> Expandir la red de estaciones para 
                    tener datos representativos nacionales antes de endurecer estandares.</li>
                    
                    <li><strong>Incentivos para Cumplimiento:</strong> Desarrollar programas de incentivos tecnicos 
                    y financieros para que industrias inviertan en tecnologias de control mas efectivas.</li>
                    
                    <li><strong>Gestion de Calidad de Aire Local:</strong> Adoptar sistema similar al de Canada 
                    (Air Zones) con clasificacion por colores y acciones de gestion vinculadas.</li>
                    
                    <li><strong>Comunicacion de Riesgos:</strong> Implementar indices de calidad del aire de facil 
                    comprension publica con recomendaciones de salud especificas.</li>
                    
                    <li><strong>Inventarios de Emisiones:</strong> Completar inventarios nacionales detallados para 
                    identificar fuentes prioritarias de reduccion.</li>
                    
                    <li><strong>Colaboracion Internacional:</strong> Aprender de experiencias de paises con normativas 
                    mas estrictas y buscar cooperacion tecnica y financiera.</li>
                </ol>
            </div>
            
            <div class='info-box' style='margin-top: 1.5rem;'>
                <p><strong>Tendencia Global:</strong> Todos los paises analizados muestran una tendencia clara 
                hacia estandares mas estrictos basados en nueva evidencia cientifica. Peru debe evaluar actualizar 
                sus ECA para mantenerse alineado con mejores practicas internacionales y proteger adecuadamente 
                la salud de su poblacion.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ===================== FOOTER CORPORATIVO =====================
st.markdown("""
<div class='corporate-footer'>
    <h3>Universidad Nacional de Moquegua</h3>
    <p style='font-size: 1.1rem; margin-top: 0.5rem;'>Facultad de Ingenieria y Arquitectura</p>
    
    <div class='divider'></div>
    
    <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; text-align: left; max-width: 1000px; margin: 2rem auto 0;'>
        <div>
            <h4 style='color: #00B8D9; margin-bottom: 0.75rem;'>Curso</h4>
            <p>Contaminacion y Control Atmosferico</p>
        </div>
        
        <div>
            <h4 style='color: #00B8D9; margin-bottom: 0.75rem;'>Docente</h4>
            <p>Prof. Dr. Jose Antonio Valeriano Zapana</p>
        </div>
        
        <div>
            <h4 style='color: #00B8D9; margin-bottom: 0.75rem;'>Actualizacion</h4>
            <p>Octubre 2024 - Ciclo 2024-II</p>
        </div>
        
        <div>
            <h4 style='color: #00B8D9; margin-bottom: 0.75rem;'>Tecnologia</h4>
            <p>Streamlit - Plotly - Python</p>
        </div>
    </div>
    
    <div class='divider'></div>
    
    <p style='font-size: 0.9rem; opacity: 0.8; margin-top: 1.5rem;'>
        Sistema Integral de Consulta de Marco Normativo de Calidad del Aire
    </p>
    <p style='font-size: 0.85rem; opacity: 0.6; margin-top: 0.5rem;'>
        Datos oficiales: MINAM - OEFA - OMS - EPA - CCME | 2024 UNAM
    </p>
</div>
""", unsafe_allow_html=True)
