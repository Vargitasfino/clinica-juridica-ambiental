import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

st.set_page_config(
    page_title="Clínica Jurídica-Ambiental",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
.stApp {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
h1, h2, h3 {
    color: #667eea !important;
}
.stAlert {
    background-color: rgba(102, 126, 234, 0.1);
    border-left: 4px solid #667eea;
}
@media (max-width: 768px) {
    .main {
        padding: 0.5rem;
    }
    h1 {
        font-size: 1.5rem !important;
    }
    h2 {
        font-size: 1.3rem !important;
    }
    h3 {
        font-size: 1.1rem !important;
    }
    .dataframe {
        font-size: 0.8rem;
    }
}
.stButton button {
    width: 100%;
    border-radius: 25px;
    border: none;
    background-color: rgba(255, 255, 255, 0.15);
    color: white;
    font-weight: 500;
    padding: 0.6rem 1.2rem;
    transition: all 0.3s ease;
    backdrop-filter: blur(10px);
}
.stButton button:hover {
    background-color: rgba(255, 255, 255, 0.25);
    transform: scale(1.02);
    box-shadow: 0 4px 15px rgba(255, 255, 255, 0.2);
}
.stButton button:active {
    background-color: rgba(102, 126, 234, 0.9);
    transform: scale(0.98);
}
div[data-testid="column"] button[kind="secondary"] {
    background-color: rgba(102, 126, 234, 0.85);
    color: white;
    font-weight: 600;
    box-shadow: 0 4px 20px rgba(102, 126, 234, 0.4);
}
</style>
""", unsafe_allow_html=True)

st.title("⚖️ Clínica Jurídica-Ambiental: Calidad del Aire")
st.markdown("### Caso 2: Central Termoeléctrica - Análisis de LMP en NOₓ/SO₂")

st.markdown("---")

# Inicializar página por defecto
if 'pagina' not in st.session_state:
    st.session_state.pagina = "📋 Caso de Estudio"

st.markdown("#### 📑 Navegación")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("📋 Caso de Estudio", 
                 use_container_width=True,
                 type="secondary" if st.session_state.pagina == "📋 Caso de Estudio" else "primary"):
        st.session_state.pagina = "📋 Caso de Estudio"

with col2:
    if st.button("📊 Matriz ECA/LMP", 
                 use_container_width=True,
                 type="secondary" if st.session_state.pagina == "📊 Matriz ECA/LMP" else "primary"):
        st.session_state.pagina = "📊 Matriz ECA/LMP"

with col3:
    if st.button("✅ Verificación QA/QC", 
                 use_container_width=True,
                 type="secondary" if st.session_state.pagina == "✅ Verificación QA/QC" else "primary"):
        st.session_state.pagina = "✅ Verificación QA/QC"

with col4:
    if st.button("⚖️ Tipificación", 
                 use_container_width=True,
                 type="secondary" if st.session_state.pagina == "⚖️ Tipificación" else "primary"):
        st.session_state.pagina = "⚖️ Tipificación"

with col5:
    if st.button("📝 Medidas", 
                 use_container_width=True,
                 type="secondary" if st.session_state.pagina == "📝 Medidas" else "primary"):
        st.session_state.pagina = "📝 Medidas"

col6, col7, col8, col9, col10 = st.columns(5)

with col6:
    if st.button("🏛️ Audiencia", 
                 use_container_width=True,
                 type="secondary" if st.session_state.pagina == "🏛️ Audiencia" else "primary"):
        st.session_state.pagina = "🏛️ Audiencia"

with col7:
    if st.button("🌐 Normativas", 
                 use_container_width=True,
                 type="secondary" if st.session_state.pagina == "🌐 Normativas" else "primary"):
        st.session_state.pagina = "🌐 Normativas"

with col8:
    if st.button("⏳ Línea Temporal", 
                 use_container_width=True,
                 type="secondary" if st.session_state.pagina == "⏳ Línea Temporal" else "primary"):
        st.session_state.pagina = "⏳ Línea Temporal"

with col9:
    if st.button("📋 Plan Adecuación", 
                 use_container_width=True,
                 type="secondary" if st.session_state.pagina == "📋 Plan Adecuación" else "primary"):
        st.session_state.pagina = "📋 Plan Adecuación"

with col10:
    if st.button("📚 Recursos", 
                 use_container_width=True,
                 type="secondary" if st.session_state.pagina == "📚 Recursos" else "primary"):
        st.session_state.pagina = "📚 Recursos"

pagina = st.session_state.pagina

st.markdown("---")

# Datos normativos
timeline_data = [
    {"fecha": "2001-06", "evento": "Perú: D.S. N° 074-2001-PCM - Primeros ECA para aire", "entidad": "OEFA"},
    {"fecha": "2005-10", "evento": "OMS: Guías de Calidad del Aire publicadas", "entidad": "OMS"},
    {"fecha": "2008-08", "evento": "Perú: Creación del MINAM", "entidad": "OEFA"},
    {"fecha": "2010-08", "evento": "Perú: D.S. N° 003-2010-MINAM - LMP para termoeléctricas", "entidad": "OEFA"},
    {"fecha": "2013-01", "evento": "EPA: Actualiza PM2.5 anual a 12 μg/m³", "entidad": "EPA"},
    {"fecha": "2017-06", "evento": "Perú: D.S. N° 003-2017-MINAM - ECA más estrictos", "entidad": "OEFA"},
    {"fecha": "2019-12", "evento": "Perú: D.S. N° 010-2019-MINAM - Modificación ECA", "entidad": "OEFA"},
    {"fecha": "2020-09", "evento": "EPA: Fortalece estándares PM2.5", "entidad": "EPA"},
    {"fecha": "2021-09", "evento": "OMS: Nuevas Directrices Globales más estrictas", "entidad": "OMS"},
    {"fecha": "2022-03", "evento": "Canadá: Actualización de Objetivos Calidad del Aire", "entidad": "Canadá"},
    {"fecha": "2023-05", "evento": "Perú: OEFA intensifica fiscalización en zonas mineras", "entidad": "OEFA"},
    {"fecha": "2024-02", "evento": "EPA: Propone estándares más estrictos para PM2.5", "entidad": "EPA"},
]

timeline_df = pd.DataFrame(timeline_data)
timeline_df['fecha'] = pd.to_datetime(timeline_df['fecha'])

# PÁGINAS

if pagina == "📋 Caso de Estudio":
    st.header("📋 Caso 2: Central Termoeléctrica")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Hechos (resumen)")
        st.info("""
        La central reporta **excedencias de LMP** en chimenea durante arranques y paradas programadas.
        Se invoca mantenimiento y cumplimiento parcial del plan de adecuación.
        
        **Contaminantes involucrados:**
        - **NOₓ** (Óxidos de Nitrógeno)
        - **SO₂** (Dióxido de Azufre)
        """)
    
    with col2:
        st.metric("Estado", "⚠️ Incumplimiento", "LMP excedido")
        st.metric("Fase", "En análisis", "")
    
    st.subheader("📄 Prueba disponible")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        #### 📊 Ensayos isocinéticos trimestrales
        - Mediciones de emisiones en chimenea
        - Datos técnicos certificados
        - Periodicidad trimestral
        """)
    
    with col2:
        st.markdown("""
        #### 📝 Bitácoras de operación
        - Registro de arranques y paradas
        - Eventos de mantenimiento
        - Historial operativo
        """)
    
    with col3:
        st.markdown("""
        #### 🔔 Registros CEMS y alarmas
        - Sistema de monitoreo continuo
        - Alertas automáticas
        - Datos en tiempo real
        """)
    
    st.markdown("---")
    
    st.subheader("⚖️ Normativa/criterios aplicables")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### 🏭 LMP para generación termoeléctrica
        - **D.S. N° 003-2010-MINAM**
        - NOₓ: Límites según tecnología
        - SO₂: Límites según combustible
        - Aplica en punto de emisión (chimenea)
        """)
    
    with col2:
        st.markdown("""
        #### 🌍 ECA aire para receptores poblacionales
        - **D.S. N° 003-2017-MINAM**
        - Protección de salud pública
        - Aplica en zona de influencia
        - Medición en estaciones de monitoreo
        """)
    
    st.markdown("---")
    
    st.subheader("❓ Preguntas guía")
    
    with st.expander("1️⃣ Diferencie LMP (fuente) vs ECA (receptor)"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **LMP (Límite Máximo Permisible)**
            - Se mide **en la fuente de emisión** (chimenea)
            - Concentración o flujo másico
            - Responsabilidad directa del titular
            - Control de emisiones industriales
            - Ejemplo: mg/Nm³ en chimenea
            """)
        with col2:
            st.markdown("""
            **ECA (Estándar de Calidad Ambiental)**
            - Se mide **en el ambiente receptor** (aire)
            - Protege salud pública y ecosistemas
            - Responsabilidad del Estado (gestión)
            - Puede tener múltiples fuentes
            - Ejemplo: μg/m³ en población
            """)
    
    with st.expander("2️⃣ ¿Existe reincidencia? ¿Atenuantes o agravantes?"):
        st.markdown("""
        **Análisis de reincidencia:**
        - Revisar historial de sanciones previas
        - Verificar si hay infracciones similares en últimos 12 meses
        - Consultar registro de fiscalización OEFA
        
        **Posibles atenuantes:**
        - ✅ Cumplimiento parcial del plan de adecuación
        - ✅ Eventos ocurren solo en arranques/paradas (no operación normal)
        - ✅ Implementación de CEMS (monitoreo continuo)
        - ✅ Colaboración con autoridades
        
        **Posibles agravantes:**
        - ❌ Falta de medidas correctivas inmediatas
        - ❌ Reiteración de excedencias
        - ❌ Impacto en zona poblada
        - ❌ Falta de notificación oportuna
        """)
    
    with st.expander("3️⃣ Proponer medidas técnicas y cronograma verificable"):
        st.markdown("""
        **Medidas técnicas propuestas:**
        
        **Corto plazo (0-3 meses):**
        - Optimización de protocolos de arranque/parada
        - Verificación y calibración de equipos de control
        - Incremento de frecuencia de monitoreo
        
        **Mediano plazo (3-12 meses):**
        - Instalación de quemadores de bajo NOₓ (Low-NOx burners)
        - Implementación de sistema SCR (Reducción Catalítica Selectiva)
        - Mejora del sistema de desulfuración (FGD)
        
        **Largo plazo (12-24 meses):**
        - Modernización completa del sistema de control de emisiones
        - Actualización del plan de adecuación
        - Certificación ISO 14001
        
        **Cronograma verificable:**
        - Hitos mensurables con fechas específicas
        - Responsables designados
        - Reportes mensuales a OEFA
        - Penalidades por incumplimiento
        """)

