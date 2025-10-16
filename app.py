import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(
    page_title="Marco Normativo del Aire - Peru",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS ULTRA PREMIUM
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
            radial-gradient(circle at 15% 20%, rgba(34, 211, 238, 0.15) 0%, transparent 45%),
            radial-gradient(circle at 85% 10%, rgba(14, 165, 233, 0.18) 0%, transparent 45%),
            radial-gradient(circle at 50% 80%, rgba(6, 182, 212, 0.12) 0%, transparent 50%);
        z-index: 0;
        animation: breathe 8s ease-in-out infinite;
    }
    
    @keyframes breathe { 0%, 100% { opacity: 1; } 50% { opacity: 0.8; } }
    @keyframes fadeInUp { from { opacity: 0; transform: translateY(50px); } to { opacity: 1; transform: translateY(0); } }
    
    .mega-header {
        text-align: center;
        padding: 80px 50px;
        background: linear-gradient(135deg, rgba(6, 182, 212, 0.08) 0%, rgba(14, 165, 233, 0.12) 50%, rgba(6, 78, 59, 0.08) 100%);
        backdrop-filter: blur(30px) saturate(200%);
        border-radius: 24px;
        margin-bottom: 50px;
        border: 1px solid rgba(34, 211, 238, 0.25);
        box-shadow: 0 30px 90px rgba(0, 0, 0, 0.9), inset 0 1px 0 rgba(34, 211, 238, 0.15), 0 0 100px rgba(6, 182, 212, 0.2);
        animation: fadeInUp 1s ease-out;
        position: relative;
        z-index: 1;
    }
    
    .mega-header h1 {
        font-size: 4.5em !important;
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
    
    .mega-header .subtitle { color: #a5f3fc; font-size: 1.6em; font-weight: 700; margin-top: 25px; }
    .mega-header .description { color: #67e8f9; font-size: 1.2em; margin-top: 20px; }
    
    .elite-glass {
        background: linear-gradient(135deg, rgba(17, 24, 39, 0.95) 0%, rgba(31, 41, 55, 0.9) 100%);
        backdrop-filter: blur(20px);
        padding: 50px;
        border-radius: 20px;
        border: 1px solid rgba(6, 182, 212, 0.25);
        margin: 30px 0;
        box-shadow: 0 25px 70px rgba(0, 0, 0, 0.8), inset 0 1px 0 rgba(6, 182, 212, 0.15);
        transition: all 0.4s;
        z-index: 1;
    }
    
    .elite-glass:hover {
        transform: translateY(-5px);
        box-shadow: 0 35px 100px rgba(0, 0, 0, 0.9), 0 0 80px rgba(6, 182, 212, 0.25);
    }
    
    .elite-glass h2 {
        font-size: 2.2em;
        font-weight: 800;
        background: linear-gradient(135deg, #06b6d4 0%, #22d3ee 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0 0 25px 0;
    }
    
    .elite-glass p { color: #e0f2fe; line-height: 1.9; font-size: 1.05em; }
    .elite-glass strong { color: #06b6d4; font-weight: 700; }
    
    .platinum-card {
        background: linear-gradient(135deg, rgba(31, 41, 55, 0.95) 0%, rgba(17, 24, 39, 0.98) 100%);
        padding: 45px;
        border-radius: 20px;
        margin: 30px 0;
        border-left: 4px solid #06b6d4;
        box-shadow: 0 25px 70px rgba(0, 0, 0, 0.8), -4px 0 30px rgba(6, 182, 212, 0.25);
        transition: all 0.5s;
        z-index: 1;
    }
    
    .platinum-card:hover {
        transform: translateX(10px);
        box-shadow: 0 35px 100px rgba(0, 0, 0, 0.9), -6px 0 50px rgba(6, 182, 212, 0.4);
    }
    
    .platinum-card h3 { color: #06b6d4 !important; font-size: 1.9em; font-weight: 800; margin: 0 0 20px 0; }
    .platinum-card p { color: #e0f2fe; font-size: 1.1em; line-height: 1.9; }
    
    .premium-badge {
        background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%);
        color: #000;
        padding: 10px 26px;
        border-radius: 25px;
        font-size: 0.85em;
        font-weight: 800;
        display: inline-block;
        margin-right: 15px;
        box-shadow: 0 10px 30px rgba(6, 182, 212, 0.5);
        text-transform: uppercase;
    }
    
    .diamond-btn {
        background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%);
        color: #000;
        padding: 18px 40px;
        border-radius: 12px;
        text-decoration: none;
        display: inline-block;
        margin: 12px 10px;
        font-weight: 800;
        box-shadow: 0 15px 40px rgba(6, 182, 212, 0.5);
        transition: all 0.3s;
    }
    
    .diamond-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 20px 60px rgba(6, 182, 212, 0.7);
    }
    
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, rgba(31, 41, 55, 0.9) 0%, rgba(17, 24, 39, 0.95) 100%);
        color: #06b6d4;
        border: 1.5px solid rgba(6, 182, 212, 0.3);
        border-radius: 12px;
        padding: 16px 20px;
        font-weight: 700;
        transition: all 0.3s;
        text-transform: uppercase;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%);
        color: #000;
        transform: translateY(-2px);
    }
    
    .dataframe {
        background: rgba(17, 24, 39, 0.95) !important;
        border-radius: 16px !important;
        border: 1px solid rgba(6, 182, 212, 0.25) !important;
    }
    
    .dataframe thead tr th {
        background: linear-gradient(135deg, rgba(6, 182, 212, 0.2) 0%, rgba(14, 165, 233, 0.25) 100%) !important;
        color: #06b6d4 !important;
        font-weight: 800 !important;
        padding: 18px !important;
    }
    
    .dataframe tbody tr td { color: #e0f2fe !important; padding: 16px !important; }
    .dataframe tbody tr:hover { background: rgba(6, 182, 212, 0.1) !important; }
</style>
""", unsafe_allow_html=True)

if 'pagina' not in st.session_state:
    st.session_state.pagina = "Inicio"

st.markdown("""
<div class='mega-header'>
    <h1>Marco Normativo de Calidad del Aire</h1>
    <p class='subtitle'>Universidad Nacional de Moquegua</p>
    <p class='description'>Herramienta Interactiva de Consulta | Normativas Peruanas e Internacionales</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

with col1:
    if st.button("INICIO", use_container_width=True):
        st.session_state.pagina = "Inicio"
with col2:
    if st.button("ECA", use_container_width=True):
        st.session_state.pagina = "ECA"
with col3:
    if st.button("LMP", use_container_width=True):
        st.session_state.pagina = "LMP"
with col4:
    if st.button("PROTOCOLO", use_container_width=True):
        st.session_state.pagina = "Protocolo"
with col5:
    if st.button("LINEAMIENTO", use_container_width=True):
        st.session_state.pagina = "Lineamiento"
with col6:
    if st.button("MEDIDAS", use_container_width=True):
        st.session_state.pagina = "Medidas"
with col7:
    if st.button("INTERNACIONAL", use_container_width=True):
        st.session_state.pagina = "Normativas"

st.markdown("<br>", unsafe_allow_html=True)

if st.session_state.pagina == "Inicio":
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("""
        <div class='elite-glass'>
            <h2>Sobre esta Herramienta</h2>
            <p style='font-size: 1.15em;'>
                Plataforma integral que reune el <strong>marco normativo completo</strong> sobre 
                calidad del aire en Peru y el mundo.
            </p>
            <ul style='font-size: 1.1em; line-height: 2.5;'>
                <li><strong>ECA:</strong> Estandares de Calidad Ambiental</li>
                <li><strong>LMP:</strong> Limites Maximos Permisibles</li>
                <li><strong>Protocolos:</strong> Monitoreo y medicion</li>
                <li><strong>Lineamientos:</strong> Guias tecnicas</li>
                <li><strong>Medidas de Control:</strong> Tecnologias</li>
                <li><strong>Normativas Internacionales:</strong> OMS, EPA, Canada</li>
            </ul>
            <p style='margin-top: 35px; font-size: 1.1em;'>
                Acceso directo a documentos oficiales con un solo click
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='elite-glass'><h2>Acceso Rapido</h2></div>", unsafe_allow_html=True)
        
        if st.button("Estandares ECA", use_container_width=True, type="primary"):
            st.session_state.pagina = "ECA"
        if st.button("Limites LMP", use_container_width=True):
            st.session_state.pagina = "LMP"
        if st.button("Protocolos", use_container_width=True):
            st.session_state.pagina = "Protocolo"
        if st.button("Lineamientos", use_container_width=True):
            st.session_state.pagina = "Lineamiento"
        if st.button("Control de Emisiones", use_container_width=True):
            st.session_state.pagina = "Medidas"
        if st.button("Normativas Mundial", use_container_width=True):
            st.session_state.pagina = "Normativas"
    
    st.markdown("""
    <div class='elite-glass'>
        <h2>Comparacion Internacional - PM2.5 Anual</h2>
        <p style='font-size: 1.05em;'>Estandares mas estrictos protegen mejor la salud publica</p>
    </div>
    """, unsafe_allow_html=True)
    
    datos_comp = pd.DataFrame([
        {'Entidad': 'OMS 2021', 'Valor': 5},
        {'Entidad': 'EPA USA', 'Valor': 9},
        {'Entidad': 'Canada', 'Valor': 8.8},
        {'Entidad': 'OEFA Peru', 'Valor': 25}
    ])
    
    fig = px.bar(datos_comp, x='Entidad', y='Valor', 
                 color='Entidad',
                 color_discrete_sequence=['#06b6d4', '#3b82f6', '#8b5cf6', '#ef4444'],
                 text='Valor')
    fig.update_traces(texttemplate='%{text} ug/m3', textposition='outside',
                      marker=dict(line=dict(color='rgba(6, 182, 212, 0.4)', width=2)),
                      textfont=dict(size=14, color='#e0f2fe'))
    fig.update_layout(
        height=550,
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0f2fe', size=15),
        xaxis=dict(showgrid=False, tickfont=dict(size=14, color='#22d3ee')),
        yaxis=dict(showgrid=True, gridcolor='rgba(6, 182, 212, 0.15)', 
                   title='Concentracion (ug/m3)', titlefont=dict(color='#06b6d4'))
    )
    st.plotly_chart(fig, use_container_width=True)
    
elif st.session_state.pagina == "ECA":
    st.info("Estandares de Calidad Ambiental - Contenido en desarrollo")
    
elif st.session_state.pagina == "LMP":
    st.info("Limites Maximos Permisibles - Contenido en desarrollo")
    
elif st.session_state.pagina == "Protocolo":
    st.info("Protocolos de Monitoreo - Contenido en desarrollo")
    
elif st.session_state.pagina == "Lineamiento":
    st.info("Lineamientos Tecnicos - Contenido en desarrollo")
    
elif st.session_state.pagina == "Medidas":
    st.info("Medidas de Control - Contenido en desarrollo")
    
elif st.session_state.pagina == "Normativas":
    st.info("Normativas Internacionales - Contenido en desarrollo")
