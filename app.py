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
    
    /* Scrollbar personalizada */
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
    st.markdown("### 🔍 NAVEGACIÓN RÁPIDA")
    
    st.markdown("---")
    
    # Búsqueda
    busqueda = st.text_input("🔎 Buscar normativa...", placeholder="Ej: PM2.5, ECA, protocolo...")
    st.session_state.busqueda = busqueda
    
    st.markdown("---")
    
    st.markdown("#### 📋 SECCIONES")
    
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
    
    st.markdown("#### 📊 ESTADÍSTICAS")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Normativas", "18+")
    with col2:
        st.metric("Países", "4")
    
    st.markdown("---")
    
    st.markdown("#### ℹ️ INFORMACIÓN")
    st.markdown("""
    <div class='info-box'>
        <p style='font-size: 0.85rem;'><strong>Última actualización:</strong><br>Octubre 2024</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("📞 Contacto"):
        st.markdown("""
        **Universidad Nacional de Moquegua**  
        Facultad de Ingeniería y Arquitectura
        
        📧 contacto@unam.edu.pe  
        📱 +51 XXX XXX XXX
        """)

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
        st.markdown("""
        <div class='corporate-card fade-in'>
            <h2>📚 Sistema de Consulta Normativo</h2>
            <p style='font-size: 1.05rem; margin-bottom: 1.5rem;'>
                Plataforma integral que centraliza el marco normativo completo sobre calidad del aire 
                en Perú y referencias internacionales, facilitando el acceso a información técnica y 
                legal actualizada.
            </p>
            
            <h3 style='font-size: 1.2rem; margin-top: 2rem; margin-bottom: 1rem;'>Contenido del Sistema</h3>
            
            <div style='display: grid; gap: 1rem;'>
                <div style='display: flex; align-items: start; gap: 1rem;'>
                    <span style='font-size: 1.5rem;'>📋</span>
                    <div>
                        <strong style='color: var(--text-primary);'>Estándares de Calidad Ambiental (ECA)</strong><br>
                        <span style='color: var(--text-secondary); font-size: 0.95rem;'>
                            Concentraciones máximas en aire ambiente para protección de salud pública
                        </span>
                    </div>
                </div>
                
                <div style='display: flex; align-items: start; gap: 1rem;'>
                    <span style='font-size: 1.5rem;'>🏭</span>
                    <div>
                        <strong style='color: var(--text-primary);'>Límites Máximos Permisibles (LMP)</strong><br>
                        <span style='color: var(--text-secondary); font-size: 0.95rem;'>
                            Emisiones máximas permitidas en la fuente por sector productivo
                        </span>
                    </div>
                </div>
                
                <div style='display: flex; align-items: start; gap: 1rem;'>
                    <span style='font-size: 1.5rem;'>📖</span>
                    <div>
                        <strong style='color: var(--text-primary);'>Protocolos de Monitoreo</strong><br>
                        <span style='color: var(--text-secondary); font-size: 0.95rem;'>
                            Procedimientos estandarizados para medición y análisis de calidad del aire
                        </span>
                    </div>
                </div>
                
                <div style='display: flex; align-items: start; gap: 1rem;'>
                    <span style='font-size: 1.5rem;'>📐</span>
                    <div>
                        <strong style='color: var(--text-primary);'>Lineamientos Técnicos</strong><br>
                        <span style='color: var(--text-secondary); font-size: 0.95rem;'>
                            Guías operativas para implementación de normativas y gestión ambiental
                        </span>
                    </div>
                </div>
                
                <div style='display: flex; align-items: start; gap: 1rem;'>
                    <span style='font-size: 1.5rem;'>🛡️</span>
                    <div>
                        <strong style='color: var(--text-primary);'>Tecnologías de Control</strong><br>
                        <span style='color: var(--text-secondary); font-size: 0.95rem;'>
                            Sistemas y medidas para reducción de emisiones atmosféricas
                        </span>
                    </div>
                </div>
                
                <div style='display: flex; align-items: start; gap: 1rem;'>
                    <span style='font-size: 1.5rem;'>🌍</span>
                    <div>
                        <strong style='color: var(--text-primary);'>Referencias Internacionales</strong><br>
                        <span style='color: var(--text-secondary); font-size: 0.95rem;'>
                            Estándares de OMS, EPA USA y Canadá para análisis comparativo
                        </span>
                    </div>
                </div>
            </div>
            
            <div class='success-box' style='margin-top: 2rem;'>
                <p><strong>✓ Acceso directo</strong> a documentos oficiales con enlaces actualizados<br>
                <strong>✓ Visualizaciones</strong> interactivas para análisis comparativo<br>
                <strong>✓ Información técnica</strong> validada y referencias normativas completas</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='corporate-card fade-in'>
            <h2>⚡ Acceso Directo</h2>
            <p style='color: rgba(255,255,255,0.9); margin-bottom: 1.5rem;'>
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
        
        st.info("💡 **Sugerencia:** Utilice el buscador del menú lateral para encontrar normativas específicas rápidamente.")
    
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
        
        <div class='info-box' style='margin-top: 1.5rem;'>
            <p><strong>Diferencia clave:</strong> ECA se mide en aire ambiente (lo que respiramos), 
            mientras que LMP se mide en la fuente de emisión (chimeneas, ductos).</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Normativas ECA
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
        <a href='https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_074-2001-pcm.pdf' 
           target='_blank' class='corporate-button'>
            📄 Ver D.S. 074-2001-PCM (Histórico)
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Tabla de valores ECA
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
    
    st.dataframe(
        eca_valores,
        use_container_width=True,
        hide_index=True,
        height=550
    )
    
    # Información adicional
    with st.expander("ℹ️ Ver información adicional sobre contaminantes criterio"):
        st.markdown("""
        #### Contaminantes Criterio Regulados
        
        **Material Particulado (PM2.5 y PM10)**
        - Partículas sólidas o líquidas suspendidas en el aire
        - PM2.5: diámetro ≤ 2.5 μm (penetran profundamente en pulmones)
        - PM10: diámetro ≤ 10 μm (afectan vías respiratorias superiores)
        - Fuentes: combustión, polvo, actividades industriales
        
        **Dióxido de Nitrógeno (NO2)**
        - Gas irritante de color marrón rojizo
        - Fuentes: combustión vehicular e industrial
        - Efectos: irritación respiratoria, reducción función pulmonar
        
        **Dióxido de Azufre (SO2)**
        - Gas incoloro con olor penetrante
        - Fuentes: combustión de combustibles fósiles con azufre
        - Efectos: irritación respiratoria, enfermedades cardiovasculares
        
        **Ozono Troposférico (O3)**
        - Contaminante secundario (no se emite directamente)
        - Se forma por reacción fotoquímica de NOx y COVs
        - Efectos: daño pulmonar, reducción función respiratoria
        
        **Monóxido de Carbono (CO)**
        - Gas incoloro e inodoro
        - Fuentes: combustión incompleta
        - Efectos: reduce capacidad de transporte de oxígeno en sangre
        
        **Plomo (Pb)**
        - Metal pesado tóxico
        - Fuentes: históricamente gasolina con plomo, industrias
        - Efectos: neurotoxicidad, afecta desarrollo infantil
        
        **Sulfuro de Hidrógeno (H2S)**
        - Gas con olor a huevo podrido
        - Fuentes: actividades petroleras, descomposición materia orgánica
        - Efectos: irritación ocular y respiratoria
        
        **Benzo(a)pireno (BaP)**
        - Hidrocarburo aromático policíclico (HAP)
        - Fuentes: combustión incompleta de materia orgánica
        - Efectos: cancerígeno, mutagénico
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
        
        <div class='info-box' style='margin-top: 1.5rem;'>
            <p><strong>Diferencia clave:</strong> Los LMP se aplican a la fuente emisora y son 
            medidos en el punto de descarga, mientras que los ECA se miden en el aire ambiente 
            que respira la población.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # LMP por sector
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
        <a href='http://www.minem.gob.pe/minem/archivos/file/DGAAM/legislacion/resolucion/RM-315-96.pdf' 
           target='_blank' class='corporate-button'>
            📄 Ver R.M. 315-96-EM/VMM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Tabla LMP Termoeléctricas
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
    
    st.dataframe(
        lmp_termo,
        use_container_width=True,
        hide_index=True,
        height=200
    )
    
    # Gráfico comparativo LMP
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
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    <div class='info-box'>
        <p><strong>📌 Nota técnica:</strong> Los límites son más estrictos para combustibles más limpios. 
        El gas natural tiene los LMP más bajos debido a su menor contenido de azufre y mejor eficiencia 
        de combustión, mientras que el residual (combustóleo) tiene los límites más permisivos debido 
        a su mayor contenido de impurezas.</p>
    </div>
    """, unsafe_allow_html=True)

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
        
        <div class='info-box' style='margin-top: 1.5rem;'>
            <p><strong>Importancia:</strong> Los protocolos aseguran la trazabilidad, precisión y 
            validez legal de las mediciones ambientales realizadas por laboratorios acreditados y 
            empresas consultoras.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
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
        <a href='http://www.digesa.minsa.gob.pe/DEPA/protocolo_calidad_aire.pdf' 
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
        <a href='https://www.minam.gob.pe/wp-content/uploads/2017/04/RM-026-2000-ITINCI.pdf' 
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
        <a href='http://www.minem.gob.pe/minem/archivos/RD%20195-2010-AAM.pdf' 
           target='_blank' class='corporate-button'>
            📄 Descargar R.D. 195-2010-MEM/AAM
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
        <a href='http://www.minem.gob.pe/minem/archivos/file/DGAAM/guias/protocmonitoreoaire.pdf' 
           target='_blank' class='corporate-button'>
            📄 Ver R.M. 247-2009-MEM/DM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Tabla de métodos EPA
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
    
    st.dataframe(
        metodos,
        use_container_width=True,
        hide_index=True,
        height=380
    )
    
    # Proceso de monitoreo
    with st.expander("📋 Ver flujo de proceso de monitoreo de calidad del aire"):
        st.markdown("""
        #### Proceso Completo de Monitoreo
        
        **1. Planificación**
        - Definición de objetivos del monitoreo
        - Selección de ubicación de estaciones (criterios de macro y microescala)
        - Determinación de parámetros y frecuencias de muestreo
        - Elaboración de Plan de Monitoreo
        
        **2. Implementación**
        - Instalación y configuración de equipos
        - Calibración inicial con gases y patrones certificados
        - Verificación de condiciones ambientales del sitio
        - Inicio de operación según protocolo
        
        **3. Operación y Mantenimiento**
        - Calibraciones periódicas (diarias, semanales, mensuales)
        - Mantenimiento preventivo de equipos
        - Verificación de flujos y condiciones operativas
        - Registro de eventos y anomalías
        
        **4. Aseguramiento de Calidad**
        - Auditorías internas y externas
        - Análisis de blancos y duplicados
        - Control de precisión y exactitud
        - Validación de datos
        
        **5. Análisis de Laboratorio**
        - Análisis gravimétrico (PM)
        - Análisis químico (metales, iones)
        - Control de calidad analítico
        - Certificados de análisis
        
        **6. Gestión de Datos**
        - Transferencia y almacenamiento de datos
        - Validación estadística
        - Cálculo de promedios según ECA
        - Identificación de excedencias
        
        **7. Reporte**
        - Informes técnicos periódicos
        - Reportes a autoridades competentes
        - Publicación de resultados (cuando aplique)
        - Acciones correctivas si hay excedencias
        """, unsafe_allow_html=True)

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
        
        <div class='info-box' style='margin-top: 1.5rem;'>
            <p><strong>Función:</strong> Los lineamientos facilitan la aplicación práctica de la normativa 
            legal, proporcionando herramientas técnicas para su cumplimiento efectivo por parte de autoridades, 
            empresas y consultores.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
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
        <a href='http://www.digesa.minsa.gob.pe/NormasLegales/Normas/DS_009-2003-SA.pdf' 
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
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>● VIGENTE</span>
        <h3>Ley N° 30754</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Ley Marco sobre Cambio Climático - Componente Calidad del Aire</strong>
        </p>
        <p>
            Establece el marco institucional para la gestión integral del cambio climático en el país. 
            Incluye lineamientos para la reducción de contaminantes climáticos de vida corta (CCVC) como 
            el carbono negro, considerando sus efectos simultáneos en calidad del aire y clima.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 18 de abril de 2018 | 
            <strong>Ámbito:</strong> Nacional
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2018/10/Ley-N%C2%B0-30754.pdf' 
           target='_blank' class='corporate-button'>
            📄 Ver Ley 30754
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Tabla de niveles de alerta
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
    
    st.dataframe(
        niveles,
        use_container_width=True,
        hide_index=True,
        height=500
    )
    
    st.markdown("""
    <div class='warning-box'>
        <p><strong>⚠️ Protocolo de activación:</strong> Las autoridades ambientales y de salud deben 
        activar los niveles de alerta cuando se registren o pronostiquen concentraciones en los rangos 
        establecidos. Las medidas incluyen difusión masiva de información, restricción de actividades, 
        y en casos de emergencia, la declaratoria de estado de emergencia ambiental.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Categorías de inventario de emisiones
    with st.expander("📊 Ver categorías del Inventario de Emisiones Atmosféricas"):
        st.markdown("""
        #### Categorías de Fuentes según R.M. 181-2016-MINAM
        
        **1. Fuentes Puntuales**
        - Definición: Emisiones identificables de chimeneas o ductos específicos
        - Ejemplos: Industrias, centrales térmicas, fundiciones
        - Datos requeridos: Caudal, concentración, temperatura, ubicación geográfica
        
        **2. Fuentes de Área**
        - Definición: Múltiples fuentes pequeñas agregadas geográficamente
        - Ejemplos: Uso de solventes, panaderías, restaurantes, estaciones de servicio
        - Datos requeridos: Consumo de combustible/materia prima, factores de emisión
        
        **3. Fuentes Móviles**
        - Definición: Vehículos automotores en circulación
        - Categorías: Livianos, pesados, motocicletas, transporte público
        - Datos requeridos: Parque automotor, km recorridos, edad vehicular, tipo combustible
        
        **4. Fuentes Naturales**
        - Definición: Emisiones de origen natural
        - Ejemplos: Polvo fugitivo de suelos áridos, emisiones biogénicas
        - Datos requeridos: Cobertura vegetal, características de suelo, meteorología
        
        **5. Emisiones Fugitivas**
        - Definición: Emisiones no canalizadas
        - Ejemplos: Patio de minerales, vías no pavimentadas, demoliciones
        - Datos requeridos: Superficie expuesta, contenido de humedad, velocidad del viento
        
        #### Contaminantes a Inventariar
        - Material Particulado (PM10, PM2.5, PST)
        - Óxidos de Nitrógeno (NOx)
        - Dióxido de Azufre (SO2)
        - Monóxido de Carbono (CO)
        - Compuestos Orgánicos Volátiles (COV)
        - Metales pesados (Pb, As, Cd, Hg, según sector)
        - Gases de Efecto Invernadero (CO2, CH4, N2O)
        - Carbono Negro (BC)
        """, unsafe_allow_html=True)

# ===================== PÁGINA MEDIDAS =====================
elif st.session_state.pagina == "Medidas":
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>🛡️ Medidas y Tecnologías de Control de Emisiones</h2>
        <p style='font-size: 1.05rem;'>
            Las tecnologías de control son <strong>sistemas y equipos diseñados para reducir las emisiones</strong> 
            de contaminantes atmosféricos desde fuentes puntuales. Su implementación es obligatoria para cumplir 
            con los LMP establecidos y representan la mejor tecnología disponible económicamente viable (BATEA).
        </p>
        
        <div class='info-box' style='margin-top: 1.5rem;'>
            <p><strong>Marco legal:</strong> La Ley General del Ambiente (Ley 28611) establece la obligación 
            de implementar medidas de prevención y control de la contaminación del aire, priorizando tecnologías 
            limpias y sistemas de reducción de emisiones.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>● VIGENTE</span>
        <h3>Ley N° 28611 - Ley General del Ambiente</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Título II, Capítulo 3: De la Calidad Ambiental</strong>
        </p>
        <p>
            Establece la obligación legal de implementar medidas de prevención, control y remediación de la 
            contaminación del aire. Define responsabilidades de titulares de actividades productivas para 
            adoptar tecnologías limpias, sistemas de tratamiento de emisiones y programas de monitoreo continuo.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 15 de octubre de 2005 | 
            <strong>Ámbito:</strong> Marco general ambiental
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2017/04/Ley-N%C2%B0-28611.pdf' 
           target='_blank' class='corporate-button'>
            📄 Ver Ley 28611
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>● VIGENTE</span>
        <h3>D.S. N° 012-2005-EM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Reglamento de Plan de Cierre de Minas - Control de Emisiones</strong>
        </p>
        <p>
            Incluye obligaciones específicas de implementación y mantenimiento de sistemas de control de 
            emisiones atmosféricas durante las fases de operación, cierre progresivo y cierre final de 
            operaciones mineras. Define responsabilidades técnicas y financieras para asegurar el cumplimiento 
            a largo plazo.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 05 de agosto de 2005 | 
            <strong>Sector:</strong> Minería
        </p>
        <a href='http://www.minem.gob.pe/minem/archivos/file/Mineria/LEGISLACION/2005/agosto/DS012-2005.pdf' 
           target='_blank' class='corporate-button'>
            📄 Ver D.S. 012-2005-EM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card ntp fade-in'>
        <span class='status-badge ntp'>● NORMAS TÉCNICAS</span>
        <h3>Normas Técnicas Peruanas (NTP) - INACAL</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Gestión Ambiental del Aire - Metodologías y Terminología</strong>
        </p>
        <p>
            <strong>NTP 900.058:2019</strong> - Gestión Ambiental. Calidad del Aire. Métodos de muestreo<br>
            <strong>NTP 900.030:2003</strong> - Gestión Ambiental. Calidad del Aire. Terminología<br>
            <strong>NTP-ISO 9169:2014</strong> - Calidad del aire. Determinación de características de funcionamiento<br><br>
            Normas técnicas que establecen procedimientos estandarizados para evaluación de eficiencia de 
            sistemas de control, métodos de medición de emisiones, y terminología técnica normalizada.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Entidad emisora:</strong> Instituto Nacional de Calidad (INACAL)
        </p>
        <a href='https://www.inacal.gob.pe/repositorioaps/data/1/1/1/jer/ctnprocedimiento/files/Catalogo_NTP_Vigentes_2023.pdf' 
           target='_blank' class='corporate-button'>
            📄 Ver Catálogo NTP INACAL
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Tabla de tecnologías
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>🔧 Tecnologías de Control de Emisiones por Contaminante</h2>
        <p style='color: var(--text-secondary); margin-bottom: 1rem;'>
            Principales sistemas utilizados en la industria peruana para cumplimiento de LMP
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    tecnologias = pd.DataFrame([
        ['Material Particulado', 'Filtros de mangas (Baghouse)', '>99%', 'Captación por filtración textil', 'Media-Alta', 'Alto', 'Industria general'],
        ['Material Particulado', 'Precipitadores electrostáticos (ESP)', '95-99%', 'Carga eléctrica y colección', 'Alta', 'Medio', 'Termoeléctricas, cemento'],
        ['Material Particulado', 'Ciclones', '70-90%', 'Separación por fuerza centrífuga', 'Baja', 'Bajo', 'Pre-tratamiento'],
        ['Material Particulado', 'Lavadores húmedos (Scrubbers)', '85-95%', 'Absorción líquido-gas', 'Media', 'Medio', 'Industria química'],
        ['SO2', 'Desulfuración húmeda (FGD)', '>95%', 'Absorción con caliza/cal + agua', 'Muy Alta', 'Alto', 'Termoeléctricas, fundiciones'],
        ['SO2', 'Desulfuración seca (SDA)', '80-95%', 'Inyección de sorbente seco', 'Alta', 'Medio-Alto', 'Industria general'],
        ['SO2', 'Scrubber de doble álcali', '90-98%', 'Absorción NaOH regenerativo', 'Alta', 'Alto', 'Metalurgia'],
        ['NOx', 'Reducción Catalítica Selectiva (SCR)', '>90%', 'Reducción con NH3/urea + catalizador', 'Muy Alta', 'Muy Alto', 'Termoeléctricas, cemento'],
        ['NOx', 'Reducción No Catalítica (SNCR)', '40-60%', 'Inyección térmica de urea', 'Media', 'Medio', 'Calderos, hornos'],
        ['NOx', 'Quemadores Low-NOx', '30-50%', 'Control de combustión (T y O2)', 'Media', 'Bajo-Medio', 'Calderos industriales'],
        ['NOx', 'Recirculación de gases (FGR)', '20-40%', 'Reducción T de llama', 'Baja-Media', 'Bajo', 'Calderos pequeños'],
        ['COVs', 'Oxidación térmica', '>95%', 'Combustión 700-850°C', 'Alta', 'Alto', 'Química, pinturas'],
        ['COVs', 'Oxidación catalítica', '>90%', 'Combustión catalítica 350-450°C', 'Alta', 'Medio-Alto', 'Imprentas, recubrimientos'],
        ['COVs', 'Adsorción carbón activado', '85-95%', 'Captura en microporos', 'Media', 'Medio', 'Baja concentración'],
        ['COVs', 'Condensación criogénica', '80-90%', 'Enfriamiento bajo punto rocío', 'Alta', 'Alto', 'Recuperación solventes'],
        ['CO', 'Oxidación catalítica', '>98%', 'Conversión CO a CO2', 'Media-Alta', 'Medio', 'Escape vehicular, hornos']
    ], columns=['Contaminante', 'Tecnología', 'Eficiencia', 'Principio de Operación', 'Complejidad', 'Costo', 'Aplicación Principal'])
    
    st.dataframe(
        tecnologias,
        use_container_width=True,
        hide_index=True,
        height=650
    )
    
    # Gráfico comparativo de eficiencias
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>📊 Comparación de Eficiencias de Remoción</h2>
        <p style='color: var(--text-secondary); margin-bottom: 1rem;'>
            Eficiencia típica de principales tecnologías de control
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    eficiencias_data = pd.DataFrame([
        {'Tecnología': 'Filtros mangas', 'Eficiencia': 99.5, 'Tipo': 'Material Particulado'},
        {'Tecnología': 'ESP', 'Eficiencia': 97, 'Tipo': 'Material Particulado'},
        {'Tecnología': 'Ciclones', 'Eficiencia': 80, 'Tipo': 'Material Particulado'},
        {'Tecnología': 'FGD Húmedo', 'Eficiencia': 97, 'Tipo': 'SO2'},
        {'Tecnología': 'SDA Seco', 'Eficiencia': 87.5, 'Tipo': 'SO2'},
        {'Tecnología': 'SCR', 'Eficiencia': 92, 'Tipo': 'NOx'},
        {'Tecnología': 'SNCR', 'Eficiencia': 50, 'Tipo': 'NOx'},
        {'Tecnología': 'Low-NOx', 'Eficiencia': 40, 'Tipo': 'NOx'},
        {'Tecnología': 'Oxidación térmica', 'Eficiencia': 97, 'Tipo': 'COVs'},
        {'Tecnología': 'Carbón activado', 'Eficiencia': 90, 'Tipo': 'COVs'}
    ])
    
    fig = px.bar(
        eficiencias_data,
        x='Tecnología',
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
    
    fig.update_traces(
        texttemplate='%{text}%',
        textposition='outside',
        marker=dict(line=dict(color='rgba(255,255,255,0.2)', width=1))
    )
    
    fig.update_layout(
        height=500,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#E3E8EF', size=12, family='Inter'),
        xaxis=dict(
            showgrid=False,
            title='',
            tickangle=-45
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(255,255,255,0.06)',
            title='Eficiencia de Remoción (%)',
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
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Información adicional
    with st.expander("💡 Ver factores de selección de tecnología de control"):
        st.markdown("""
        #### Factores Clave para Selección de Tecnología
        
        **1. Características del Efluente Gaseoso**
        - Caudal volumétrico: m³/h o Nm³/h
        - Temperatura: °C (afecta volumen y selección de materiales)
        - Concentración de contaminante: mg/Nm³ o ppm
        - Características químicas: pH, humedad, presencia de otros compuestos
        - Concentración de polvo: puede requerir pre-tratamiento
        
        **2. Requisitos Regulatorios**
        - LMP aplicables: según sector y tipo de fuente
        - ECA de zona: considerar impacto en calidad de aire ambiente
        - Plazos de cumplimiento: gradualidad normativa
        - Reporte y monitoreo: CEMS vs mediciones periódicas
        
        **3. Aspectos Técnicos**
        - Eficiencia requerida: calculada según emisión actual y LMP
        - Confiabilidad operativa: disponibilidad >95% típicamente requerida
        - Vida útil de equipos: 15-25 años para equipos principales
        - Espacio disponible: footprint de la instalación
        - Servicios requeridos: energía eléctrica, agua, aire comprimido, vapor
        
        **4. Aspectos Económicos**
        - CAPEX (inversión inicial): equipos, instalación, ingeniería
        - OPEX (costos operativos): energía, reactivos, mantenimiento, mano de obra
        - Generación de residuos: tratamiento y disposición de residuos secundarios
        - Valor presente neto (VPN): análisis de costo-beneficio a 20 años
        
        **5. Consideraciones Ambientales**
        - Consumo energético: kWh/Nm³ tratado
        - Consumo de agua: si aplica (scrubbers, FGD)
        - Generación de residuos: lodos, catalizadores gastados, filtros
        - Emisiones secundarias: CO2 de consumo energético
        
        **6. Mejores Técnicas Disponibles (MTD/BAT)**
        - Documentos BREF europeos: referencia técnica de BAT
        - Guías EPA: AP-42 y documentos sectoriales
        - Benchmarking internacional: plantas similares en región
        - Innovaciones tecnológicas: considerar mejoras disponibles
        
        #### Proceso de Evaluación Recomendado
        1. Caracterización completa del efluente gaseoso
        2. Identificación de tecnologías técnicamente factibles
        3. Evaluación multicriterio (técnica, económica, ambiental)
        4. Análisis de sensibilidad y riesgos
        5. Selección de tecnología óptima
        6. Diseño de ingeniería detallada
        7. Implementación y puesta en marcha
        8. Monitoreo de desempeño y optimización continua
        """, unsafe_allow_html=True)

# ===================== PÁGINA NORMATIVAS INTERNACIONALES =====================
elif st.session_state.pagina == "Normativas":
    
    st.markdown("<h1 style='text-align: center; margin-bottom: 2rem;'>🌍 Normativas Internacionales de Calidad del Aire</h1>", unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["🌍 OMS", "🇺🇸 EPA USA", "🇨🇦 Canadá", "📊 Análisis Comparativo"])
    
    with tab1:
        st.markdown("""
        <div class='corporate-card fade-in'>
            <h2>🌍 Organización Mundial de la Salud (OMS)</h2>
            <p style='font-size: 1.05rem;'>
                La OMS establece las <strong>directrices globales más estrictas</strong> para proteger 
                la salud pública de la contaminación del aire basándose en la mejor evidencia científica disponible.
            </p>
            
            <div class='success-box' style='margin-top: 1.5rem;'>
                <p><strong>✓ Referencia mundial:</strong> Las guías OMS son reconocidas internacionalmente como 
                la mejor evidencia científica disponible sobre efectos de la contaminación del aire en la salud.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='normative-card internacional fade-in'>
            <span class='status-badge internacional'>● GUÍAS 2021</span>
            <h3>WHO Global Air Quality Guidelines 2021</h3>
            <p style='font-size: 1.05rem; margin: 1rem 0;'>
                <strong>Directrices Mundiales de Calidad del Aire</strong>
            </p>
            <p>
                Primera actualización mayor desde 2005. Reduce niveles recomendados en 50% para PM2.5 basándose en 
                más de 500 estudios científicos que demuestran efectos adversos en salud incluso a concentraciones 
                muy bajas. Establece guías para PM2.5, PM10, O3, NO2, SO2 y CO, con metas intermedias para 
                implementación gradual en países en desarrollo.
            </p>
            <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
                <strong>Publicación:</strong> 22 de septiembre de 2021 | 
                <strong>Impacto:</strong> Referencia mundial
            </p>
            <a href='https://www.who.int/publications/i/item/9789240034228' 
               target='_blank' class='corporate-button'>
                📄 Ver Directrices OMS 2021 (Inglés)
            </a>
            <a href='https://www.who.int/es/news-room/feature-stories/detail/what-are-the-who-air-quality-guidelines' 
               target='_blank' class='corporate-button'>
                📖 Resumen Ejecutivo en Español
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        # Tabla OMS
        oms_tabla = pd.DataFrame([
            ['PM2.5', 5, 15, 'μg/m³', 'Media anual / 24h'],
            ['PM10', 15, 45, 'μg/m³', 'Media anual / 24h'],
            ['NO2', 10, 25, 'μg/m³', 'Media anual / 24h'],
            ['SO2', None, 40, 'μg/m³', '24 horas'],
            ['O3', None, 100, 'μg/m³', 'Pico estacional (8h)'],
            ['CO', None, 4, 'mg/m³', '24 horas']
        ], columns=['Contaminante', 'Anual', '24 horas', 'Unidad', 'Período'])
        
        st.markdown("<h3 style='text-align: center; color: #00B8D9; margin-top: 2rem;'>📊 Valores Guía OMS 2021</h3>", unsafe_allow_html=True)
        st.dataframe(oms_tabla, use_container_width=True, hide_index=True, height=280)
        
        st.markdown("""
        <div class='info-box' style='margin-top: 1.5rem;'>
            <p><strong>💡 Metas Intermedias:</strong> La OMS también establece 4 niveles intermedios (IT-1 a IT-4) 
            para países que no pueden alcanzar inmediatamente las guías finales, permitiendo una mejora progresiva 
            de la calidad del aire.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("""
        <div class='corporate-card fade-in'>
            <h2>🇺🇸 Environmental Protection Agency (EPA)</h2>
            <p style='font-size: 1.05rem;'>
                La EPA de Estados Unidos establece los <strong>National Ambient Air Quality Standards (NAAQS)</strong>, 
                estándares vinculantes de cumplimiento obligatorio que se revisan cada 5 años basándose en la mejor 
                ciencia disponible.
            </p>
            
            <div class='success-box' style='margin-top: 1.5rem;'>
                <p><strong>✓ Sistema dual:</strong> La EPA establece estándares primarios (protección de salud) 
                y secundarios (protección de bienestar público, incluyendo vegetación, visibilidad, edificios).</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='normative-card internacional fade-in'>
            <span class='status-badge internacional'>● NAAQS 2024</span>
            <h3>National Ambient Air Quality Standards</h3>
            <p style='font-size: 1.05rem; margin: 1rem 0;'>
                <strong>Estándares Nacionales de Calidad del Aire Ambiente</strong>
            </p>
            <p>
                Última actualización: PM2.5 anual reducido de 12 a 9.0 μg/m³ (febrero 2024), el cambio más 
                significativo desde 2012. Los NAAQS son legalmente vinculantes y su cumplimiento es monitoreado 
                en todo el territorio estadounidense. Estados que no cumplen deben implementar State Implementation 
                Plans (SIPs) con medidas correctivas.
            </p>
            <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
                <strong>Base legal:</strong> Clean Air Act (1970, enmendado 1990) | 
                <strong>Revisión:</strong> Cada 5 años
            </p>
            <a href='https://www.epa.gov/criteria-air-pollutants/naaqs-table' 
               target='_blank' class='corporate-button'>
                📄 Ver Tabla Completa NAAQS
            </a>
            <a href='https://www.epa.gov/pm-pollution/national-ambient-air-quality-standards-naaqs-pm' 
               target='_blank' class='corporate-button'>
                📖 Estándares PM Detallados
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        epa_tabla = pd.DataFrame([
            ['PM2.5', '9.0 (P)', '35 (P)', 'μg/m³', '2024', 'Anual / 24h'],
            ['PM2.5', '15.0 (S)', '35 (S)', 'μg/m³', '2012', 'Anual / 24h (secundario)'],
            ['PM10', None, '150 (P,S)', 'μg/m³', '2012', '24 horas'],
            ['NO2', '53 (P,S)', '100 (P)', 'ppb', '2010', 'Anual / 1h'],
            ['SO2', None, '75 (P)', 'ppb', '2010', '1 hora (percentil 99)'],
            ['O3', None, '70 (P,S)', 'ppb', '2015', '8h (4to máximo anual)'],
            ['CO', None, '9 ppm (P)', 'ppm', '1971', '8 horas'],
            ['CO', None, '35 ppm (P)', 'ppm', '1971', '1 hora'],
            ['Pb', '0.15 (P,S)', None, 'μg/m³', '2008', 'Promedio móvil 3 meses']
        ], columns=['Contaminante', 'Anual', 'Corto Plazo', 'Unidad', 'Última Actualización', 'Forma del Estándar'])
        
        st.markdown("<h3 style='text-align: center; color: #00B8D9; margin-top: 2rem;'>📊 Estándares EPA (NAAQS)</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: var(--text-secondary); margin-bottom: 1rem;'>(P) = Primario (salud) | (S) = Secundario (bienestar)</p>", unsafe_allow_html=True)
        st.dataframe(epa_tabla, use_container_width=True, hide_index=True, height=400)
        
        st.markdown("""
        <div class='warning-box' style='margin-top: 1.5rem;'>
            <p><strong>⚠️ Designaciones de no cumplimiento:</strong> Áreas que exceden NAAQS son designadas como 
            "nonattainment" y deben desarrollar planes de mejora con cronograma específico. El incumplimiento 
            persistente puede resultar en sanciones federales.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("""
        <div class='corporate-card fade-in'>
            <h2>🇨🇦 Canadian Ambient Air Quality Standards (CAAQS)</h2>
            <p style='font-size: 1.05rem;'>
                Canadá utiliza un <strong>sistema de mejora continua</strong> con estándares que se actualizan 
                progresivamente cada 5 años. La gestión se realiza por Air Zones con sistema de clasificación 
                por colores que determina las acciones requeridas.
            </p>
            
            <div class='success-box' style='margin-top: 1.5rem;'>
                <p><strong>✓ Enfoque innovador:</strong> Sistema de "Management Levels" (Verde, Amarillo, Naranja, Rojo) 
                que vincula automáticamente el nivel de calidad del aire con acciones de gestión obligatorias.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='normative-card internacional fade-in'>
            <span class='status-badge internacional'>● CAAQS 2020-2025</span>
            <h3>Canadian Ambient Air Quality Standards</h3>
            <p style='font-size: 1.05rem; margin: 1rem 0;'>
                <strong>Estándares Canadienses de Calidad del Aire Ambiente</strong>
            </p>
            <p>
                Sistema de gestión por Air Zones implementado nacionalmente. Los estándares 2020 están en vigor 
                y los estándares 2025 entrarán en vigencia próximamente. El sistema incluye objetivos a 2030. 
                Cada provincia y territorio gestiona sus Air Zones con obligación de reportar anualmente al 
                Canadian Council of Ministers of the Environment (CCME).
            </p>
            <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
                <strong>Base legal:</strong> Canadian Environmental Protection Act | 
                <strong>Coordinación:</strong> CCME
            </p>
            <a href='https://www.ccme.ca/en/air-quality-report' 
               target='_blank' class='corporate-button'>
                📄 Ver Reporte CAAQS Anual
            </a>
            <a href='https://www.canada.ca/en/environment-climate-change/services/air-quality-health-index.html' 
               target='_blank' class='corporate-button'>
                📖 Índice de Calidad del Aire
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        canada_tabla = pd.DataFrame([
            ['PM2.5', 8.8, 8.0, 6.0, 'μg/m³', 'Anual (percentil 98 de promedios diarios)'],
            ['PM2.5', 27, 25, 20, 'μg/m³', '24h (percentil 98)'],
            ['O3', 62, 60, 56, 'ppb', '8h (4to valor máximo anual)'],
            ['NO2', 60, 50, 42, 'ppb', '1h (percentil 98 anual)'],
            ['SO2', 70, 65, 50, 'ppb', '1h (percentil 99 anual)']
        ], columns=['Contaminante', 'Estándar 2020', 'Meta 2025', 'Objetivo 2030', 'Unidad', 'Forma del Estándar'])
        
        st.markdown("<h3 style='text-align: center; color: #00B8D9; margin-top: 2rem;'>📊 Evolución de Estándares CAAQS</h3>", unsafe_allow_html=True)
        st.dataframe(canada_tabla, use_container_width=True, hide_index=True, height=250)
        
        # Sistema de Air Zone Management
        st.markdown("""
        <div class='corporate-card' style='margin-top: 2rem;'>
            <h3>🎯 Sistema de Gestión por Air Zones</h3>
            <p style='color: var(--text-secondary); margin-bottom: 1.5rem;'>
                Clasificación por niveles de gestión según cumplimiento de CAAQS
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div style='background: linear-gradient(135deg, rgba(0, 200, 83, 0.15), rgba(0, 230, 118, 0.1)); 
                        padding: 1.5rem; border-radius: 10px; border-left: 4px solid #00C853; margin: 0.5rem 0;'>
                <h4 style='color: #00C853; margin: 0 0 0.5rem 0;'>🟢 Verde - Buena Gestión</h4>
                <p style='color: var(--text-secondary); font-size: 0.95rem; margin: 0;'>
                    Cumple todos los CAAQS. Mantener acciones actuales de gestión.
                </p>
            </div>
            
            <div style='background: linear-gradient(135deg, rgba(255, 179, 0, 0.15), rgba(255, 152, 0, 0.1)); 
                        padding: 1.5rem; border-radius: 10px; border-left: 4px solid #FFB300; margin: 0.5rem 0;'>
                <h4 style='color: #FFB300; margin: 0 0 0.5rem 0;'>🟡 Amarillo - Gestión Activa</h4>
                <p style='color: var(--text-secondary); font-size: 0.95rem; margin: 0;'>
                    Se acerca a exceder CAAQS. Implementar medidas preventivas.
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style='background: linear-gradient(135deg, rgba(255, 87, 34, 0.15), rgba(244, 67, 54, 0.1)); 
                        padding: 1.5rem; border-radius: 10px; border-left: 4px solid #FF5722; margin: 0.5rem 0;'>
                <h4 style='color: #FF5722; margin: 0 0 0.5rem 0;'>🟠 Naranja - Acción Obligatoria</h4>
                <p style='color: var(--text-secondary); font-size: 0.95rem; margin: 0;'>
                    Excede CAAQS. Plan de gestión obligatorio con metas y cronograma.
                </p>
            </div>
            
            <div style='background: linear-gradient(135deg, rgba(211, 47, 47, 0.15), rgba(198, 40, 40, 0.1)); 
                        padding: 1.5rem; border-radius: 10px; border-left: 4px solid #D32F2F; margin: 0.5rem 0;'>
                <h4 style='color: #D32F2F; margin: 0 0 0.5rem 0;'>🔴 Rojo - Intervención Urgente</h4>
                <p style='color: var(--text-secondary); font-size: 0.95rem; margin: 0;'>
                    Excede significativamente CAAQS. Plan de acción inmediato y estricto.
                </p>
            </div>
            """, unsafe_allow_html=True)
    
    with tab4:
        st.markdown("<h2 style='text-align: center; margin-bottom: 2rem;'>📊 Análisis Comparativo Internacional</h2>", unsafe_allow_html=True)
        
        # Comparación PM2.5
        st.markdown("""
        <div class='corporate-card fade-in'>
            <h3>Comparación PM2.5 - Estándar Más Crítico para Salud</h3>
            <p style='color: var(--text-secondary); margin-bottom: 1rem;'>
                Valores anuales y de 24 horas según cada jurisdicción
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        comparacion = pd.DataFrame([
            {'Entidad': 'OMS 2021', 'Anual': 5, '24h': 15, 'Región': 'Global'},
            {'Entidad': 'EPA USA 2024', 'Anual': 9, '24h': 35, 'Región': 'América'},
            {'Entidad': 'Canadá 2025', 'Anual': 8, '24h': 25, 'Región': 'América'},
            {'Entidad': 'OEFA Perú', 'Anual': 25, '24h': 50, 'Región': 'América'}
        ])
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
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
        
        fig.add_trace(go.Bar(
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
        
        fig.update_layout(
            barmode='group',
            height=550,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#E3E8EF', size=13, family='Inter'),
            xaxis=dict(showgrid=False, title=''),
            yaxis=dict(
                showgrid=True,
                gridcolor='rgba(255,255,255,0.06)',
                title='Concentración (μg/m³)',
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
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Tabla comparativa completa
        st.markdown("""
        <div class='corporate-card' style='margin-top: 2rem;'>
            <h3>Tabla Comparativa Completa de Estándares</h3>
            <p style='color: var(--text-secondary); margin-bottom: 1rem;'>
                Comparación de todos los contaminantes criterio
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        tabla_completa = pd.DataFrame([
            ['PM2.5 Anual', '5 μg/m³', '9 μg/m³', '8 μg/m³', '25 μg/m³', '⚠️ Perú 5x más permisivo'],
            ['PM2.5 24h', '15 μg/m³', '35 μg/m³', '25 μg/m³', '50 μg/m³', '⚠️ Perú 3.3x más permisivo'],
            ['PM10 Anual', '15 μg/m³', 'No establece', 'No establece', '50 μg/m³', '⚠️ Perú 3.3x más permisivo'],
            ['PM10 24h', '45 μg/m³', '150 μg/m³', 'No establece', '100 μg/m³', '✓ Perú más estricto que EPA'],
            ['NO2 Anual', '10 μg/m³', '100 μg/m³', '113 μg/m³', '100 μg/m³', '⚠️ Perú 10x más permisivo'],
            ['NO2 1h', '25 μg/m³', '188 μg/m³', '113 μg/m³', '200 μg/m³', '⚠️ Perú 8x más permisivo'],
            ['SO2 24h', '40 μg/m³', 'No establece', 'No establece', '250 μg/m³', '⚠️ Perú 6.25x más permisivo'],
            ['O3 8h', '100 μg/m³', '137 μg/m³', '120 μg/m³', '100 μg/m³', '✓ Perú igual a OMS'],
            ['CO 8h', '4 mg/m³', '10 mg/m³', 'No establece', '10 mg/m³', '⚠️ Perú 2.5x más permisivo']
        ], columns=['Contaminante/Período', 'OMS 2021', 'EPA USA', 'Canadá 2025', 'Perú (ECA)', 'Evaluación'])
        
        st.dataframe(tabla_completa, use_container_width=True, hide_index=True, height=400)
        
        # Análisis y conclusiones
        st.markdown("""
        <div class='corporate-card' style='margin-top: 2rem;'>
            <h3>💡 Análisis Comparativo y Recomendaciones</h3>
            
            <div style='margin-top: 1.5rem;'>
                <h4 style='color: #00B8D9; font-size: 1.1rem;'>Principales Hallazgos:</h4>
                <ul style='color: var(--text-secondary); line-height: 1.8; margin-top: 1rem;'>
                    <li><strong>Material Particulado Fino (PM2.5):</strong> El estándar peruano anual (25 μg/m³) 
                    es 5 veces más permisivo que la recomendación OMS (5 μg/m³) y 2.8 veces más alto que EPA USA (9 μg/m³). 
                    Esta brecha representa el mayor desafío normativo nacional.</li>
                    
                    <li><strong>Dióxido de Nitrógeno (NO2):</strong> Perú tiene uno de los estándares más permisivos 
                    internacionalmente. La OMS 2021 redujo su recomendación a 10 μg/m³ anual, 10 veces más estricto 
                    que el ECA peruano.</li>
                    
                    <li><strong>Dióxido de Azufre (SO2):</strong> El estándar peruano de 24h (250 μg/m³) contrasta con 
                    la guía OMS (40 μg/m³). EPA eliminó el estándar de 24h y usa uno de 1h más estricto.</li>
                    
                    <li><strong>Ozono (O3):</strong> Perú mantiene un estándar alineado con OMS (100 μg/m³ en 8h), 
                    siendo uno de los pocos parámetros donde la normativa nacional es competitiva internacionalmente.</li>
                    
                    <li><strong>PM10:</strong> Paradójicamente, el estándar peruano de 24h para PM10 (100 μg/m³) es 
                    más estricto que el de EPA (150 μg/m³), aunque menos que OMS (45 μg/m³).</li>
                </ul>
            </div>
            
            <div class='warning-box' style='margin-top: 2rem;'>
                <h4 style='margin-top: 0;'>⚠️ Implicaciones para Salud Pública</h4>
                <p>
                    La evidencia científica revisada por la OMS en 2021 demuestra que <strong>no existe un umbral seguro</strong> 
                    para material particulado: incluso concentraciones bajas causan efectos adversos en salud. Los estándares 
                    más permisivos implican mayor carga de enfermedad y mortalidad prematura en la población peruana.
                </p>
            </div>
            
            <div class='success-box' style='margin-top: 1.5rem;'>
                <h4 style='margin-top: 0;'>✓ Recomendaciones Estratégicas</h4>
                <ol style='color: var(--text-secondary); line-height: 1.8; padding-left: 1.2rem;'>
                    <li><strong>Actualización Gradual de ECA:</strong> Implementar una hoja de ruta de 10 años con 
                    metas intermedias progresivas hacia estándares similares a EPA y eventualmente OMS.</li>
                    
                    <li><strong>Priorización de PM2.5:</strong> Enfocar esfuerzos iniciales en reducir el estándar 
                    de PM2.5 anual, el contaminante con mayor impacto en salud pública.</li>
                    
                    <li><strong>Fortalecimiento de Redes de Monitoreo:</strong> Expandir la red de estaciones para 
                    tener datos representativos nacionales antes de endurecer estándares.</li>
                    
                    <li><strong>Incentivos para Cumplimiento:</strong> Desarrollar programas de incentivos técnicos 
                    y financieros para que industrias inviertan en tecnologías de control más efectivas.</li>
                    
                    <li><strong>Gestión de Calidad de Aire Local:</strong> Adoptar sistema similar al de Canadá 
                    (Air Zones) con clasificación por colores y acciones de gestión vinculadas.</li>
                    
                    <li><strong>Comunicación de Riesgos:</strong> Implementar índices de calidad del aire de fácil 
                    comprensión pública con recomendaciones de salud específicas.</li>
                    
                    <li><strong>Inventarios de Emisiones:</strong> Completar inventarios nacionales detallados para 
                    identificar fuentes prioritarias de reducción.</li>
                    
                    <li><strong>Colaboración Internacional:</strong> Aprender de experiencias de países con normativas 
                    más estrictas y buscar cooperación técnica y financiera.</li>
                </ol>
            </div>
            
            <div class='info-box' style='margin-top: 1.5rem;'>
                <p><strong>📈 Tendencia Global:</strong> Todos los países analizados muestran una tendencia clara 
                hacia estándares más estrictos basados en nueva evidencia científica. Perú debe evaluar actualizar 
                sus ECA para mantenerse alineado con mejores prácticas internacionales y proteger adecuadamente 
                la salud de su población.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ===================== FOOTER CORPORATIVO =====================
st.markdown("""
<div class='corporate-footer'>
    <h3>Universidad Nacional de Moquegua</h3>
    <p style='font-size: 1.1rem; margin-top: 0.5rem;'>Facultad de Ingeniería y Arquitectura</p>
    
    <div class='divider'></div>
    
    <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; text-align: left; max-width: 1000px; margin: 2rem auto 0;'>
        <div>
            <h4 style='color: #00B8D9; margin-bottom: 0.75rem;'>📚 Curso</h4>
            <p>Contaminación y Control Atmosférico</p>
        </div>
        
        <div>
            <h4 style='color: #00B8D9; margin-bottom: 0.75rem;'>👨‍🏫 Docente</h4>
            <p>Prof. Dr. José Antonio Valeriano Zapana</p>
        </div>
        
        <div>
            <h4 style='color: #00B8D9; margin-bottom: 0.75rem;'>🔄 Actualización</h4>
            <p>Octubre 2024 - Ciclo 2024-II</p>
        </div>
        
        <div>
            <h4 style='color: #00B8D9; margin-bottom: 0.75rem;'>🛠️ Tecnología</h4>
            <p>Streamlit • Plotly • Python</p>
        </div>
    </div>
    
    <div class='divider'></div>
    
    <p style='font-size: 0.9rem; opacity: 0.8; margin-top: 1.5rem;'>
        Sistema Integral de Consulta de Marco Normativo de Calidad del Aire
    </p>
    <p style='font-size: 0.85rem; opacity: 0.6; margin-top: 0.5rem;'>
        Datos oficiales: MINAM • OEFA • OMS • EPA • CCME | © 2024 UNAM
    </p>
</div>
""", unsafe_allow_html=True)
