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
    
    /* CRÍTICO: Color del texto mientras escribes */
    [data-testid="stSidebar"] input,
    [data-testid="stSidebar"] input:focus,
    [data-testid="stSidebar"] textarea {
        color: white !important;
        -webkit-text-fill-color: white !important;
    }
    
    /* También para el valor del input */
    [data-testid="stSidebar"] [data-baseweb="input"] input {
        color: white !important;
        -webkit-text-fill-color: white !important;
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
    
    /* Botones de Streamlit personalizados */
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
    
    /* Expanders mejorados */
    .streamlit-expanderHeader {
        background: rgba(19, 47, 76, 0.6);
        backdrop-filter: blur(10px);
        border-radius: 8px;
        border: 1px solid rgba(255, 255, 255, 0.06);
        color: var(--text-primary);
        font-weight: 600;
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
    
    /* Animaciones Timeline */
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    @keyframes slide-in {
        from { opacity: 0; transform: translateX(-30px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    .timeline-item {
        animation: slide-in 0.6s ease-out;
    }
    
    .timeline-icon:hover {
        animation: float 2s ease-in-out infinite;
        transform: scale(1.1);
    }
    
    .timeline-card:hover {
        transform: translateX(10px) scale(1.02);
        box-shadow: 0 20px 60px rgba(0,101,255,0.4);
    }
    
    .number-badge {
        position: absolute;
        top: -10px;
        left: -10px;
        width: 35px;
        height: 35px;
        background: linear-gradient(135deg, #FFB300, #FF6F00);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 800;
        color: white;
        font-size: 1rem;
        box-shadow: 0 4px 15px rgba(255,179,0,0.5);
        z-index: 10;
    }
</style>
""", unsafe_allow_html=True)

# Estado de sesión
if 'pagina' not in st.session_state:
    st.session_state.pagina = "Inicio"

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
        st.markdown("## 📚 Sistema de Consulta Normativo")
        st.write("Plataforma integral que centraliza el marco normativo completo sobre calidad del aire en Perú y referencias internacionales, facilitando el acceso a información técnica y legal actualizada.")
        
        st.markdown("---")
        st.markdown("### 🔄 Proceso del Marco Normativo")
        st.caption("Flujo interactivo del sistema de gestión de calidad del aire")
        
        # Línea de tiempo CORREGIDA
        timeline_html = """
        <div style='margin: 2rem 0;'>
            <div class='timeline-item' style='position: relative; margin-bottom: 2.5rem;'>
                <div style='display: flex; align-items: stretch; gap: 1.5rem;'>
                    <div class='timeline-icon' style='position: relative; flex-shrink: 0; width: 100px; height: 100px; background: linear-gradient(135deg, #0065FF 0%, #00B8D9 100%); border-radius: 20px; display: flex; align-items: center; justify-content: center; box-shadow: 0 15px 35px rgba(0,101,255,0.4); transition: all 0.4s;'>
                        <div class='number-badge'>1</div>
                        <span style='font-size: 3rem;'>📋</span>
                    </div>
                    <div class='timeline-card' style='flex: 1; background: linear-gradient(135deg, rgba(0,101,255,0.15) 0%, rgba(0,184,217,0.1) 100%); backdrop-filter: blur(20px); padding: 1.8rem; border-radius: 16px; border-left: 5px solid #0065FF; transition: all 0.3s;'>
                        <div style='display: flex; justify-content: space-between; margin-bottom: 1rem;'>
                            <div>
                                <h3 style='margin: 0; color: white; font-size: 1.4rem;'>Estándares de Calidad Ambiental</h3>
                                <p style='margin: 0; color: #60A5FA; font-size: 0.9rem;'>ECA • Aire Ambiente</p>
                            </div>
                            <div style='background: linear-gradient(135deg, rgba(0,101,255,0.4), rgba(0,184,217,0.4)); padding: 0.5rem 1.2rem; border-radius: 25px;'>
                                <span style='color: white; font-weight: 700;'>12</span> <span style='color: rgba(255,255,255,0.8);'>norm.</span>
                            </div>
                        </div>
                        <p style='color: rgba(255,255,255,0.85); margin: 0; line-height: 1.6;'>
                            ✓ Define concentraciones máximas permitidas<br>
                            ✓ Protege la salud de la población<br>
                            ✓ Medido en estaciones de monitoreo
                        </p>
                    </div>
                </div>
                <div style='position: absolute; left: 49px; top: 100px; width: 3px; height: 50px; background: linear-gradient(180deg, #0065FF, #00B8D9); opacity: 0.6;'></div>
            </div>
            
            <div class='timeline-item' style='position: relative; margin-bottom: 2.5rem;'>
                <div style='display: flex; align-items: stretch; gap: 1.5rem;'>
                    <div class='timeline-icon' style='position: relative; flex-shrink: 0; width: 100px; height: 100px; background: linear-gradient(135deg, #00B8D9 0%, #00C853 100%); border-radius: 20px; display: flex; align-items: center; justify-content: center; box-shadow: 0 15px 35px rgba(0,184,217,0.4); transition: all 0.4s;'>
                        <div class='number-badge'>2</div>
                        <span style='font-size: 3rem;'>🏭</span>
                    </div>
                    <div class='timeline-card' style='flex: 1; background: linear-gradient(135deg, rgba(0,184,217,0.15) 0%, rgba(0,200,83,0.1) 100%); backdrop-filter: blur(20px); padding: 1.8rem; border-radius: 16px; border-left: 5px solid #00B8D9; transition: all 0.3s;'>
                        <div style='display: flex; justify-content: space-between; margin-bottom: 1rem;'>
                            <div>
                                <h3 style='margin: 0; color: white; font-size: 1.4rem;'>Límites Máximos Permisibles</h3>
                                <p style='margin: 0; color: #00B8D9; font-size: 0.9rem;'>LMP • Fuente de Emisión</p>
                            </div>
                            <div style='background: linear-gradient(135deg, rgba(0,184,217,0.4), rgba(0,200,83,0.4)); padding: 0.5rem 1.2rem; border-radius: 25px;'>
                                <span style='color: white; font-weight: 700;'>8</span> <span style='color: rgba(255,255,255,0.8);'>sect.</span>
                            </div>
                        </div>
                        <p style='color: rgba(255,255,255,0.85); margin: 0; line-height: 1.6;'>
                            ✓ Controla emisiones en chimeneas y ductos<br>
                            ✓ Específico por sector industrial<br>
                            ✓ Obligatorio para cumplimiento ambiental
                        </p>
                    </div>
                </div>
                <div style='position: absolute; left: 49px; top: 100px; width: 3px; height: 50px; background: linear-gradient(180deg, #00B8D9, #00C853); opacity: 0.6;'></div>
            </div>
            
            <div class='timeline-item' style='position: relative; margin-bottom: 2.5rem;'>
                <div style='display: flex; align-items: stretch; gap: 1.5rem;'>
                    <div class='timeline-icon' style='position: relative; flex-shrink: 0; width: 100px; height: 100px; background: linear-gradient(135deg, #00C853 0%, #8BC34A 100%); border-radius: 20px; display: flex; align-items: center; justify-content: center; box-shadow: 0 15px 35px rgba(0,200,83,0.4); transition: all 0.4s;'>
                        <div class='number-badge'>3</div>
                        <span style='font-size: 3rem;'>📖</span>
                    </div>
                    <div class='timeline-card' style='flex: 1; background: linear-gradient(135deg, rgba(0,200,83,0.15) 0%, rgba(139,195,74,0.1) 100%); backdrop-filter: blur(20px); padding: 1.8rem; border-radius: 16px; border-left: 5px solid #00C853; transition: all 0.3s;'>
                        <div style='display: flex; justify-content: space-between; margin-bottom: 1rem;'>
                            <div>
                                <h3 style='margin: 0; color: white; font-size: 1.4rem;'>Protocolos de Monitoreo</h3>
                                <p style='margin: 0; color: #00C853; font-size: 0.9rem;'>Medición y Análisis</p>
                            </div>
                            <div style='background: linear-gradient(135deg, rgba(0,200,83,0.4), rgba(139,195,74,0.4)); padding: 0.5rem 1.2rem; border-radius: 25px;'>
                                <span style='color: white; font-weight: 700;'>5</span> <span style='color: rgba(255,255,255,0.8);'>prot.</span>
                            </div>
                        </div>
                        <p style='color: rgba(255,255,255,0.85); margin: 0; line-height: 1.6;'>
                            ✓ Procedimientos estandarizados de muestreo<br>
                            ✓ Garantiza comparabilidad de resultados<br>
                            ✓ Métodos EPA y normas técnicas
                        </p>
                    </div>
                </div>
                <div style='position: absolute; left: 49px; top: 100px; width: 3px; height: 50px; background: linear-gradient(180deg, #00C853, #FFB300); opacity: 0.6;'></div>
            </div>
            
            <div class='timeline-item' style='position: relative; margin-bottom: 2.5rem;'>
                <div style='display: flex; align-items: stretch; gap: 1.5rem;'>
                    <div class='timeline-icon' style='position: relative; flex-shrink: 0; width: 100px; height: 100px; background: linear-gradient(135deg, #FFB300 0%, #FF6F00 100%); border-radius: 20px; display: flex; align-items: center; justify-content: center; box-shadow: 0 15px 35px rgba(255,179,0,0.4); transition: all 0.4s;'>
                        <div class='number-badge'>4</div>
                        <span style='font-size: 3rem;'>📐</span>
                    </div>
                    <div class='timeline-card' style='flex: 1; background: linear-gradient(135deg, rgba(255,179,0,0.15) 0%, rgba(255,111,0,0.1) 100%); backdrop-filter: blur(20px); padding: 1.8rem; border-radius: 16px; border-left: 5px solid #FFB300; transition: all 0.3s;'>
                        <div style='display: flex; justify-content: space-between; margin-bottom: 1rem;'>
                            <div>
                                <h3 style='margin: 0; color: white; font-size: 1.4rem;'>Lineamientos y Guías</h3>
                                <p style='margin: 0; color: #FFB300; font-size: 0.9rem;'>Implementación</p>
                            </div>
                            <div style='background: linear-gradient(135deg, rgba(255,179,0,0.4), rgba(255,111,0,0.4)); padding: 0.5rem 1.2rem; border-radius: 25px;'>
                                <span style='color: white; font-weight: 700;'>★</span>
                            </div>
                        </div>
                        <p style='color: rgba(255,255,255,0.85); margin: 0; line-height: 1.6;'>
                            ✓ Guías técnicas operativas<br>
                            ✓ Inventarios de emisiones atmosféricas<br>
                            ✓ Estados de alerta y emergencia
                        </p>
                    </div>
                </div>
                <div style='position: absolute; left: 49px; top: 100px; width: 3px; height: 50px; background: linear-gradient(180deg, #FFB300, #8B5CF6); opacity: 0.6;'></div>
            </div>
            
            <div class='timeline-item' style='position: relative; margin-bottom: 2.5rem;'>
                <div style='display: flex; align-items: stretch; gap: 1.5rem;'>
                    <div class='timeline-icon' style='position: relative; flex-shrink: 0; width: 100px; height: 100px; background: linear-gradient(135deg, #8B5CF6 0%, #6366F1 100%); border-radius: 20px; display: flex; align-items: center; justify-content: center; box-shadow: 0 15px 35px rgba(139,92,246,0.4); transition: all 0.4s;'>
                        <div class='number-badge'>5</div>
                        <span style='font-size: 3rem;'>🛡️</span>
                    </div>
                    <div class='timeline-card' style='flex: 1; background: linear-gradient(135deg, rgba(139,92,246,0.15) 0%, rgba(99,102,241,0.1) 100%); backdrop-filter: blur(20px); padding: 1.8rem; border-radius: 16px; border-left: 5px solid #8B5CF6; transition: all 0.3s;'>
                        <div style='display: flex; justify-content: space-between; margin-bottom: 1rem;'>
                            <div>
                                <h3 style='margin: 0; color: white; font-size: 1.4rem;'>Medidas de Control</h3>
                                <p style='margin: 0; color: #8B5CF6; font-size: 0.9rem;'>Tecnologías BAT</p>
                            </div>
                            <div style='background: linear-gradient(135deg, rgba(139,92,246,0.4), rgba(99,102,241,0.4)); padding: 0.5rem 1.2rem; border-radius: 25px;'>
                                <span style='color: white; font-weight: 700;'>★★</span>
                            </div>
                        </div>
                        <p style='color: rgba(255,255,255,0.85); margin: 0; line-height: 1.6;'>
                            ✓ Sistemas de reducción de emisiones<br>
                            ✓ Filtros, precipitadores, scrubbers<br>
                            ✓ Mejores técnicas disponibles (MTD)
                        </p>
                    </div>
                </div>
                <div style='position: absolute; left: 49px; top: 100px; width: 3px; height: 50px; background: linear-gradient(180deg, #8B5CF6, #EC4899); opacity: 0.6;'></div>
            </div>
            
            <div class='timeline-item' style='position: relative;'>
                <div style='display: flex; align-items: stretch; gap: 1.5rem;'>
                    <div class='timeline-icon' style='position: relative; flex-shrink: 0; width: 100px; height: 100px; background: linear-gradient(135deg, #EC4899 0%, #F43F5E 100%); border-radius: 20px; display: flex; align-items: center; justify-content: center; box-shadow: 0 15px 35px rgba(236,72,153,0.4); transition: all 0.4s;'>
                        <div class='number-badge'>6</div>
                        <span style='font-size: 3rem;'>🌍</span>
                    </div>
                    <div class='timeline-card' style='flex: 1; background: linear-gradient(135deg, rgba(236,72,153,0.15) 0%, rgba(244,63,94,0.1) 100%); backdrop-filter: blur(20px); padding: 1.8rem; border-radius: 16px; border-left: 5px solid #EC4899; transition: all 0.3s;'>
                        <div style='display: flex; justify-content: space-between; margin-bottom: 1rem;'>
                            <div>
                                <h3 style='margin: 0; color: white; font-size: 1.4rem;'>Referencia Internacional</h3>
                                <p style='margin: 0; color: #EC4899; font-size: 0.9rem;'>OMS • EPA • Canadá</p>
                            </div>
                            <div style='background: linear-gradient(135deg, rgba(236,72,153,0.4), rgba(244,63,94,0.4)); padding: 0.5rem 1.2rem; border-radius: 25px;'>
                                <span style='color: white; font-weight: 700;'>★★★</span>
                            </div>
                        </div>
                        <p style='color: rgba(255,255,255,0.85); margin: 0; line-height: 1.6;'>
                            ✓ Benchmarking internacional<br>
                            ✓ Mejores prácticas globales<br>
                            ✓ Actualización continua de estándares
                        </p>
                    </div>
                </div>
            </div>
        </div>
        """
        
        st.markdown(timeline_html, unsafe_allow_html=True)
        
        st.markdown("---")
        st.success("✓ **Acceso directo** a documentos oficiales con enlaces actualizados  \n✓ **Visualizaciones** interactivas para análisis comparativo  \n✓ **Información técnica** validada y referencias normativas completas")
    
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
        <p style='color: rgba(255,255,255,0.9); margin-bottom: 1.5rem;'>
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

else:
    st.info(f"Página {st.session_state.pagina} en construcción...")

# FOOTER CORPORATIVO
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
