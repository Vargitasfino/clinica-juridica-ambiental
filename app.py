st.markdown("---")
st.markdown("### 🔄 Proceso del Marco Normativo")
st.caption("Flujo interactivo del sistema de gestión de calidad del aire")

# Línea de tiempo ultra moderna con efectos 3D y animaciones
st.markdown("""
<style>
@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
}

@keyframes pulse-ring {
    0% { transform: scale(0.95); opacity: 1; }
    50% { transform: scale(1.05); opacity: 0.7; }
    100% { transform: scale(0.95); opacity: 1; }
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

<div style='margin: 2rem 0;'>
    <!-- Paso 1: ECA -->
    <div class='timeline-item' style='position: relative; margin-bottom: 2.5rem;'>
        <div style='display: flex; align-items: stretch; gap: 1.5rem;'>
            <!-- Icono 3D -->
            <div class='timeline-icon' style='position: relative; flex-shrink: 0; width: 100px; height: 100px; background: linear-gradient(135deg, #0065FF 0%, #00B8D9 100%); border-radius: 20px; display: flex; align-items: center; justify-content: center; box-shadow: 0 15px 35px rgba(0,101,255,0.4), inset 0 -5px 15px rgba(0,0,0,0.2); transform: perspective(1000px) rotateY(-5deg); transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);'>
                <div class='number-badge'>1</div>
                <span style='font-size: 3rem; filter: drop-shadow(0 4px 8px rgba(0,0,0,0.3));'>📋</span>
            </div>
            
            <!-- Card de contenido -->
            <div class='timeline-card' style='flex: 1; background: linear-gradient(135deg, rgba(0,101,255,0.15) 0%, rgba(0,184,217,0.1) 100%); backdrop-filter: blur(20px); padding: 1.8rem; border-radius: 16px; border: 1px solid rgba(0,101,255,0.3); border-left: 5px solid #0065FF; box-shadow: 0 10px 40px rgba(0,0,0,0.2); transition: all 0.3s ease; position: relative; overflow: hidden;'>
                <!-- Efecto de brillo -->
                <div style='position: absolute; top: 0; right: 0; width: 100px; height: 100%; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.05), transparent); pointer-events: none;'></div>
                
                <div style='display: flex; justify-content: space-between; align-items: start; margin-bottom: 1rem;'>
                    <div>
                        <h3 style='margin: 0 0 0.3rem 0; color: white; font-size: 1.4rem; font-weight: 700; letter-spacing: -0.02em;'>Estándares de Calidad Ambiental</h3>
                        <p style='margin: 0; color: #60A5FA; font-size: 0.9rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em;'>ECA • Aire Ambiente</p>
                    </div>
                    <div style='background: linear-gradient(135deg, rgba(0,101,255,0.4), rgba(0,184,217,0.4)); padding: 0.5rem 1.2rem; border-radius: 25px; box-shadow: 0 4px 15px rgba(0,101,255,0.3); backdrop-filter: blur(10px);'>
                        <span style='color: white; font-weight: 700; font-size: 1.1rem;'>12</span>
                        <span style='color: rgba(255,255,255,0.8); font-size: 0.85rem; margin-left: 0.3rem;'>norm.</span>
                    </div>
                </div>
                
                <p style='color: rgba(255,255,255,0.85); margin: 0.8rem 0 0 0; line-height: 1.6; font-size: 0.95rem;'>
                    ✓ Define concentraciones máximas permitidas<br>
                    ✓ Protege la salud de la población<br>
                    ✓ Medido en estaciones de monitoreo
                </p>
            </div>
        </div>
        <!-- Línea conectora animada -->
        <div style='position: absolute; left: 49px; top: 100px; width: 3px; height: 50px; background: linear-gradient(180deg, #0065FF, #00B8D9); opacity: 0.6;'></div>
    </div>
    
    <!-- Paso 2: LMP -->
    <div class='timeline-item' style='position: relative; margin-bottom: 2.5rem; animation-delay: 0.1s;'>
        <div style='display: flex; align-items: stretch; gap: 1.5rem;'>
            <div class='timeline-icon' style='position: relative; flex-shrink: 0; width: 100px; height: 100px; background: linear-gradient(135deg, #00B8D9 0%, #00C853 100%); border-radius: 20px; display: flex; align-items: center; justify-content: center; box-shadow: 0 15px 35px rgba(0,184,217,0.4), inset 0 -5px 15px rgba(0,0,0,0.2); transform: perspective(1000px) rotateY(-5deg); transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);'>
                <div class='number-badge'>2</div>
                <span style='font-size: 3rem; filter: drop-shadow(0 4px 8px rgba(0,0,0,0.3));'>🏭</span>
            </div>
            
            <div class='timeline-card' style='flex: 1; background: linear-gradient(135deg, rgba(0,184,217,0.15) 0%, rgba(0,200,83,0.1) 100%); backdrop-filter: blur(20px); padding: 1.8rem; border-radius: 16px; border: 1px solid rgba(0,184,217,0.3); border-left: 5px solid #00B8D9; box-shadow: 0 10px 40px rgba(0,0,0,0.2); transition: all 0.3s ease; position: relative; overflow: hidden;'>
                <div style='position: absolute; top: 0; right: 0; width: 100px; height: 100%; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.05), transparent); pointer-events: none;'></div>
                
                <div style='display: flex; justify-content: space-between; align-items: start; margin-bottom: 1rem;'>
                    <div>
                        <h3 style='margin: 0 0 0.3rem 0; color: white; font-size: 1.4rem; font-weight: 700; letter-spacing: -0.02em;'>Límites Máximos Permisibles</h3>
                        <p style='margin: 0; color: #00B8D9; font-size: 0.9rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em;'>LMP • Fuente de Emisión</p>
                    </div>
                    <div style='background: linear-gradient(135deg, rgba(0,184,217,0.4), rgba(0,200,83,0.4)); padding: 0.5rem 1.2rem; border-radius: 25px; box-shadow: 0 4px 15px rgba(0,184,217,0.3); backdrop-filter: blur(10px);'>
                        <span style='color: white; font-weight: 700; font-size: 1.1rem;'>8</span>
                        <span style='color: rgba(255,255,255,0.8); font-size: 0.85rem; margin-left: 0.3rem;'>sect.</span>
                    </div>
                </div>
                
                <p style='color: rgba(255,255,255,0.85); margin: 0.8rem 0 0 0; line-height: 1.6; font-size: 0.95rem;'>
                    ✓ Controla emisiones en chimeneas y ductos<br>
                    ✓ Específico por sector industrial<br>
                    ✓ Obligatorio para cumplimiento ambiental
                </p>
            </div>
        </div>
        <div style='position: absolute; left: 49px; top: 100px; width: 3px; height: 50px; background: linear-gradient(180deg, #00B8D9, #00C853); opacity: 0.6;'></div>
    </div>
    
    <!-- Paso 3: Protocolos -->
    <div class='timeline-item' style='position: relative; margin-bottom: 2.5rem; animation-delay: 0.2s;'>
        <div style='display: flex; align-items: stretch; gap: 1.5rem;'>
            <div class='timeline-icon' style='position: relative; flex-shrink: 0; width: 100px; height: 100px; background: linear-gradient(135deg, #00C853 0%, #8BC34A 100%); border-radius: 20px; display: flex; align-items: center; justify-content: center; box-shadow: 0 15px 35px rgba(0,200,83,0.4), inset 0 -5px 15px rgba(0,0,0,0.2); transform: perspective(1000px) rotateY(-5deg); transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);'>
                <div class='number-badge'>3</div>
                <span style='font-size: 3rem; filter: drop-shadow(0 4px 8px rgba(0,0,0,0.3));'>📖</span>
            </div>
            
            <div class='timeline-card' style='flex: 1; background: linear-gradient(135deg, rgba(0,200,83,0.15) 0%, rgba(139,195,74,0.1) 100%); backdrop-filter: blur(20px); padding: 1.8rem; border-radius: 16px; border: 1px solid rgba(0,200,83,0.3); border-left: 5px solid #00C853; box-shadow: 0 10px 40px rgba(0,0,0,0.2); transition: all 0.3s ease; position: relative; overflow: hidden;'>
                <div style='position: absolute; top: 0; right: 0; width: 100px; height: 100%; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.05), transparent); pointer-events: none;'></div>
                
                <div style='display: flex; justify-content: space-between; align-items: start; margin-bottom: 1rem;'>
                    <div>
                        <h3 style='margin: 0 0 0.3rem 0; color: white; font-size: 1.4rem; font-weight: 700; letter-spacing: -0.02em;'>Protocolos de Monitoreo</h3>
                        <p style='margin: 0; color: #00C853; font-size: 0.9rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em;'>Medición y Análisis</p>
                    </div>
                    <div style='background: linear-gradient(135deg, rgba(0,200,83,0.4), rgba(139,195,74,0.4)); padding: 0.5rem 1.2rem; border-radius: 25px; box-shadow: 0 4px 15px rgba(0,200,83,0.3); backdrop-filter: blur(10px);'>
                        <span style='color: white; font-weight: 700; font-size: 1.1rem;'>5</span>
                        <span style='color: rgba(255,255,255,0.8); font-size: 0.85rem; margin-left: 0.3rem;'>prot.</span>
                    </div>
                </div>
                
                <p style='color: rgba(255,255,255,0.85); margin: 0.8rem 0 0 0; line-height: 1.6; font-size: 0.95rem;'>
                    ✓ Procedimientos estandarizados de muestreo<br>
                    ✓ Garantiza comparabilidad de resultados<br>
                    ✓ Métodos EPA y normas técnicas
                </p>
            </div>
        </div>
        <div style='position: absolute; left: 49px; top: 100px; width: 3px; height: 50px; background: linear-gradient(180deg, #00C853, #FFB300); opacity: 0.6;'></div>
    </div>
    
    <!-- Paso 4: Lineamientos -->
    <div class='timeline-item' style='position: relative; margin-bottom: 2.5rem; animation-delay: 0.3s;'>
        <div style='display: flex; align-items: stretch; gap: 1.5rem;'>
            <div class='timeline-icon' style='position: relative; flex-shrink: 0; width: 100px; height: 100px; background: linear-gradient(135deg, #FFB300 0%, #FF6F00 100%); border-radius: 20px; display: flex; align-items: center; justify-content: center; box-shadow: 0 15px 35px rgba(255,179,0,0.4), inset 0 -5px 15px rgba(0,0,0,0.2); transform: perspective(1000px) rotateY(-5deg); transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);'>
                <div class='number-badge'>4</div>
                <span style='font-size: 3rem; filter: drop-shadow(0 4px 8px rgba(0,0,0,0.3));'>📐</span>
            </div>
            
            <div class='timeline-card' style='flex: 1; background: linear-gradient(135deg, rgba(255,179,0,0.15) 0%, rgba(255,111,0,0.1) 100%); backdrop-filter: blur(20px); padding: 1.8rem; border-radius: 16px; border: 1px solid rgba(255,179,0,0.3); border-left: 5px solid #FFB300; box-shadow: 0 10px 40px rgba(0,0,0,0.2); transition: all 0.3s ease; position: relative; overflow: hidden;'>
                <div style='position: absolute; top: 0; right: 0; width: 100px; height: 100%; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.05), transparent); pointer-events: none;'></div>
                
                <div style='display: flex; justify-content: space-between; align-items: start; margin-bottom: 1rem;'>
                    <div>
                        <h3 style='margin: 0 0 0.3rem 0; color: white; font-size: 1.4rem; font-weight: 700; letter-spacing: -0.02em;'>Lineamientos y Guías</h3>
                        <p style='margin: 0; color: #FFB300; font-size: 0.9rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em;'>Implementación</p>
                    </div>
                    <div style='background: linear-gradient(135deg, rgba(255,179,0,0.4), rgba(255,111,0,0.4)); padding: 0.5rem 1.2rem; border-radius: 25px; box-shadow: 0 4px 15px rgba(255,179,0,0.3); backdrop-filter: blur(10px);'>
                        <span style='color: white; font-weight: 700; font-size: 1.1rem;'>★</span>
                    </div>
                </div>
                
                <p style='color: rgba(255,255,255,0.85); margin: 0.8rem 0 0 0; line-height: 1.6; font-size: 0.95rem;'>
                    ✓ Guías técnicas operativas<br>
                    ✓ Inventarios de emisiones atmosféricas<br>
                    ✓ Estados de alerta y emergencia
                </p>
            </div>
        </div>
        <div style='position: absolute; left: 49px; top: 100px; width: 3px; height: 50px; background: linear-gradient(180deg, #FFB300, #8B5CF6); opacity: 0.6;'></div>
    </div>
    
    <!-- Paso 5: Control -->
    <div class='timeline-item' style='position: relative; margin-bottom: 2.5rem; animation-delay: 0.4s;'>
        <div style='display: flex; align-items: stretch; gap: 1.5rem;'>
            <div class='timeline-icon' style='position: relative; flex-shrink: 0; width: 100px; height: 100px; background: linear-gradient(135deg, #8B5CF6 0%, #6366F1 100%); border-radius: 20px; display: flex; align-items: center; justify-content: center; box-shadow: 0 15px 35px rgba(139,92,246,0.4), inset 0 -5px 15px rgba(0,0,0,0.2); transform: perspective(1000px) rotateY(-5deg); transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);'>
                <div class='number-badge'>5</div>
                <span style='font-size: 3rem; filter: drop-shadow(0 4px 8px rgba(0,0,0,0.3));'>🛡️</span>
            </div>
            
            <div class='timeline-card' style='flex: 1; background: linear-gradient(135deg, rgba(139,92,246,0.15) 0%, rgba(99,102,241,0.1) 100%); backdrop-filter: blur(20px); padding: 1.8rem; border-radius: 16px; border: 1px solid rgba(139,92,246,0.3); border-left: 5px solid #8B5CF6; box-shadow: 0 10px 40px rgba(0,0,0,0.2); transition: all 0.3s ease; position: relative; overflow: hidden;'>
                <div style='position: absolute; top: 0; right: 0; width: 100px; height: 100%; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.05), transparent); pointer-events: none;'></div>
                
                <div style='display: flex; justify-content: space-between; align-items: start; margin-bottom: 1rem;'>
                    <div>
                        <h3 style='margin: 0 0 0.3rem 0; color: white; font-size: 1.4rem; font-weight: 700; letter-spacing: -0.02em;'>Medidas de Control</h3>
                        <p style='margin: 0; color: #8B5CF6; font-size: 0.9rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em;'>Tecnologías BAT</p>
                    </div>
                    <div style='background: linear-gradient(135deg, rgba(139,92,246,0.4), rgba(99,102,241,0.4)); padding: 0.5rem 1.2rem; border-radius: 25px; box-shadow: 0 4px 15px rgba(139,92,246,0.3); backdrop-filter: blur(10px);'>
                        <span style='color: white; font-weight: 700; font-size: 1.1rem;'>★★</span>
                    </div>
                </div>
                
                <p style='color: rgba(255,255,255,0.85); margin: 0.8rem 0 0 0; line-height: 1.6; font-size: 0.95rem;'>
                    ✓ Sistemas de reducción de emisiones<br>
                    ✓ Filtros, precipitadores, scrubbers<br>
                    ✓ Mejores técnicas disponibles (MTD)
                </p>
            </div>
        </div>
        <div style='position: absolute; left: 49px; top: 100px; width: 3px; height: 50px; background: linear-gradient(180deg, #8B5CF6, #EC4899); opacity: 0.6;'></div>
    </div>
    
    <!-- Paso 6: Internacional -->
    <div class='timeline-item' style='position: relative; animation-delay: 0.5s;'>
        <div style='display: flex; align-items: stretch; gap: 1.5rem;'>
            <div class='timeline-icon' style='position: relative; flex-shrink: 0; width: 100px; height: 100px; background: linear-gradient(135deg, #EC4899 0%, #F43F5E 100%); border-radius: 20px; display: flex; align-items: center; justify-content: center; box-shadow: 0 15px 35px rgba(236,72,153,0.4), inset 0 -5px 15px rgba(0,0,0,0.2); transform: perspective(1000px) rotateY(-5deg); transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);'>
                <div class='number-badge'>6</div>
                <span style='font-size: 3rem; filter: drop-shadow(0 4px 8px rgba(0,0,0,0.3));'>🌍</span>
            </div>
            
            <div class='timeline-card' style='flex: 1; background: linear-gradient(135deg, rgba(236,72,153,0.15) 0%, rgba(244,63,94,0.1) 100%); backdrop-filter: blur(20px); padding: 1.8rem; border-radius: 16px; border: 1px solid rgba(236,72,153,0.3); border-left: 5px solid #EC4899; box-shadow: 0 10px 40px rgba(0,0,0,0.2); transition: all 0.3s ease; position: relative; overflow: hidden;'>
                <div style='position: absolute; top: 0; right: 0; width: 100px; height: 100%; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.05), transparent); pointer-events: none;'></div>
                
                <div style='display: flex; justify-content: space-between; align-items: start; margin-bottom: 1rem;'>
                    <div>
                        <h3 style='margin: 0 0 0.3rem 0; color: white; font-size: 1.4rem; font-weight: 700; letter-spacing: -0.02em;'>Referencia Internacional</h3>
                        <p style='margin: 0; color: #EC4899; font-size: 0.9rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em;'>OMS • EPA • Canadá</p>
                    </div>
                    <div style='background: linear-gradient(135deg, rgba(236,72,153,0.4), rgba(244,63,94,0.4)); padding: 0.5rem 1.2rem; border-radius: 25px; box-shadow: 0 4px 15px rgba(236,72,153,0.3); backdrop-filter: blur(10px);'>
                        <span style='color: white; font-weight: 700; font-size: 1.1rem;'>★★★</span>
                    </div>
                </div>
                
                <p style='color: rgba(255,255,255,0.85); margin: 0.8rem 0 0 0; line-height: 1.6; font-size: 0.95rem;'>
                    ✓ Benchmarking internacional<br>
                    ✓ Mejores prácticas globales<br>
                    ✓ Actualización continua de estándares
                </p>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
