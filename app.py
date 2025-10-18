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

# CSS Ultra Profesional (mantengo tu CSS completo...)
# [Aquí va todo el CSS que ya tienes - no lo modifico]

# Estado de sesión
if 'pagina' not in st.session_state:
    st.session_state.pagina = "Inicio"

# Sidebar
with st.sidebar:
    st.markdown("### 🔍 NAVEGACIÓN")
    
    if st.button("🏠 Inicio", use_container_width=True):
        st.session_state.pagina = "Inicio"
    
    if st.button("📋 ECA", use_container_width=True):
        st.session_state.pagina = "ECA"
    
    if st.button("🏭 LMP", use_container_width=True):
        st.session_state.pagina = "LMP"

# Header
st.markdown(f"""
<div class='institutional-header fade-in'>
    <h1>🌍 Marco Normativo de Calidad del Aire</h1>
    <p class='subtitle'>Sistema Integral de Consulta</p>
</div>
""", unsafe_allow_html=True)

# Página INICIO con línea de tiempo
if st.session_state.pagina == "Inicio":
    
    # Métricas
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Normativas", "12")
    with col2:
        st.metric("Estándares", "6")
    with col3:
        st.metric("Contaminantes", "8")
    with col4:
        st.metric("Protocolos", "5")
    
    # LÍNEA DE TIEMPO
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h3 style='text-align: center; margin-bottom: 2rem;'>
            ⏳ Evolución del Marco Normativo
        </h3>
        
        <div class='timeline'>
            <div class='timeline-item'>
                <div class='timeline-marker'>
                    <div class='timeline-dot'></div>
                    <div class='timeline-line'></div>
                </div>
                <div class='timeline-content'>
                    <div class='timeline-year'>2001</div>
                    <div class='timeline-card'>
                        <div class='timeline-icon'>📋</div>
                        <h4>D.S. N° 074-2001-PCM</h4>
                        <p class='timeline-title'>Primer Reglamento ECA</p>
                        <p class='timeline-desc'>Primeros estándares nacionales de calidad del aire.</p>
                        <div class='timeline-badge historical'>Histórico</div>
                    </div>
                </div>
            </div>
            
            <div class='timeline-item highlight'>
                <div class='timeline-marker'>
                    <div class='timeline-dot highlight-dot'></div>
                    <div class='timeline-line'></div>
                </div>
                <div class='timeline-content'>
                    <div class='timeline-year highlight-year'>2017</div>
                    <div class='timeline-card highlight-card'>
                        <div class='timeline-icon'>🌟</div>
                        <h4>D.S. N° 003-2017-MINAM</h4>
                        <p class='timeline-title'>Nuevos Estándares ECA</p>
                        <p class='timeline-desc'>Actualización mayor con 8 contaminantes criterio.</p>
                        <div class='timeline-badge highlight-badge'>Norma Principal</div>
                    </div>
                </div>
            </div>
            
            <div class='timeline-item future'>
                <div class='timeline-marker'>
                    <div class='timeline-dot future-dot'></div>
                </div>
                <div class='timeline-content'>
                    <div class='timeline-year future-year'>2024</div>
                    <div class='timeline-card future-card'>
                        <div class='timeline-icon'>🔮</div>
                        <h4>Actualización Esperada</h4>
                        <p class='timeline-title'>Revisión de Estándares</p>
                        <p class='timeline-desc'>Alineación con guías OMS 2021.</p>
                        <div class='timeline-badge future'>En Evaluación</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Gráfico comparativo
    st.markdown("## 📊 Análisis Comparativo PM2.5")
    
    datos_comp = pd.DataFrame([
        {'Entidad': 'OMS 2021', 'Valor': 5, 'Tipo': 'Internacional'},
        {'Entidad': 'EPA USA', 'Valor': 9, 'Tipo': 'Internacional'},
        {'Entidad': 'Perú', 'Valor': 25, 'Tipo': 'Nacional'}
    ])
    
    fig = px.bar(
        datos_comp,
        x='Entidad',
        y='Valor',
        color='Tipo',
        text='Valor'
    )
    
    fig.update_traces(texttemplate='%{text} μg/m³', textposition='outside')
    
    fig.update_layout(
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#E3E8EF'),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)')
    )
    
    st.plotly_chart(fig, use_container_width=True)

elif st.session_state.pagina == "ECA":
    st.markdown("## 📋 Estándares de Calidad Ambiental")
    st.info("Contenido de ECA aquí...")

elif st.session_state.pagina == "LMP":
    st.markdown("## 🏭 Límites Máximos Permisibles")
    st.info("Contenido de LMP aquí...")

# Footer
st.markdown("""
<div class='corporate-footer'>
    <h3>Universidad Nacional de Moquegua</h3>
    <p>© 2024 UNAM</p>
</div>
""", unsafe_allow_html=True)
