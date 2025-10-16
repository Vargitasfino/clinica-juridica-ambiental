import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Configuración
st.set_page_config(
    page_title="Marco Normativo del Aire - Perú",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS Simple y Profesional
st.markdown("""
<style>
    [data-testid="stSidebar"] {display: none;}
    .main {background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);}
    .stApp {background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);}
    
    .logo-container {
        position: fixed;
        top: 20px;
        right: 30px;
        z-index: 1000;
        background: white;
        padding: 10px;
        border-radius: 12px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.3);
    }
    
    .logo-container img {
        width: 80px;
        height: 80px;
        object-fit: contain;
    }
    
    .content-box {
        background: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
        margin: 15px 0;
    }
    
    .header-box {
        text-align: center;
        padding: 50px 20px;
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        margin-bottom: 30px;
        border: 2px solid rgba(255,255,255,0.3);
    }
    
    h1 {
        color: white !important; 
        text-shadow: 3px 3px 8px rgba(0,0,0,0.4);
        font-size: 3em !important;
    }
    
    h2, h3 {
        color: white !important; 
        text-shadow: 2px 2px 6px rgba(0,0,0,0.3);
    }
    
    .normativa-card {
        background: white;
        padding: 25px;
        border-radius: 12px;
        margin: 15px 0;
        border-left: 6px solid #3b82f6;
        transition: all 0.3s;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .normativa-card:hover {
        transform: translateX(10px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
        border-left-color: #1e3a8a;
    }
    
    .enlace-btn {
        background: linear-gradient(135deg, #3b82f6 0%, #1e3a8a 100%);
        color: white;
        padding: 12px 25px;
        border-radius: 8px;
        text-decoration: none;
        display: inline-block;
        margin: 5px;
        transition: all 0.3s;
        font-weight: bold;
    }
    
    .enlace-btn:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 20px rgba(59, 130, 246, 0.5);
    }
    
    .categoria-badge {
        background: #ef4444;
        color: white;
        padding: 5px 15px;
        border-radius: 20px;
        font-size: 0.85em;
        font-weight: bold;
        display: inline-block;
        margin-right: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Estado
if 'pagina' not in st.session_state:
    st.session_state.pagina = "Inicio"

# HEADER
st.markdown("""
<div class='header-box'>
    <h1>🌍 Marco Normativo de Calidad del Aire</h1>
    <p style='color: white; font-size: 1.3em; margin-top: 15px;'>
        Herramienta de Consulta - Normativas Peruanas e Internacionales
    </p>
    <p style='color: rgba(255,255,255,0.8); margin-top: 10px;'>
        Universidad Nacional de Moquegua | Prof. Dr. José Antonio Valeriano Zapana
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
    if st.button("🌍 NORMATIVAS", use_container_width=True):
        st.session_state.pagina = "Normativas"

st.markdown("---")

# ===================== PÁGINA INICIO =====================
if st.session_state.pagina == "Inicio":
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='content-box'>
            <h2 style='color: #1e3a8a !important; text-shadow: none;'>📚 Sobre esta Herramienta</h2>
            <p style='color: #333; font-size: 1.1em; line-height: 1.8;'>
                Esta plataforma reúne el <strong>marco normativo completo sobre calidad del aire</strong> 
                en Perú y el mundo, incluyendo:
            </p>
            <ul style='color: #555; font-size: 1.05em; line-height: 2;'>
                <li>✅ <strong>ECA:</strong> Estándares de Calidad Ambiental</li>
                <li>✅ <strong>LMP:</strong> Límites Máximos Permisibles</li>
                <li>✅ <strong>Protocolos:</strong> De monitoreo y medición</li>
                <li>✅ <strong>Lineamientos:</strong> Técnicos y operativos</li>
                <li>✅ <strong>Medidas de Control:</strong> Para emisiones</li>
                <li>✅ <strong>Normativas Internacionales:</strong> OMS, EPA, Canadá</li>
            </ul>
            <p style='color: #666; margin-top: 20px;'>
                Cada sección incluye <strong>enlaces directos a documentos oficiales</strong>.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='content-box'>
            <h2 style='color: #1e3a8a !important; text-shadow: none;'>🎯 Acceso Rápido</h2>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("📋 Estándares de Calidad Ambiental (ECA)", use_container_width=True):
            st.session_state.pagina = "ECA"
        
        if st.button("🏭 Límites Máximos Permisibles (LMP)", use_container_width=True):
            st.session_state.pagina = "LMP"
        
        if st.button("📖 Protocolos de Monitoreo", use_container_width=True):
            st.session_state.pagina = "Protocolo"
        
        if st.button("📐 Lineamientos Técnicos", use_container_width=True):
            st.session_state.pagina = "Lineamiento"
        
        if st.button("🛡️ Medidas de Control de Emisiones", use_container_width=True):
            st.session_state.pagina = "Medidas"
        
        if st.button("🌍 Normativas Internacionales (OMS, EPA, Canadá)", use_container_width=True):
            st.session_state.pagina = "Normativas"
    
    # Gráfico comparativo inicial
    st.markdown("""
    <div class='content-box'>
        <h2 style='color: #1e3a8a !important; text-shadow: none;'>📊 Comparación PM2.5 - Estándares Anuales</h2>
    </div>
    """, unsafe_allow_html=True)
    
    datos_comp = pd.DataFrame([
        {'Entidad': 'OMS 2021', 'Valor': 5},
        {'Entidad': 'EPA USA', 'Valor': 9},
        {'Entidad': 'Canadá', 'Valor': 8.8},
        {'Entidad': 'OEFA Perú', 'Valor': 25}
    ])
    
    fig = px.bar(datos_comp, x='Entidad', y='Valor', 
                 color='Valor', color_continuous_scale='RdYlGn_r',
                 title='PM2.5 Anual (μg/m³) - Comparación Internacional',
                 text='Valor')
    fig.update_traces(texttemplate='%{text} μg/m³', textposition='outside')
    fig.update_layout(height=450, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

# ===================== PÁGINA ECA =====================
elif st.session_state.pagina == "ECA":
    st.markdown("<h1>📋 Estándares de Calidad Ambiental (ECA) para Aire</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='content-box'>
        <h2 style='color: #1e3a8a !important; text-shadow: none;'>📜 Marco Legal Principal</h2>
        <p style='color: #333; font-size: 1.1em;'>
            Los ECA son <strong>estándares de calidad del aire ambiente</strong> que se miden en 
            estaciones de monitoreo y protegen la salud de la población.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Normativas ECA con enlaces
    st.markdown("""
    <div class='normativa-card'>
        <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
            <span class='categoria-badge'>VIGENTE</span>
            D.S. N° 003-2017-MINAM
        </h3>
        <p style='color: #555; margin: 15px 0;'>
            <strong>Estándares de Calidad Ambiental (ECA) para Aire</strong><br>
            Establece los valores de concentración de contaminantes del aire que no deben superarse 
            para proteger la salud de las personas.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2017/06/DS-003-2017-MINAM.pdf' 
           target='_blank' class='enlace-btn'>
            📄 Descargar D.S. 003-2017-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normativa-card'>
        <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
            <span class='categoria-badge'>MODIFICATORIA</span>
            D.S. N° 010-2019-MINAM
        </h3>
        <p style='color: #555; margin: 15px 0;'>
            <strong>Modificatoria de ECA para Aire</strong><br>
            Actualiza algunos parámetros y períodos de evaluación de los estándares de calidad del aire.
        </p>
        <a href='https://busquedas.elperuano.pe/download/url/decreto-supremo-que-modifica-el-decreto-supremo-n-003-2017-decreto-supremo-n-010-2019-minam-1792823-1' 
           target='_blank' class='enlace-btn'>
            📄 Descargar D.S. 010-2019-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normativa-card'>
        <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
            <span class='categoria-badge' style='background: #6b7280;'>ANTERIOR</span>
            D.S. N° 074-2001-PCM
        </h3>
        <p style='color: #555; margin: 15px 0;'>
            <strong>Reglamento de Estándares Nacionales de Calidad Ambiental del Aire (Primera versión)</strong><br>
            Norma original de ECA para Aire en Perú, derogada por el D.S. 003-2017-MINAM.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_074-2001-pcm.pdf' 
           target='_blank' class='enlace-btn'>
            📄 Ver D.S. 074-2001-PCM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Tabla de valores ECA
    st.markdown("""
    <div class='content-box'>
        <h2 style='color: #1e3a8a !important; text-shadow: none;'>📊 Valores de ECA Vigentes</h2>
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
    
    st.dataframe(eca_valores, use_container_width=True, hide_index=True, height=420)

# ===================== PÁGINA LMP =====================
elif st.session_state.pagina == "LMP":
    st.markdown("<h1>🏭 Límites Máximos Permisibles (LMP) para Aire</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='content-box'>
        <h2 style='color: #1e3a8a !important; text-shadow: none;'>📜 ¿Qué son los LMP?</h2>
        <p style='color: #333; font-size: 1.1em;'>
            Los LMP son <strong>límites de emisión en la fuente (chimeneas)</strong> que regulan 
            la concentración de contaminantes que puede emitir una actividad productiva específica.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # LMP Termoeléctricas
    st.markdown("""
    <div class='normativa-card'>
        <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
            <span class='categoria-badge'>VIGENTE</span>
            D.S. N° 003-2010-MINAM
        </h3>
        <p style='color: #555; margin: 15px 0;'>
            <strong>LMP de emisiones atmosféricas para actividades de generación termoeléctrica</strong><br>
            Establece límites para NOx, SO2 y Material Particulado en centrales termoeléctricas.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_003-2010-minam.pdf' 
           target='_blank' class='enlace-btn'>
            📄 Descargar D.S. 003-2010-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normativa-card'>
        <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
            <span class='categoria-badge'>VIGENTE</span>
            D.S. N° 011-2009-MINAM
        </h3>
        <p style='color: #555; margin: 15px 0;'>
            <strong>LMP de emisiones de vehículos automotores</strong><br>
            Regula las emisiones de gases contaminantes de vehículos automotores nuevos y usados.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_011-2009-minam.pdf' 
           target='_blank' class='enlace-btn'>
            📄 Descargar D.S. 011-2009-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normativa-card'>
        <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
            <span class='categoria-badge'>VIGENTE</span>
            D.S. N° 010-2010-MINAM
        </h3>
        <p style='color: #555; margin: 15px 0;'>
            <strong>LMP de emisiones atmosféricas para minería metalúrgica y no metálica</strong><br>
            Establece límites para la actividad minera en operaciones de procesamiento.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_010-2010-minam.pdf' 
           target='_blank' class='enlace-btn'>
            📄 Descargar D.S. 010-2010-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Tabla LMP Termoeléctricas
    st.markdown("""
    <div class='content-box'>
        <h2 style='color: #1e3a8a !important; text-shadow: none;'>📊 LMP Centrales Termoeléctricas (D.S. 003-2010-MINAM)</h2>
        <p style='color: #666;'>Valores en condiciones estándar: 25°C, 1 atm, base seca, 15% O2</p>
    </div>
    """, unsafe_allow_html=True)
    
    lmp_termo = pd.DataFrame([
        ['NOx', 320, 850, 2000, 'mg/Nm³'],
        ['SO2', 'N/A', 1700, 3500, 'mg/Nm³'],
        ['Material Particulado', 50, 150, 350, 'mg/Nm³']
    ], columns=['Contaminante', 'Gas Natural', 'Diesel', 'Residual', 'Unidad'])
    
    st.dataframe(lmp_termo, use_container_width=True, hide_index=True)

# ===================== PÁGINA PROTOCOLO =====================
elif st.session_state.pagina == "Protocolo":
    st.markdown("<h1>📖 Protocolos de Monitoreo de Calidad del Aire</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='content-box'>
        <h2 style='color: #1e3a8a !important; text-shadow: none;'>📜 ¿Qué son los Protocolos?</h2>
        <p style='color: #333; font-size: 1.1em;'>
            Los protocolos establecen los <strong>procedimientos estandarizados</strong> para el 
            monitoreo de la calidad del aire y medición de emisiones.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Protocolos
    st.markdown("""
    <div class='normativa-card'>
        <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
            <span class='categoria-badge'>VIGENTE</span>
            R.D. N° 1404-2005/DIGESA/SA
        </h3>
        <p style='color: #555; margin: 15px 0;'>
            <strong>Protocolo de Monitoreo de Calidad del Aire y Gestión de Datos</strong><br>
            Define los procedimientos para el monitoreo de calidad del aire ambiente en el territorio nacional.
        </p>
        <a href='http://www.digesa.minsa.gob.pe/DEPA/protocolo_calidad_aire.pdf' 
           target='_blank' class='enlace-btn'>
            📄 Descargar Protocolo DIGESA
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normativa-card'>
        <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
            <span class='categoria-badge'>VIGENTE</span>
            R.M. N° 026-2000-ITINCI/DM
        </h3>
        <p style='color: #555; margin: 15px 0;'>
            <strong>Protocolo de Monitoreo de Calidad de Aire y Emisiones</strong><br>
            Aprueba los protocolos de monitoreo de calidad de aire y emisiones para el sector industrial.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2017/04/RM-026-2000-ITINCI.pdf' 
           target='_blank' class='enlace-btn'>
            📄 Ver Protocolo PRODUCE
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normativa-card'>
        <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
            <span class='categoria-badge'>VIGENTE</span>
            R.D. N° 195-2010-MEM/AAM
        </h3>
        <p style='color: #555; margin: 15px 0;'>
            <strong>Protocolo para el Monitoreo de Emisiones de Calderos y Hornos</strong><br>
            Establece los procedimientos para el monitoreo de emisiones atmosféricas en calderos y hornos.
        </p>
        <a href='http://www.minem.gob.pe/minem/archivos/RD%20195-2010-AAM.pdf' 
           target='_blank' class='enlace-btn'>
            📄 Descargar Protocolo MEM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Métodos de referencia
    st.markdown("""
    <div class='content-box'>
        <h2 style='color: #1e3a8a !important; text-shadow: none;'>🔬 Métodos de Referencia EPA</h2>
        <p style='color: #555;'>Métodos de la Agencia de Protección Ambiental de EE.UU. adoptados en Perú</p>
    </div>
    """, unsafe_allow_html=True)
    
    metodos_epa = pd.DataFrame([
        ['PM10', 'EPA Method 40 CFR Part 50, Appendix J', 'Gravimétrico'],
        ['PM2.5', 'EPA Method 40 CFR Part 50, Appendix L', 'Gravimétrico'],
        ['SO2', 'EPA Method 40 CFR Part 50, Appendix A-1', 'Fluorescencia UV'],
        ['NO2', 'EPA Method 40 CFR Part 50, Appendix F', 'Quimioluminiscencia'],
        ['CO', 'EPA Method 40 CFR Part 50, Appendix C', 'Infrarrojo no dispersivo'],
        ['O3', 'EPA Method 40 CFR Part 50, Appendix D', 'Fotometría UV']
    ], columns=['Contaminante', 'Método EPA', 'Técnica'])
    
    st.dataframe(metodos_epa, use_container_width=True, hide_index=True)

# ===================== PÁGINA LINEAMIENTO =====================
elif st.session_state.pagina == "Lineamiento":
    st.markdown("<h1>📐 Lineamientos Técnicos para Calidad del Aire</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='content-box'>
        <h2 style='color: #1e3a8a !important; text-shadow: none;'>📜 ¿Qué son los Lineamientos?</h2>
        <p style='color: #333; font-size: 1.1em;'>
            Los lineamientos son <strong>guías técnicas y operativas</strong> que complementan 
            la normativa legal y orientan su implementación práctica.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normativa-card'>
        <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
            <span class='categoria-badge'>VIGENTE</span>
            R.M. N° 181-2016-MINAM
        </h3>
        <p style='color: #555; margin: 15px 0;'>
            <strong>Lineamientos para la elaboración del Inventario de Emisiones Atmosféricas</strong><br>
            Establece la metodología para elaborar inventarios de emisiones de contaminantes del aire.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2016/07/RM-N%C2%B0-181-2016-MINAM.pdf' 
           target='_blank' class='enlace-btn'>
            📄 Descargar R.M. 181-2016-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normativa-card'>
        <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
            <span class='categoria-badge'>VIGENTE</span>
            D.S. N° 009-2003-SA
        </h3>
        <p style='color: #555; margin: 15px 0;'>
            <strong>Reglamento de los Niveles de Estados de Alerta Nacionales para Contaminantes del Aire</strong><br>
            Define los niveles de alerta y las acciones correspondientes ante episodios de contaminación.
        </p>
        <a href='http://www.digesa.minsa.gob.pe/NormasLegales/Normas/DS_009-2003-SA.pdf' 
           target='_blank' class='enlace-btn'>
            📄 Descargar D.S. 009-2003-SA
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normativa-card'>
        <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
            <span class='categoria-badge'>VIGENTE</span>
            Decreto Legislativo N° 1278
        </h3>
        <p style='color: #555; margin: 15px 0;'>
            <strong>Ley de Gestión Integral de Residuos Sólidos (Emisiones de Incineración)</strong><br>
            Establece lineamientos para el control de emisiones atmosféricas de plantas de tratamiento de residuos.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2017/04/Decreto-Legislativo-N%C2%B0-1278.pdf' 
           target='_blank' class='enlace-btn'>
            📄 Ver DL 1278
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Niveles de Alerta
    st.markdown("""
    <div class='content-box'>
        <h2 style='color: #1e3a8a !important; text-shadow: none;'>⚠️ Niveles de Estados de Alerta (D.S. 009-2003-SA)</h2>
    </div>
    """, unsafe_allow_html=True)
    
    niveles_alerta = pd.DataFrame([
        ['PM10', 'Cuidado', 250, 'μg/m³', 'Información a población sensible'],
        ['PM10', 'Peligro', 350, 'μg/m³', 'Alerta a toda la población'],
        ['PM10', 'Emergencia', 420, 'μg/m³', 'Emergencia sanitaria'],
        ['SO2', 'Cuidado', 500, 'μg/m³', 'Información a población sensible'],
        ['SO2', 'Peligro', 1000, 'μg/m³', 'Alerta a toda la población'],
        ['SO2', 'Emergencia', 1600, 'μg/m³', 'Emergencia sanitaria'],
        ['NO2', 'Cuidado', 600, 'μg/m³', 'Información a población sensible'],
        ['NO2', 'Peligro', 1200, 'μg/m³', 'Alerta a toda la población'],
        ['NO2', 'Emergencia', 1600, 'μg/m³', 'Emergencia sanitaria']
    ], columns=['Contaminante', 'Estado', 'Concentración', 'Unidad', 'Acción'])
    
    st.dataframe(niveles_alerta, use_container_width=True, hide_index=True, height=380)

# ===================== PÁGINA MEDIDAS DE CONTROL =====================
elif st.session_state.pagina == "Medidas":
    st.markdown("<h1>🛡️ Medidas de Control de Emisiones Atmosféricas</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='content-box'>
        <h2 style='color: #1e3a8a !important; text-shadow: none;'>📜 Marco Normativo de Control</h2>
        <p style='color: #333; font-size: 1.1em;'>
            Las medidas de control son <strong>tecnologías y prácticas</strong> para reducir 
            emisiones de contaminantes atmosféricos en la fuente.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normativa-card'>
        <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
            <span class='categoria-badge'>VIGENTE</span>
            Ley N° 28611 - Ley General del Ambiente
        </h3>
        <p style='color: #555; margin: 15px 0;'>
            <strong>Prevención, Control y Remediación Ambiental (Título II, Capítulo 3)</strong><br>
            Establece la obligación de implementar medidas de prevención y control de la contaminación del aire.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2017/04/Ley-N%C2%B0-28611.pdf' 
           target='_blank' class='enlace-btn'>
            📄 Ver Ley 28611
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normativa-card'>
        <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
            <span class='categoria-badge'>VIGENTE</span>
            D.S. N° 012-2005-EM
        </h3>
        <p style='color: #555; margin: 15px 0;'>
            <strong>Plan de Cierre de Minas - Control de emisiones</strong><br>
            Incluye obligaciones de control de emisiones atmosféricas durante operación y cierre de minas.
        </p>
        <a href='http://www.minem.gob.pe/minem/archivos/file/Mineria/LEGISLACION/2005/agosto/DS012-2005.pdf' 
           target='_blank' class='enlace-btn'>
            📄 Ver D.S. 012-2005-EM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # NTP relacionadas
    st.markdown("""
    <div class='normativa-card'>
        <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
            <span class='categoria-badge' style='background: #f97316;'>NTP</span>
            Normas Técnicas Peruanas - Medición y Control
        </h3>
        <p style='color: #555; margin: 15px 0;'>
            <strong>NTP 900.058:2019</strong> - Gestión Ambiental. Aire. Calidad del aire. Métodos de muestreo<br>
            <strong>NTP 900.030:2003</strong> - Gestión Ambiental. Aire. Terminología
        </p>
        <a href='https://www.inacal.gob.pe/repositorioaps/data/1/1/1/jer/ctnprocedimiento/files/Catalogo_NTP_Vigentes_2023.pdf' 
           target='_blank' class='enlace-btn'>
            📄 Ver Catálogo NTP INACAL
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Tecnologías de Control
    st.markdown("""
    <div class='content-box'>
        <h2 style='color: #1e3a8a !important; text-shadow: none;'>🔧 Principales Tecnologías de Control</h2>
    </div>
    """, unsafe_allow_html=True)
    
    tecnologias = pd.DataFrame([
        ['Material Particulado', 'Filtros de mangas', '>99%', 'Textil poroso captura partículas'],
        ['Material Particulado', 'Precipitadores electrostáticos', '95-99%', 'Carga eléctrica y colección'],
        ['Material Particulado', 'Ciclones', '70-90%', 'Fuerza centrífuga'],
        ['SO2', 'Desulfuración húmeda (FGD)', '>95%', 'Absorción con caliza/cal'],
        ['SO2', 'Desulfuración seca', '80-95%', 'Inyección de sorbente'],
        ['NOx', 'Reducción Catalítica Selectiva (SCR)', '>90%', 'Catalizador + urea/amoniaco'],
        ['NOx', 'Quemadores Low-NOx', '30-50%', 'Control de combustión'],
        ['NOx', 'Reducción No Catalítica (SNCR)', '40-60%', 'Inyección de urea sin catalizador'],
        ['COVs', 'Oxidación térmica', '>95%', 'Combustión a alta temperatura'],
        ['COVs', 'Adsorción en carbón activado', '85-95%', 'Captura en superficie porosa']
    ], columns=['Contaminante', 'Tecnología', 'Eficiencia', 'Principio'])
    
    st.dataframe(tecnologias, use_container_width=True, hide_index=True, height=420)

# ===================== PÁGINA NORMATIVAS INTERNACIONALES =====================
elif st.session_state.pagina == "Normativas":
    st.markdown("<h1>🌍 Normativas Internacionales de Calidad del Aire</h1>", unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["🌍 OMS", "🇺🇸 EPA USA", "🇨🇦 Canadá", "📊 Comparación"])
    
    # TAB OMS
    with tab1:
        st.markdown("""
        <div class='content-box'>
            <h2 style='color: #1e3a8a !important; text-shadow: none;'>🌍 Organización Mundial de la Salud (OMS)</h2>
            <p style='color: #333; font-size: 1.1em;'>
                La OMS establece las <strong>directrices globales más estrictas</strong> para proteger 
                la salud pública de la contaminación del aire.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='normativa-card'>
            <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
                <span class='categoria-badge' style='background: #10b981;'>2021</span>
                WHO Global Air Quality Guidelines
            </h3>
            <p style='color: #555; margin: 15px 0;'>
                <strong>Directrices Mundiales de Calidad del Aire de la OMS 2021</strong><br>
                Actualización de las guías de 2005, con niveles 50% más estrictos basados en nueva evidencia científica.
            </p>
            <a href='https://www.who.int/publications/i/item/9789240034228' 
               target='_blank' class='enlace-btn'>
                📄 Ver Directrices OMS 2021
            </a>
            <a href='https://www.who.int/es/news-room/feature-stories/detail/what-are-the-who-air-quality-guidelines' 
               target='_blank' class='enlace-btn'>
                📖 Resumen en Español
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        # Tabla OMS
        st.markdown("<h3 style='color: white;'>📊 Directrices OMS 2021</h3>", unsafe_allow_html=True)
        oms_tabla = pd.DataFrame([
            ['PM2.5', 5, 15, 'μg/m³'],
            ['PM10', 15, 45, 'μg/m³'],
            ['NO2', 10, 25, 'μg/m³'],
            ['SO2', None, 40, 'μg/m³'],
            ['O3', None, 100, 'μg/m³ (8h)'],
            ['CO', None, 4000, 'μg/m³ (24h)']
        ], columns=['Contaminante', 'Anual', '24 horas', 'Unidad'])
        
        st.dataframe(oms_tabla, use_container_width=True, hide_index=True)
    
    # TAB EPA
    with tab2:
        st.markdown("""
        <div class='content-box'>
            <h2 style='color: #1e3a8a !important; text-shadow: none;'>🇺🇸 Environmental Protection Agency (EPA)</h2>
            <p style='color: #333; font-size: 1.1em;'>
                La EPA de EE.UU. establece los <strong>National Ambient Air Quality Standards (NAAQS)</strong>.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='normativa-card'>
            <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
                <span class='categoria-badge' style='background: #3b82f6;'>2024</span>
                NAAQS - National Ambient Air Quality Standards
            </h3>
            <p style='color: #555; margin: 15px 0;'>
                <strong>Estándares Nacionales de Calidad del Aire Ambiente</strong><br>
                Última actualización: PM2.5 anual reducido a 9.0 μg/m³ (febrero 2024)
            </p>
            <a href='https://www.epa.gov/criteria-air-pollutants/naaqs-table' 
               target='_blank' class='enlace-btn'>
                📄 Ver Tabla NAAQS
            </a>
            <a href='https://www.epa.gov/pm-pollution/national-ambient-air-quality-standards-naaqs-pm' 
               target='_blank' class='enlace-btn'>
                📖 Estándares PM
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        # Tabla EPA
        st.markdown("<h3 style='color: white;'>📊 Estándares EPA (NAAQS)</h3>", unsafe_allow_html=True)
        epa_tabla = pd.DataFrame([
            ['PM2.5', 9.0, 35, 'μg/m³', '2024'],
            ['PM10', None, 150, 'μg/m³', '2012'],
            ['NO2', 53, 100, 'ppb', '2010'],
            ['SO2', None, 75, 'ppb (1h)', '2010'],
            ['O3', None, 70, 'ppb (8h)', '2015'],
            ['CO', None, '9 ppm (8h)', None, '1971']
        ], columns=['Contaminante', 'Anual', 'Corto Plazo', 'Unidad', 'Última Actualización'])
        
        st.dataframe(epa_tabla, use_container_width=True, hide_index=True)
    
    # TAB CANADÁ
    with tab3:
        st.markdown("""
        <div class='content-box'>
            <h2 style='color: #1e3a8a !important; text-shadow: none;'>🇨🇦 Canadian Ambient Air Quality Standards (CAAQS)</h2>
            <p style='color: #333; font-size: 1.1em;'>
                Canadá utiliza un sistema de <strong>mejora continua</strong> con estándares actualizados cada 5 años.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='normativa-card'>
            <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
                <span class='categoria-badge' style='background: #ef4444;'>2025</span>
                CAAQS 2025
            </h3>
            <p style='color: #555; margin: 15px 0;'>
                <strong>Estándares Canadienses de Calidad del Aire Ambiente</strong><br>
                Sistema de gestión por Air Zones con mejora continua progresiva.
            </p>
            <a href='https://www.ccme.ca/en/air-quality-report' 
               target='_blank' class='enlace-btn'>
                📄 Ver Estándares CAAQS
            </a>
            <a href='https://www.canada.ca/en/environment-climate-change/services/air-quality-health-index.html' 
               target='_blank' class='enlace-btn'>
                📖 Air Quality Health Index
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        # Tabla Canadá
        st.markdown("<h3 style='color: white;'>📊 Estándares CAAQS</h3>", unsafe_allow_html=True)
        canada_tabla = pd.DataFrame([
            ['PM2.5', 8.8, 8.0, 'μg/m³', 'Anual'],
            ['PM2.5', 27, 25, 'μg/m³', '24h'],
            ['O3', 62, 60, 'ppb', '8h'],
            ['NO2', 60, 50, 'ppb', '1h'],
            ['SO2', 70, 65, 'ppb', '1h']
        ], columns=['Contaminante', '2020', '2025', 'Unidad', 'Período'])
        
        st.dataframe(canada_tabla, use_container_width=True, hide_index=True)
    
    # TAB COMPARACIÓN
    with tab4:
        st.markdown("<h2 style='color: white;'>📊 Comparación Internacional - PM2.5 Anual</h2>", unsafe_allow_html=True)
        
        comparacion = pd.DataFrame([
            {'Entidad': 'OMS 2021', 'PM2.5 Anual': 5, 'PM2.5 24h': 15},
            {'Entidad': 'EPA USA', 'PM2.5 Anual': 9, 'PM2.5 24h': 35},
            {'Entidad': 'Canadá 2025', 'PM2.5 Anual': 8, 'PM2.5 24h': 25},
            {'Entidad': 'OEFA Perú', 'PM2.5 Anual': 25, 'PM2.5 24h': 50}
        ])
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=comparacion['Entidad'],
            y=comparacion['PM2.5 Anual'],
            name='Anual',
            marker_color='#3b82f6',
            text=comparacion['PM2.5 Anual']
        ))
        fig.add_trace(go.Bar(
            x=comparacion['Entidad'],
            y=comparacion['PM2.5 24h'],
            name='24 horas',
            marker_color='#8b5cf6',
            text=comparacion['PM2.5 24h']
        ))
        
        fig.update_traces(texttemplate='%{text} μg/m³', textposition='outside')
        fig.update_layout(
            title='Comparación PM2.5 (μg/m³)',
            barmode='group',
            height=450,
            xaxis_title='',
            yaxis_title='Concentración (μg/m³)'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("""
        **Observación:** La OMS 2021 establece los estándares más estrictos (5 μg/m³ anual), 
        mientras que Perú mantiene valores más permisivos (25 μg/m³ anual). EPA y Canadá 
        tienen valores intermedios y actualizan sus estándares regularmente.
        """)

# FOOTER
st.markdown("---")
st.markdown("""
<div style='text-align: center; background: white; padding: 30px; border-radius: 15px; margin-top: 40px;'>
    <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
        Universidad Nacional de Moquegua
    </h3>
    <p style='color: #555; margin: 10px 0;'>
        Facultad de Ingeniería y Arquitectura
    </p>
    <p style='color: #666; margin: 5px 0;'>
        <strong>Curso:</strong> Contaminación y Control Atmosférico
    </p>
    <p style='color: #666; margin: 5px 0;'>
        <strong>Docente:</strong> Prof. Dr. José Antonio Valeriano Zapana
    </p>
    <p style='color: #999; font-size: 0.9em; margin-top: 15px;'>
        2024-2025 | Herramienta de Consulta de Marco Normativo del Aire
    </p>
</div>
""", unsafe_allow_html=True)
