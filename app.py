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
        <span class='status-badge referencia'>● REFERENCIA HISTÓ
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
