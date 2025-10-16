import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Configuración
st.set_page_config(
    page_title="Marco Normativo del Aire - Perú",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS ULTRA PREMIUM - $1000 DESIGN
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600;700;800;900&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    [data-testid="stSidebar"] {display: none;}
    
    /* BACKGROUND OSCURO PROFESIONAL */
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
            radial-gradient(circle at 15% 20%, rgba(34, 211, 238, 0.15) 0%, transparent 45%),
            radial-gradient(circle at 85% 10%, rgba(14, 165, 233, 0.18) 0%, transparent 45%),
            radial-gradient(circle at 50% 80%, rgba(6, 182, 212, 0.12) 0%, transparent 50%),
            radial-gradient(circle at 90% 70%, rgba(56, 189, 248, 0.1) 0%, transparent 45%);
        z-index: 0;
        animation: breathe 8s ease-in-out infinite;
    }
    
    @keyframes breathe {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.8; }
    }
    
    .main::after {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            linear-gradient(180deg, rgba(0,0,0,0) 0%, rgba(0,0,0,0.3) 100%);
        z-index: 0;
        pointer-events: none;
    }
    
    .stApp {
        background: transparent;
    }
    
    /* Animaciones Premium */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(50px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-40px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes shimmer {
        0% {
            background-position: -1000px 0;
        }
        100% {
            background-position: 1000px 0;
        }
    }
    
    @keyframes glow-pulse {
        0%, 100% {
            box-shadow: 
                0 0 40px rgba(6, 182, 212, 0.35),
                0 0 80px rgba(6, 182, 212, 0.2),
                0 20px 60px rgba(0, 0, 0, 0.6);
        }
        50% {
            box-shadow: 
                0 0 60px rgba(6, 182, 212, 0.5),
                0 0 100px rgba(6, 182, 212, 0.3),
                0 30px 80px rgba(0, 0, 0, 0.7);
        }
    }
    
    /* HEADER ÉPICO - NIVEL $1000 */
    .mega-header {
        text-align: center;
        padding: 80px 50px;
        background: 
            linear-gradient(135deg, 
                rgba(6, 182, 212, 0.08) 0%,
                rgba(14, 165, 233, 0.12) 50%,
                rgba(6, 78, 59, 0.08) 100%);
        backdrop-filter: blur(30px) saturate(200%);
        border-radius: 24px;
        margin-bottom: 50px;
        border: 1px solid rgba(34, 211, 238, 0.25);
        box-shadow: 
            0 30px 90px rgba(0, 0, 0, 0.9),
            inset 0 1px 0 rgba(34, 211, 238, 0.15),
            0 0 100px rgba(6, 182, 212, 0.2);
        animation: fadeInUp 1s ease-out, glow-pulse 4s ease-in-out infinite;
        position: relative;
        z-index: 1;
        overflow: hidden;
    }
    
    .mega-header::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: 
            repeating-conic-gradient(
                from 0deg at 50% 50%,
                rgba(6, 182, 212, 0.06) 0deg 30deg,
                transparent 30deg 60deg
            );
        animation: rotate-slow 30s linear infinite;
        opacity: 0.4;
    }
    
    @keyframes rotate-slow {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    .mega-header h1 {
        font-size: 4.5em !important;
        font-weight: 900 !important;
        background: linear-gradient(135deg, 
            #06b6d4 0%, 
            #22d3ee 25%,
            #67e8f9 50%,
            #22d3ee 75%,
            #06b6d4 100%);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0 !important;
        position: relative;
        z-index: 2;
        letter-spacing: -0.03em;
        text-shadow: 0 0 100px rgba(6, 182, 212, 0.5);
        animation: shimmer-text 3s linear infinite;
    }
    
    @keyframes shimmer-text {
        0% { background-position: 0% center; }
        100% { background-position: 200% center; }
    }
    
    .mega-header .subtitle {
        color: #a5f3fc;
        font-size: 1.6em;
        font-weight: 700;
        margin-top: 25px;
        position: relative;
        z-index: 2;
        letter-spacing: 0.02em;
        text-transform: uppercase;
        font-family: 'Space Grotesk', sans-serif;
        text-shadow: 0 2px 20px rgba(6, 182, 212, 0.3);
    }
    
    .mega-header .description {
        color: #67e8f9;
        font-size: 1.2em;
        margin-top: 20px;
        font-weight: 500;
        position: relative;
        z-index: 2;
        line-height: 1.6;
    }
    
    .mega-header .meta {
        color: #22d3ee;
        font-size: 1em;
        margin-top: 25px;
        position: relative;
        z-index: 2;
        font-weight: 600;
    }
    
    /* GLASS CARDS - ELEGANCIA MÁXIMA */
    .elite-glass {
        background: linear-gradient(135deg, 
            rgba(17, 24, 39, 0.95) 0%, 
            rgba(31, 41, 55, 0.9) 100%);
        backdrop-filter: blur(20px) saturate(180%);
        padding: 50px;
        border-radius: 20px;
        border: 1px solid rgba(6, 182, 212, 0.25);
        margin: 30px 0;
        box-shadow: 
            0 25px 70px rgba(0, 0, 0, 0.8),
            inset 0 1px 0 rgba(6, 182, 212, 0.15),
            0 0 60px rgba(6, 182, 212, 0.15);
        animation: slideIn 0.8s ease-out;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        z-index: 1;
    }
    
    .elite-glass::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 1px;
        background: linear-gradient(90deg, 
            transparent, 
            rgba(6, 182, 212, 0.6), 
            transparent);
    }
    
    .elite-glass:hover {
        transform: translateY(-5px);
        box-shadow: 
            0 35px 100px rgba(0, 0, 0, 0.9),
            inset 0 1px 0 rgba(6, 182, 212, 0.25),
            0 0 80px rgba(6, 182, 212, 0.25);
        border-color: rgba(6, 182, 212, 0.4);
    }
    
    .elite-glass h2 {
        font-size: 2.2em;
        font-weight: 800;
        background: linear-gradient(135deg, #06b6d4 0%, #22d3ee 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0 0 25px 0;
        letter-spacing: -0.02em;
        font-family: 'Space Grotesk', sans-serif;
    }
    
    .elite-glass h3 {
        font-size: 1.6em;
        font-weight: 700;
        color: #22d3ee;
        margin: 20px 0;
        letter-spacing: -0.01em;
    }
    
    .elite-glass p, .elite-glass li {
        color: #e0f2fe;
        line-height: 1.9;
        font-size: 1.05em;
        font-weight: 400;
    }
    
    .elite-glass strong {
        color: #06b6d4;
        font-weight: 700;
    }
    
    /* LUXURY NORMATIVA CARDS */
    .platinum-card {
        background: linear-gradient(135deg, 
            rgba(31, 41, 55, 0.95) 0%, 
            rgba(17, 24, 39, 0.98) 100%);
        backdrop-filter: blur(20px);
        padding: 45px;
        border-radius: 20px;
        margin: 30px 0;
        border-left: 4px solid #06b6d4;
        box-shadow: 
            0 25px 70px rgba(0, 0, 0, 0.8),
            inset 0 1px 0 rgba(6, 182, 212, 0.15),
            -4px 0 30px rgba(6, 182, 212, 0.25);
        transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        animation: slideIn 0.8s ease-out;
        position: relative;
        overflow: hidden;
        z-index: 1;
    }
    
    .platinum-card::before {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 200px;
        height: 200px;
        background: radial-gradient(circle, rgba(6, 182, 212, 0.12) 0%, transparent 70%);
        border-radius: 50%;
    }
    
    .platinum-card:hover {
        transform: translateX(10px);
        box-shadow: 
            0 35px 100px rgba(0, 0, 0, 0.9),
            inset 0 1px 0 rgba(6, 182, 212, 0.25),
            -6px 0 50px rgba(6, 182, 212, 0.4);
        border-left-width: 6px;
    }
    
    .platinum-card h3 {
        color: #06b6d4 !important;
        font-size: 1.9em;
        font-weight: 800;
        margin: 0 0 20px 0;
        letter-spacing: -0.02em;
        font-family: 'Space Grotesk', sans-serif;
        position: relative;
        z-index: 2;
    }
    
    .platinum-card p {
        color: #e0f2fe;
        font-size: 1.1em;
        line-height: 1.9;
        margin: 20px 0;
        position: relative;
        z-index: 2;
    }
    
    .platinum-card strong {
        color: #22d3ee;
        font-weight: 700;
    }
    
    /* BADGES PREMIUM */
    .premium-badge {
        background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%);
        color: #000000;
        padding: 10px 26px;
        border-radius: 25px;
        font-size: 0.85em;
        font-weight: 800;
        display: inline-block;
        margin-right: 15px;
        box-shadow: 
            0 10px 30px rgba(6, 182, 212, 0.5),
            inset 0 1px 0 rgba(255, 255, 255, 0.3);
        letter-spacing: 0.05em;
        text-transform: uppercase;
        border: 1px solid rgba(255, 255, 255, 0.2);
        position: relative;
        z-index: 2;
    }
    
    .premium-badge.vigente {
        background: linear-gradient(135deg, #06b6d4 0%, #22d3ee 100%);
        box-shadow: 0 10px 30px rgba(6, 182, 212, 0.6);
    }
    
    .premium-badge.modificatoria {
        background: linear-gradient(135deg, #f59e0b 0%, #fbbf24 100%);
        box-shadow: 0 10px 30px rgba(245, 158, 11, 0.5);
    }
    
    .premium-badge.anterior {
        background: linear-gradient(135deg, #6b7280 0%, #9ca3af 100%);
        box-shadow: 0 10px 30px rgba(107, 114, 128, 0.4);
    }
    
    .premium-badge.ntp {
        background: linear-gradient(135deg, #3b82f6 0%, #60a5fa 100%);
        box-shadow: 0 10px 30px rgba(59, 130, 246, 0.5);
    }
    
    /* BOTONES PREMIUM */
    .diamond-btn {
        background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%);
        color: #000000;
        padding: 18px 40px;
        border-radius: 12px;
        text-decoration: none;
        display: inline-block;
        margin: 12px 10px;
        font-weight: 800;
        font-size: 1em;
        box-shadow: 
            0 15px 40px rgba(6, 182, 212, 0.5),
            inset 0 1px 0 rgba(255, 255, 255, 0.3);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        letter-spacing: 0.02em;
        border: 1px solid rgba(255, 255, 255, 0.2);
        z-index: 2;
    }
    
    .diamond-btn::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, 
            transparent, 
            rgba(255, 255, 255, 0.4), 
            transparent);
        transition: left 0.5s;
    }
    
    .diamond-btn:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 
            0 20px 60px rgba(6, 182, 212, 0.7),
            inset 0 1px 0 rgba(255, 255, 255, 0.4);
    }
    
    .diamond-btn:hover::before {
        left: 100%;
    }
    
    /* BOTONES DE NAVEGACIÓN */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, 
            rgba(31, 41, 55, 0.9) 0%, 
            rgba(17, 24, 39, 0.95) 100%);
        color: #06b6d4;
        border: 1.5px solid rgba(6, 182, 212, 0.3);
        border-radius: 12px;
        padding: 16px 20px;
        font-weight: 700;
        font-size: 0.95em;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        backdrop-filter: blur(10px);
        box-shadow: 
            0 8px 24px rgba(0, 0, 0, 0.6),
            inset 0 1px 0 rgba(6, 182, 212, 0.1);
        letter-spacing: 0.02em;
        text-transform: uppercase;
        font-family: 'Space Grotesk', sans-serif;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%);
        border-color: #06b6d4;
        color: #000000;
        transform: translateY(-2px);
        box-shadow: 
            0 15px 40px rgba(6, 182, 212, 0.5),
            inset 0 1px 0 rgba(255, 255, 255, 0.2);
    }
    
    /* TABS ELEGANTES */
    .stTabs [data-baseweb="tab-list"] {
        gap: 15px;
        background: rgba(17, 24, 39, 0.8);
        padding: 15px;
        border-radius: 16px;
        backdrop-filter: blur(20px);
        border: 1px solid rgba(6, 182, 212, 0.2);
    }
    
    .stTabs [data-baseweb="tab"] {
        background: linear-gradient(135deg, 
            rgba(31, 41, 55, 0.9) 0%, 
            rgba(17, 24, 39, 0.9) 100%);
        color: #22d3ee;
        border-radius: 12px;
        padding: 14px 30px;
        font-weight: 700;
        border: 1.5px solid rgba(6, 182, 212, 0.2);
        transition: all 0.3s ease;
        letter-spacing: 0.02em;
        text-transform: uppercase;
        font-size: 0.9em;
        font-family: 'Space Grotesk', sans-serif;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        border-color: rgba(6, 182, 212, 0.5);
        transform: translateY(-2px);
        color: #06b6d4;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%);
        color: #000000;
        box-shadow: 0 10px 30px rgba(6, 182, 212, 0.5);
        border-color: transparent;
    }
    
    /* DATAFRAMES PREMIUM */
    .dataframe {
        background: rgba(17, 24, 39, 0.95) !important;
        border-radius: 16px !important;
        overflow: hidden !important;
        border: 1px solid rgba(6, 182, 212, 0.25) !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6) !important;
    }
    
    .dataframe thead tr th {
        background: linear-gradient(135deg, 
            rgba(6, 182, 212, 0.2) 0%, 
            rgba(14, 165, 233, 0.25) 100%) !important;
        color: #06b6d4 !important;
        font-weight: 800 !important;
        padding: 18px !important;
        border-bottom: 2px solid rgba(6, 182, 212, 0.4) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
        font-size: 0.85em !important;
        font-family: 'Space Grotesk', sans-serif !important;
    }
    
    .dataframe tbody tr {
        transition: all 0.2s ease;
        border-bottom: 1px solid rgba(6, 182, 212, 0.1) !important;
    }
    
    .dataframe tbody tr:hover {
        background: rgba(6, 182, 212, 0.1) !important;
    }
    
    .dataframe tbody tr td {
        color: #e0f2fe !important;
        padding: 16px !important;
        font-weight: 500 !important;
    }
    
    /* MÉTRICAS */
    [data-testid="stMetricValue"] {
        font-size: 2.8em;
        font-weight: 900;
        background: linear-gradient(135deg, #06b6d4 0%, #22d3ee 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.02em;
    }
    
    [data-testid="stMetricLabel"] {
        color: #22d3ee !important;
        font-weight: 700;
        font-size: 1.1em;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* SCROLLBAR */
    ::-webkit-scrollbar {
        width: 14px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(17, 24, 39, 0.8);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%);
        border-radius: 10px;
        border: 2px solid rgba(17, 24, 39, 0.8);
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #22d3ee 0%, #06b6d4 100%);
    }
    
    /* TÍTULOS GLOBALES */
    h1, h2, h3, h4, h5, h6 {
        font-weight: 800 !important;
        letter-spacing: -0.02em !important;
        font-family: 'Space Grotesk', sans-serif !important;
    }
    
    /* LINKS */
    a {
        color: #06b6d4;
        text-decoration: none;
        transition: all 0.3s ease;
        font-weight: 700;
    }
    
    a:hover {
        color: #22d3ee;
        text-shadow: 0 0 20px rgba(6, 182, 212, 0.6);
    }
    
    /* SEPARADOR */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, 
            transparent, 
            rgba(6, 182, 212, 0.4), 
            transparent);
        margin: 60px 0;
    }
