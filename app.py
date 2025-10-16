import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import time

# Configuración de la página
st.set_page_config(
    page_title="Sistema de Calidad del Aire",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo CSS mejorado y más dinámico
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .content-box {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        margin: 10px 0;
        animation: fadeIn 0.5s;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        transition: transform 0.3s;
    }
    .metric-card:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
    }
    .alert-box {
        padding: 15px;
        border-radius: 10px;
        margin: 15px 0;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.8; }
    }
    h1, h2, h3 {
        color: white !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
</style>
""", unsafe_allow_html=True)

# Datos
air_standards = {
    'pm25': pd.DataFrame([
        {'entidad': 'OMS 2021', 'anual': 5, 'dia24h': 15},
        {'entidad': 'OEFA Peru', 'anual': 25, 'dia24h': 50},
        {'entidad': 'EPA USA', 'anual': 9, 'dia24h': 35},
        {'entidad': 'Canada', 'anual': 8.8, 'dia24h': 27}
    ]),
    'pm10': pd.DataFrame([
        {'entidad': 'OMS 2021', 'anual': 15, 'dia24h': 45},
        {'entidad': 'OEFA Peru', 'anual': 50, 'dia24h': 100},
        {'entidad': 'EPA USA', 'anual': None, 'dia24h': 150},
        {'entidad': 'Canada', 'anual': None, 'dia24h': 50}
    ]),
    'no2': pd.DataFrame([
        {'entidad': 'OMS 2021', 'anual': 10, 'dia24h': 25, 'hora1': None},
        {'entidad': 'OEFA Peru', 'anual': 100, 'dia24h': None, 'hora1': 200},
        {'entidad': 'EPA USA', 'anual': 53, 'dia24h': None, 'hora1': 100},
        {'entidad': 'Canada', 'anual': None, 'dia24h': None, 'hora1': 60}
    ]),
    'so2': pd.DataFrame([
        {'entidad': 'OMS 2021', 'dia24h': 40, 'hora1': None},
        {'entidad': 'OEFA Peru', 'dia24h': 250, 'hora1': None},
        {'entidad': 'EPA USA', 'dia24h': None, 'hora1': 75},
        {'entidad': 'Canada', 'dia24h': None, 'hora1': 70}
    ]),
    'o3': pd.DataFrame([
        {'entidad': 'OMS 2021', 'hora8': 100},
        {'entidad': 'OEFA Peru', 'hora8': 100},
        {'entidad': 'EPA USA', 'hora8': 70},
        {'entidad': 'Canada', 'hora8': 62}
    ])
}

lmp_thermoelectric = pd.DataFrame([
    {'contaminante': 'NOx', 'gasNatural': 320, 'diesel': 850, 'residual': 2000, 'unidad': 'mg/Nm3'},
    {'contaminante': 'SO2', 'gasNatural': None, 'diesel': 1700, 'residual': 3500, 'unidad': 'mg/Nm3'},
    {'contaminante': 'PM', 'gasNatural': 50, 'diesel': 150, 'residual': 350, 'unidad': 'mg/Nm3'}
])

timeline = pd.DataFrame([
    {'año': 2001, 'evento': 'D.S. 074-2001-PCM - Primeros ECA Aire Peru', 'entidad': 'OEFA'},
    {'año': 2005, 'evento': 'OMS - Guías Calidad del Aire', 'entidad': 'OMS'},
    {'año': 2010, 'evento': 'D.S. 003-2010-MINAM - LMP Termoeléctricas', 'entidad': 'OEFA'},
    {'año': 2013, 'evento': 'EPA - PM2.5 Anual reducido a 12 ug/m3', 'entidad': 'EPA'},
    {'año': 2017, 'evento': 'D.S. 003-2017-MINAM - ECA Aire más estrictos', 'entidad': 'OEFA'},
    {'año': 2019, 'evento': 'D.S. 010-2019-MINAM - Modificatoria ECA', 'entidad': 'OEFA'},
    {'año': 2020, 'evento': 'EPA - Fortalece PM2.5', 'entidad': 'EPA'},
    {'año': 2021, 'evento': 'OMS - Nuevas Directrices (50% más estrictas)', 'entidad': 'OMS'},
    {'año': 2022, 'evento': 'Canada - Actualización CAAQS', 'entidad': 'Canada'},
    {'año': 2024, 'evento': 'EPA - PM2.5 Anual a 9.0 ug/m3', 'entidad': 'EPA'}
])

plantas_comparacion = pd.DataFrame([
    {'tipo': 'Hidroeléctrica', 'emisionNOx': 0, 'emisionSO2': 0, 'emisionPM': 0, 'impactoAire': 'Nulo'},
    {'tipo': 'Termoeléctrica Gas', 'emisionNOx': 280, 'emisionSO2': 0, 'emisionPM': 40, 'impactoAire': 'Moderado'},
    {'tipo': 'Termoeléctrica Diesel', 'emisionNOx': 750, 'emisionSO2': 1500, 'emisionPM': 130, 'impactoAire': 'Alto'},
    {'tipo': 'Termoeléctrica Carbón', 'emisionNOx': 1800, 'emisionSO2': 3200, 'emisionPM': 320, 'impactoAire': 'Muy Alto'}
])

# SIDEBAR - Navegación mejorada
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/air-quality.png", width=100)
    st.title("🌍 Navegación")
    st.markdown("---")
    
    # Contador de visitas simulado
    if 'visitas' not in st.session_state:
        st.session_state.visitas = 0
    st.session_state.visitas += 1
    st.metric("Visitas", st.session_state.visitas)
    
    st.markdown("---")
    
    # Navegación con botones interactivos
    pagina = st.radio(
        "Selecciona una sección:",
        ["🏠 Inicio", "🌍 OMS", "🇵🇪 OEFA Perú", "🇺🇸 EPA USA", 
         "🇨🇦 Canadá", "📅 Línea Tiempo", "⚡ Comparación Plantas", 
         "📋 PAMA", "🎯 Caso Práctico"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.info("📚 **Universidad Nacional de Moquegua**\n\nProf. Dr. José Antonio Valeriano Zapana")
    
    # Reloj en tiempo real
    tiempo_actual = datetime.now().strftime("%H:%M:%S")
    st.caption(f"🕐 {tiempo_actual}")

# PÁGINA INICIO
if pagina == "🏠 Inicio":
    st.markdown("<h1 style='text-align: center;'>🌍 Sistema Integral de Normativas de Calidad del Aire</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Caso 2: Central Termoeléctrica - Análisis de LMP en NOx/SO2</h3>", unsafe_allow_html=True)
    
    # Animación de bienvenida
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress_bar.progress(i + 1)
    progress_bar.empty()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class='metric-card'>
            <h2>🌍</h2>
            <h3>OMS</h3>
            <p>Estándares Globales</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='metric-card'>
            <h2>🇵🇪</h2>
            <h3>OEFA</h3>
            <p>Normativa Peruana</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='metric-card'>
            <h2>🇺🇸</h2>
            <h3>EPA</h3>
            <p>Estándares USA</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class='metric-card'>
            <h2>🇨🇦</h2>
            <h3>Canadá</h3>
            <p>CAAQS</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='content-box'>
        <h2>📊 Resumen Ejecutivo</h2>
        <p style='color: #333; font-size: 16px;'>
        Este sistema interactivo compara las principales normativas internacionales de calidad del aire,
        enfocándose en el análisis de Límites Máximos Permisibles (LMP) para centrales termoeléctricas.
        </p>
        <ul style='color: #333; font-size: 15px;'>
            <li>✅ Comparación de estándares OMS, EPA, OEFA y Canadá</li>
            <li>✅ Análisis de emisiones NOx y SO2</li>
            <li>✅ Evaluación de impacto ambiental</li>
            <li>✅ Planes de Adecuación (PAMA)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Gráfico comparativo animado
    st.markdown("<div class='content-box'>", unsafe_allow_html=True)
    st.subheader("📈 Comparación Rápida - PM2.5 Anual")
    fig = px.bar(air_standards['pm25'], x='entidad', y='anual', 
                 color='anual', 
                 title='Estándares PM2.5 Anual (μg/m³)',
                 color_continuous_scale='RdYlGn_r',
                 text='anual')
    fig.update_traces(texttemplate='%{text} μg/m³', textposition='outside')
    fig.update_layout(showlegend=False, height=400)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# PÁGINA OMS
elif pagina == "🌍 OMS":
    st.title("🌍 Organización Mundial de la Salud (OMS)")
    
    st.markdown("""
    <div class='alert-box' style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;'>
        <h4>⚠️ Directrices OMS 2021</h4>
        <p>Las más estrictas del mundo. Representan niveles que protegen la salud pública según la mejor evidencia científica.</p>
    </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["PM2.5", "PM10", "NO2", "SO2", "O3"])
    
    with tab1:
        st.markdown("<div class='content-box'>", unsafe_allow_html=True)
        col1, col2 = st.columns([2, 1])
        
        with col1:
            fig_pm25 = go.Figure()
            fig_pm25.add_trace(go.Bar(x=air_standards['pm25']['entidad'], y=air_standards['pm25']['anual'], 
                                      name='Anual', marker_color='#4f46e5', text=air_standards['pm25']['anual']))
            fig_pm25.add_trace(go.Bar(x=air_standards['pm25']['entidad'], y=air_standards['pm25']['dia24h'], 
                                      name='24 horas', marker_color='#818cf8', text=air_standards['pm25']['dia24h']))
            fig_pm25.update_traces(texttemplate='%{text}', textposition='outside')
            fig_pm25.update_layout(title='Estándares PM2.5 (μg/m³)', barmode='group', height=400)
            st.plotly_chart(fig_pm25, use_container_width=True)
        
        with col2:
            st.metric("OMS Anual", "5 μg/m³", delta="-20 vs OEFA", delta_color="normal")
            st.metric("OMS 24h", "15 μg/m³", delta="-35 vs OEFA", delta_color="normal")
            st.progress(5/50, text="OMS vs OEFA (10%)")
        
        st.error("⚠️ **Impacto en Salud:** Enfermedades cardiovasculares, cáncer de pulmón, muerte prematura. PM2.5 es el contaminante más peligroso por su tamaño microscópico.")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with tab2:
        st.markdown("<div class='content-box'>", unsafe_allow_html=True)
        fig_pm10 = px.bar(air_standards['pm10'], x='entidad', y=['anual', 'dia24h'], 
                          title='Estándares PM10 (μg/m³)', barmode='group',
                          color_discrete_sequence=['#10b981', '#6ee7b7'])
        fig_pm10.update_layout(height=400)
        st.plotly_chart(fig_pm10, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with tab3:
        st.markdown("<div class='content-box'>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("🟡 OMS Anual", "10 μg/m³", help="Promedio anual")
        with col2:
            st.metric("🟠 OMS 24h", "25 μg/m³", help="Promedio 24 horas")
        with col3:
            st.metric("🔴 OEFA Anual", "100 μg/m³", help="Perú - Estándar nacional")
        
        st.warning("**Fuente principal:** Tráfico vehicular, termoeléctricas. **Efectos:** Irritación respiratoria, asma, precursor de ozono.")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with tab4:
        st.markdown("<div class='content-box'>", unsafe_allow_html=True)
        fig_so2 = px.bar(air_standards['so2'], x='entidad', y=['dia24h', 'hora1'],
                         title='Estándares SO2 (μg/m³)', barmode='group',
                         color_discrete_sequence=['#ef4444', '#f87171'])
        st.plotly_chart(fig_so2, use_container_width=True)
        st.info("**Fuente:** Quema de carbón, refinación de petróleo, fundición. **Impacto:** Lluvia ácida, irritación respiratoria severa.")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with tab5:
        st.markdown("<div class='content-box'>", unsafe_allow_html=True)
        fig_o3 = px.bar(air_standards['o3'], x='entidad', y='hora8',
                        title='Estándares O3 - 8 horas (μg/m³)',
                        color='hora8', color_continuous_scale='Purples')
        st.plotly_chart(fig_o3, use_container_width=True)
        st.success("**Contaminante secundario:** Se forma por reacción fotoquímica entre NOx y VOCs bajo luz solar.")
        st.markdown("</div>", unsafe_allow_html=True)

# PÁGINA OEFA
elif pagina == "🇵🇪 OEFA Perú":
    st.title("🇵🇪 OEFA - Organismo de Evaluación y Fiscalización Ambiental")
    
    st.markdown("""
    <div class='alert-box' style='background: #dc2626; color: white;'>
        <h4>📜 Marco Legal Principal</h4>
        <p>D.S. N° 003-2017-MINAM (ECA Aire) y D.S. N° 003-2010-MINAM (LMP Termoeléctricas)</p>
    </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📊 ECA Aire", "🏭 LMP Termoeléctricas", "⚖️ ECA vs LMP"])
    
    with tab1:
        st.markdown("<div class='content-box'>", unsafe_allow_html=True)
        st.subheader("Estándares de Calidad Ambiental (ECA) - Aire")
        
        eca_data = pd.DataFrame([
            ['PM2.5', '24 horas', 50, 'μg/m³', '🟡'],
            ['PM2.5', 'Anual', 25, 'μg/m³', '🟢'],
            ['PM10', '24 horas', 100, 'μg/m³', '🟡'],
            ['PM10', 'Anual', 50, 'μg/m³', '🟢'],
            ['NO2', '1 hora', 200, 'μg/m³', '🔴'],
            ['NO2', 'Anual', 100, 'μg/m³', '🟠'],
            ['SO2', '24 horas', 250, 'μg/m³', '🔴'],
            ['O3', '8 horas', 100, 'μg/m³', '🟡'],
            ['CO', '8 horas', 10000, 'μg/m³', '🟢'],
            ['CO', '1 hora', 30000, 'μg/m³', '🟡']
        ], columns=['Contaminante', 'Periodo', 'Valor ECA', 'Unidad', 'Nivel'])
        
        st.dataframe(eca_data, use_container_width=True, hide_index=True, height=400)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with tab2:
        st.markdown("<div class='content-box'>", unsafe_allow_html=True)
        st.subheader("Límites Máximos Permisibles (LMP) - Termoeléctricas")
        st.caption("D.S. N° 003-2010-MINAM | Se miden en la chimenea (punto de emisión)")
        
        # Gráfico interactivo de LMP
        fig_lmp = go.Figure()
        for col in ['gasNatural', 'diesel', 'residual']:
            fig_lmp.add_trace(go.Bar(
                x=lmp_thermoelectric['contaminante'],
                y=lmp_thermoelectric[col],
                name=col.replace('gasNatural', 'Gas Natural').replace('diesel', 'Diesel').replace('residual', 'Residual'),
                text=lmp_thermoelectric[col],
                textposition='auto'
            ))
        fig_lmp.update_layout(title='LMP por Tipo de Combustible (mg/Nm³)', barmode='group', height=400)
        st.plotly_chart(fig_lmp, use_container_width=True)
        
        st.dataframe(lmp_thermoelectric, use_container_width=True, hide_index=True)
        
        st.error("⚠️ **Caso 2:** Central termoeléctrica reporta excedencias de LMP de NOx y SO2 durante arranques y paradas programadas.")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with tab3:
        st.markdown("<div class='content-box'>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div style='background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%); padding: 20px; border-radius: 10px; color: white;'>
                <h3>🌍 ECA (Receptor)</h3>
                <ul>
                    <li>✓ Se mide en el ambiente</li>
                    <li>✓ Protege salud pública</li>
                    <li>✓ Múltiples fuentes</li>
                    <li>✓ Estación de monitoreo</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style='background: linear-gradient(135deg, #10b981 0%, #059669 100%); padding: 20px; border-radius: 10px; color: white;'>
                <h3>🏭 LMP (Fuente)</h3>
                <ul>
                    <li>✓ Se mide en chimenea</li>
                    <li>✓ Responsabilidad titular</li>
                    <li>✓ Control industrial</li>
                    <li>✓ Emisión directa</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# PÁGINA EPA USA
elif pagina == "🇺🇸 EPA USA":
    st.title("🇺🇸 EPA - Environmental Protection Agency")
    
    st.markdown("<div class='content-box'>", unsafe_allow_html=True)
    st.info("**NAAQS:** Estándares primarios (salud) y secundarios (bienestar público, visibilidad, ecosistemas)")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Estándares Actuales")
        st.metric("PM2.5 Anual", "9.0 μg/m³", delta="2024 ✨", delta_color="off")
        st.metric("PM2.5 24h", "35 μg/m³")
        st.metric("PM10 24h", "150 μg/m³")
        st.metric("O3 8h", "0.070 ppm")
        st.metric("SO2 1h", "75 ppb")
    
    with col2:
        st.subheader("Evolución PM2.5 Anual")
        evolucion_data = pd.DataFrame([
            {'año': 1997, 'valor': 15},
            {'año': 2006, 'valor': 15},
            {'año': 2012, 'valor': 12},
            {'año': 2024, 'valor': 9}
        ])
        fig_evol = px.line(evolucion_data, x='año', y='valor', markers=True,
                           title='Reducción del 40% desde 1997')
        fig_evol.update_traces(line_color='#8b5cf6', line_width=4, marker_size=12)
        fig_evol.update_layout(height=400)
        st.plotly_chart(fig_evol, use_container_width=True)
    
    st.success("""
    **🎯 Implementación:**
    - Estados desarrollan SIP (State Implementation Plans)
    - Zonas de no cumplimiento requieren medidas adicionales
    - Sistema de permisos de emisión
    - Monitoreo continuo obligatorio
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# PÁGINA CANADÁ
elif pagina == "🇨🇦 Canadá":
    st.title("🇨🇦 Canadá - CAAQS")
    
    st.markdown("<div class='content-box'>", unsafe_allow_html=True)
    st.info("Sistema de gestión por **Air Zones** con mejora continua. Estándares cada 5 años.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Estándares 2020-2025")
        canada_data = pd.DataFrame([
            ['PM2.5 (24h)', 27, 25],
            ['PM2.5 (Anual)', 8.8, 8.0],
            ['O3 (8h)', 62, 60],
            ['NO2 (1h)', 60, 50],
            ['SO2 (1h)', 70, 65]
        ], columns=['Contaminante', '2020', '2025'])
        
        fig_canada = go.Figure()
        fig_canada.add_trace(go.Bar(x=canada_data['Contaminante'], y=canada_data['2020'], name='2020', marker_color='#fbbf24'))
        fig_canada.add_trace(go.Bar(x=canada_data['Contaminante'], y=canada_data['2025'], name='2025', marker_color='#10b981'))
        fig_canada.update_layout(title='Evolución Estándares', barmode='group', height=400)
        st.plotly_chart(fig_canada, use_container_width=True)
    
    with col2:
        st.subheader("Gestión por Air Zones")
        st.success("🟢 **Verde - Achievement:** Cumple estándares")
        st.warning("🟡 **Amarillo - Management:** Requiere gestión")
        st.error("🟠 **Naranja - Action:** Acciones requeridas")
        st.error("🔴 **Rojo - Critical:** Intervención urgente")
        
        # Simulación de zona
        zona_seleccionada = st.selectbox("Simular Air Zone:", ["Verde", "Amarillo", "Naranja", "Rojo"])
        
        if zona_seleccionada == "Verde":
            st.balloons()
            st.success("✅ Zona en cumplimiento total")
        elif zona_seleccionada == "Rojo":
            st.error("⚠️ Requiere intervención urgente")
    
    st.info("**🚀 Innovación:** Líder en monitoreo satelital, modelamiento atmosférico y gestión de incendios forestales.")
    st.markdown("</div>", unsafe_allow_html=True)

# PÁGINA LÍNEA DE TIEMPO
elif pagina == "📅 Línea Tiempo":
    st.title("📅 Línea de Tiempo - Evolución Normativas")
    
    st.markdown("<div class='content-box'>", unsafe_allow_html=True)
    
    # Timeline visual con colores
    for idx, row in timeline.iterrows():
        color_map = {
            'OEFA': '#a855f7',
            'OMS': '#10b981',
            'EPA': '#3b82f6',
            'Canada': '#f97316'
        }
        color = color_map.get(row['entidad'], '#6b7280')
        
        st.markdown(f"""
        <div style='background: {color}; padding: 15px; border-radius: 10px; margin: 10px 0; color: white; border-left: 5px solid white;'>
            <h3>📅 {row['año']} - {row['entidad']}</h3>
            <p style='font-size: 16px;'>{row['evento']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# PÁGINA COMPARACIÓN PLANTAS
elif pagina == "⚡ Comparación Plantas":
    st.title("⚡ Hidroeléctricas vs Termoeléctricas")
    
    st.markdown("<div class='content-box'>", unsafe_allow_html=True)
    st.error("⚠️ Las hidroeléctricas NO emiten contaminantes atmosféricos, las termoeléctricas SÍ (NOx, SO2, PM)")
    
    fig_plantas = go.Figure()
    fig_plantas.add_trace(go.Bar(x=plantas_comparacion['tipo'], y=plantas_comparacion['emisionNOx'], 
                                 name='NOx', marker_color='#fbbf24'))
    fig_plantas.add_trace(go.Bar(x=plantas_comparacion['tipo'], y=plantas_comparacion['emisionSO2'], 
                                 name='SO2', marker_color='#ef4444'))
    fig_plantas.add_trace(go.Bar(x=plantas_comparacion['tipo'], y=plantas_comparacion['emisionPM'], 
                                 name='PM', marker_color='#6b7280'))
    fig_plantas.update_layout(title='Emisiones por Tipo de Planta (mg/Nm³)', barmode='group', height=500)
    st.plotly_chart(fig_plantas, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        ### ✅ Hidroeléctrica
        - Cero emisiones atmosféricas
        - Energía 100% renovable
        - No requiere LMP de aire
        - No contribuye cambio climático
        """)
    
    with col2:
        st.error("""
        ### ⚠️ Termoeléctrica
        - Alta emisión NOx y SO2
        - Contribuye lluvia ácida
        - Requiere LMP estrictos
        - Emisiones CO2
        """)
    
    st.markdown("</div>", unsafe_allow_html=True)

# PÁGINA PAMA
elif pagina == "📋 PAMA":
    st.title("📋 Plan de Adecuación y Manejo Ambiental")
    
    st.markdown("<div class='content-box'>", unsafe_allow_html=True)
    st.info("El PAMA permite adecuarse gradualmente a los LMP mediante inversiones en tecnología de control.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Objetivos")
        st.write("""
        - ✅ Cumplir LMP vigentes
        - ✅ Reducir emisiones progresivamente
        - ✅ Implementar mejores tecnologías
        - ✅ Mantener operatividad económica
        - ✅ Proteger salud pública
        """)
    
    with col2:
        st.subheader("⏱️ Plazos Típicos")
        plazos = pd.DataFrame([
            ['Diagnóstico', 3],
            ['Ingeniería', 7.5],
            ['Adquisición', 9],
            ['Instalación', 15],
            ['Pruebas', 4.5]
        ], columns=['Fase', 'Meses'])
        
        fig_plazos = px.bar(plazos, x='Fase', y='Meses', color='Meses',
                            title='Duración de Fases (meses)',
                            color_continuous_scale='Viridis')
        st.plotly_chart(fig_plazos, use_container_width=True)
    
    st.subheader("💰 Costos Tecnologías de Control")
    tecnologias = pd.DataFrame([
        ['Sistema SCR', 'NOx', '>90%', '$2-5 millones', '12-18 meses'],
        ['Desulfuración (FGD)', 'SO2', '>95%', '$5-10 millones', '18-24 meses'],
        ['Quemadores Low-NOx', 'NOx', '30-50%', '$500k-1M', '6-12 meses'],
        ['Filtros de mangas', 'PM', '>99%', '$1-3 millones', '9-15 meses']
    ], columns=['Tecnología', 'Contaminante', 'Eficiencia', 'Costo (USD)', 'Plazo'])
    
    st.dataframe(tecnologias, use_container_width=True, hide_index=True)
    st.markdown("</div>", unsafe_allow_html=True)

# PÁGINA CASO PRÁCTICO
elif pagina == "🎯 Caso Práctico":
    st.title("🎯 Caso 2: Central Termoeléctrica")
    
    st.markdown("<div class='content-box'>", unsafe_allow_html=True)
    st.error("""
    ### ⚠️ Situación
    Central termoeléctrica reporta excedencias de LMP de NOx y SO2 **durante arranques y paradas programadas**, 
    alegando cumplimiento parcial del PAMA.
    """)
    
    st.subheader("❓ Preguntas Clave para Análisis")
    
    with st.expander("1️⃣ ¿Las excedencias durante arranques/paradas están contempladas?"):
        st.write("Analizar si la normativa permite excepciones durante eventos operacionales transitorios.")
        respuesta1 = st.radio("Tu análisis:", ["Sí, están permitidas", "No, no están permitidas", "Depende del caso"], key="q1")
        if respuesta1:
            st.success(f"✅ Seleccionaste: {respuesta1}")
    
    with st.expander("2️⃣ ¿El PAMA incluye medidas para estos eventos?"):
        st.write("Verificar si el PAMA presentado contempla protocolos específicos para arranques/paradas.")
        respuesta2 = st.text_area("Escribe tu análisis:", key="q2")
        if respuesta2:
            st.info(f"📝 Tu respuesta: {respuesta2}")
    
    with st.expander("3️⃣ ¿Existe reincidencia o es la primera vez?"):
        st.write("Determinar si hay antecedentes de infracciones similares.")
        col1, col2 = st.columns(2)
        with col1:
            veces = st.number_input("Número de veces:", min_value=0, max_value=10, value=1)
        with col2:
            if veces == 0:
                st.success("✅ Primera vez")
            elif veces <= 2:
                st.warning("⚠️ Reincidente")
            else:
                st.error("🚨 Reincidente crónico")
    
    with st.expander("4️⃣ ¿Hay atenuantes o agravantes?"):
        st.write("Evaluar circunstancias que afectan la gravedad.")
        atenuantes = st.multiselect("Atenuantes:", 
            ["Inversión en tecnología", "Cumplimiento parcial PAMA", "Primera infracción", "Autoreporte"])
        agravantes = st.multiselect("Agravantes:",
            ["Impacto en población", "Reincidencia", "No presentó PAMA", "Daño ambiental comprobado"])
        
        if atenuantes or agravantes:
            st.write(f"**Balance:** {len(atenuantes)} atenuantes vs {len(agravantes)} agravantes")
    
    with st.expander("5️⃣ ¿Qué medidas técnicas inmediatas?"):
        st.write("Proponer soluciones técnicas aplicables.")
        medidas = st.multiselect("Medidas recomendadas:",
            ["Instalar quemadores Low-NOx", "Sistema SCR", "Optimizar arranques", 
             "Monitoreo continuo", "Capacitación operadores", "Plan de mantenimiento"])
        
        if medidas:
            st.success(f"✅ Seleccionaste {len(medidas)} medidas")
    
    # Calculadora de multa simulada
    st.subheader("💰 Simulador de Sanción")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        excedencia_nox = st.slider("Excedencia NOx (%)", 0, 200, 50)
    with col2:
        excedencia_so2 = st.slider("Excedencia SO2 (%)", 0, 200, 30)
    with col3:
        dias_incumplimiento = st.number_input("Días incumplimiento", 1, 365, 10)
    
    # Fórmula simplificada de multa
    multa_base = 50000  # USD
    factor_excedencia = (excedencia_nox + excedencia_so2) / 100
    multa_estimada = multa_base * factor_excedencia * (dias_incumplimiento / 30)
    
    st.metric("💵 Multa Estimada", f"${multa_estimada:,.0f} USD", 
              help="Estimación simplificada, no oficial")
    
    if multa_estimada > 100000:
        st.error("⚠️ Multa elevada - Se recomienda inversión inmediata en tecnología")
    else:
        st.warning("⚠️ Multa moderada - Implementar PAMA urgente")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; background: white; padding: 20px; border-radius: 10px;'>
    <p><strong>Universidad Nacional de Moquegua</strong> | Facultad de Ingeniería y Arquitectura</p>
    <p>Curso: Contaminación y Control Atmosférico | Prof. Dr. José Antonio Valeriano Zapana</p>
    <p style='font-size: 12px; color: #6B7280;'>2024-2025 | Sistema basado en normativas oficiales</p>
</div>
""", unsafe_allow_html=True)