elif pagina == "📊 Matriz ECA/LMP":
    st.header("📊 Matriz ECA/LMP - Comparación de Resultados")
    
    st.info("Complete esta matriz con los datos de monitoreo de la central termoeléctrica")
    
    # Crear DataFrame editable
    if 'df_matriz' not in st.session_state:
        st.session_state.df_matriz = pd.DataFrame({
            'Parámetro': ['NOₓ', 'SO₂', 'PM10', 'PM2.5'],
            'Período': ['', '', '', ''],
            'Valor observado': ['', '', '', ''],
            'ECA/LMP': ['', '', '', ''],
            '¿Cumple? (Sí/No)': ['', '', '', '']
        })
    
    st.markdown("### 📝 Ingrese los datos de monitoreo:")
    
    edited_df = st.data_editor(
        st.session_state.df_matriz,
        use_container_width=True,
        num_rows="dynamic",
        column_config={
            "Parámetro": st.column_config.TextColumn("Parámetro", help="NOₓ, SO₂, PM, etc."),
            "Período": st.column_config.SelectboxColumn(
                "Período",
                options=["1h", "24h", "Anual"],
                help="Seleccione el período de medición"
            ),
            "Valor observado": st.column_config.NumberColumn("Valor observado (μg/m³)"),
            "ECA/LMP": st.column_config.NumberColumn("ECA/LMP (μg/m³)"),
            "¿Cumple? (Sí/No)": st.column_config.SelectboxColumn(
                "¿Cumple?",
                options=["Sí", "No"],
            )
        }
    )
    
    st.session_state.df_matriz = edited_df
    
    st.markdown("---")
    
    st.subheader("📌 Valores de referencia normativos")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🇵🇪 LMP Perú - Termoeléctricas (D.S. 003-2010-MINAM)")
        lmp_peru = pd.DataFrame({
            'Contaminante': ['NOₓ', 'SO₂', 'PM'],
            'Unidad': ['mg/Nm³', 'mg/Nm³', 'mg/Nm³'],
            'LMP Gas Natural': ['320', '---', '50'],
            'LMP Diésel': ['850', '1700', '150'],
        })
        st.dataframe(lmp_peru, use_container_width=True)
    
    with col2:
        st.markdown("#### 🌍 ECA Aire Perú (D.S. 003-2017-MINAM)")
        eca_peru = pd.DataFrame({
            'Contaminante': ['NO₂', 'SO₂', 'PM10', 'PM2.5'],
            'Período': ['1h / Anual', '24h', '24h / Anual', '24h / Anual'],
            'ECA (μg/m³)': ['200 / 100', '250', '100 / 50', '50 / 25'],
        })
        st.dataframe(eca_peru, use_container_width=True)