</style>
""", unsafe_allow_html=True)

# Estado
if 'pagina' not in st.session_state:
    st.session_state.pagina = "Inicio"

# HEADER MEGA PREMIUM
st.markdown("""
<div class='mega-header'>
    <h1>🌍 Marco Normativo de Calidad del Aire</h1>
    <p class='subtitle'>Universidad Nacional de Moquegua</p>
    <p class='description'>
        Herramienta Interactiva de Consulta | Normativas Peruanas e Internacionales
    </p>
    <p class='meta'>
        Prof. Dr. José Antonio Valeriano Zapana | 2024-2025
    </p>
</div>
""", unsafe_allow_html=True)

# MENÚ HORIZONTAL
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

with col1:
    if st.button("🏠 INICIO", use_container_width=True):
        st.session_state.pagina = "Inicio"

with col2:
    if st.button("📋 ECA", use_container_width=True):
        st.session_state.pagina = "ECA"

with col3:
    if st.button("🏭 LMP", use_container_width=True):
        st.session_state.pagina = "LMP"

with col4:
    if st.button("📖 PROTOCOLO", use_container_width=True):
        st.session_state.pagina = "Protocolo"

with col5:
    if st.button("📐 LINEAMIENTO", use_container_width=True):
        st.session_state.pagina = "Lineamiento"

with col6:
    if st.button("🛡️ MEDIDAS", use_container_width=True):
        st.session_state.pagina = "Medidas"

with col7:
    if st.button("🌍 INTERNACIONAL", use_container_width=True):
        st.session_state.pagina = "Normativas"

st.markdown("<br>", unsafe_allow_html=True)

# ===================== PÁGINA INICIO =====================
if st.session_state.pagina == "Inicio":
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("""
        <div class='elite-glass'>
            <h2>📚 Sobre esta Herramienta</h2>
            <p style='font-size: 1.15em;'>
                Plataforma integral que reúne el <strong>marco normativo completo</strong> sobre 
                calidad del aire en Perú y el mundo.
            </p>
            <ul style='font-size: 1.1em; line-height: 2.5;'>
                <li>✅ <strong>ECA:</strong> Estándares de Calidad Ambiental</li>
                <li>✅ <strong>LMP:</strong> Límites Máximos Permisibles</li>
                <li>✅ <strong>Protocolos:</strong> Monitoreo y medición</li>
                <li>✅ <strong>Lineamientos:</strong> Guías técnicas</li>
                <li>✅ <strong>Medidas de Control:</strong> Tecnologías</li>
                <li>✅ <strong>Normativas Internacionales:</strong> OMS, EPA, Canadá</li>
            </ul>
            <p style='margin-top: 35px; font-size: 1.1em;'>
                💡 <strong>Acceso directo</strong> a documentos oficiales con un solo click
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='elite-glass'>
            <h2>🎯 Acceso Rápido</h2>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("📋 Estándares ECA", use_container_width=True, type="primary"):
            st.session_state.pagina = "ECA"
        
        if st.button("🏭 Límites LMP", use_container_width=True):
            st.session_state.pagina = "LMP"
        
        if st.button("📖 Protocolos", use_container_width=True):
            st.session_state.pagina = "Protocolo"
        
        if st.button("📐 Lineamientos", use_container_width=True):
            st.session_state.pagina = "Lineamiento"
        
        if st.button("🛡️ Control de Emisiones", use_container_width=True):
            st.session_state.pagina = "Medidas"
        
        if st.button("🌍 Normativas Mundial", use_container_width=True):
            st.session_state.pagina = "Normativas"
    
    # Gráfico comparativo
    st.markdown("""
    <div class='elite-glass'>
        <h2>📊 Comparación Internacional - PM2.5 Anual</h2>
        <p style='font-size: 1.05em;'>Estándares más estrictos protegen mejor la salud pública</p>
    </div>
    """, unsafe_allow_html=True)
    
    datos_comp = pd.DataFrame([
        {'Entidad': 'OMS 2021', 'Valor': 5, 'Color': '#06b6d4'},
        {'Entidad': 'EPA USA', 'Valor': 9, 'Color': '#3b82f6'},
        {'Entidad': 'Canadá', 'Valor': 8.8, 'Color': '#8b5cf6'},
        {'Entidad': 'OEFA Perú', 'Valor': 25, 'Color': '#ef4444'}
    ])
    
    fig = px.bar(datos_comp, x='Entidad', y='Valor', 
                 color='Entidad',
                 color_discrete_sequence=['#06b6d4', '#3b82f6', '#8b5cf6', '#ef4444'],
                 title='',
                 text='Valor')
    fig.update_traces(texttemplate='%{text} μg/m³', textposition='outside',
                      marker=dict(line=dict(color='rgba(6, 182, 212, 0.4)', width=2)),
                      textfont=dict(size=14, color='#e0f2fe', family='Space Grotesk'))
    fig.update_layout(
        height=550,
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0f2fe', size=15, family='Space Grotesk'),
        xaxis=dict(showgrid=False, tickfont=dict(size=14, color='#22d3ee')),
        yaxis=dict(showgrid=True, gridcolor='rgba(6, 182, 212, 0.15)', 
                   title='Concentración (μg/m³)', 
                   titlefont=dict(color='#06b6d4'))
    )
    st.plotly_chart(fig, use_container_width=True)

