import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Configuración de la página
st.set_page_config(
    page_title="Sistema de Calidad del Aire",
    page_icon="🌍",
    layout="wide"
)

# Estilo CSS personalizado
st.markdown("""
<style>
    .main {
        background: linear-gradient(to bottom right, #EFF6FF, #E0E7FF);
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 10px 20px;
        background-color: white;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Título principal
st.markdown("<h1 style='text-align: center; color: #312E81;'>Sistema Integral de Normativas de Calidad del Aire</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Caso 2: Central Termoeléctrica - Análisis de LMP en NOx/SO2</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6B7280;'>Universidad Nacional de Moquegua | Prof. Dr. José Antonio Valeriano Zapana</p>", unsafe_allow_html=True)
st.markdown("---")

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

# Tabs principales
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "🌍 OMS", "🇵🇪 OEFA Peru", "🇺🇸 EPA USA", "🇨🇦 Canada", 
    "📅 Línea Tiempo", "⚡ Plantas", "📋 PAMA"
])

# TAB 1: OMS
with tab1:
    st.header("Organización Mundial de la Salud (OMS)")
    st.info("Las directrices de la OMS 2021 son las más estrictas del mundo. Representan niveles de calidad del aire que protegen la salud pública según la mejor evidencia científica disponible.")
    
    st.subheader("Material Particulado PM2.5")
    fig_pm25 = go.Figure()
    fig_pm25.add_trace(go.Bar(x=air_standards['pm25']['entidad'], y=air_standards['pm25']['anual'], name='Anual', marker_color='#4f46e5'))
    fig_pm25.add_trace(go.Bar(x=air_standards['pm25']['entidad'], y=air_standards['pm25']['dia24h'], name='24 horas', marker_color='#818cf8'))
    fig_pm25.update_layout(title='Estándares PM2.5 (μg/m³)', barmode='group', height=400)
    st.plotly_chart(fig_pm25, use_container_width=True)
    
    st.info("**OMS 2021:** Anual 5 μg/m³, 24h 15 μg/m³\n\n**Impacto en salud:** Enfermedades cardiovasculares, cáncer de pulmón, muerte prematura. PM2.5 es el contaminante más peligroso por su tamaño microscópico.")
    
    st.subheader("Material Particulado PM10")
    fig_pm10 = go.Figure()
    fig_pm10.add_trace(go.Bar(x=air_standards['pm10']['entidad'], y=air_standards['pm10']['anual'], name='Anual', marker_color='#10b981'))
    fig_pm10.add_trace(go.Bar(x=air_standards['pm10']['entidad'], y=air_standards['pm10']['dia24h'], name='24 horas', marker_color='#6ee7b7'))
    fig_pm10.update_layout(title='Estándares PM10 (μg/m³)', barmode='group', height=400)
    st.plotly_chart(fig_pm10, use_container_width=True)
    
    st.subheader("Dióxido de Nitrógeno (NO2)")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("OMS 2021 - Anual", "10 μg/m³")
    with col2:
        st.metric("OMS 2021 - 24h", "25 μg/m³")
    with col3:
        st.metric("OEFA Peru - Anual", "100 μg/m³")
    st.caption("**Fuente principal:** Tráfico vehicular, termoeléctricas. **Efectos:** Irritación respiratoria, asma, precursor de ozono.")
    
    st.subheader("Dióxido de Azufre (SO2)")
    fig_so2 = go.Figure()
    fig_so2.add_trace(go.Bar(x=air_standards['so2']['entidad'], y=air_standards['so2']['dia24h'], name='24 horas', marker_color='#ef4444'))
    fig_so2.add_trace(go.Bar(x=air_standards['so2']['entidad'], y=air_standards['so2']['hora1'], name='1 hora', marker_color='#f87171'))
    fig_so2.update_layout(title='Estándares SO2 (μg/m³)', barmode='group', height=350)
    st.plotly_chart(fig_so2, use_container_width=True)
    st.caption("**Fuente:** Quema de carbón, refinación de petróleo, fundición de metales. **Impacto:** Lluvia ácida, irritación respiratoria severa.")
    
    st.subheader("Ozono Troposférico (O3)")
    fig_o3 = go.Figure()
    fig_o3.add_trace(go.Bar(x=air_standards['o3']['entidad'], y=air_standards['o3']['hora8'], name='8 horas', marker_color='#8b5cf6'))
    fig_o3.update_layout(title='Estándares O3 (μg/m³)', height=350)
    st.plotly_chart(fig_o3, use_container_width=True)
    st.caption("**Contaminante secundario:** No se emite directamente, se forma por reacción fotoquímica entre NOx y VOCs bajo luz solar. Niveles más altos en días soleados.")

# TAB 2: OEFA
with tab2:
    st.header("OEFA - Organismo de Evaluación y Fiscalización Ambiental")
    st.info("**Marco legal principal:** D.S. N° 003-2017-MINAM (ECA Aire) y D.S. N° 003-2010-MINAM (LMP para Termoeléctricas)")
    
    st.subheader("Estándares de Calidad Ambiental (ECA) - Aire")
    eca_data = pd.DataFrame([
        ['PM2.5', '24 horas', 50, 'μg/m³'],
        ['PM2.5', 'Anual', 25, 'μg/m³'],
        ['PM10', '24 horas', 100, 'μg/m³'],
        ['PM10', 'Anual', 50, 'μg/m³'],
        ['NO2', '1 hora', 200, 'μg/m³'],
        ['NO2', 'Anual', 100, 'μg/m³'],
        ['SO2', '24 horas', 250, 'μg/m³'],
        ['O3', '8 horas', 100, 'μg/m³'],
        ['CO', '8 horas', 10000, 'μg/m³'],
        ['CO', '1 hora', 30000, 'μg/m³']
    ], columns=['Contaminante', 'Periodo', 'Valor ECA', 'Unidad'])
    st.dataframe(eca_data, use_container_width=True, hide_index=True)
    
    st.subheader("Límites Máximos Permisibles (LMP) - Termoeléctricas")
    st.caption("D.S. N° 003-2010-MINAM | Se miden en la chimenea (punto de emisión)")
    st.dataframe(lmp_thermoelectric, use_container_width=True, hide_index=True)
    
    st.warning("**Caso 2:** Tu central termoeléctrica reporta excedencias de LMP de NOx y SO2 durante arranques y paradas programadas. Estos valores aplican en condiciones normales de operación.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("**ECA (Receptor)**\n- Se mide en el ambiente\n- Protege salud pública\n- Puede tener múltiples fuentes\n- Ejemplo: Estación de monitoreo en población")
    with col2:
        st.success("**LMP (Fuente)**\n- Se mide en la chimenea\n- Responsabilidad del titular\n- Control de emisiones industriales\n- Ejemplo: Chimenea de termoeléctrica")

# TAB 3: EPA
with tab3:
    st.header("EPA - Environmental Protection Agency (USA)")
    st.info("**NAAQS (National Ambient Air Quality Standards):** Estándares primarios (salud) y secundarios (bienestar público, visibilidad, ecosistemas)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Estándares Actuales")
        st.metric("PM2.5 Anual", "9.0 μg/m³", help="2024")
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
        fig_evol.update_traces(line_color='#8b5cf6', line_width=3)
        st.plotly_chart(fig_evol, use_container_width=True)
    
    st.success("**Implementación**\n- Estados desarrollan SIP (State Implementation Plans)\n- Zonas de no cumplimiento requieren medidas adicionales\n- Sistema de permisos de emisión\n- Monitoreo continuo obligatorio")

# TAB 4: Canada
with tab4:
    st.header("Canada - CAAQS (Canadian Ambient Air Quality Standards)")
    st.info("Sistema de gestión por **Air Zones** con mejora continua. Estándares se actualizan cada 5 años.")
    
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
        st.dataframe(canada_data, use_container_width=True, hide_index=True)
    
    with col2:
        st.subheader("Gestión por Air Zones")
        st.success("**Verde - Achievement:** Cumple estándares")
        st.warning("**Amarillo - Management:** Requiere gestión")
        st.error("**Naranja - Action:** Acciones requeridas")
        st.error("**Rojo - Critical:** Intervención urgente")
    
    st.info("**Innovación Canadiense:** Canadá es líder en monitoreo satelital de calidad del aire, modelamiento atmosférico avanzado, y gestión de incendios forestales. Enfoque de mejora continua con estándares progresivamente más estrictos basados en evidencia científica.")

# TAB 5: Línea de Tiempo
with tab5:
    st.header("Línea de Tiempo - Evolución de Normativas de Aire")
    
    for idx, row in timeline.iterrows():
        color = {
            'OEFA': '🟣',
            'OMS': '🟢',
            'EPA': '🔵',
            'Canada': '🟠'
        }.get(row['entidad'], '⚪')
        
        st.markdown(f"{color} **{row['año']} - {row['entidad']}**")
        st.caption(row['evento'])
        st.divider()

# TAB 6: Plantas
with tab6:
    st.header("Comparación: Plantas Hidroeléctricas vs Termoeléctricas")
    st.info("Las plantas hidroeléctricas NO emiten contaminantes atmosféricos, mientras que las termoeléctricas son una fuente significativa de NOx, SO2 y PM.")
    
    st.subheader("Emisiones por Tipo de Planta (mg/Nm³)")
    fig_plantas = go.Figure()
    fig_plantas.add_trace(go.Bar(x=plantas_comparacion['tipo'], y=plantas_comparacion['emisionNOx'], name='NOx', marker_color='#fbbf24'))
    fig_plantas.add_trace(go.Bar(x=plantas_comparacion['tipo'], y=plantas_comparacion['emisionSO2'], name='SO2', marker_color='#ef4444'))
    fig_plantas.add_trace(go.Bar(x=plantas_comparacion['tipo'], y=plantas_comparacion['emisionPM'], name='PM', marker_color='#6b7280'))
    fig_plantas.update_layout(barmode='group', height=400)
    st.plotly_chart(fig_plantas, use_container_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("**Hidroeléctrica - Ventajas ambientales:**\n- Cero emisiones atmosféricas\n- Energía renovable\n- No requiere LMP de aire\n- No contribuye al cambio climático")
    with col2:
        st.error("**Termoeléctrica - Características:**\n- Alta emisión de NOx y SO2\n- Contribuye a lluvia ácida\n- Requiere cumplir LMP estrictos\n- Emisiones de CO2")

# TAB 7: PAMA
with tab7:
    st.header("Plan de Adecuación y Manejo Ambiental (PAMA)")
    st.info("El PAMA permite a las empresas adecuarse gradualmente a los LMP mediante inversiones en tecnología de control de emisiones.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Objetivos del PAMA")
        st.markdown("""
        - Cumplir con LMP vigentes
        - Reducir emisiones progresivamente
        - Implementar mejores tecnologías disponibles
        - Mantener operatividad económica
        - Proteger salud pública
        """)
    
    with col2:
        st.subheader("Plazos Típicos")
        st.markdown("""
        - **Diagnóstico:** 3 meses
        - **Ingeniería:** 6-9 meses
        - **Adquisición:** 6-12 meses
        - **Instalación:** 12-18 meses
        - **Pruebas:** 3-6 meses
        - **Total:** 24-36 meses
        """)
    
    st.subheader("Costos Estimados de Tecnologías de Control")
    tecnologias = pd.DataFrame([
        ['Sistema SCR', 'NOx', '>90%', '$2-5 millones', '12-18 meses'],
        ['Desulfuración (FGD)', 'SO2', '>95%', '$5-10 millones', '18-24 meses'],
        ['Quemadores Low-NOx', 'NOx', '30-50%', '$500k-1M', '6-12 meses'],
        ['Filtros de mangas', 'PM', '>99%', '$1-3 millones', '9-15 meses']
    ], columns=['Tecnología', 'Contaminante', 'Eficiencia', 'Costo (USD)', 'Plazo'])
    st.dataframe(tecnologias, use_container_width=True, hide_index=True)
    
    st.warning("""
    **Caso 2: Central Termoeléctrica**
    
    Tu caso involucra una central que reporta excedencias de LMP de NOx y SO2 **durante arranques y paradas programadas**, 
    y alega cumplimiento parcial del PAMA.
    
    **Preguntas clave para análisis:**
    1. ¿Las excedencias durante arranques/paradas están contempladas en la normativa?
    2. ¿El PAMA incluye medidas para estos eventos operacionales?
    3. ¿Existe reincidencia o es la primera vez?
    4. ¿Hay atenuantes (inversión en tecnología) o agravantes (impacto en población)?
    5. ¿Qué medidas técnicas inmediatas se pueden implementar?
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 20px; background-color: white; border-radius: 10px;'>
    <p><strong>Universidad Nacional de Moquegua</strong> | Facultad de Ingeniería y Arquitectura</p>
    <p>Curso: Contaminación y Control Atmosférico | Prof. Dr. José Antonio Valeriano Zapana</p>
    <p style='font-size: 12px; color: #6B7280;'>2024-2025 | Sistema basado en normativas oficiales de OEFA, OMS, EPA y Canada</p>
</div>
""", unsafe_allow_html=True)