elif pagina == "✅ Verificación QA/QC":
    st.header("✅ Lista de Verificación QA/QC (Calidad de Datos)")
    
    st.info("Marque los criterios cumplidos para validar la calidad de los datos de monitoreo")
    
    st.subheader("📍 Criterios de calidad de datos")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🎯 Representatividad y calibración")
        
        check1 = st.checkbox("✓ Representatividad de la estación (ubicación, zona de influencia)")
        if check1:
            st.success("La estación está ubicada estratégicamente")
        
        check2 = st.checkbox("✓ Calibración/último mantenimiento del instrumento")
        if check2:
            fecha_calib = st.date_input("Fecha última calibración")
            st.success(f"Calibrado el: {fecha_calib}")
        
        check3 = st.checkbox("✓ Datos válidos ≥ 75% por período de reporte")
        if check3:
            porcentaje = st.slider("Porcentaje de datos válidos", 0, 100, 85)
            if porcentaje >= 75:
                st.success(f"✅ {porcentaje}% de datos válidos (cumple)")
            else:
                st.error(f"❌ {porcentaje}% de datos válidos (no cumple)")
        
        check4 = st.checkbox("✓ Tratamiento de outliers y datos faltantes documentado")
        if check4:
            st.text_area("Describa el tratamiento aplicado:", key="outliers")
    
    with col2:
        st.markdown("#### 📋 Métodos y trazabilidad")
        
        check5 = st.checkbox("✓ Compatibilidad de métodos (CEMS/isocinéticos/laboratorio)")
        if check5:
            metodo = st.selectbox(
                "Método utilizado:",
                ["EPA Method 3A", "EPA Method 7E", "ISO 10396", "Otro"]
            )
            st.success(f"Método: {metodo}")
        
        check6 = st.checkbox("✓ Trazabilidad y cadena de custodia de reportes")
        if check6:
            st.success("Documentación completa de trazabilidad")
        
        check7 = st.checkbox("✓ Laboratorio acreditado (ISO 17025 o equivalente)")
        if check7:
            lab_nombre = st.text_input("Nombre del laboratorio:")
            st.success(f"Laboratorio: {lab_nombre}")
        
        check8 = st.checkbox("✓ Reporte firmado por profesional competente")
        if check8:
            st.success("Profesional autorizado verificado")
    
    st.markdown("---")
    
    # Resumen de verificación
    total_checks = sum([check1, check2, check3, check4, check5, check6, check7, check8])
    porcentaje_cumpl = (total_checks / 8) * 100
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Criterios cumplidos", f"{total_checks}/8")
    with col2:
        st.metric("Porcentaje de cumplimiento", f"{porcentaje_cumpl:.1f}%")
    with col3:
        if porcentaje_cumpl >= 75:
            st.metric("Estado", "✅ APROBADO", "")
        else:
            st.metric("Estado", "❌ OBSERVADO", "")