# ===================== PÁGINA ECA =====================
elif st.session_state.pagina == "ECA":
    st.markdown("<h1 style='text-align: center; font-size: 3.5em; background: linear-gradient(135deg, #06b6d4 0%, #22d3ee 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-family: Space Grotesk;'>📋 Estándares de Calidad Ambiental (ECA)</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='elite-glass'>
        <h2>📜 ¿Qué son los ECA?</h2>
        <p style='font-size: 1.2em;'>
            Los ECA son <strong>estándares de calidad del aire ambiente</strong> que se miden en 
            estaciones de monitoreo para proteger la salud de la población. Establecen concentraciones 
            máximas de contaminantes permitidas en el aire que respiramos.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='platinum-card'>
        <span class='premium-badge vigente'>VIGENTE</span>
        <h3>D.S. N° 003-2017-MINAM</h3>
        <p style='font-size: 1.1em;'>
            <strong>Estándares de Calidad Ambiental (ECA) para Aire</strong><br><br>
            Establece los valores de concentración de contaminantes del aire que no deben superarse 
            para proteger la salud de las personas. Es la norma principal vigente en Perú.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2017/06/DS-003-2017-MINAM.pdf' 
           target='_blank' class='diamond-btn'>
            📄 Descargar Normativa Oficial
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='platinum-card'>
        <span class='premium-badge modificatoria'>MODIFICATORIA</span>
        <h3>D.S. N° 010-2019-MINAM</h3>
        <p style='font-size: 1.1em;'>
            <strong>Modificatoria de ECA para Aire</strong><br><br>
            Actualiza parámetros y períodos de evaluación para adaptarse a nueva evidencia científica 
            sobre efectos en la salud pública.
        </p>
        <a href='https://busquedas.elperuano.pe/download/url/decreto-supremo-que-modifica-el-decreto-supremo-n-003-2017-decreto-supremo-n-010-2019-minam-1792823-1' 
           target='_blank' class='diamond-btn'>
            📄 Descargar Modificatoria
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='platinum-card'>
        <span class='premium-badge anterior'>REFERENCIA HISTÓRICA</span>
        <h3>D.S. N° 074-2001-PCM</h3>
        <p style='font-size: 1.1em;'>
            <strong>Primera Norma de ECA en Perú</strong><br><br>
            Reglamento original de Estándares Nacionales de Calidad Ambiental del Aire. 
            Derogada por el D.S. 003-2017-MINAM pero importante para contexto histórico.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_074-2001-pcm.pdf' 
           target='_blank' class='diamond-btn'>
            📄 Ver Documento Histórico
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='elite-glass'>
        <h2>📊 Valores de ECA Vigentes - D.S. 003-2017-MINAM</h2>
        <p style='margin-bottom: 25px; font-size: 1.05em;'>Concentraciones máximas permitidas en aire ambiente</p>
    </div>
    """, unsafe_allow_html=True)
    
    eca_valores = pd.DataFrame([
        ['PM2.5', '24 horas', 50, 'μg/m³', 'No exceder más de 7 veces/año'],
        ['PM2.5', 'Anual', 25, 'μg/m³', 'Media aritmética anual'],
        ['PM10', '24 horas', 100, 'μg/m³', 'No exceder más de 7 veces/año'],
        ['PM10', 'Anual', 50, 'μg/m³', 'Media aritmética anual'],
        ['NO2', '1 hora', 200, 'μg/m³', 'No exceder más de 24 veces/año'],
        ['NO2', 'Anual', 100, 'μg/m³', 'Media aritmética anual'],
        ['SO2', '24 horas', 250, 'μg/m³', 'No exceder más de 7 veces/año'],
        ['O3', '8 horas', 100, 'μg/m³', 'Máximas diarias de promedios móviles'],
        ['CO', '8 horas', 10000, 'μg/m³', 'Promedio móvil'],
        ['CO', '1 hora', 30000, 'μg/m³', 'No exceder más de 1 vez/año'],
    ], columns=['Contaminante', 'Período', 'Valor', 'Unidad', 'Forma del Estándar'])
    
    st.dataframe(eca_valores, use_container_width=True, hide_index=True, height=450)

# ===================== PÁGINA LMP =====================
elif st.session_state.pagina == "LMP":
    st.markdown("<h1 style='text-align: center; font-size: 3.5em; background: linear-gradient(135deg, #06b6d4 0%, #22d3ee 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-family: Space Grotesk;'>🏭 Límites Máximos Permisibles (LMP)</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='elite-glass'>
        <h2>📜 ¿Qué son los LMP?</h2>
        <p style='font-size: 1.2em;'>
            Los LMP son <strong>límites de emisión en la fuente (chimeneas)</strong> que regulan 
            la concentración máxima de contaminantes que puede emitir una actividad productiva. 
            A diferencia de los ECA, se miden directamente en el punto de emisión.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='platinum-card'>
        <span class='premium-badge vigente'>VIGENTE</span>
        <h3>D.S. N° 003-2010-MINAM</h3>
        <p style='font-size: 1.1em;'>
            <strong>LMP para Centrales Termoeléctricas</strong><br><br>
            Establece límites de emisión de NOx, SO2 y Material Particulado para plantas de generación 
            termoeléctrica según tipo de combustible (gas natural, diesel, residual).
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_003-2010-minam.pdf' 
           target='_blank' class='diamond-btn'>
            📄 Descargar D.S. 003-2010-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='platinum-card'>
        <span class='premium-badge vigente'>VIGENTE</span>
        <h3>D.S. N° 011-2009-MINAM</h3>
        <p style='font-size: 1.1em;'>
            <strong>LMP de Emisiones Vehiculares</strong><br><br>
            Regula las emisiones de gases contaminantes de vehículos automotores nuevos y usados. 
            Incluye límites para CO, HC, NOx y material particulado.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_011-2009-minam.pdf' 
           target='_blank' class='diamond-btn'>
            📄 Descargar D.S. 011-2009-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='platinum-card'>
        <span class='premium-badge vigente'>VIGENTE</span>
        <h3>D.S. N° 010-2010-MINAM</h3>
        <p style='font-size: 1.1em;'>
            <strong>LMP para Industria Minera</strong><br><br>
            Límites de emisiones atmosféricas para minería metalúrgica y no metálica en operaciones 
            de procesamiento y fundición.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_010-2010-minam.pdf' 
           target='_blank' class='diamond-btn'>
            📄 Descargar D.S. 010-2010-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='elite-glass'>
        <h2>📊 LMP Centrales Termoeléctricas por Combustible</h2>
        <p style='font-size: 1.05em;'>D.S. 003-2010-MINAM | Condiciones: 25°C, 1 atm, base seca, 15% O2</p>
    </div>
    """, unsafe_allow_html=True)
    
    lmp_termo = pd.DataFrame([
        ['NOx', 320, 850, 2000],
        ['SO2', 0, 1700, 3500],
        ['Material Particulado', 50, 150, 350]
    ], columns=['Contaminante', 'Gas Natural', 'Diesel', 'Residual'])
    
    fig = go.Figure()
    fig.add_trace(go.Bar(name='Gas Natural', x=lmp_termo['Contaminante'], y=lmp_termo['Gas Natural'],
                         marker_color='#06b6d4', text=lmp_termo['Gas Natural'],
                         marker=dict(line=dict(color='rgba(6, 182, 212, 0.4)', width=2))))
    fig.add_trace(go.Bar(name='Diesel', x=lmp_termo['Contaminante'], y=lmp_termo['Diesel'],
                         marker_color='#f59e0b', text=lmp_termo['Diesel'],
                         marker=dict(line=dict(color='rgba(245, 158, 11, 0.4)', width=2))))
    fig.add_trace(go.Bar(name='Residual', x=lmp_termo['Contaminante'], y=lmp_termo['Residual'],
                         marker_color='#ef4444', text=lmp_termo['Residual'],
                         marker=dict(line=dict(color='rgba(239, 68, 68, 0.4)', width=2))))
    
    fig.update_traces(texttemplate='%{text}', textposition='outside',
                      textfont=dict(size=14, color='#e0f2fe', family='Space Grotesk'))
    fig.update_layout(
        barmode='group',
        height=500,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0f2fe', family='Space Grotesk', size=14),
        xaxis=dict(showgrid=False, tickfont=dict(color='#22d3ee')),
        yaxis=dict(showgrid=True, gridcolor='rgba(6, 182, 212, 0.15)', 
                   title='mg/Nm³', titlefont=dict(color='#06b6d4')),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1,
                   bgcolor='rgba(17, 24, 39, 0.9)', bordercolor='rgba(6, 182, 212, 0.3)', borderwidth=1,
                   font=dict(color='#e0f2fe'))
    )
    st.plotly_chart(fig, use_container_width=True)

