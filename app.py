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

# CSS ULTRA PREMIUM
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
        letter-spacing: -0.01em;
    }
    
    [data-testid="stSidebar"] {display: none;}
    
    /* Background con gradiente animado */
    .main {
        background: #0a0e27;
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
            radial-gradient(circle at 20% 50%, rgba(120, 119, 198, 0.15) 0%, transparent 50%),
            radial-gradient(circle at 80% 80%, rgba(99, 102, 241, 0.15) 0%, transparent 50%),
            radial-gradient(circle at 40% 20%, rgba(168, 85, 247, 0.1) 0%, transparent 50%);
        animation: gradient-shift 15s ease infinite;
        z-index: -1;
    }
    
    @keyframes gradient-shift {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.8; transform: scale(1.1); }
    }
    
    .stApp {
        background: transparent;
    }
    
    /* Animaciones suaves */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(40px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(-60px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes glow {
        0%, 100% {
            box-shadow: 0 0 20px rgba(99, 102, 241, 0.3),
                        0 0 40px rgba(99, 102, 241, 0.2),
                        0 0 60px rgba(99, 102, 241, 0.1);
        }
        50% {
            box-shadow: 0 0 30px rgba(99, 102, 241, 0.4),
                        0 0 60px rgba(99, 102, 241, 0.3),
                        0 0 80px rgba(99, 102, 241, 0.2);
        }
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
    }
    
    /* HEADER ULTRA PREMIUM */
    .ultra-header {
        text-align: center;
        padding: 80px 40px;
        background: linear-gradient(135deg, 
            rgba(99, 102, 241, 0.08) 0%, 
            rgba(168, 85, 247, 0.08) 50%,
            rgba(236, 72, 153, 0.08) 100%);
        backdrop-filter: blur(30px) saturate(180%);
        border-radius: 32px;
        margin-bottom: 50px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: 
            0 30px 90px rgba(0, 0, 0, 0.6),
            inset 0 1px 0 rgba(255, 255, 255, 0.1);
        animation: fadeInUp 1s ease-out, glow 4s ease-in-out infinite;
        position: relative;
        overflow: hidden;
    }
    
    .ultra-header::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: conic-gradient(
            from 0deg at 50% 50%,
            rgba(99, 102, 241, 0.1) 0deg,
            transparent 60deg,
            transparent 300deg,
            rgba(168, 85, 247, 0.1) 360deg
        );
        animation: rotate 20s linear infinite;
    }
    
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    .ultra-header h1 {
        font-size: 4.5em !important;
        font-weight: 900 !important;
        background: linear-gradient(135deg, 
            #818cf8 0%, 
            #c084fc 40%, 
            #f0abfc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0 !important;
        position: relative;
        z-index: 1;
        text-shadow: 0 0 80px rgba(129, 140, 248, 0.5);
        letter-spacing: -0.03em;
    }
    
    .ultra-header .subtitle {
        color: #e0e7ff;
        font-size: 1.6em;
        font-weight: 600;
        margin-top: 20px;
        position: relative;
        z-index: 1;
        letter-spacing: -0.01em;
    }
    
    .ultra-header .description {
        color: #c7d2fe;
        font-size: 1.2em;
        margin-top: 15px;
        font-weight: 400;
        opacity: 0.95;
        position: relative;
        z-index: 1;
    }
    
    .ultra-header .meta {
        color: #a5b4fc;
        font-size: 1em;
        margin-top: 20px;
        opacity: 0.8;
        position: relative;
        z-index: 1;
    }
    
    /* Glass Card Premium */
    .premium-glass {
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 0.05) 0%, 
            rgba(255, 255, 255, 0.02) 100%);
        backdrop-filter: blur(20px) saturate(180%);
        padding: 45px;
        border-radius: 28px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        margin: 25px 0;
        box-shadow: 
            0 20px 60px rgba(0, 0, 0, 0.4),
            inset 0 1px 0 rgba(255, 255, 255, 0.1);
        animation: fadeInUp 0.8s ease-out;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .premium-glass::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, 
            transparent, 
            rgba(255, 255, 255, 0.08), 
            transparent);
        transition: left 0.6s;
    }
    
    .premium-glass:hover {
        transform: translateY(-8px);
        box-shadow: 
            0 30px 90px rgba(99, 102, 241, 0.25),
            inset 0 1px 0 rgba(255, 255, 255, 0.15);
        border-color: rgba(129, 140, 248, 0.3);
    }
    
    .premium-glass:hover::before {
        left: 100%;
    }
    
    .premium-glass h2 {
        font-size: 2em;
        font-weight: 800;
        background: linear-gradient(135deg, #818cf8 0%, #c084fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0 0 20px 0;
        letter-spacing: -0.02em;
    }
    
    .premium-glass h3 {
        font-size: 1.5em;
        font-weight: 700;
        background: linear-gradient(135deg, #a5b4fc 0%, #ddd6fe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 15px 0;
        letter-spacing: -0.01em;
    }
    
    .premium-glass p, .premium-glass li {
        color: #e0e7ff;
        line-height: 1.9;
        font-size: 1.05em;
        font-weight: 400;
    }
    
    /* Luxury Card para Normativas */
    .luxury-card {
        background: linear-gradient(135deg, 
            rgba(99, 102, 241, 0.08) 0%, 
            rgba(168, 85, 247, 0.08) 100%);
        backdrop-filter: blur(20px) saturate(180%);
        padding: 40px;
        border-radius: 24px;
        margin: 25px 0;
        border-left: 4px solid;
        border-image: linear-gradient(180deg, #818cf8, #c084fc) 1;
        box-shadow: 
            0 20px 60px rgba(0, 0, 0, 0.4),
            inset 0 1px 0 rgba(255, 255, 255, 0.08);
        transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        animation: slideInRight 0.8s ease-out;
        position: relative;
        overflow: hidden;
    }
    
    .luxury-card::after {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(129, 140, 248, 0.1) 0%, transparent 70%);
        opacity: 0;
        transition: opacity 0.5s;
    }
    
    .luxury-card:hover {
        transform: translateX(15px) scale(1.02);
        box-shadow: 
            0 30px 90px rgba(129, 140, 248, 0.4),
            inset 0 1px 0 rgba(255, 255, 255, 0.15);
        border-left-width: 6px;
    }
    
    .luxury-card:hover::after {
        opacity: 1;
    }
    
    .luxury-card h3 {
        color: #a5b4fc !important;
        font-size: 1.8em;
        font-weight: 800;
        margin: 0 0 20px 0;
        letter-spacing: -0.02em;
    }
    
    .luxury-card p {
        color: #e0e7ff;
        font-size: 1.1em;
        line-height: 1.8;
        margin: 15px 0;
    }
    
    /* Badges Premium */
    .elite-badge {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        color: white;
        padding: 10px 24px;
        border-radius: 30px;
        font-size: 0.9em;
        font-weight: 700;
        display: inline-block;
        margin-right: 12px;
        box-shadow: 
            0 8px 24px rgba(99, 102, 241, 0.5),
            0 0 0 1px rgba(255, 255, 255, 0.1) inset;
        letter-spacing: 0.02em;
        text-transform: uppercase;
        animation: float 3s ease-in-out infinite;
    }
    
    .elite-badge.vigente {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        box-shadow: 0 8px 24px rgba(16, 185, 129, 0.5);
    }
    
    .elite-badge.modificatoria {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        box-shadow: 0 8px 24px rgba(245, 158, 11, 0.5);
    }
    
    .elite-badge.anterior {
        background: linear-gradient(135deg, #64748b 0%, #475569 100%);
        box-shadow: 0 8px 24px rgba(100, 116, 139, 0.5);
    }
    
    .elite-badge.ntp {
        background: linear-gradient(135deg, #f97316 0%, #ea580c 100%);
        box-shadow: 0 8px 24px rgba(249, 115, 22, 0.5);
    }
    
    /* Botones Ultra Premium */
    .quantum-btn {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        color: white;
        padding: 18px 36px;
        border-radius: 16px;
        text-decoration: none;
        display: inline-block;
        margin: 10px 8px;
        font-weight: 700;
        font-size: 1.05em;
        box-shadow: 
            0 12px 36px rgba(99, 102, 241, 0.5),
            0 0 0 1px rgba(255, 255, 255, 0.1) inset;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        letter-spacing: 0.01em;
    }
    
    .quantum-btn::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, 
            transparent, 
            rgba(255, 255, 255, 0.3), 
            transparent);
        transition: left 0.5s;
    }
    
    .quantum-btn:hover {
        transform: translateY(-4px) scale(1.05);
        box-shadow: 
            0 20px 50px rgba(99, 102, 241, 0.6),
            0 0 0 2px rgba(255, 255, 255, 0.2) inset;
    }
    
    .quantum-btn:hover::before {
        left: 100%;
    }
    
    .quantum-btn:active {
        transform: translateY(-2px) scale(1.02);
    }
    
    /* Botones de navegación Premium */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, 
            rgba(99, 102, 241, 0.15) 0%, 
            rgba(168, 85, 247, 0.15) 100%);
        color: #e0e7ff;
        border: 1.5px solid rgba(129, 140, 248, 0.3);
        border-radius: 16px;
        padding: 16px 24px;
        font-weight: 700;
        font-size: 1em;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
        letter-spacing: 0.01em;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, 
            rgba(99, 102, 241, 0.25) 0%, 
            rgba(168, 85, 247, 0.25) 100%);
        border-color: rgba(129, 140, 248, 0.6);
        transform: translateY(-3px);
        box-shadow: 0 12px 32px rgba(99, 102, 241, 0.4);
        color: white;
    }
    
    .stButton > button:active {
        transform: translateY(-1px);
    }
    
    /* Tabs Ultra Premium */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 0.05) 0%, 
            rgba(255, 255, 255, 0.02) 100%);
        padding: 12px;
        border-radius: 20px;
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.08);
    }
    
    .stTabs [data-baseweb="tab"] {
        background: linear-gradient(135deg, 
            rgba(99, 102, 241, 0.15) 0%, 
            rgba(168, 85, 247, 0.15) 100%);
        color: #c7d2fe;
        border-radius: 14px;
        padding: 14px 28px;
        font-weight: 700;
        border: 1.5px solid rgba(129, 140, 248, 0.2);
        transition: all 0.3s ease;
        letter-spacing: 0.01em;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        border-color: rgba(129, 140, 248, 0.5);
        transform: translateY(-2px);
        color: #e0e7ff;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        color: white;
        box-shadow: 0 8px 24px rgba(99, 102, 241, 0.5);
        border-color: transparent;
    }
    
    /* DataFrames Premium */
    .dataframe {
        background: rgba(15, 23, 42, 0.6) !important;
        border-radius: 20px !important;
        overflow: hidden !important;
        border: 1px solid rgba(129, 140, 248, 0.2) !important;
    }
    
    .dataframe thead tr th {
        background: linear-gradient(135deg, 
            rgba(99, 102, 241, 0.2) 0%, 
            rgba(168, 85, 247, 0.2) 100%) !important;
        color: #e0e7ff !important;
        font-weight: 700 !important;
        padding: 16px !important;
        border-bottom: 2px solid rgba(129, 140, 248, 0.3) !important;
    }
    
    .dataframe tbody tr {
        transition: all 0.2s ease;
    }
    
    .dataframe tbody tr:hover {
        background: rgba(99, 102, 241, 0.1) !important;
    }
    
    .dataframe tbody tr td {
        color: #c7d2fe !important;
        padding: 14px !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important;
    }
    
    /* Métricas Premium */
    [data-testid="stMetricValue"] {
        font-size: 2.5em;
        font-weight: 900;
        background: linear-gradient(135deg, #818cf8 0%, #c084fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.02em;
    }
    
    [data-testid="stMetricLabel"] {
        color: #a5b4fc !important;
        font-weight: 600;
        font-size: 1.1em;
    }
    
    /* Scrollbar Premium */
    ::-webkit-scrollbar {
        width: 12px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(15, 23, 42, 0.5);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        border-radius: 10px;
        border: 2px solid rgba(15, 23, 42, 0.5);
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #818cf8 0%, #a78bfa 100%);
    }
    
    /* Títulos Globales */
    h1, h2, h3, h4, h5, h6 {
        font-weight: 800 !important;
        letter-spacing: -0.02em !important;
    }
    
    /* Links Premium */
    a {
        color: #a5b4fc;
        text-decoration: none;
        transition: all 0.3s ease;
        font-weight: 600;
    }
    
    a:hover {
        color: #c7d2fe;
        text-shadow: 0 0 20px rgba(165, 180, 252, 0.5);
    }
</style>
""", unsafe_allow_html=True)

# Estado
if 'pagina' not in st.session_state:
    st.session_state.pagina = "Inicio"

# HEADER ULTRA PREMIUM
st.markdown("""
<div class='ultra-header'>
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

# MENÚ HORIZONTAL PREMIUM
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
        <div class='premium-glass'>
            <h2>📚 Sobre esta Herramienta</h2>
            <p style='font-size: 1.15em;'>
                Plataforma integral que reúne el <strong>marco normativo completo</strong> sobre 
                calidad del aire en Perú y el mundo.
            </p>
            <ul style='font-size: 1.1em; line-height: 2.4;'>
                <li>✅ <strong>ECA:</strong> Estándares de Calidad Ambiental</li>
                <li>✅ <strong>LMP:</strong> Límites Máximos Permisibles</li>
                <li>✅ <strong>Protocolos:</strong> Monitoreo y medición</li>
                <li>✅ <strong>Lineamientos:</strong> Guías técnicas</li>
                <li>✅ <strong>Medidas de Control:</strong> Tecnologías</li>
                <li>✅ <strong>Normativas Internacionales:</strong> OMS, EPA, Canadá</li>
            </ul>
            <p style='margin-top: 30px; font-size: 1.1em; opacity: 0.95;'>
                💡 <strong>Acceso directo</strong> a documentos oficiales con un solo click
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='premium-glass'>
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
    
    # Gráfico comparativo mejorado
    st.markdown("""
    <div class='premium-glass'>
        <h2>📊 Comparación Internacional - PM2.5 Anual</h2>
        <p style='opacity: 0.95; font-size: 1.05em;'>Estándares más estrictos protegen mejor la salud pública</p>
    </div>
    """, unsafe_allow_html=True)
    
    datos_comp = pd.DataFrame([
        {'Entidad': 'OMS 2021', 'Valor': 5, 'Color': '#10b981'},
        {'Entidad': 'EPA USA', 'Valor': 9, 'Color': '#6366f1'},
        {'Entidad': 'Canadá', 'Valor': 8.8, 'Color': '#8b5cf6'},
        {'Entidad': 'OEFA Perú', 'Valor': 25, 'Color': '#ef4444'}
    ])
    
    fig = px.bar(datos_comp, x='Entidad', y='Valor', 
                 color='Entidad',
                 color_discrete_sequence=['#10b981', '#6366f1', '#8b5cf6', '#ef4444'],
                 title='',
                 text='Valor')
    fig.update_traces(texttemplate='%{text} μg/m³', textposition='outside',
                      marker=dict(line=dict(color='rgba(255,255,255,0.2)', width=2)))
    fig.update_layout(
        height=550,
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0e7ff', size=15, family='Inter'),
        xaxis=dict(showgrid=False, tickfont=dict(size=14)),
        yaxis=dict(showgrid=True, gridcolor='rgba(129, 140, 248, 0.1)', title='Concentración (μg/m³)')
    )
    st.plotly_chart(fig, use_container_width=True)

# ===================== PÁGINA ECA =====================
elif st.session_state.pagina == "ECA":
    st.markdown("<h1 style='text-align: center; font-size: 3.5em; background: linear-gradient(135deg, #818cf8 0%, #c084fc 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>📋 Estándares de Calidad Ambiental (ECA)</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='premium-glass'>
        <h2>📜 ¿Qué son los ECA?</h2>
        <p style='font-size: 1.2em;'>
            Los ECA son <strong>estándares de calidad del aire ambiente</strong> que se miden en 
            estaciones de monitoreo para proteger la salud de la población. Establecen concentraciones 
            máximas de contaminantes permitidas en el aire que respiramos.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Normativas ECA con diseño ultra premium
    st.markdown("""
    <div class='luxury-card'>
        <span class='elite-badge vigente'>VIGENTE</span>
        <h3>D.S. N° 003-2017-MINAM</h3>
        <p style='font-size: 1.1em;'>
            <strong>Estándares de Calidad Ambiental (ECA) para Aire</strong><br><br>
            Establece los valores de concentración de contaminantes del aire que no deben superarse 
            para proteger la salud de las personas. Es la norma principal vigente en Perú.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2017/06/DS-003-2017-MINAM.pdf' 
           target='_blank' class='quantum-btn'>
            📄 Descargar Normativa Oficial
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='luxury-card'>
        <span class='elite-badge modificatoria'>MODIFICATORIA</span>
        <h3>D.S. N° 010-2019-MINAM</h3>
        <p style='font-size: 1.1em;'>
            <strong>Modificatoria de ECA para Aire</strong><br><br>
            Actualiza parámetros y períodos de evaluación para adaptarse a nueva evidencia científica 
            sobre efectos en la salud pública.
        </p>
        <a href='https://busquedas.elperuano.pe/download/url/decreto-supremo-que-modifica-el-decreto-supremo-n-003-2017-decreto-supremo-n-010-2019-minam-1792823-1' 
           target='_blank' class='quantum-btn'>
            📄 Descargar Modificatoria
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='luxury-card'>
        <span class='elite-badge anterior'>REFERENCIA HISTÓRICA</span>
        <h3>D.S. N° 074-2001-PCM</h3>
        <p style='font-size: 1.1em;'>
            <strong>Primera Norma de ECA en Perú</strong><br><br>
            Reglamento original de Estándares Nacionales de Calidad Ambiental del Aire. 
            Derogada por el D.S. 003-2017-MINAM pero importante para contexto histórico.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_074-2001-pcm.pdf' 
           target='_blank' class='quantum-btn'>
            📄 Ver Documento Histórico
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Tabla interactiva
    st.markdown("""
    <div class='premium-glass'>
        <h2>📊 Valores de ECA Vigentes - D.S. 003-2017-MINAM</h2>
        <p style='opacity: 0.95; margin-bottom: 25px; font-size: 1.05em;'>Concentraciones máximas permitidas en aire ambiente</p>
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
    st.markdown("<h1 style='text-align: center; font-size: 3.5em; background: linear-gradient(135deg, #818cf8 0%, #c084fc 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>🏭 Límites Máximos Permisibles (LMP)</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='premium-glass'>
        <h2>📜 ¿Qué son los LMP?</h2>
        <p style='font-size: 1.2em;'>
            Los LMP son <strong>límites de emisión en la fuente (chimeneas)</strong> que regulan 
            la concentración máxima de contaminantes que puede emitir una actividad productiva. 
            A diferencia de los ECA, se miden directamente en el punto de emisión.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # LMP con diseño mejorado
    st.markdown("""
    <div class='luxury-card'>
        <span class='elite-badge vigente'>VIGENTE</span>
        <h3>D.S. N° 003-2010-MINAM</h3>
        <p style='font-size: 1.1em;'>
            <strong>LMP para Centrales Termoeléctricas</strong><br><br>
            Establece límites de emisión de NOx, SO2 y Material Particulado para plantas de generación 
            termoeléctrica según tipo de combustible (gas natural, diesel, residual).
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_003-2010-minam.pdf' 
           target='_blank' class='quantum-btn'>
            📄 Descargar D.S. 003-2010-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='luxury-card'>
        <span class='elite-badge vigente'>VIGENTE</span>
        <h3>D.S. N° 011-2009-MINAM</h3>
        <p style='font-size: 1.1em;'>
            <strong>LMP de Emisiones Vehiculares</strong><br><br>
            Regula las emisiones de gases contaminantes de vehículos automotores nuevos y usados. 
            Incluye límites para CO, HC, NOx y material particulado.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_011-2009-minam.pdf' 
           target='_blank' class='quantum-btn'>
            📄 Descargar D.S. 011-2009-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='luxury-card'>
        <span class='elite-badge vigente'>VIGENTE</span>
        <h3>D.S. N° 010-2010-MINAM</h3>
        <p style='font-size: 1.1em;'>
            <strong>LMP para Industria Minera</strong><br><br>
            Límites de emisiones atmosféricas para minería metalúrgica y no metálica en operaciones 
            de procesamiento y fundición.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_010-2010-minam.pdf' 
           target='_blank' class='quantum-btn'>
            📄 Descargar D.S. 010-2010-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Tabla con gráfico
    st.markdown("""
    <div class='premium-glass'>
        <h2>📊 LMP Centrales Termoeléctricas por Combustible</h2>
        <p style='opacity: 0.95; font-size: 1.05em;'>D.S. 003-2010-MINAM | Condiciones: 25°C, 1 atm, base seca, 15% O2</p>
    </div>
    """, unsafe_allow_html=True)
    
    lmp_termo = pd.DataFrame([
        ['NOx', 320, 850, 2000],
        ['SO2', 0, 1700, 3500],
        ['Material Particulado', 50, 150, 350]
    ], columns=['Contaminante', 'Gas Natural', 'Diesel', 'Residual'])
    
    # Gráfico de barras agrupadas
    fig = go.Figure()
    fig.add_trace(go.Bar(name='Gas Natural', x=lmp_termo['Contaminante'], y=lmp_termo['Gas Natural'],
                         marker_color='#10b981', text=lmp_termo['Gas Natural'],
                         marker=dict(line=dict(color='rgba(255,255,255,0.2)', width=2))))
    fig.add_trace(go.Bar(name='Diesel', x=lmp_termo['Contaminante'], y=lmp_termo['Diesel'],
                         marker_color='#f59e0b', text=lmp_termo['Diesel'],
                         marker=dict(line=dict(color='rgba(255,255,255,0.2)', width=2))))
    fig.add_trace(go.Bar(name='Residual', x=lmp_termo['Contaminante'], y=lmp_termo['Residual'],
                         marker_color='#ef4444', text=lmp_termo['Residual'],
                         marker=dict(line=dict(color='rgba(255,255,255,0.2)', width=2))))
    
    fig.update_traces(texttemplate='%{text}', textposition='outside')
    fig.update_layout(
        barmode='group',
        height=500,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0e7ff', family='Inter', size=14),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='rgba(129, 140, 248, 0.1)', title='mg/Nm³'),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1,
                   bgcolor='rgba(15, 23, 42, 0.8)', bordercolor='rgba(129, 140, 248, 0.3)', borderwidth=1)
    )
    st.plotly_chart(fig, use_container_width=True)

# ===================== PÁGINA PROTOCOLO =====================
elif st.session_state.pagina == "Protocolo":
    st.markdown("<h1 style='text-align: center; font-size: 3.5em; background: linear-gradient(135deg, #818cf8 0%, #c084fc 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>📖 Protocolos de Monitoreo</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='premium-glass'>
        <h2>📜 ¿Qué son los Protocolos?</h2>
        <p style='font-size: 1.2em;'>
            Los protocolos establecen <strong>procedimientos estandarizados</strong> para el monitoreo 
            de calidad del aire y medición de emisiones. Garantizan que las mediciones sean comparables 
            y confiables a nivel nacional.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='luxury-card'>
        <span class='elite-badge vigente'>VIGENTE</span>
        <h3>R.D. N° 1404-2005/DIGESA/SA</h3>
        <p style='font-size: 1.1em;'>
            <strong>Protocolo de Monitoreo de Calidad del Aire y Gestión de Datos</strong><br><br>
            Define procedimientos técnicos para el monitoreo de calidad del aire ambiente en todo el 
            territorio nacional. Incluye métodos de muestreo, calibración y análisis.
        </p>
        <a href='http://www.digesa.minsa.gob.pe/DEPA/protocolo_calidad_aire.pdf' 
           target='_blank' class='quantum-btn'>
            📄 Descargar Protocolo DIGESA
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='luxury-card'>
        <span class='elite-badge vigente'>VIGENTE</span>
        <h3>R.M. N° 026-2000-ITINCI/DM</h3>
        <p style='font-size: 1.1em;'>
            <strong>Protocolo de Monitoreo para el Sector Industrial</strong><br><br>
            Aprueba protocolos específicos de monitoreo de calidad de aire y emisiones para 
            actividades industriales y manufactureras.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2017/04/RM-026-2000-ITINCI.pdf' 
           target='_blank' class='quantum-btn'>
            📄 Ver Protocolo PRODUCE
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='luxury-card'>
        <span class='elite-badge vigente'>VIGENTE</span>
        <h3>R.D. N° 195-2010-MEM/AAM</h3>
        <p style='font-size: 1.1em;'>
            <strong>Protocolo para Calderos y Hornos</strong><br><br>
            Procedimientos para el monitoreo de emisiones atmosféricas en calderos y hornos 
            industriales. Incluye métodos isocinéticos y análisis de gases.
        </p>
        <a href='http://www.minem.gob.pe/minem/archivos/RD%20195-2010-AAM.pdf' 
           target='_blank' class='quantum-btn'>
            📄 Descargar Protocolo MEM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Tabla de métodos EPA
    st.markdown("""
    <div class='premium-glass'>
        <h2>🔬 Métodos de Referencia EPA Adoptados en Perú</h2>
        <p style='opacity: 0.95; font-size: 1.05em;'>Métodos estandarizados de la Agencia de Protección Ambiental de EE.UU.</p>
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
    st.markdown("<h1 style='text-align: center; font-size: 3.5em; background: linear-gradient(135deg, #818cf8 0%, #c084fc 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>📐 Lineamientos Técnicos</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='premium-glass'>
        <h2>📜 ¿Qué son los Lineamientos?</h2>
        <p style='font-size: 1.2em;'>
            Los lineamientos son <strong>guías técnicas y operativas</strong> que complementan la 
            normativa legal y orientan su implementación práctica. Proporcionan metodologías y 
            procedimientos específicos.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='luxury-card'>
        <span class='elite-badge vigente'>VIGENTE</span>
        <h3>R.M. N° 181-2016-MINAM</h3>
        <p style='font-size: 1.1em;'>
            <strong>Lineamientos para Inventario de Emisiones Atmosféricas</strong><br><br>
            Metodología estandarizada para elaborar inventarios de emisiones de contaminantes del aire. 
            Incluye factores de emisión y procedimientos de cálculo.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2016/07/RM-N%C2%B0-181-2016-MINAM.pdf' 
           target='_blank' class='quantum-btn'>
            📄 Descargar R.M. 181-2016-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='luxury-card'>
        <span class='elite-badge vigente'>VIGENTE</span>
        <h3>D.S. N° 009-2003-SA</h3>
        <p style='font-size: 1.1em;'>
            <strong>Reglamento de Niveles de Estados de Alerta</strong><br><br>
            Define niveles de alerta (Cuidado, Peligro, Emergencia) y las acciones correspondientes 
            ante episodios críticos de contaminación del aire.
        </p>
        <a href='http://www.digesa.minsa.gob.pe/NormasLegales/Normas/DS_009-2003-SA.pdf' 
           target='_blank' class='quantum-btn'>
            📄 Descargar D.S. 009-2003-SA
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='luxury-card'>
        <span class='elite-badge vigente'>VIGENTE</span>
        <h3>Decreto Legislativo N° 1278</h3>
        <p style='font-size: 1.1em;'>
            <strong>Ley de Gestión Integral de Residuos Sólidos</strong><br><br>
            Lineamientos para control de emisiones atmosféricas de plantas de tratamiento e 
            incineración de residuos sólidos.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2017/04/Decreto-Legislativo-N%C2%B0-1278.pdf' 
           target='_blank' class='quantum-btn'>
            📄 Ver DL 1278
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Tabla de niveles de alerta
    st.markdown("""
    <div class='premium-glass'>
        <h2>⚠️ Niveles de Estados de Alerta Nacional (D.S. 009-2003-SA)</h2>
        <p style='opacity: 0.95; font-size: 1.05em;'>Concentraciones que activan protocolos de emergencia</p>
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
    st.markdown("<h1 style='text-align: center; font-size: 3.5em; background: linear-gradient(135deg, #818cf8 0%, #c084fc 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>🛡️ Medidas de Control de Emisiones</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='premium-glass'>
        <h2>📜 Marco Normativo de Control</h2>
        <p style='font-size: 1.2em;'>
            Las medidas de control son <strong>tecnologías y prácticas</strong> para reducir 
            emisiones de contaminantes atmosféricos en la fuente. Son obligatorias para cumplir 
            con los LMP establecidos.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='luxury-card'>
        <span class='elite-badge vigente'>VIGENTE</span>
        <h3>Ley N° 28611 - Ley General del Ambiente</h3>
        <p style='font-size: 1.1em;'>
            <strong>Prevención, Control y Remediación Ambiental</strong><br><br>
            Título II, Capítulo 3: Establece obligación de implementar medidas de prevención y 
            control de contaminación del aire. Base legal para exigir tecnologías de control.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2017/04/Ley-N%C2%B0-28611.pdf' 
           target='_blank' class='quantum-btn'>
            📄 Ver Ley 28611
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='luxury-card'>
        <span class='elite-badge vigente'>VIGENTE</span>
        <h3>D.S. N° 012-2005-EM</h3>
        <p style='font-size: 1.1em;'>
            <strong>Plan de Cierre de Minas - Control de Emisiones</strong><br><br>
            Incluye obligaciones específicas de control de emisiones atmosféricas durante operación 
            y cierre de operaciones mineras.
        </p>
        <a href='http://www.minem.gob.pe/minem/archivos/file/Mineria/LEGISLACION/2005/agosto/DS012-2005.pdf' 
           target='_blank' class='quantum-btn'>
            📄 Ver D.S. 012-2005-EM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='luxury-card'>
        <span class='elite-badge ntp'>NTP</span>
        <h3>Normas Técnicas Peruanas (NTP) - Control y Medición</h3>
        <p style='font-size: 1.1em;'>
            <strong>NTP 900.058:2019</strong> - Gestión Ambiental. Aire. Métodos de muestreo<br>
            <strong>NTP 900.030:2003</strong> - Gestión Ambiental. Aire. Terminología<br><br>
            Normas técnicas que establecen procedimientos estandarizados para medición y control.
        </p>
        <a href='https://www.inacal.gob.pe/repositorioaps/data/1/1/1/jer/ctnprocedimiento/files/Catalogo_NTP_Vigentes_2023.pdf' 
           target='_blank' class='quantum-btn'>
            📄 Ver Catálogo NTP INACAL
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Tecnologías de control con tabla mejorada
    st.markdown("""
    <div class='premium-glass'>
        <h2>🔧 Principales Tecnologías de Control de Emisiones</h2>
        <p style='opacity: 0.95; margin-bottom: 25px; font-size: 1.05em;'>Sistemas utilizados para cumplir con LMP establecidos</p>
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
    st.markdown("<h1 style='text-align: center; font-size: 3.5em; background: linear-gradient(135deg, #818cf8 0%, #c084fc 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>🌍 Normativas Internacionales</h1>", unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["🌍 OMS", "🇺🇸 EPA USA", "🇨🇦 Canadá", "📊 Comparación"])
    
    with tab1:
        st.markdown("""
        <div class='premium-glass'>
            <h2>🌍 Organización Mundial de la Salud (OMS)</h2>
            <p style='font-size: 1.15em;'>
                La OMS establece las <strong>directrices globales más estrictas</strong> para proteger 
                la salud pública de la contaminación del aire basándose en la mejor evidencia científica disponible.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='luxury-card'>
            <span class='elite-badge vigente'>2021</span>
            <h3>WHO Global Air Quality Guidelines</h3>
            <p style='font-size: 1.1em;'>
                <strong>Directrices Mundiales de Calidad del Aire de la OMS 2021</strong><br><br>
                Actualización mayor de las guías de 2005, con niveles 50% más estrictos basados en 
                nueva evidencia científica sobre efectos en salud a bajas concentraciones.
            </p>
            <a href='https://www.who.int/publications/i/item/9789240034228' 
               target='_blank' class='quantum-btn'>
                📄 Ver Directrices OMS 2021 (Inglés)
            </a>
            <a href='https://www.who.int/es/news-room/feature-stories/detail/what-are-the-who-air-quality-guidelines' 
               target='_blank' class='quantum-btn'>
                📖 Resumen en Español
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        # Tabla OMS
        oms_tabla = pd.DataFrame([
            ['PM2.5', 5, 15, 'μg/m³'],
            ['PM10', 15, 45, 'μg/m³'],
            ['NO2', 10, 25, 'μg/m³'],
            ['SO2', None, 40, 'μg/m³'],
            ['O3', None, 100, 'μg/m³ (8h)'],
            ['CO', None, 4000, 'μg/m³ (24h)']
        ], columns=['Contaminante', 'Anual', '24 horas', 'Unidad'])
        
        st.markdown("<h3 style='text-align: center; background: linear-gradient(135deg, #818cf8 0%, #c084fc 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 1.8em;'>📊 Valores Guía OMS 2021</h3>", unsafe_allow_html=True)
        st.dataframe(oms_tabla, use_container_width=True, hide_index=True, height=280)
    
    with tab2:
        st.markdown("""
        <div class='premium-glass'>
            <h2>🇺🇸 Environmental Protection Agency (EPA)</h2>
            <p style='font-size: 1.15em;'>
                La EPA de EE.UU. establece los <strong>National Ambient Air Quality Standards (NAAQS)</strong>, 
                estándares vinculantes que se actualizan basándose en revisiones científicas periódicas.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='luxury-card'>
            <span class='elite-badge vigente'>2024</span>
            <h3>NAAQS - National Ambient Air Quality Standards</h3>
            <p style='font-size: 1.1em;'>
                <strong>Estándares Nacionales de Calidad del Aire Ambiente</strong><br><br>
                Última actualización: PM2.5 anual reducido de 12 a 9.0 μg/m³ (febrero 2024). 
                Incluye estándares primarios (salud) y secundarios (bienestar).
            </p>
            <a href='https://www.epa.gov/criteria-air-pollutants/naaqs-table' 
               target='_blank' class='quantum-btn'>
                📄 Ver Tabla Completa NAAQS
            </a>
            <a href='https://www.epa.gov/pm-pollution/national-ambient-air-quality-standards-naaqs-pm' 
               target='_blank' class='quantum-btn'>
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
        
        st.markdown("<h3 style='text-align: center; background: linear-gradient(135deg, #818cf8 0%, #c084fc 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 1.8em;'>📊 Estándares EPA (NAAQS)</h3>", unsafe_allow_html=True)
        st.dataframe(epa_tabla, use_container_width=True, hide_index=True, height=280)
    
    with tab3:
        st.markdown("""
        <div class='premium-glass'>
            <h2>🇨🇦 Canadian Ambient Air Quality Standards (CAAQS)</h2>
            <p style='font-size: 1.15em;'>
                Canadá utiliza un sistema de <strong>mejora continua</strong> con estándares que se actualizan 
                cada 5 años y gestión por Air Zones para implementación regional.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='luxury-card'>
            <span class='elite-badge vigente'>2025</span>
            <h3>CAAQS 2020-2025</h3>
            <p style='font-size: 1.1em;'>
                <strong>Estándares Canadienses de Calidad del Aire Ambiente</strong><br><br>
                Sistema de gestión por Air Zones (Verde, Amarillo, Naranja, Rojo) con estándares 
                progresivamente más estrictos hacia 2025 y 2030.
            </p>
            <a href='https://www.ccme.ca/en/air-quality-report' 
               target='_blank' class='quantum-btn'>
                📄 Ver Reporte CAAQS
            </a>
            <a href='https://www.canada.ca/en/environment-climate-change/services/air-quality-health-index.html' 
               target='_blank' class='quantum-btn'>
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
        
        st.markdown("<h3 style='text-align: center; background: linear-gradient(135deg, #818cf8 0%, #c084fc 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 1.8em;'>📊 Estándares CAAQS - Evolución</h3>", unsafe_allow_html=True)
        st.dataframe(canada_tabla, use_container_width=True, hide_index=True, height=240)
    
    with tab4:
        st.markdown("<h2 style='text-align: center; background: linear-gradient(135deg, #818cf8 0%, #c084fc 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 2.5em;'>📊 Comparación Internacional - PM2.5</h2>", unsafe_allow_html=True)
        
        comparacion = pd.DataFrame([
            {'Entidad': 'OMS 2021', 'Anual': 5, '24h': 15, 'Color': '#10b981'},
            {'Entidad': 'EPA USA 2024', 'Anual': 9, '24h': 35, 'Color': '#6366f1'},
            {'Entidad': 'Canadá 2025', 'Anual': 8, '24h': 25, 'Color': '#8b5cf6'},
            {'Entidad': 'OEFA Perú', 'Anual': 25, '24h': 50, 'Color': '#ef4444'}
        ])
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=comparacion['Entidad'],
            y=comparacion['Anual'],
            name='Anual',
            marker_color=['#10b981', '#6366f1', '#8b5cf6', '#ef4444'],
            text=comparacion['Anual'],
            marker=dict(line=dict(color='rgba(255,255,255,0.2)', width=2))
        ))
        fig.add_trace(go.Bar(
            x=comparacion['Entidad'],
            y=comparacion['24h'],
            name='24 horas',
            marker_color=['#34d399', '#818cf8', '#a78bfa', '#f87171'],
            text=comparacion['24h'],
            marker=dict(line=dict(color='rgba(255,255,255,0.2)', width=2))
        ))
        
        fig.update_traces(texttemplate='%{text} μg/m³', textposition='outside')
        fig.update_layout(
            barmode='group',
            height=550,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#e0e7ff', size=15, family='Inter'),
            xaxis=dict(showgrid=False, tickfont=dict(size=14)),
            yaxis=dict(showgrid=True, gridcolor='rgba(129, 140, 248, 0.1)', title='Concentración (μg/m³)'),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1,
                       bgcolor='rgba(15, 23, 42, 0.8)', bordercolor='rgba(129, 140, 248, 0.3)', borderwidth=1)
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class='premium-glass'>
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
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.08) 0%, rgba(168, 85, 247, 0.08) 100%); 
            backdrop-filter: blur(30px) saturate(180%); 
            padding: 60px 40px; 
            border-radius: 32px; 
            margin-top: 60px; 
            border: 1px solid rgba(255,255,255,0.08); 
            box-shadow: 0 30px 90px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.1);'>
    <h2 style='background: linear-gradient(135deg, #818cf8 0%, #c084fc 100%); 
               -webkit-background-clip: text; 
               -webkit-text-fill-color: transparent; 
               margin: 0; 
               font-weight: 900; 
               font-size: 2.5em;
               letter-spacing: -0.02em;'>
        Universidad Nacional de Moquegua
    </h2>
    <p style='color: #e0e7ff; font-size: 1.3em; margin: 20px 0; font-weight: 600;'>
        Facultad de Ingeniería y Arquitectura
    </p>
    <p style='color: #c7d2fe; margin: 15px 0; font-size: 1.05em;'>
        <strong>Curso:</strong> Contaminación y Control Atmosférico
    </p>
    <p style='color: #c7d2fe; margin: 15px 0; font-size: 1.05em;'>
        <strong>Docente:</strong> Prof. Dr. José Antonio Valeriano Zapana
    </p>
    <div style='margin-top: 35px; padding-top: 30px; border-top: 1px solid rgba(129, 140, 248, 0.2);'>
        <p style='color: #a5b4fc; font-size: 1em; font-weight: 600;'>
            2024-2025 | Herramienta Interactiva de Consulta de Marco Normativo del Aire
        </p>
        <p style='color: #6366f1; font-size: 0.9em; margin-top: 15px; font-weight: 500;'>
            Desarrollado con Streamlit & Plotly | Datos oficiales de MINAM, OMS, EPA y CCME
        </p>
    </div>
</div>
""", unsafe_allow_html=True)