elif pagina == "⚖️ Tipificación":
    st.header("⚖️ Tipificación y Responsabilidad")
    
    st.info("Identifique los hechos probados, normas infringidas y responsables")
    
    st.subheader("📋 Matriz de tipificación")
    
    if 'df_tipificacion' not in st.session_state:
        st.session_state.df_tipificacion = pd.DataFrame({
            'Hecho/probado': ['', '', ''],
            'Norma infringida': ['', '', ''],
            'Responsable(s)': ['', '', ''],
            'Agrav./Atenuantes': ['', '', '']
        })
    
    edited_tipif = st.data_editor(
        st.session_state.df_tipificacion,
        use_container_width=True,
        num_rows="dynamic"
    )
    
    st.session_state.df_tipificacion = edited_tipif
    
    st.markdown("---")
    
    st.subheader("📚 Marco legal de referencia")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### Normativa aplicable - Perú
        
        **Ley N° 28611 - Ley General del Ambiente**
        - Art. 31: Estándares de Calidad Ambiental
        - Art. 32: Límites Máximos Permisibles
        
        **Ley N° 29325 - Ley del SINEFA**
        - Competencias de fiscalización ambiental
        - Procedimiento sancionador
        
        **D.S. N° 003-2010-MINAM**
        - LMP para generación termoeléctrica
        - Obligaciones de monitoreo
        
        **D.S. N° 003-2017-MINAM**
        - ECA para aire
        - Gestión de calidad de aire
        """)
    
    with col2:
        st.markdown("""
        #### Infracciones típicas
        
        **Tipo I - Leve:**
        - Excedencia menor del 10%
        - Incumplimiento de reporte
        - Multa: hasta 100 UIT
        
        **Tipo II - Grave:**
        - Excedencia 10-50%
        - Reincidencia
        - Multa: 100-500 UIT
        
        **Tipo III - Muy Grave:**
        - Excedencia >50%
        - Daño ambiental
        - Multa: 500-10,000 UIT
        - Posible paralización
        """)

elif pagina == "📝 Medidas":
    st.header("📝 Medidas y Sanción Propuesta")
    
    st.info("Proponga medidas correctivas, preventivas o estructurales con fundamento técnico-legal")
    
    if 'df_medidas' not in st.session_state:
        st.session_state.df_medidas = pd.DataFrame({
            'Medida (cautelar/correctiva/estructural)': ['', '', ''],
            'Fundamento técnico-legal': ['', '', ''],
            'Plazo': ['', '', ''],
            'Observaciones': ['', '', '']
        })
    
    edited_medidas = st.data_editor(
        st.session_state.df_medidas,
        use_container_width=True,
        num_rows="dynamic",
        column_config={
            "Medida (cautelar/correctiva/estructural)": st.column_config.TextColumn(
                "Medida",
                help="Describa la medida propuesta",
                width="large"
            ),
            "Plazo": st.column_config.SelectboxColumn(
                "Plazo",
                options=["Inmediato", "15 días", "1 mes", "3 meses", "6 meses", "12 meses"],
            )
        }
    )
    
    st.session_state.df_medidas = edited_medidas
    
    st.markdown("---")
    
    st.subheader("💡 Ejemplos de medidas técnicas")
    
    tab1, tab2, tab3 = st.tabs(["🚨 Cautelares", "🔧 Correctivas", "🏗️ Estructurales"])
    
    with tab1:
        st.markdown("""
        ### Medidas Cautelares (inmediatas)
        
        **Objetivo:** Prevenir daño inminente o grave
        
        - **Limitación operativa temporal**
          - Reducir carga de operación al 70%
          - Plazo: Hasta implementar correctivas
        
        - **Incremento de monitoreo**
          - Monitoreo continuo 24/7
          - Reportes diarios a OEFA
        
        - **Retención de equipos**
          - Intervención de CEMS para auditoría
          - Verificación independiente
        """)
    
    with tab2:
        st.markdown("""
        ### Medidas Correctivas (corto-mediano plazo)
        
        **Objetivo:** Corregir la conducta infractora
        
        - **Optimización de procesos**
          - Ajuste de parámetros de combustión
          - Actualización de protocolos de arranque/parada
          - Plazo: 1-3 meses
        
        - **Mantenimiento intensivo**
          - Revisión completa de quemadores
          - Reparación de sistema de control
          - Plazo: 2 meses
        
        - **Capacitación de personal**
          - Operación eficiente de equipos
          - Manejo de situaciones críticas
          - Plazo: 1 mes
        """)
    
    with tab3:
        st.markdown("""
        ### Medidas Estructurales (largo plazo)
        
        **Objetivo:** Solución definitiva
        
        - **Instalación de sistema SCR**
          - Reducción Catalítica Selectiva para NOₓ
          - Eficiencia: >90%
          - Inversión: ~$2-5 millones
          - Plazo: 12-18 meses
        
        - **Sistema de desulfuración (FGD)**
          - Reducción de SO₂
          - Eficiencia: >95%
          - Inversión: ~$5-10 millones
          - Plazo: 18-24 meses
        
        - **Modernización integral**
          - Quemadores Low-NOₓ
          - Sistema de control automatizado
          - Plazo: 24 meses
        """)
    
    st.markdown("---")
    
    st.subheader("💰 Cálculo de sanción económica")
    
    col1, col2 = st.columns(2)
    
    with col1:
        gravedad = st.selectbox("Gravedad de la infracción:", 
                                ["Leve (I)", "Grave (II)", "Muy Grave (III)"])
        uit = st.number_input("Valor UIT actual (S/)", value=5150, step=50)
        
        if gravedad == "Leve (I)":
            multa_min, multa_max = 10, 100
        elif gravedad == "Grave (II)":
            multa_min, multa_max = 100, 500
        else:
            multa_min, multa_max = 500, 10000
        
        multa_uit = st.slider(f"Multa propuesta (UIT)", multa_min, multa_max, 
                              value=(multa_min + multa_max) // 2)
    
    with col2:
        st.markdown("### 💵 Resumen de sanción")
        multa_soles = multa_uit * uit
        st.metric("Multa en UIT", f"{multa_uit} UIT")
        st.metric("Multa en Soles", f"S/ {multa_soles:,.2f}")
        st.metric("Multa en USD", f"$ {multa_soles/3.8:,.2f}", 
                  help="Tipo de cambio referencial: S/ 3.80")

elif pagina == "🏛️ Audiencia":
    st.header("🏛️ Minuta de Audiencia (síntesis)")
    
    st.info("Resumen de los aspectos clave de la audiencia de fiscalización")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "⚖️ Posición Autoridad", 
        "🏭 Descargos Empresa", 
        "👨‍🔬 Informe Peritos",
        "📋 Acuerdos"
    ])
    
    with tab1:
        st.subheader("Posición de la autoridad/tribunal")
        posicion_autoridad = st.text_area(
            "Detalle la posición de OEFA o el tribunal:",
            height=200,
            placeholder="Ej: La OEFA sostiene que la empresa excedió los LMP de NOₓ en 3 ocasiones durante el trimestre evaluado..."
        )
        
        st.markdown("**Fundamentos principales:**")
        fund1 = st.text_input("Fundamento 1:", placeholder="Ej: Incumplimiento del D.S. 003-2010-MINAM")
        fund2 = st.text_input("Fundamento 2:", placeholder="Ej: Informes técnicos de laboratorio acreditado")
        fund3 = st.text_input("Fundamento 3:", placeholder="Ej: Reincidencia documentada")
    
    with tab2:
        st.subheader("Descargos del administrado/empresa")
        descargos = st.text_area(
            "Detalle los argumentos de defensa de la empresa:",
            height=200,
            placeholder="Ej: La empresa alega que las excedencias ocurrieron únicamente durante arranques programados..."
        )
        
        st.markdown("**Argumentos de defensa:**")
        arg1 = st.text_input("Argumento 1:", placeholder="Ej: Cumplimiento del plan de adecuación")
        arg2 = st.text_input("Argumento 2:", placeholder="Ej: Inversión en mejoras tecnológicas")
        arg3 = st.text_input("Argumento 3:", placeholder="Ej: Caso fortuito o fuerza mayor")
        
        st.markdown("**Pruebas presentadas:**")
        prueba1 = st.checkbox("Informes técnicos de consultores")
        prueba2 = st.checkbox("Bitácoras de operación")
        prueba3 = st.checkbox("Contratos de mejora tecnológica")
        prueba4 = st.checkbox("Testimonio de expertos")
    
    with tab3:
        st.subheader("Informe de peritos")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Perito designado:**")
            nombre_perito = st.text_input("Nombre del perito:")
            especialidad = st.text_input("Especialidad:")
            institucion = st.text_input("Institución:")
        
        with col2:
            st.markdown("**Conclusiones:**")
            conclusion_principal = st.text_area(
                "Conclusión principal del peritaje:",
                height=150
            )
        
        st.markdown("**Recomendaciones técnicas del perito:**")
        rec_peritos = st.text_area(
            "Recomendaciones:",
            height=100,
            placeholder="Ej: Instalación de sistema SCR en plazo de 12 meses..."
        )
    
    with tab4:
        st.subheader("Acuerdos/Decisión preliminar")
        
        decision_tipo = st.radio(
            "Tipo de decisión:",
            ["Sanción confirmada", "Sanción reducida", "Absolución", 
             "Suspensión del procedimiento", "Decisión pendiente"]
        )
        
        if decision_tipo in ["Sanción confirmada", "Sanción reducida"]:
            col1, col2 = st.columns(2)
            with col1:
                sancion_uit = st.number_input("Sanción (UIT):", min_value=0, max_value=10000)
            with col2:
                plazo_pago = st.number_input("Plazo de pago (días):", min_value=15, max_value=180, value=30)
        
        st.markdown("**Medidas ordenadas:**")
        medidas_ordenadas = st.text_area(
            "Detalle las medidas que debe cumplir la empresa:",
            height=150,
            placeholder="Ej: 1. Implementar sistema de monitoreo continuo\n2. Presentar plan de mejora en 30 días\n3..."
        )
        
        st.markdown("**Fecha de próxima audiencia o plazo de cumplimiento:**")
        proxima_fecha = st.date_input("Fecha:")
        
    st.markdown("---")
    
    if st.button("📄 Generar Resumen Ejecutivo"):
        st.success("✅ Resumen ejecutivo generado")
        
        st.markdown("### 📋 Resumen Ejecutivo de Audiencia")
        st.markdown(f"""
        **Fecha:** {datetime.now().strftime('%d/%m/%Y')}
        
        **Caso:** Central Termoeléctrica - Excedencia LMP NOₓ/SO₂
        
        **Posición Autoridad:**
        {posicion_autoridad if posicion_autoridad else 'No especificada'}
        
        **Descargos Empresa:**
        {descargos if descargos else 'No especificados'}
        
        **Decisión:**
        {decision_tipo}
        
        **Medidas Ordenadas:**
        {medidas_ordenadas if medidas_ordenadas else 'No especificadas'}
        """)

elif pagina == "🌐 Normativas":
    st.header("🌐 Normativas Internacionales de Calidad del Aire")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🇵🇪 OEFA Perú", "🌍 OMS", "🇺🇸 EPA", "🇨🇦 Canadá"])
    
    with tab1:
        st.subheader("🇵🇪 Normativa Peruana - OEFA")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            #### Marco Legal Principal
            
            **D.S. N° 003-2017-MINAM - ECA para Aire**
            - PM2.5: 25 μg/m³ (anual), 50 μg/m³ (24h)
            - PM10: 50 μg/m³ (anual), 100 μg/m³ (24h)
            - NO₂: 100 μg/m³ (anual), 200 μg/m³ (1h)
            - SO₂: 250 μg/m³ (24h)
            - O₃: 100 μg/m³ (8h)
            - CO: 10,000 μg/m³ (8h), 30,000 μg/m³ (1h)
            
            **D.S. N° 003-2010-MINAM - LMP Termoeléctricas**
            - NOₓ: 320-850 mg/Nm³ (según combustible)
            - SO₂: hasta 1700 mg/Nm³
            - PM: 50-150 mg/Nm³
            """)
        
        with col2:
            st.info("""
            **OEFA**
            
            Organismo de Evaluación y Fiscalización Ambiental
            
            - Supervisión
            - Fiscalización
            - Sanción
            - Incentivos
            """)
        
        st.markdown("---")
        
        st.markdown("#### 📋 ECA Aire Perú - Tabla Completa")
        
        eca_peru_completo = pd.DataFrame({
            'Contaminante': ['PM2.5', 'PM2.5', 'PM10', 'PM10', 'SO₂', 'NO₂', 'NO₂', 'O₃', 'CO', 'CO', 'Plomo (Pb)', 'Benceno'],
            'Período': ['24h', 'Anual', '24h', 'Anual', '24h', '1h', 'Anual', '8h', '8h', '1h', 'Anual', 'Anual'],
            'Valor ECA': [50, 25, 100, 50, 250, 200, 100, 100, 10000, 30000, 0.5, 2],
            'Unidad': ['μg/m³'] * 12,
            'Norma': ['D.S. 003-2017-MINAM'] * 12
        })
        
        st.dataframe(eca_peru_completo, use_container_width=True)
    
    with tab2:
        st.subheader("🌍 Directrices OMS - Organización Mundial de la Salud")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            #### OMS 2021 - Nuevas Directrices
            
            Las más estrictas a nivel mundial:
            
            - **PM2.5:** 5 μg/m³ (anual), 15 μg/m³ (24h)
            - **PM10:** 15 μg/m³ (anual), 45 μg/m³ (24h)
            - **NO₂:** 10 μg/m³ (anual), 25 μg/m³ (24h)
            - **SO₂:** 40 μg/m³ (24h)
            - **O₃:** 100 μg/m³ (temporada alta 8h)
            - **CO:** 4 mg/m³ (24h)
            
            **Objetivo:** Proteger la salud pública
            """)
        
        with col2:
            st.markdown("""
            #### OMS 2005 (anterior)
            
            Directrices previas:
            
            - **PM2.5:** 10 μg/m³ (anual), 25 μg/m³ (24h)
            - **PM10:** 20 μg/m³ (anual), 50 μg/m³ (24h)
            - **NO₂:** 40 μg/m³ (anual)
            - **SO₂:** 20 μg/m³ (24h)
            - **O₃:** 100 μg/m³ (8h)
            
            **Cambio:** Valores 2021 son más estrictos
            """)
        
        st.markdown("---")
        
        st.markdown("#### 📊 Comparación OMS 2005 vs 2021")
        
        oms_comparacion = pd.DataFrame({
            'Contaminante': ['PM2.5', 'PM2.5', 'PM10', 'PM10', 'NO₂', 'NO₂', 'SO₂', 'O₃'],
            'Período': ['Anual', '24h', 'Anual', '24h', 'Anual', '24h', '24h', '8h'],
            'OMS 2005 (μg/m³)': [10, 25, 20, 50, 40, 25, 20, 100],
            'OMS 2021 (μg/m³)': [5, 15, 15, 45, 10, 25, 40, 100],
            'Cambio (%)': ['-50%', '-40%', '-25%', '-10%', '-75%', '0%', '+100%', '0%']
        })
        
        st.dataframe(oms_comparacion, use_container_width=True)
        
        st.info("""
        **💡 Nota importante:** Las directrices de la OMS son **orientadoras**, no vinculantes. 
        Cada país establece sus propios estándares considerando su realidad económica, 
        tecnológica y sanitaria.
        """)
    
    with tab3:
        st.subheader("🇺🇸 EPA - Agencia de Protección Ambiental (USA)")
        
        st.markdown("""
        #### National Ambient Air Quality Standards (NAAQS)
        
        La EPA establece dos tipos de estándares:
        - **Primarios:** Protegen la salud pública
        - **Secundarios:** Protegen bienestar público (vegetación, visibilidad)
        """)
        
        epa_standards = pd.DataFrame({
            'Contaminante': ['PM2.5', 'PM2.5', 'PM10', 'O₃', 'SO₂', 'NO₂', 'NO₂', 'CO', 'CO', 'Pb'],
            'Período': ['24h', 'Anual', '24h', '8h', '1h', '1h', 'Anual', '8h', '1h', 'Trimestral'],
            'Estándar Primario': ['35 μg/m³', '9.0 μg/m³', '150 μg/m³', '0.070 ppm', '75 ppb', 
                                  '100 ppb', '53 ppb', '9 ppm', '35 ppm', '0.15 μg/m³'],
            'Última actualización': ['2024', '2024', '1987', '2015', '2010', 
                                     '2010', '2010', '1971', '1971', '2008']
        })
        
        st.dataframe(epa_standards, use_container_width=True)
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            #### 🔄 Última actualización 2024
            
            **PM2.5 anual:**
            - Anterior: 12 μg/m³
            - **Nuevo: 9.0 μg/m³** ✅
            - Cambio: -25%
            
            Más protector para:
            - Niños
            - Adultos mayores
            - Personas con asma
            """)
        
        with col2:
            st.markdown("""
            #### 📍 Implementación
            
            - Estados deben cumplir NAAQS
            - Planes estatales de implementación (SIP)
            - Zonas de no cumplimiento
            - Programa de permisos
            - Sanciones por incumplimiento
            """)
    
    with tab4:
        st.subheader("🇨🇦 Estándares Canadienses de Calidad del Aire")
        
        st.markdown("""
        #### Canadian Ambient Air Quality Standards (CAAQS)
        
        Sistema de gestión de calidad del aire basado en:
        - Estándares nacionales
        - Gestión por cuencas atmosféricas
        - Mejora continua
        """)
        
        canada_standards = pd.DataFrame({
            'Contaminante': ['PM2.5', 'PM2.5', 'O₃', 'NO₂', 'SO₂'],
            'Período': ['24h', 'Anual', '8h', '1h', '1h'],
            'Estándar 2020 (μg/m³)': [27, 8.8, 62, 60, 70],
            'Estándar 2025 (μg/m³)': [25, 8.0, 60, 50, 65],
            'Meta a futuro': ['progresivo', 'progresivo', 'progresivo', 'progresivo', 'progresivo']
        })
        
        st.dataframe(canada_standards, use_container_width=True)
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            #### 🎯 Gestión por Air Zones
            
            Canadá divide el territorio en "Air Zones":
            
            **Categorías:**
            - 🟢 Verde: Cumple estándares
            - 🟡 Amarillo: En gestión
            - 🟠 Naranja: Acciones requeridas
            - 🔴 Rojo: Intervención urgente
            """)
        
        with col2:
            st.markdown("""
            #### 📈 Mejora continua
            
            Características del sistema:
            - Estándares se actualizan cada 5 años
            - Progresivamente más estrictos
            - Basados en evidencia científica
            - Coordinación federal-provincial
            """)
        
        st.info("""
        **💡 Dato:** Canadá es reconocido por su enfoque de "gestión adaptativa" 
        de la calidad del aire, que combina estándares nacionales con flexibilidad regional.
        """)

elif pagina == "⏳ Línea Temporal":
    st.header("⏳ Línea de Tiempo de Cambios Normativos")
    
    st.info("Evolución histórica de las normativas de calidad del aire en diferentes jurisdicciones")
    
    # Gráfico interactivo
    fig = px.scatter(timeline_df, 
                     x='fecha', 
                     y='entidad',
                     color='entidad',
                     size_max=15,
                     hover_data={'evento': True, 'fecha': '|%Y-%m'},
                     title='Hitos clave en normativas de calidad del aire (2001-2024)',
                     labels={'fecha': 'Año', 'entidad': 'Organismo'},
                     color_discrete_map={
                         'OEFA': '#667eea',
                         'OMS': '#43a047',
                         'EPA': '#e53935',
                         'Canadá': '#ff6f00'
                     })
    
    fig.update_traces(marker=dict(size=12, line=dict(width=2, color='white')))
    fig.update_layout(height=500, hovermode='closest')
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    st.subheader("📅 Cronología detallada")
    
    # Filtros
    col1, col2 = st.columns([1, 3])
    
    with col1:
        filtro_entidad = st.multiselect(
            "Filtrar por organismo:",
            options=timeline_df['entidad'].unique(),
            default=timeline_df['entidad'].unique()
        )
    
    timeline_filtrado = timeline_df[timeline_df['entidad'].isin(filtro_entidad)]
    timeline_filtrado = timeline_filtrado.sort_values('fecha', ascending=False)
    
    # Mostrar eventos
    for idx, row in timeline_filtrado.iterrows():
        fecha_str = row['fecha'].strftime('%B %Y')
        
        if row['entidad'] == 'OEFA':
            emoji = "🇵🇪"
            color = "#667eea"
        elif row['entidad'] == 'OMS':
            emoji = "🌍"
            color = "#43a047"
        elif row['entidad'] == 'EPA':
            emoji = "🇺🇸"
            color = "#e53935"
        else:
            emoji = "🇨🇦"
            color = "#ff6f00"
        
        st.markdown(f"""
        <div style="border-left: 4px solid {color}; padding-left: 15px; margin-bottom: 20px;">
            <h4>{emoji} {fecha_str}</h4>
            <p><strong>{row['entidad']}</strong></p>
            <p>{row['evento']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("📊 Frecuencia de actualizaciones por organismo")
    
    actualizaciones_count = timeline_df.groupby('entidad').size().reset_index(name='Número de actualizaciones')
    
    fig2 = px.bar(actualizaciones_count, 
                  x='entidad', 
                  y='Número de actualizaciones',
                  color='entidad',
                  title='Cantidad de cambios normativos por organismo (2001-2024)',
                  color_discrete_map={
                      'OEFA': '#667eea',
                      'OMS': '#43a047',
                      'EPA': '#e53935',
                      'Canadá': '#ff6f00'
                  })
    
    st.plotly_chart(fig2, use_container_width=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        oefa_count = len(timeline_df[timeline_df['entidad'] == 'OEFA'])
        st.metric("🇵🇪 OEFA", f"{oefa_count} cambios", "Perú")
    
    with col2:
        oms_count = len(timeline_df[timeline_df['entidad'] == 'OMS'])
        st.metric("🌍 OMS", f"{oms_count} cambios", "Global")
    
    with col3:
        epa_count = len(timeline_df[timeline_df['entidad'] == 'EPA'])
        st.metric("🇺🇸 EPA", f"{epa_count} cambios", "USA")
    
    with col4:
        canada_count = len(timeline_df[timeline_df['entidad'] == 'Canadá'])
        st.metric("🇨🇦 Canadá", f"{canada_count} cambios", "Canadá")

elif pagina == "📋 Plan Adecuación":
    st.header("📋 Plan de Adecuación Ambiental")
    
    st.info("""
    El Plan de Adecuación y Manejo Ambiental (PAMA) es un instrumento de gestión que permite 
    a las empresas adecuarse gradualmente a los nuevos límites máximos permisibles.
    """)
    
    st.subheader("🎯 Objetivos del Plan de Adecuación")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### Objetivos generales
        
        - ✅ Cumplir con LMP vigentes
        - ✅ Reducir progresivamente emisiones
        - ✅ Implementar mejores tecnologías disponibles
        - ✅ Proteger salud pública y ambiente
        - ✅ Mantener operatividad económica
        """)
    
    with col2:
        st.markdown("""
        #### Marco legal
        
        - **Ley N° 28611** - Ley General del Ambiente
        - **D.S. N° 003-2010-MINAM** - LMP Termoeléctricas
        - **Resolución Ministerial específica**
        - **Plazos aprobados por OEFA**
        """)
    
    st.markdown("---")
    
    st.subheader("📅 Cronograma de Implementación")
    
    st.markdown("#### Ingrese las actividades del plan de adecuación:")
    
    if 'df_pama' not in st.session_state:
        st.session_state.df_pama = pd.DataFrame({
            'Actividad': [
                'Diagnóstico inicial y línea base',
                'Diseño de ingeniería sistema SCR',
                'Adquisición de equipos',
                'Instalación y montaje',
                'Pruebas y puesta en marcha',
                'Operación regular y monitoreo'
            ],
            'Responsable': ['', '', '', '', '', ''],
            'Fecha inicio': ['', '', '', '', '', ''],
            'Fecha fin': ['', '', '', '', '', ''],
            'Presupuesto (US$)': [0, 0, 0, 0, 0, 0],
            'Estado': ['Pendiente', 'Pendiente', 'Pendiente', 'Pendiente', 'Pendiente', 'Pendiente']
        })
    
    edited_pama = st.data_editor(
        st.session_state.df_pama,
        use_container_width=True,
        num_rows="dynamic",
        column_config={
            "Estado": st.column_config.SelectboxColumn(
                "Estado",
                options=["Pendiente", "En proceso", "Completado", "Retrasado"],
            ),
            "Presupuesto (US$)": st.column_config.NumberColumn(
                "Presupuesto (US$)",
                format="$%d"
            )
        }
    )
    
    st.session_state.df_pama = edited_pama
    
    st.markdown("---")
    
    st.subheader("💰 Análisis Financiero")
    
    total_presupuesto = st.session_state.df_pama['Presupuesto (US$)'].sum()
    completadas = len(st.session_state.df_pama[st.session_state.df_pama['Estado'] == 'Completado'])
    en_proceso = len(st.session_state.df_pama[st.session_state.df_pama['Estado'] == 'En proceso'])
    pendientes = len(st.session_state.df_pama[st.session_state.df_pama['Estado'] == 'Pendiente'])
    retrasadas = len(st.session_state.df_pama[st.session_state.df_pama['Estado'] == 'Retrasado'])
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("💵 Presupuesto Total", f"${total_presupuesto:,.0f}")
    with col2:
        st.metric("✅ Completadas", completadas)
    with col3:
        st.metric("🔄 En Proceso", en_proceso)
    with col4:
        st.metric("⏸️ Pendientes", pendientes)
    
    if retrasadas > 0:
        st.warning(f"⚠️ Atención: {retrasadas} actividad(es) retrasada(s)")
    
    st.markdown("---")
    
    st.subheader("📊 Indicadores de Avance")
    
    total_actividades = len(st.session_state.df_pama)
    porcentaje_avance = (completadas / total_actividades * 100) if total_actividades > 0 else 0
    
    st.progress(porcentaje_avance / 100)
    st.markdown(f"**Avance general: {porcentaje_avance:.1f}%**")
    
    st.markdown("---")
    
    st.subheader("🎯 Metas de Reducción de Emisiones")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### NOₓ (Óxidos de Nitrógeno)")
        nox_actual = st.number_input("Emisión actual (mg/Nm³):", value=850.0, key="nox_act")
        nox_meta = st.number_input("Meta LMP (mg/Nm³):", value=320.0, key="nox_meta")
        reduccion_nox = ((nox_actual - nox_meta) / nox_actual * 100)
        st.metric("Reducción requerida", f"{reduccion_nox:.1f}%")
        
        if reduccion_nox > 0:
            st.success(f"Meta: Reducir {nox_actual - nox_meta:.0f} mg/Nm³")
        else:
            st.success("✅ Ya cumple con el LMP")
    
    with col2:
        st.markdown("#### SO₂ (Dióxido de Azufre)")
        so2_actual = st.number_input("Emisión actual (mg/Nm³):", value=1700.0, key="so2_act")
        so2_meta = st.number_input("Meta LMP (mg/Nm³):", value=500.0, key="so2_meta")
        reduccion_so2 = ((so2_actual - so2_meta) / so2_actual * 100)
        st.metric("Reducción requerida", f"{reduccion_so2:.1f}%")
        
        if reduccion_so2 > 0:
            st.success(f"Meta: Reducir {so2_actual - so2_meta:.0f} mg/Nm³")
        else:
            st.success("✅ Ya cumple con el LMP")
    
    st.markdown("---")
    
    st.subheader("📝 Compromisos y Garantías")
    
    st.markdown("""
    #### Compromisos de la empresa:
    """)
    
    comp1 = st.checkbox("Cumplir con el cronograma aprobado")
    comp2 = st.checkbox("Reportar avances trimestrales a OEFA")
    comp3 = st.checkbox("Mantener monitoreo continuo (CEMS)")
    comp4 = st.checkbox("No superar línea base durante implementación")
    comp5 = st.checkbox("Implementar mejores tecnologías disponibles (BAT)")
    
    st.markdown("""
    #### Garantías requeridas:
    """)
    
    garantia_monto = st.number_input("Monto de garantía (% del presupuesto):", 
                                     min_value=0, max_value=100, value=10)
    garantia_valor = total_presupuesto * (garantia_monto / 100)
    
    st.info(f"💰 Garantía requerida: ${garantia_valor:,.2f}")
    
    tipo_garantia = st.selectbox(
        "Tipo de garantía:",
        ["Carta fianza bancaria", "Póliza de caución", "Depósito en garantía", "Hipoteca"]
    )
    
    st.success(f"✅ Tipo seleccionado: {tipo_garantia}")

elif pagina == "📚 Recursos":
    st.header("📚 Recursos y Enlaces Oficiales")
    
    st.info("Acceda a normativas, guías técnicas y contactos de las autoridades ambientales")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🇵🇪 Perú - OEFA",
        "🌍 OMS",
        "🇺🇸 EPA",
        "🇨🇦 Canadá",
        "📖 Guías Técnicas"
    ])
    
    with tab1:
        st.subheader("🇵🇪 OEFA - Perú")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            #### Enlaces oficiales
            
            - 🌐 [Portal OEFA](https://www.oefa.gob.pe/)
            - 📋 [Sistema de Información Ambiental](https://www.oefa.gob.pe/fiscalizacion-ambiental/)
            - 📊 [Reportes de fiscalización](https://www.oefa.gob.pe/fiscalizacion-ambiental/reportes/)
            - ⚖️ [Tribunal de Fiscalización Ambiental](https://www.oefa.gob.pe/tribunal/)
            - 📖 [Normativa ambiental](https://www.oefa.gob.pe/normativa/)
            """)
            
            st.markdown("""
            #### Contacto
            
            - 📞 Central telefónica: **(01) 717-6000**
            - 📧 Email: contacto@oefa.gob.pe
            - 📍 Dirección: Av. Faustino Sánchez Carrión 603, Jesús María, Lima
            - 🕒 Atención: Lunes a Viernes 8:30 - 17:00
            """)
        
        with col2:
            st.markdown("""
            #### Documentos clave
            
            **Normativa vigente:**
            - D.S. N° 003-2017-MINAM (ECA Aire)
            - D.S. N° 003-2010-MINAM (LMP Termoeléctricas)
            - D.S. N° 010-2019-MINAM (Modificatoria ECA)
            - Ley N° 28611 (Ley General del Ambiente)
            - Ley N° 29325 (Ley del SINEFA)
            
            **Guías y protocolos:**
            - Protocolo de monitoreo de calidad de aire
            - Guía de elaboración de PAMA
            - Manual de fiscalización ambiental
            """)
            
            st.info("""
            **💡 Línea Verde OEFA**
            
            Para denuncias ambientales:
            - 📞 0800-00-668 (gratuito)
            - 📱 WhatsApp: 988-234-316
            """)
    
    with tab2:
        st.subheader("🌍 OMS - Organización Mundial de la Salud")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            #### Enlaces oficiales
            
            - 🌐 [Portal OMS](https://www.who.int/)
            - 🌫️ [Calidad del aire](https://www.who.int/health-topics/air-pollution)
            - 📊 [Base de datos global](https://www.who.int/data/gho/data/themes/air-pollution)
            - 📖 [Directrices 2021](https://www.who.int/news-room/feature-stories/detail/what-are-the-who-air-quality-guidelines)
            """)
            
            st.markdown("""
            #### Publicaciones principales
            
            - **WHO Air Quality Guidelines (2021)**
            - Global air quality guidelines
            - Health risk assessment
            - Regional reports
            - Country profiles
            """)
        
        with col2:
            st.markdown("""
            #### Datos y estadísticas
            
            **Impacto global:**
            - 💀 7 millones de muertes prematuras/año
            - 🌍 99% población respira aire contaminado
            - 🏭 91% población en áreas que exceden directrices
            - 💰 $5 trillones en costos anuales
            
            **Principales contaminantes:**
            1. Material particulado (PM2.5, PM10)
            2. Ozono (O₃)
            3. Dióxido de nitrógeno (NO₂)
            4. Dióxido de azufre (SO₂)
            5. Monóxido de carbono (CO)
            """)
    
    with tab3:
        st.subheader("🇺🇸 EPA - Agencia de Protección Ambiental (USA)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            #### Enlaces oficiales
            
            - 🌐 [Portal EPA](https://www.epa.gov/)
            - 🌫️ [Air Quality](https://www.epa.gov/air-quality)
            - 📊 [AirNow - Tiempo real](https://www.airnow.gov/)
            - 📖 [NAAQS Standards](https://www.epa.gov/criteria-air-pollutants/naaqs-table)
            - 🔬 [Métodos de medición](https://www.epa.gov/air-research)
            """)
            
            st.markdown("""
            #### Programas principales
            
            - **Clean Air Act**
            - State Implementation Plans (SIP)
            - New Source Performance Standards (NSPS)
            - National Emission Standards (NESHAP)
            - Air Quality Index (AQI)
            """)
        
        with col2:
            st.markdown("""
            #### Herramientas técnicas
            
            **Software y modelos:**
            - AERMOD (modelamiento dispersión)
            - AP-42 (factores de emisión)
            - WebFIRE (base de datos emisiones)
            - CEMS (monitoreo continuo)
            
            **Métodos de referencia:**
            - EPA Method 3A (O₂, CO₂)
            - EPA Method 7E (NOₓ)
            - EPA Method 6C (SO₂)
            - EPA Method 5 (PM)
            """)
            
            st.success("""
            **📱 App AirNow**
            
            Descarga la app para monitoreo en tiempo real de calidad del aire
            - iOS / Android disponible
            - Alertas personalizadas
            - Índice de calidad (AQI)
            """)
    
    with tab4:
        st.subheader("🇨🇦 Canadá - Environment and Climate Change Canada")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            #### Enlaces oficiales
            
            - 🌐 [Portal ECCC](https://www.canada.ca/en/environment-climate-change.html)
            - 🌫️ [Air Quality](https://www.canada.ca/en/environment-climate-change/services/air-quality.html)
            - 📊 [CAAQS](https://www.ccme.ca/en/air-quality)
            - 📖 [Air Quality Health Index](https://weather.gc.ca/airquality/pages/index_e.html)
            """)
            
            st.markdown("""
            #### Sistema CAAQS
            
            **Canadian Ambient Air Quality Standards:**
            - Gestión por Air Zones
            - Mejora continua
            - Actualización cada 5 años
            - Coordinación federal-provincial
            - Basado en salud y factibilidad
            """)
        
        with col2:
            st.markdown("""
            #### Air Quality Management System
            
            **Componentes clave:**
            1. Standards (CAAQS)
            2. Air Zone Management
            3. Base/Target Level
            4. Transboundary considerations
            5. Mobile source emissions
            
            **Clasificación Air Zones:**
            - 🟢 Verde (Achievement)
            - 🟡 Amarillo (Management)
            - 🟠 Naranja (Action)
            - 🔴 Rojo (Critical)
            """)
            
            st.info("""
            **🔬 Innovación canadiense**
            
            Canadá es líder en:
            - Monitoreo satelital
            - Modelamiento de calidad del aire
            - Gestión de incendios forestales
            - Políticas de transporte limpio
            """)
    
    with tab5:
        st.subheader("📖 Guías Técnicas y Metodologías")
        
        st.markdown("#### 🔬 Métodos de monitoreo")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            **Monitoreo continuo (CEMS)**
            
            - Sistemas automáticos
            - Medición en tiempo real
            - Transmisión de datos
            - Calibración periódica
            - Cumplimiento normativo
            
            **Ventajas:**
            ✅ Datos continuos
            ✅ Detección inmediata
            ✅ Menor manipulación
            """)
        
        with col2:
            st.markdown("""
            **Método isocinético**
            
            - Muestreo puntual
            - Medición de flujo
            - Representativo
            - Análisis laboratorio
            - Certificado acreditado
            
            **Aplicaciones:**
            ✅ Verificación CEMS
            ✅ Baseline studies
            ✅ Auditorías
            """)
        
        with col3:
            st.markdown("""
            **Métodos pasivos**
            
            - Difusión molecular
            - Bajo costo
            - Sin energía
            - Promedio temporal
            - Screening inicial
            
            **Ideal para:**
            ✅ Redes amplias
            ✅ Zonas remotas
            ✅ Estudios preliminares
            """)
        
        st.markdown("---")
        
        st.markdown("#### 📐 Protocolos de muestreo")
        
        protocolos = pd.DataFrame({
            'Parámetro': ['PM10', 'PM2.5', 'NO₂', 'SO₂', 'O₃', 'CO'],
            'Método EPA': ['EPA-10', 'EPA-10', 'EPA-7E', 'EPA-6C', 'EPA-10A', 'EPA-3A'],
            'Método ISO': ['ISO 9096', 'ISO 9096', 'ISO 10849', 'ISO 7935', 'ISO 10313', 'ISO 12039'],
            'Frecuencia mínima': ['24h c/6 días', '24h c/3 días', 'Continuo', 'Continuo', 'Continuo', 'Continuo'],
            'Laboratorio': ['Acreditado ISO 17025'] * 6
        })
        
        st.dataframe(protocolos, use_container_width=True)
        
        st.markdown("---")
        
        st.markdown("#### 📚 Bibliografía recomendada")
        
        with st.expander("📖 Libros y manuales"):
            st.markdown("""
            1. **Air Pollution Control Engineering** - Noel de Nevers
            2. **Atmospheric Chemistry and Physics** - John H. Seinfeld
            3. **Manual de Contaminación Atmosférica** - Christian Seigneur
            4. **Air Quality** - Thad Godish
            5. **Fundamentals of Air Pollution** - Daniel Vallero
            """)
        
        with st.expander("🔬 Artículos científicos clave"):
            st.markdown("""
            - WHO Global Air Quality Guidelines (2021)
            - Health effects of air pollution - Lancet Commission
            - IPCC Reports on Air Quality and Climate
            - Regional air pollution studies
            - Technology assessments for emission control
            """)
        
        with st.expander("⚖️ Legislación comparada"):
            st.markdown("""
            **Jurisdicciones de referencia:**
            - 🇪🇺 Unión Europea (Directivas de calidad del aire)
            - 🇨🇱 Chile (D.S. 12/2011 - Normas primarias)
            - 🇲🇽 México (NOM-020-SSA1-2014)
            - 🇨🇴 Colombia (Resolución 2254/2017)
            - 🇦🇷 Argentina (Ley 20.284)
            """)

st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 20px; background: rgba(255,255,255,0.1); border-radius: 10px;'>
    <h3>⚖️ Clínica Jurídica-Ambiental</h3>
    <p><strong>Universidad Nacional de Moquegua</strong></p>
    <p>Facultad de Ingeniería y Arquitectura</p>
    <p>Escuela Profesional de Ingeniería Ambiental</p>
    <p style='margin-top: 15px;'>Curso: Contaminación y Control Atmosférico</p>
    <p>Docente: Prof. Dr. José Antonio Valeriano Zapana</p>
    <p style='margin-top: 15px; font-size: 0.9em;'>© 2024-2025 - Sistema de análisis jurídico-ambiental</p>
    <p style='font-size: 0.85em;'>Información basada en normativas oficiales de OEFA, OMS, EPA y Canadá</p>
</div>
""", unsafe_allow_html=True)