# ===================== PÁGINA PROTOCOLO =====================
elif st.session_state.pagina == "Protocolo":
    st.markdown("<h1 style='text-align: center; font-size: 3.5em; background: linear-gradient(135deg, #06b6d4 0%, #22d3ee 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-family: Space Grotesk;'>📖 Protocolos de Monitoreo</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='elite-glass'>
        <h2>📜 ¿Qué son los Protocolos?</h2>
        <p style='font-size: 1.2em;'>
            Los protocolos establecen <strong>procedimientos estandarizados</strong> para el monitoreo 
            de calidad del aire y medición de emisiones. Garantizan que las mediciones sean comparables 
            y confiables a nivel nacional.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='platinum-card'>
        <span class='premium-badge vigente'>VIGENTE</span>
        <h3>R.D. N° 1404-2005/DIGESA/SA</h3>
        <p style='font-size: 1.1em;'>
            <strong>Protocolo de Monitoreo de Calidad del Aire y Gestión de Datos</strong><br><br>
            Define procedimientos técnicos para el monitoreo de calidad del aire ambiente en todo el 
            territorio nacional. Incluye métodos de muestreo, calibración y análisis.
        </p>
        <a href='http://www.digesa.minsa.gob.pe/DEPA/protocolo_calidad_aire.pdf' 
           target='_blank' class='diamond-btn'>
            📄 Descargar Protocolo DIGESA
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='platinum-card'>
        <span class='premium-badge vigente'>VIGENTE</span>
        <h3>R.M. N° 026-2000-ITINCI/DM</h3>
        <p style='font-size: 1.1em;'>
            <strong>Protocolo de Monitoreo para el Sector Industrial</strong><br><br>
            Aprueba protocolos específicos de monitoreo de calidad de aire y emisiones para 
            actividades industriales y manufactureras.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2017/04/RM-026-2000-ITINCI.pdf' 
           target='_blank' class='diamond-btn'>
            📄 Ver Protocolo PRODUCE
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='platinum-card'>
        <span class='premium-badge vigente'>VIGENTE</span>
        <h3>R.D. N° 195-2010-MEM/AAM</h3>
        <p style='font-size: 1.1em;'>
            <strong>Protocolo para Calderos y Hornos</strong><br><br>
            Procedimientos para el monitoreo de emisiones atmosféricas en calderos y hornos 
            industriales. Incluye métodos isocinéticos y análisis de gases.
        </p>
        <a href='http://www.minem.gob.pe/minem/archivos/RD%20195-2010-AAM.pdf' 
           target='_blank' class='diamond-btn'>
            📄 Descargar Protocolo MEM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='elite-glass'>
        <h2>🔬 Métodos de Referencia EPA Adoptados en Perú</h2>
        <p style='font-size: 1.05em;'>Métodos estandarizados de la Agencia de Protección Ambiental de EE.UU.</p>
    </div>
    """, unsafe_allow_html=True)
    
    metodos = pd.DataFrame([
        ['PM10', 'EPA Method 40 CFR Part 50 Appendix J', 'Gravimetrico'],
        ['PM2.5', 'EPA Method 40 CFR Part 50 Appendix L', 'Gravimetrico'],
        ['SO2', 'EPA Method 40 CFR Part 50 Appendix A-1', 'Fluorescencia UV'],
        ['NO2', 'EPA Method 40 CFR Part 50 Appendix F', 'Quimioluminiscencia'],
        ['CO', 'EPA Method 40 CFR Part 50 Appendix C', 'Infrarrojo no dispersivo'],
        ['O3', 'EPA Method 40 CFR Part 50 Appendix D', 'Fotometria UV']
    ], columns=['Contaminante', 'Metodo EPA', 'Tecnica Analitica'])
    
    st.dataframe(metodos, use_container_width=True, hide_index=True, height=320) font-family: Space Grotesk;'>📖 Protocolos de Monitoreo</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='elite-glass'>
        <h2>📜 ¿Qué son los Protocolos?</h2>
        <p style='font-size: 1.2em;'>
            Los protocolos establecen <strong>procedimientos estandarizados</strong> para el monitoreo 
            de calidad del aire y medición de emisiones. Garantizan que las mediciones sean comparables 
            y confiables a nivel nacional.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='platinum-card'>
        <span class='premium-badge vigente'>VIGENTE</span>
        <h3>R.D. N° 1404-2005/DIGESA/SA</h3>
        <p style='font-size: 1.1em;'>
            <strong>Protocolo de Monitoreo de Calidad del Aire y Gestión de Datos</strong><br><br>
            Define procedimientos técnicos para el monitoreo de calidad del aire ambiente en todo el 
            territorio nacional. Incluye métodos de muestreo, calibración y análisis.
        </p>
        <a href='http://www.digesa.minsa.gob.pe/DEPA/protocolo_calidad_aire.pdf' 
           target='_blank' class='diamond-btn'>
            📄 Descargar Protocolo DIGESA
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='platinum-card'>
        <span class='premium-badge vigente'>VIGENTE</span>
        <h3>R.M. N° 026-2000-ITINCI/DM</h3>
        <p style='font-size: 1.1em;'>
            <strong>Protocolo de Monitoreo para el Sector Industrial</strong><br><br>
            Aprueba protocolos específicos de monitoreo de calidad de aire y emisiones para 
            actividades industriales y manufactureras.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2017/04/RM-026-2000-ITINCI.pdf' 
           target='_blank' class='diamond-btn'>
            📄 Ver Protocolo PRODUCE
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='platinum-card'>
        <span class='premium-badge vigente'>VIGENTE</span>
        <h3>R.D. N° 195-2010-MEM/AAM</h3>
        <p style='font-size: 1.1em;'>
            <strong>Protocolo para Calderos y Hornos</strong><br><br>
            Procedimientos para el monitoreo de emisiones atmosféricas en calderos y hornos 
            industriales. Incluye métodos isocinéticos y análisis de gases.
        </p>
        <a href='http://www.minem.gob.pe/minem/archivos/RD%20195-2010-AAM.pdf' 
           target='_blank' class='diamond-btn'>
            📄 Descargar Protocolo MEM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='elite-glass'>
        <h2>🔬 Métodos de Referencia EPA Adoptados en Perú</h2>
        <p style='font-size: 1.05em;'>Métodos estandarizados de la Agencia de Protección Ambiental de EE.UU.</p>
    </div>
    """, unsafe_allow_html=True)
    
    metodos = pd.DataFrame([
        ['PM10', 'EPA Method 40 CFR Part 50, Appendix J', 'Gravimétrico'],
        ['PM2.5', 'EPA Method 40 CFR Part 50, Appendix L', 'Gravimétrico'],
        ['SO2', 'EPA Method 40 CFR Part 50, Appendix A-1', 'Fluorescencia UV'],
        ['NO2', 'EPA Method 40 CFR Part 50, Appendix F', 'Quimioluminiscencia'],
        ['CO', 'EPA Method 40 CFR Part 50, Appendix C', 'Infrarrojo no dispersivo'],
        ['O3', 'EPA Method 40 CFR Part 50, Appendix D', 'Fotometría UV']
    ], columns=['Contaminante', 'Método EPA', 'Técnica Analítica'])
    
    st.dataframe(metodos, use_container_width=True, hide_index=True, height=320)

# ===================== PÁGINA LINEAMIENTO =====================
elif st.session_state.pagina == "Lineamiento":
    st.markdown("<h1 style='text-align: center; font-size: 3.5em; background: linear-gradient(135deg, #06b6d4 0%, #22d3ee 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-family: Space Grotesk;'>📐 Lineamientos Técnicos</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='elite-glass'>
        <h2>📜 ¿Qué son los Lineamientos?</h2>
        <p style='font-size: 1.2em;'>
            Los lineamientos son <strong>guías técnicas y operativas</strong> que complementan la 
            normativa legal y orientan su implementación práctica. Proporcionan metodologías y 
            procedimientos específicos.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='platinum-card'>
        <span class='premium-badge vigente'>VIGENTE</span>
        <h3>R.M. N° 181-2016-MINAM</h3>
        <p style='font-size: 1.1em;'>
            <strong>Lineamientos para Inventario de Emisiones Atmosféricas</strong><br><br>
            Metodología estandarizada para elaborar inventarios de emisiones de contaminantes del aire. 
            Incluye factores de emisión y procedimientos de cálculo.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2016/07/RM-N%C2%B0-181-2016-MINAM.pdf' 
           target='_blank' class='diamond-btn'>
            📄 Descargar R.M. 181-2016-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='platinum-card'>
        <span class='premium-badge vigente'>VIGENTE</span>
        <h3>D.S. N° 009-2003-SA</h3>
        <p style='font-size: 1.1em;'>
            <strong>Reglamento de Niveles de Estados de Alerta</strong><br><br>
            Define niveles de alerta (Cuidado, Peligro, Emergencia) y las acciones correspondientes 
            ante episodios críticos de contaminación del aire.
        </p>
        <a href='http://www.digesa.minsa.gob.pe/NormasLegales/Normas/DS_009-2003-SA.pdf' 
           target='_blank' class='diamond-btn'>
            📄 Descargar D.S. 009-2003-SA
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='platinum-card'>
        <span class='premium-badge vigente'>VIGENTE</span>
        <h3>Decreto Legislativo N° 1278</h3>
        <p style='font-size: 1.1em;'>
            <strong>Ley de Gestión Integral de Residuos Sólidos</strong><br><br>
            Lineamientos para control de emisiones atmosféricas de plantas de tratamiento e 
            incineración de residuos sólidos.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2017/04/Decreto-Legislativo-N%C2%B0-1278.pdf' 
           target='_blank' class='diamond-btn'>
            📄 Ver DL 1278
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='elite-glass'>
        <h2>⚠️ Niveles de Estados de Alerta Nacional (D.S. 009-2003-SA)</h2>
        <p style='font-size: 1.05em;'>Concentraciones que activan protocolos de emergencia</p>
    </div>
    """, unsafe_allow_html=True)
    
    niveles = pd.DataFrame([
        ['PM10', '🟡 Cuidado', 250, 'μg/m³', 'Información a población sensible'],
        ['PM10', '🟠 Peligro', 350, 'μg/m³', 'Alerta a toda la población'],
        ['PM10', '🔴 Emergencia', 420, 'μg/m³', 'Emergencia sanitaria'],
        ['SO2', '🟡 Cuidado', 500, 'μg/m³', 'Información a población sensible'],
        ['SO2', '🟠 Peligro', 1000, 'μg/m³', 'Alerta a toda la población'],
        ['SO2', '🔴 Emergencia', 1600, 'μg/m³', 'Emergencia sanitaria'],
        ['NO2', '🟡 Cuidado', 600, 'μg/m³', 'Información a población sensible'],
        ['NO2', '🟠 Peligro', 1200, 'μg/m³', 'Alerta a toda la población'],
        ['NO2', '🔴 Emergencia', 1600, 'μg/m³', 'Emergencia sanitaria']
    ], columns=['Contaminante', 'Nivel', 'Concentración', 'Unidad', 'Acción Requerida'])
    
    st.dataframe(niveles, use_container_width=True, hide_index=True, height=400)

# ===================== PÁGINA MEDIDAS =====================
elif st.session_state.pagina == "Medidas":
    st.markdown("<h1 style='text-align: center; font-size: 3.5em; background: linear-gradient(135deg, #06b6d4 0%, #22d3ee 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-family: Space Grotesk;'>🛡️ Medidas de Control de Emisiones</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='elite-glass'>
        <h2>📜 Marco Normativo de Control</h2>
        <p style='font-size: 1.2em;'>
            Las medidas de control son <strong>tecnologías y prácticas</strong> para reducir 
            emisiones de contaminantes atmosféricos en la fuente. Son obligatorias para cumplir 
            con los LMP establecidos.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='platinum-card'>
        <span class='premium-badge vigente'>VIGENTE</span>
        <h3>Ley N° 28611 - Ley General del Ambiente</h3>
        <p style='font-size: 1.1em;'>
            <strong>Prevención, Control y Remediación Ambiental</strong><br><br>
            Título II, Capítulo 3: Establece obligación de implementar medidas de prevención y 
            control de contaminación del aire. Base legal para exigir tecnologías de control.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2017/04/Ley-N%C2%B0-28611.pdf' 
           target='_blank' class='diamond-btn'>
            📄 Ver Ley 28611
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='platinum-card'>
        <span class='premium-badge vigente'>VIGENTE</span>
        <h3>D.S. N° 012-2005-EM</h3>
        <p style='font-size: 1.1em;'>
            <strong>Plan de Cierre de Minas - Control de Emisiones</strong><br><br>
            Incluye obligaciones específicas de control de emisiones atmosféricas durante operación 
            y cierre de operaciones mineras.
        </p>
        <a href='http://www.minem.gob.pe/minem/archivos/file/Mineria/LEGISLACION/2005/agosto/DS012-2005.pdf' 
           target='_blank' class='diamond-btn'>
            📄 Ver D.S. 012-2005-EM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='platinum-card'>
        <span class='premium-badge ntp'>NTP</span>
        <h3>Normas Técnicas Peruanas (NTP) - Control y Medición</h3>
        <p style='font-size: 1.1em;'>
            <strong>NTP 900.058:2019</strong> - Gestión Ambiental. Aire. Métodos de muestreo<br>
            <strong>NTP 900.030:2003</strong> - Gestión Ambiental. Aire. Terminología<br><br>
            Normas técnicas que establecen procedimientos estandarizados para medición y control.
        </p>
        <a href='https://www.inacal.gob.pe/repositorioaps/data/1/1/1/jer/ctnprocedimiento/files/Catalogo_NTP_Vigentes_2023.pdf' 
           target='_blank' class='diamond-btn'>
            📄 Ver Catálogo NTP INACAL
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='elite-glass'>
        <h2>🔧 Principales Tecnologías de Control de Emisiones</h2>
        <p style='margin-bottom: 25px; font-size: 1.05em;'>Sistemas utilizados para cumplir con LMP establecidos</p>
    </div>
    """, unsafe_allow_html=True)
    
    tecnologias = pd.DataFrame([
        ['Material Particulado', 'Filtros de mangas', '>99%', 'Textil poroso captura partículas', '💰💰'],
        ['Material Particulado', 'Precipitadores electrostáticos', '95-99%', 'Carga eléctrica y colección', '💰💰💰'],
        ['Material Particulado', 'Ciclones', '70-90%', 'Fuerza centrífuga', '💰'],
        ['SO2', 'Desulfuración húmeda (FGD)', '>95%', 'Absorción con caliza/cal', '💰💰💰💰'],
        ['SO2', 'Desulfuración seca', '80-95%', 'Inyección de sorbente', '💰💰💰'],
        ['NOx', 'Reducción Catalítica (SCR)', '>90%', 'Catalizador + urea/amoniaco', '💰💰💰💰'],
        ['NOx', 'Quemadores Low-NOx', '30-50%', 'Control de combustión', '💰💰'],
        ['NOx', 'Reducción No Catalítica (SNCR)', '40-60%', 'Inyección de urea', '💰💰'],
        ['COVs', 'Oxidación térmica', '>95%', 'Combustión alta temperatura', '💰💰💰'],
        ['COVs', 'Adsorción carbón activado', '85-95%', 'Captura en superficie porosa', '💰💰']
    ], columns=['Contaminante', 'Tecnología', 'Eficiencia', 'Principio de Operación', 'Costo'])
    
    st.dataframe(tecnologias, use_container_width=True, hide_index=True, height=450)

# ===================== PÁGINA NORMATIVAS INTERNACIONALES =====================
elif st.session_state.pagina == "Normativas":
    st.markdown("<h1 style='text-align: center; font-size: 3.5em; background: linear-gradient(135deg, #06b6d4 0%, #22d3ee 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-family: Space Grotesk;'>🌍 Normativas Internacionales</h1>", unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["🌍 OMS", "🇺🇸 EPA USA", "🇨🇦 Canadá", "📊 Comparación"])
    
    with tab1:
        st.markdown("""
        <div class='elite-glass'>
            <h2>🌍 Organización Mundial de la Salud (OMS)</h2>
            <p style='font-size: 1.15em;'>
                La OMS establece las <strong>directrices globales más estrictas</strong> para proteger 
                la salud pública de la contaminación del aire basándose en la mejor evidencia científica disponible.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='platinum-card'>
            <span class='premium-badge vigente'>2021</span>
            <h3>WHO Global Air Quality Guidelines</h3>
            <p style='font-size: 1.1em;'>
                <strong>Directrices Mundiales de Calidad del Aire de la OMS 2021</strong><br><br>
                Actualización mayor de las guías de 2005, con niveles 50% más estrictos basados en 
                nueva evidencia científica sobre efectos en salud a bajas concentraciones.
            </p>
            <a href='https://www.who.int/publications/i/item/9789240034228' 
               target='_blank' class='diamond-btn'>
                📄 Ver Directrices OMS 2021 (Inglés)
            </a>
            <a href='https://www.who.int/es/news-room/feature-stories/detail/what-are-the-who-air-quality-guidelines' 
               target='_blank' class='diamond-btn'>
                📖 Resumen en Español
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        oms_tabla = pd.DataFrame([
            ['PM2.5', 5, 15, 'μg/m³'],
            ['PM10', 15, 45, 'μg/m³'],
            ['NO2', 10, 25, 'μg/m³'],
            ['SO2', None, 40, 'μg/m³'],
            ['O3', None, 100, 'μg/m³ (8h)'],
            ['CO', None, 4000, 'μg/m³ (24h)']
        ], columns=['Contaminante', 'Anual', '24 horas', 'Unidad'])
        
        st.markdown("<h3 style='text-align: center; background: linear-gradient(135deg, #06b6d4 0%, #22d3ee 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 1.8em; font-family: Space Grotesk;'>📊 Valores Guía OMS 2021</h3>", unsafe_allow_html=True)
        st.dataframe(oms_tabla, use_container_width=True, hide_index=True, height=280)
    
    with tab2:
        st.markdown("""
        <div class='elite-glass'>
            <h2>🇺🇸 Environmental Protection Agency (EPA)</h2>
            <p style='font-size: 1.15em;'>
                La EPA de EE.UU. establece los <strong>National Ambient Air Quality Standards (NAAQS)</strong>, 
                estándares vinculantes que se actualizan basándose en revisiones científicas periódicas.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='platinum-card'>
            <span class='premium-badge vigente'>2024</span>
            <h3>NAAQS - National Ambient Air Quality Standards</h3>
            <p style='font-size: 1.1em;'>
                <strong>Estándares Nacionales de Calidad del Aire Ambiente</strong><br><br>
                Última actualización: PM2.5 anual reducido de 12 a 9.0 μg/m³ (febrero 2024). 
                Incluye estándares primarios (salud) y secundarios (bienestar).
            </p>
            <a href='https://www.epa.gov/criteria-air-pollutants/naaqs-table' 
               target='_blank' class='diamond-btn'>
                📄 Ver Tabla Completa NAAQS
            </a>
            <a href='https://www.epa.gov/pm-pollution/national-ambient-air-quality-standards-naaqs-pm' 
               target='_blank' class='diamond-btn'>
                📖 Estándares PM Detallados
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        epa_tabla = pd.DataFrame([
            ['PM2.5', 9.0, 35, 'μg/m³', '2024'],
            ['PM10', None, 150, 'μg/m³', '2012'],
            ['NO2', 53, 100, 'ppb', '2010'],
            ['SO2', None, 75, 'ppb (1h)', '2010'],
            ['O3', None, 70, 'ppb (8h)', '2015'],
            ['CO', None, '9 ppm (8h)', None, '1971']
        ], columns=['Contaminante', 'Anual', 'Corto Plazo', 'Unidad', 'Última Actualización'])
        
    with tab2:
        st.markdown("""
        <div class='elite-glass'>
            <h2>🇺🇸 Environmental Protection Agency (EPA)</h2>
            <p style='font-size: 1.15em;'>
                La EPA de EE.UU. establece los <strong>National Ambient Air Quality Standards (NAAQS)</strong>, 
                estándares vinculantes que se actualizan basándose en revisiones científicas periódicas.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='platinum-card'>
            <span class='premium-badge vigente'>2024</span>
            <h3>NAAQS - National Ambient Air Quality Standards</h3>
            <p style='font-size: 1.1em;'>
                <strong>Estándares Nacionales de Calidad del Aire Ambiente</strong><br><br>
                Última actualización: PM2.5 anual reducido de 12 a 9.0 μg/m³ (febrero 2024). 
                Incluye estándares primarios (salud) y secundarios (bienestar).
            </p>
            <a href='https://www.epa.gov/criteria-air-pollutants/naaqs-table' 
               target='_blank' class='diamond-btn'>
                📄 Ver Tabla Completa NAAQS
            </a>
            <a href='https://www.epa.gov/pm-pollution/national-ambient-air-quality-standards-naaqs-pm' 
               target='_blank' class='diamond-btn'>
                📖 Estándares PM Detallados
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        epa_tabla = pd.DataFrame([
            ['PM2.5', 9.0, 35, 'μg/m³', '2024'],
            ['PM10', None, 150, 'μg/m³', '2012'],
            ['NO2', 53, 100, 'ppb', '2010'],
            ['SO2', None, 75, 'ppb (1h)', '2010'],
            ['O3', None, 70, 'ppb (8h)', '2015'],
            ['CO', None, '9 ppm (8h)', None, '1971']
        ], columns=['Contaminante', 'Anual', 'Corto Plazo', 'Unidad', 'Última Actualización'])
        
        st.markdown("<h3 style='text-align: center; background: linear-gradient(135deg, #06b6d4 0%, #22d3ee 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 1.8em; font-family: Space Grotesk;'>📊 Estándares EPA (NAAQS)</h3>", unsafe_allow_html=True)
        st.dataframe(epa_tabla, use_container_width=True, hide_index=True, height=280)
    
    with tab3:
        st.markdown("""
        <div class='elite-glass'>
            <h2>🇨🇦 Canadian Ambient Air Quality Standards (CAAQS)</h2>
            <p style='font-size: 1.15em;'>
                Canadá utiliza un sistema de <strong>mejora continua</strong> con estándares que se actualizan 
                cada 5 años y gestión por Air Zones para implementación regional.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='platinum-card'>
            <span class='premium-badge vigente'>2025</span>
            <h3>CAAQS 2020-2025</h3>
            <p style='font-size: 1.1em;'>
                <strong>Estándares Canadienses de Calidad del Aire Ambiente</strong><br><br>
                Sistema de gestión por Air Zones (Verde, Amarillo, Naranja, Rojo) con estándares 
                progresivamente más estrictos hacia 2025 y 2030.
            </p>
            <a href='https://www.ccme.ca/en/air-quality-report' 
               target='_blank' class='diamond-btn'>
                📄 Ver Reporte CAAQS
            </a>
            <a href='https://www.canada.ca/en/environment-climate-change/services/air-quality-health-index.html' 
               target='_blank' class='diamond-btn'>
                📖 Índice de Calidad del Aire
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        canada_tabla = pd.DataFrame([
            ['PM2.5', 8.8, 8.0, 'μg/m³', 'Anual'],
            ['PM2.5', 27, 25, 'μg/m³', '24h'],
            ['O3', 62, 60, 'ppb', '8h'],
            ['NO2', 60, 50, 'ppb', '1h'],
            ['SO2', 70, 65, 'ppb', '1h']
        ], columns=['Contaminante', 'Estándar 2020', 'Meta 2025', 'Unidad', 'Período'])
        
        st.markdown("<h3 style='text-align: center; background: linear-gradient(135deg, #06b6d4 0%, #22d3ee 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 1.8em; font-family: Space Grotesk;'>📊 Estándares CAAQS - Evolución</h3>", unsafe_allow_html=True)
        st.dataframe(canada_tabla, use_container_width=True, hide_index=True, height=240)
    
    with tab4:
        st.markdown("<h2 style='text-align: center; background: linear-gradient(135deg, #06b6d4 0%, #22d3ee 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 2.5em; font-family: Space Grotesk;'>📊 Comparación Internacional - PM2.5</h2>", unsafe_allow_html=True)
        
        comparacion = pd.DataFrame([
            {'Entidad': 'OMS 2021', 'Anual': 5, '24h': 15, 'Color': '#06b6d4'},
            {'Entidad': 'EPA USA 2024', 'Anual': 9, '24h': 35, 'Color': '#3b82f6'},
            {'Entidad': 'Canadá 2025', 'Anual': 8, '24h': 25, 'Color': '#8b5cf6'},
            {'Entidad': 'OEFA Perú', 'Anual': 25, '24h': 50, 'Color': '#ef4444'}
        ])
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=comparacion['Entidad'],
            y=comparacion['Anual'],
            name='Anual',
            marker_color=['#06b6d4', '#3b82f6', '#8b5cf6', '#ef4444'],
            text=comparacion['Anual'],
            marker=dict(line=dict(color='rgba(6, 182, 212, 0.4)', width=2))
        ))
        fig.add_trace(go.Bar(
            x=comparacion['Entidad'],
            y=comparacion['24h'],
            name='24 horas',
            marker_color=['#22d3ee', '#60a5fa', '#a78bfa', '#f87171'],
            text=comparacion['24h'],
            marker=dict(line=dict(color='rgba(6, 182, 212, 0.4)', width=2))
        ))
        
        fig.update_traces(texttemplate='%{text} μg/m³', textposition='outside',
                          textfont=dict(size=14, color='#e0f2fe', family='Space Grotesk'))
        fig.update_layout(
            barmode='group',
            height=550,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#e0f2fe', size=15, family='Space Grotesk'),
            xaxis=dict(showgrid=False, tickfont=dict(size=14, color='#22d3ee')),
            yaxis=dict(showgrid=True, gridcolor='rgba(6, 182, 212, 0.15)', 
                       title='Concentración (μg/m³)', titlefont=dict(color='#06b6d4')),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1,
                       bgcolor='rgba(17, 24, 39, 0.9)', bordercolor='rgba(6, 182, 212, 0.3)', 
                       borderwidth=1, font=dict(color='#e0f2fe'))
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class='elite-glass'>
            <h3>💡 Análisis Comparativo</h3>
            <p style='font-size: 1.1em; line-height: 2;'>
                <strong>OMS 2021:</strong> Establece los estándares más estrictos (5 μg/m³ anual) basados en 
                la mejor evidencia científica sobre efectos en salud.<br><br>
                
                <strong>EPA y Canadá:</strong> Valores intermedios (8-9 μg/m³ anual) con actualizaciones 
                regulares basadas en revisiones científicas periódicas.<br><br>
                
                <strong>OEFA Perú:</strong> Estándares más permisivos (25 μg/m³ anual) que consideran 
                factibilidad técnica y económica, pero significativamente por encima de recomendaciones OMS.<br><br>
                
                <strong>Recomendación:</strong> Perú debería considerar una actualización gradual de sus ECA 
                para alinearse mejor con estándares internacionales y proteger mejor la salud pública.
            </p>
        </div>
        """, unsafe_allow_html=True)

# FOOTER ULTRA PREMIUM
st.markdown("---")
st.markdown("""
<div style='text-align: center; 
            background: linear-gradient(135deg, rgba(6, 182, 212, 0.08) 0%, rgba(14, 165, 233, 0.12) 100%); 
            backdrop-filter: blur(30px) saturate(200%); 
            padding: 70px 50px; 
            border-radius: 24px; 
            margin-top: 70px; 
            border: 1px solid rgba(6, 182, 212, 0.25); 
            box-shadow: 0 30px 90px rgba(0, 0, 0, 0.9), inset 0 1px 0 rgba(6, 182, 212, 0.15);
            position: relative;
            overflow: hidden;'>
    <div style='position: absolute; top: 0; left: 0; width: 100%; height: 2px; 
                background: linear-gradient(90deg, transparent, #06b6d4, transparent);'></div>
    <h2 style='background: linear-gradient(135deg, #06b6d4 0%, #22d3ee 100%); 
               -webkit-background-clip: text; 
               -webkit-text-fill-color: transparent; 
               margin: 0; 
               font-weight: 900; 
               font-size: 2.8em;
               letter-spacing: -0.02em;
               font-family: Space Grotesk;'>
        Universidad Nacional de Moquegua
    </h2>
    <p style='color: #a5f3fc; font-size: 1.4em; margin: 25px 0; font-weight: 700; 
              text-transform: uppercase; letter-spacing: 0.1em; font-family: Space Grotesk;'>
        Facultad de Ingeniería y Arquitectura
    </p>
    <p style='color: #67e8f9; margin: 18px 0; font-size: 1.1em; font-weight: 500;'>
        <strong style='color: #06b6d4;'>Curso:</strong> Contaminación y Control Atmosférico
    </p>
    <p style='color: #67e8f9; margin: 18px 0; font-size: 1.1em; font-weight: 500;'>
        <strong style='color: #06b6d4;'>Docente:</strong> Prof. Dr. José Antonio Valeriano Zapana
    </p>
    <div style='margin-top: 40px; padding-top: 35px; border-top: 1px solid rgba(6, 182, 212, 0.25);'>
        <p style='color: #22d3ee; font-size: 1.05em; font-weight: 700; letter-spacing: 0.02em;'>
            2024-2025 | Herramienta Interactiva de Consulta de Marco Normativo del Aire
        </p>
        <p style='color: #06b6d4; font-size: 0.95em; margin-top: 18px; font-weight: 600;'>
            Desarrollado con Streamlit & Plotly | Datos oficiales de MINAM, OMS, EPA y CCME
        </p>
        <p style='color: #22d3ee; font-size: 0.85em; margin-top: 12px; font-weight: 500; opacity: 0.9;'>
            Diseño Premium • Actualización Continua • Acceso Instantáneo
        </p>
    </div>
</div>
""", unsafe_allow_html=True)
