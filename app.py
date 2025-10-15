import React, { useState } from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { Alert, AlertDescription } from '@/components/ui/alert';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, LineChart, Line, ScatterChart, Scatter } from 'recharts';

const AirQualityApp = () => {
  const [activeTab, setActiveTab] = useState('oms');

  // Datos de normativas comparadas - AIRE
  const airStandards = {
    pm25: [
      { entidad: 'OMS 2021', anual: 5, dia24h: 15 },
      { entidad: 'OEFA Perú', anual: 25, dia24h: 50 },
      { entidad: 'EPA USA', anual: 9, dia24h: 35 },
      { entidad: 'Canadá', anual: 8.8, dia24h: 27 }
    ],
    pm10: [
      { entidad: 'OMS 2021', anual: 15, dia24h: 45 },
      { entidad: 'OEFA Perú', anual: 50, dia24h: 100 },
      { entidad: 'EPA USA', anual: null, dia24h: 150 },
      { entidad: 'Canadá', anual: null, dia24h: 50 }
    ],
    no2: [
      { entidad: 'OMS 2021', anual: 10, dia24h: 25, hora1: null },
      { entidad: 'OEFA Perú', anual: 100, dia24h: null, hora1: 200 },
      { entidad: 'EPA USA', anual: 53, dia24h: null, hora1: 100 },
      { entidad: 'Canadá', anual: null, dia24h: null, hora1: 60 }
    ],
    so2: [
      { entidad: 'OMS 2021', dia24h: 40 },
      { entidad: 'OEFA Perú', dia24h: 250 },
      { entidad: 'EPA USA', hora1: 75 },
      { entidad: 'Canadá', hora1: 70 }
    ],
    o3: [
      { entidad: 'OMS 2021', hora8: 100 },
      { entidad: 'OEFA Perú', hora8: 100 },
      { entidad: 'EPA USA', hora8: 70 },
      { entidad: 'Canadá', hora8: 62 }
    ]
  };

  // LMP para termoeléctricas - Perú
  const lmpThermoelectric = [
    { contaminante: 'NOx', gasNatural: 320, diesel: 850, residual: 2000, unidad: 'mg/Nm³' },
    { contaminante: 'SO₂', gasNatural: null, diesel: 1700, residual: 3500, unidad: 'mg/Nm³' },
    { contaminante: 'PM', gasNatural: 50, diesel: 150, residual: 350, unidad: 'mg/Nm³' }
  ];

  // Línea de tiempo de cambios normativos
  const timeline = [
    { año: 2001, evento: 'D.S. 074-2001-PCM - Primeros ECA Aire Perú', entidad: 'OEFA' },
    { año: 2005, evento: 'OMS - Guías Calidad del Aire', entidad: 'OMS' },
    { año: 2010, evento: 'D.S. 003-2010-MINAM - LMP Termoeléctricas', entidad: 'OEFA' },
    { año: 2013, evento: 'EPA - PM2.5 Anual reducido a 12 μg/m³', entidad: 'EPA' },
    { año: 2017, evento: 'D.S. 003-2017-MINAM - ECA Aire más estrictos', entidad: 'OEFA' },
    { año: 2019, evento: 'D.S. 010-2019-MINAM - Modificatoria ECA', entidad: 'OEFA' },
    { año: 2020, evento: 'EPA - Fortalece PM2.5', entidad: 'EPA' },
    { año: 2021, evento: 'OMS - Nuevas Directrices (50% más estrictas)', entidad: 'OMS' },
    { año: 2022, evento: 'Canadá - Actualización CAAQS', entidad: 'Canadá' },
    { año: 2024, evento: 'EPA - PM2.5 Anual a 9.0 μg/m³', entidad: 'EPA' }
  ];

  // Plantas hidroeléctricas vs termoeléctricas
  const plantasComparacion = [
    { tipo: 'Hidroeléctrica', emisionNOx: 0, emisionSO2: 0, emisionPM: 0, impactoAire: 'Nulo' },
    { tipo: 'Termoeléctrica Gas', emisionNOx: 280, emisionSO2: 0, emisionPM: 40, impactoAire: 'Moderado' },
    { tipo: 'Termoeléctrica Diésel', emisionNOx: 750, emisionSO2: 1500, emisionPM: 130, impactoAire: 'Alto' },
    { tipo: 'Termoeléctrica Carbón', emisionNOx: 1800, emisionSO2: 3200, emisionPM: 320, impactoAire: 'Muy Alto' }
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-6">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-indigo-900 mb-2">
            ⚖️ Sistema Integral de Normativas de Calidad del Aire
          </h1>
          <p className="text-lg text-gray-700">
            Caso 2: Central Termoeléctrica - Análisis de LMP en NOₓ/SO₂
          </p>
          <p className="text-sm text-gray-600 mt-2">
            Universidad Nacional de Moquegua | Prof. Dr. José Antonio Valeriano Zapana
          </p>
        </div>

        {/* Tabs principales */}
        <Tabs value={activeTab} onValueChange={setActiveTab} className="w-full">
          <TabsList className="grid w-full grid-cols-7 mb-6">
            <TabsTrigger value="oms">🌍 OMS</TabsTrigger>
            <TabsTrigger value="oefa">🇵🇪 OEFA</TabsTrigger>
            <TabsTrigger value="epa">🇺🇸 EPA</TabsTrigger>
            <TabsTrigger value="canada">🇨🇦 Canadá</TabsTrigger>
            <TabsTrigger value="linea">⏳ Línea Tiempo</TabsTrigger>
            <TabsTrigger value="plantas">⚡ Plantas</TabsTrigger>
            <TabsTrigger value="pama">📋 PAMA</TabsTrigger>
          </TabsList>

          {/* OMS */}
          <TabsContent value="oms">
            <Card>
              <CardHeader>
                <CardTitle className="text-2xl">🌍 Organización Mundial de la Salud (OMS)</CardTitle>
              </CardHeader>
              <CardContent className="space-y-6">
                <Alert>
                  <AlertDescription>
                    Las directrices de la OMS 2021 son las más estrictas del mundo. Representan niveles 
                    de calidad del aire que protegen la salud pública según la mejor evidencia científica disponible.
                  </AlertDescription>
                </Alert>

                {/* PM2.5 */}
                <div>
                  <h3 className="text-xl font-semibold mb-3 text-indigo-800">Material Particulado PM2.5</h3>
                  <ResponsiveContainer width="100%" height={300}>
                    <BarChart data={airStandards.pm25}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="entidad" />
                      <YAxis label={{ value: 'μg/m³', angle: -90, position: 'insideLeft' }} />
                      <Tooltip />
                      <Legend />
                      <Bar dataKey="anual" fill="#4f46e5" name="Anual" />
                      <Bar dataKey="dia24h" fill="#818cf8" name="24 horas" />
                    </BarChart>
                  </ResponsiveContainer>
                  <div className="mt-4 p-4 bg-blue-50 rounded-lg">
                    <p className="text-sm"><strong>OMS 2021:</strong> Anual 5 μg/m³, 24h 15 μg/m³</p>
                    <p className="text-sm mt-2"><strong>Impacto en salud:</strong> Enfermedades cardiovasculares, 
                    cáncer de pulmón, muerte prematura. PM2.5 es el contaminante más peligroso por su tamaño microscópico.</p>
                  </div>
                </div>

                {/* PM10 */}
                <div>
                  <h3 className="text-xl font-semibold mb-3 text-indigo-800">Material Particulado PM10</h3>
                  <ResponsiveContainer width="100%" height={300}>
                    <BarChart data={airStandards.pm10}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="entidad" />
                      <YAxis label={{ value: 'μg/m³', angle: -90, position: 'insideLeft' }} />
                      <Tooltip />
                      <Legend />
                      <Bar dataKey="anual" fill="#10b981" name="Anual" />
                      <Bar dataKey="dia24h" fill="#6ee7b7" name="24 horas" />
                    </BarChart>
                  </ResponsiveContainer>
                </div>

                {/* NO2 */}
                <div>
                  <h3 className="text-xl font-semibold mb-3 text-indigo-800">Dióxido de Nitrógeno (NO₂)</h3>
                  <div className="grid grid-cols-3 gap-4">
                    <div className="p-4 bg-yellow-50 rounded-lg text-center">
                      <p className="text-2xl font-bold text-yellow-700">10</p>
                      <p className="text-sm">μg/m³ Anual</p>
                      <p className="text-xs text-gray-600">OMS 2021</p>
                    </div>
                    <div className="p-4 bg-orange-50 rounded-lg text-center">
                      <p className="text-2xl font-bold text-orange-700">25</p>
                      <p className="text-sm">μg/m³ 24h</p>
                      <p className="text-xs text-gray-600">OMS 2021</p>
                    </div>
                    <div className="p-4 bg-red-50 rounded-lg text-center">
                      <p className="text-2xl font-bold text-red-700">100</p>
                      <p className="text-sm">μg/m³ Anual</p>
                      <p className="text-xs text-gray-600">OEFA Perú</p>
                    </div>
                  </div>
                  <p className="text-sm mt-3 text-gray-700">
                    <strong>Fuente principal:</strong> Tráfico vehicular, termoeléctricas. 
                    <strong> Efectos:</strong> Irritación respiratoria, asma, precursor de ozono.
                  </p>
                </div>

                {/* SO2 */}
                <div>
                  <h3 className="text-xl font-semibold mb-3 text-indigo-800">Dióxido de Azufre (SO₂)</h3>
                  <ResponsiveContainer width="100%" height={250}>
                    <BarChart data={airStandards.so2}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="entidad" />
                      <YAxis label={{ value: 'μg/m³', angle: -90, position: 'insideLeft' }} />
                      <Tooltip />
                      <Bar dataKey="dia24h" fill="#ef4444" name="24 horas" />
                      <Bar dataKey="hora1" fill="#f87171" name="1 hora" />
                    </BarChart>
                  </ResponsiveContainer>
                  <p className="text-sm mt-3 text-gray-700">
                    <strong>Fuente:</strong> Quema de carbón, refinación de petróleo, fundición de metales.
                    <strong> Impacto:</strong> Lluvia ácida, irritación respiratoria severa.
                  </p>
                </div>

                {/* Ozono */}
                <div>
                  <h3 className="text-xl font-semibold mb-3 text-indigo-800">Ozono Troposférico (O₃)</h3>
                  <ResponsiveContainer width="100%" height={250}>
                    <BarChart data={airStandards.o3}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="entidad" />
                      <YAxis label={{ value: 'μg/m³', angle: -90, position: 'insideLeft' }} />
                      <Tooltip />
                      <Bar dataKey="hora8" fill="#8b5cf6" name="8 horas" />
                    </BarChart>
                  </ResponsiveContainer>
                  <p className="text-sm mt-3 text-gray-700">
                    <strong>Contaminante secundario:</strong> No se emite directamente, se forma por reacción 
                    fotoquímica entre NOx y VOCs bajo luz solar. Niveles más altos en días soleados.
                  </p>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          {/* OEFA */}
          <TabsContent value="oefa">
            <Card>
              <CardHeader>
                <CardTitle className="text-2xl">🇵🇪 OEFA - Organismo de Evaluación y Fiscalización Ambiental</CardTitle>
              </CardHeader>
              <CardContent className="space-y-6">
                <Alert className="bg-indigo-50 border-indigo-200">
                  <AlertDescription>
                    <strong>Marco legal principal:</strong> D.S. N° 003-2017-MINAM (ECA Aire) y 
                    D.S. N° 003-2010-MINAM (LMP para Termoeléctricas)
                  </AlertDescription>
                </Alert>

                {/* ECA Aire Perú */}
                <div>
                  <h3 className="text-xl font-semibold mb-3">📊 Estándares de Calidad Ambiental (ECA) - Aire</h3>
                  <div className="overflow-x-auto">
                    <table className="w-full border-collapse border border-gray-300">
                      <thead className="bg-indigo-100">
                        <tr>
                          <th className="border p-2">Contaminante</th>
                          <th className="border p-2">Período</th>
                          <th className="border p-2">Valor ECA</th>
                          <th className="border p-2">Unidad</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr><td className="border p-2">PM2.5</td><td className="border p-2">24 horas</td><td className="border p-2 font-bold">50</td><td className="border p-2">μg/m³</td></tr>
                        <tr><td className="border p-2">PM2.5</td><td className="border p-2">Anual</td><td className="border p-2 font-bold">25</td><td className="border p-2">μg/m³</td></tr>
                        <tr><td className="border p-2">PM10</td><td className="border p-2">24 horas</td><td className="border p-2 font-bold">100</td><td className="border p-2">μg/m³</td></tr>
                        <tr><td className="border p-2">PM10</td><td className="border p-2">Anual</td><td className="border p-2 font-bold">50</td><td className="border p-2">μg/m³</td></tr>
                        <tr className="bg-yellow-50"><td className="border p-2">NO₂</td><td className="border p-2">1 hora</td><td className="border p-2 font-bold">200</td><td className="border p-2">μg/m³</td></tr>
                        <tr className="bg-yellow-50"><td className="border p-2">NO₂</td><td className="border p-2">Anual</td><td className="border p-2 font-bold">100</td><td className="border p-2">μg/m³</td></tr>
                        <tr className="bg-red-50"><td className="border p-2">SO₂</td><td className="border p-2">24 horas</td><td className="border p-2 font-bold">250</td><td className="border p-2">μg/m³</td></tr>
                        <tr><td className="border p-2">O₃</td><td className="border p-2">8 horas</td><td className="border p-2 font-bold">100</td><td className="border p-2">μg/m³</td></tr>
                        <tr><td className="border p-2">CO</td><td className="border p-2">8 horas</td><td className="border p-2 font-bold">10,000</td><td className="border p-2">μg/m³</td></tr>
                        <tr><td className="border p-2">CO</td><td className="border p-2">1 hora</td><td className="border p-2 font-bold">30,000</td><td className="border p-2">μg/m³</td></tr>
                      </tbody>
                    </table>
                  </div>
                </div>

                {/* LMP Termoeléctricas */}
                <div>
                  <h3 className="text-xl font-semibold mb-3">🏭 Límites Máximos Permisibles (LMP) - Termoeléctricas</h3>
                  <p className="text-sm mb-3 text-gray-700">
                    D.S. N° 003-2010-MINAM | Se miden en la chimenea (punto de emisión)
                  </p>
                  <div className="overflow-x-auto">
                    <table className="w-full border-collapse border border-gray-300">
                      <thead className="bg-green-100">
                        <tr>
                          <th className="border p-2">Contaminante</th>
                          <th className="border p-2">Gas Natural</th>
                          <th className="border p-2">Diésel</th>
                          <th className="border p-2">Residual</th>
                          <th className="border p-2">Unidad</th>
                        </tr>
                      </thead>
                      <tbody>
                        {lmpThermoelectric.map((row, idx) => (
                          <tr key={idx} className={idx % 2 === 0 ? 'bg-white' : 'bg-gray-50'}>
                            <td className="border p-2 font-semibold">{row.contaminante}</td>
                            <td className="border p-2 text-center">{row.gasNatural || '---'}</td>
                            <td className="border p-2 text-center font-bold text-orange-700">{row.diesel || '---'}</td>
                            <td className="border p-2 text-center">{row.residual || '---'}</td>
                            <td className="border p-2">{row.unidad}</td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                  
                  <Alert className="mt-4">
                    <AlertDescription>
                      <strong>⚠️ Caso 2:</strong> Tu central termoeléctrica reporta excedencias de LMP de NOₓ 
                      y SO₂ durante arranques y paradas programadas. Estos valores aplican en condiciones normales de operación.
                    </AlertDescription>
                  </Alert>
                </div>

                {/* Diferencia ECA vs LMP */}
                <div className="grid grid-cols-2 gap-4">
                  <div className="p-4 bg-blue-50 rounded-lg">
                    <h4 className="font-bold text-blue-900 mb-2">📍 ECA (Receptor)</h4>
                    <ul className="text-sm space-y-1">
                      <li>✓ Se mide en el ambiente</li>
                      <li>✓ Protege salud pública</li>
                      <li>✓ Puede tener múltiples fuentes</li>
                      <li>✓ Ejemplo: Estación de monitoreo en población</li>
                    </ul>
                  </div>
                  <div className="p-4 bg-green-50 rounded-lg">
                    <h4 className="font-bold text-green-900 mb-2">🏭 LMP (Fuente)</h4>
                    <ul className="text-sm space-y-1">
                      <li>✓ Se mide en la chimenea</li>
                      <li>✓ Responsabilidad del titular</li>
                      <li>✓ Control de emisiones industriales</li>
                      <li>✓ Ejemplo: Chimenea de termoeléctrica</li>
                    </ul>
                  </div>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          {/* EPA */}
          <TabsContent value="epa">
            <Card>
              <CardHeader>
                <CardTitle className="text-2xl">🇺🇸 EPA - Environmental Protection Agency (USA)</CardTitle>
              </CardHeader>
              <CardContent className="space-y-6">
                <Alert className="bg-blue-50 border-blue-200">
                  <AlertDescription>
                    <strong>NAAQS (National Ambient Air Quality Standards):</strong> Estándares primarios 
                    (salud) y secundarios (bienestar público, visibilidad, ecosistemas)
                  </AlertDescription>
                </Alert>

                <div className="grid grid-cols-2 gap-6">
                  <div>
                    <h3 className="text-lg font-semibold mb-3">📊 Estándares Actuales</h3>
                    <div className="space-y-2">
                      <div className="p-3 bg-purple-50 rounded">
                        <p className="font-semibold">PM2.5</p>
                        <p className="text-sm">Anual: <strong>9.0 μg/m³</strong> (2024) ✨</p>
                        <p className="text-sm">24h: <strong>35 μg/m³</strong></p>
                      </div>
                      <div className="p-3 bg-blue-50 rounded">
                        <p className="font-semibold">PM10</p>
                        <p className="text-sm">24h: <strong>150 μg/m³</strong></p>
                      </div>
                      <div className="p-3 bg-yellow-50 rounded">
                        <p className="font-semibold">O₃</p>
                        <p className="text-sm">8h: <strong>0.070 ppm</strong></p>
                      </div>
                      <div className="p-3 bg-red-50 rounded">
                        <p className="font-semibold">SO₂</p>
                        <p className="text-sm">1h: <strong>75 ppb</strong></p>
                      </div>
                    </div>
                  </div>

                  <div>
                    <h3 className="text-lg font-semibold mb-3">📈 Evolución PM2.5 Anual</h3>
                    <ResponsiveContainer width="100%" height={200}>
                      <LineChart data={[
                        { año: 1997, valor: 15 },
                        { año: 2006, valor: 15 },
                        { año: 2012, valor: 12 },
                        { año: 2024, valor: 9 }
                      ]}>
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis dataKey="año" />
                        <YAxis />
                        <Tooltip />
                        <Line type="monotone" dataKey="valor" stroke="#8b5cf6" strokeWidth={3} />
                      </LineChart>
                    </ResponsiveContainer>
                    <p className="text-xs text-gray-600 mt-2">
                      Reducción del 40% desde 1997 basada en evidencia científica
                    </p>
                  </div>
                </div>

                <div className="p-4 bg-green-50 rounded-lg">
                  <h4 className="font-semibold text-green-900 mb-2">✅ Implementación</h4>
                  <ul className="text-sm space-y-1">
                    <li>• Estados desarrollan SIP (State Implementation Plans)</li>
                    <li>• Zonas de no cumplimiento requieren medidas adicionales</li>
                    <li>• Sistema de permisos de emisión</li>
                    <li>• Monitoreo continuo obligatorio</li>
                  </ul>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          {/* Canadá */}
          <TabsContent value="canada">
            <Card>
              <CardHeader>
                <CardTitle className="text-2xl">🇨🇦 Canadá - CAAQS (Canadian Ambient Air Quality Standards)</CardTitle>
              </CardHeader>
              <CardContent className="space-y-6">
                <Alert>
                  <AlertDescription>
                    Sistema de gestión por <strong>Air Zones</strong> con mejora continua. 
                    Estándares se actualizan cada 5 años.
                  </AlertDescription>
                </Alert>

                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <h3 className="text-lg font-semibold mb-3">📊 Estándares 2020-2025</h3>
                    <div className="overflow-x-auto">
                      <table className="w-full border text-sm">
                        <thead className="bg-red-100">
                          <tr>
                            <th className="border p-2">Contaminante</th>
                            <th className="border p-2">2020</th>
                            <th className="border p-2">2025</th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr><td className="border p-2">PM2.5 (24h)</td><td className="border p-2">27</td><td className="border p-2">25</td></tr>
                          <tr><td className="border p-2">PM2.5 (Anual)</td><td className="border p-2">8.8</td><td className="border p-2">8.0</td></tr>
                          <tr><td className="border p-2">O₃ (8h)</td><td className="border p-2">62</td><td className="border p-2">60</td></tr>
                          <tr><td className="border p-2">NO₂ (1h)</td><td className="border p-2">60</td><td className="border p-2">50</td></tr>
                          <tr><td className="border p-2">SO₂ (1h)</td><td className="border p-2">70</td><td className="border p-2">65</td></tr>
                        </tbody>
                      </table>
                    </div>
                  </div>

                  <div>
                    <h3 className="text-lg font-semibold mb-3">🎯 Gestión por Air Zones</h3>
                    <div className="space-y-2">
                      <div className="p-3 bg-green-100 rounded flex items-center">
                        <span className="text-2xl mr-3">🟢</span>
                        <div>
                          <p className="font-semibold">Verde - Achievement</p>
                          <p className="text-xs">Cumple estándares</p>
                        </div>
                      </div>
                      <div className="p-3 bg-yellow-100 rounded flex items-center">
                        <span className="text-2xl mr-3">🟡</span>
                        <div>
                          <p className="font-semibold">Amarillo - Management</p>
                          <p className="text-xs">Requiere gestión</p>
                        </div>
                      </div>
                      <div className="p-3 bg-orange-100 rounded flex items-center">
                        <span className="text-2xl mr-3">🟠</span>
                        <div>
                          <p className="font-semibold">Naranja - Action</p>
                          <p className="text-xs">Acciones requeridas</p>
                        </div>
                      </div>
                      <div className="p-3 bg-red-100 rounded flex items-center">
                        <span className="text-2xl mr-3">🔴</span>
                        <div>
                          <p className="font-semibold">Rojo - Critical</p>
                          <p className="text-xs">Intervención urgente</p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                <div className="p-4 bg-blue-50 rounded-lg">
                  <h4 className="font-semibold mb-2">💡 Innovación Canadiense</h4>
                  <p className="text-sm">
                    Canadá es líder en monitoreo satelital de calidad del aire, modelamiento atmosférico 
                    avanzado, y gestión de incendios forestales. Enfoque de "mejora continua" con 
                    estándares progresivamente más estrictos basados en evidencia científica.
                  </p>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          {/* Línea de Tiempo */}
          <TabsContent value="linea">
            <Card>
              <CardHeader>
                <CardTitle className="text-2xl">⏳ Línea de Tiempo - Evolución de Normativas de Aire</CardTitle>
              </CardHeader>
              <CardContent>
                <ResponsiveContainer width="100%" height={400}>
                  <ScatterChart>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="año" domain={[2000, 2025]} />
                    <YAxis dataKey="dummy" ticks={[]} />
                    <Tooltip content={({ payload }) => {
                      if (payload && payload.length > 0) {
                        const data = payload[0].payload;
                        return (
                          <div className="bg-white p-3 border rounded shadow-lg">
                            <p className="font-bold">{data.año}</p>
                            <p className="text-sm">{data.evento}</p>
                          </div>
                        );
                      }
                      return null;
                    }} />
                    <Scatter 
                      data={timeline.map(item => ({ ...item, dummy: item.entidad === 'OEFA' ? 1 : item.entidad === 'OMS' ? 2 : item.entidad === 'EPA' ? 3 : 4 }))} 
                      fill="#8884d8" 
                    />
                  </ScatterChart>
                </ResponsiveContainer>

                <div className="mt-6 space-y-3">
                  {timeline.map((item, idx) => (
                    <div key={idx} className={`p-3 rounded-lg border-l-4 ${
                      item.entidad === 'OEFA' ? 'bg-purple-50 border-purple-500' :
                      item.entidad === 'OMS' ? 'bg-green-50 border-green-500' :
                      item.entidad === 'EPA' ? 'bg-blue-50 border-blue-500' :
                      'bg-orange-50 border-orange-500'
                    }`}>
                      <div className="flex justify-between items-start">
                        <div>
                          <p className="font-semibold">{item.año} - {item.entidad}</p>
                          <p className="text-sm text-gray-700">{item.evento}</p>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          {/* Plantas Hidroeléctricas vs Termoeléctricas */}
          <TabsContent value="plantas">
            <Card>
              <CardHeader>
                <CardTitle className="text-2xl">⚡ Comparación: Plantas Hidroeléctricas vs Termoeléctricas</CardTitle>
              </CardHeader>
              <CardContent className="space-y-6">
                <Alert className="bg-blue-50">
                  <AlertDescription>
                    Las plantas hidroeléctricas NO emiten contaminantes atmosféricos, mientras que las 
                    termoeléctricas son una fuente significativa de NOx, SO₂ y PM.
                  </AlertDescription>
                </Alert>

                <div>
                  <h3 className="text-lg font-semibold mb-3">📊 Emisiones por Tipo de Planta (mg/Nm³)</h3>
                  <ResponsiveContainer width="100%" height={300}>
                    <BarChart data={plantasComparacion}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="tipo" />
                      <YAxis />
                      <Tooltip />
                      <Legend />
                      <Bar dataKey="emisionNOx" fill="#fbbf24" name="NOx" />
                      <Bar dataKey="emisionSO2" fill="#ef4444" name="SO₂" />
                      <Bar dataKey="emisionPM" fill="#6b7280" name="PM" />
                    </BarChart>
                  </ResponsiveContainer>
                </div>

                <div className="grid grid-cols-2 gap-4">
                  <div className="p-4 bg-green-50 rounded-lg border-2 border-green-500">
                    <h4 className="font-bold text-green-900 mb-3">💧 Hidroeléctrica</h4>
                    <p className="text-sm mb-2"><strong>Ventajas ambientales:</strong></p>
                    <ul className="text-sm space-y-1">
                      <li>✅ Cero emisiones atmosféricas</li>
                      <li>✅ Energía renovable</li>
                      <li>✅ No requiere LMP de aire</li>
                      <li>✅ No contribuye al cambio climático</li>
                    </ul>
                    <p className="text-sm mt-2"><strong>Desventajas:</strong></p>
                    <ul className="text-sm space-y-1">
                      <li>❌ Impacto en ecosistemas acuáticos</li>
                      <li>❌ Desplazamiento de poblaciones</li>
                      <li>❌ Dependencia de disponibilidad hídrica</li>
                    </ul>
                  </div>

                  <div className="p-4 bg-red-50 rounded-lg border-2 border-red-500">
                    <h4 className="font-bold text-red-900 mb-3">🔥 Termoeléctrica</h4>
                    <p className="text-sm mb-2"><strong>Características:</strong></p>
                    <ul className="text-sm space-y-1">
                      <li>⚠️ Alta emisión de NOx y SO₂</li>
                      <li>⚠️ Contribuye a lluvia ácida</li>
                      <li>⚠️ Requiere cumplir LMP estrictos</li>
                      <li>⚠️ Emisiones de CO₂ (calentamiento global)</li>
                    </ul>
                    <p className="text-sm mt-2"><strong>Control de emisiones:</strong></p>
                    <ul className="text-sm space-y-1">
                      <li>🔧 Quemadores Low-NOx</li>
                      <li>🔧 Sistema SCR (Reducción Catalítica)</li>
                      <li>🔧 Desulfuración (FGD)</li>
                      <li>🔧 Filtros de partículas</li>
                    </ul>
                  </div>
                </div>

                <div className="p-4 bg-yellow-50 rounded-lg">
                  <h4 className="font-semibold mb-2">⚖️ Contexto Peruano</h4>
                  <p className="text-sm">
                    Perú tiene una <strong>matriz energética mixta</strong>: aproximadamente 60% hidroeléctrica 
                    y 40% térmica. El desafío es reducir la dependencia de termoeléctricas a diésel/carbón y 
                    transitar hacia gas natural y renovables (solar, eólica) para reducir emisiones atmosféricas 
                    y cumplir con compromisos internacionales de cambio climático.
                  </p>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          {/* Plan de Adecuación */}
          <TabsContent value="pama">
            <Card>
              <CardHeader>
                <CardTitle className="text-2xl">📋 Plan de Adecuación y Manejo Ambiental (PAMA)</CardTitle>
              </CardHeader>
              <CardContent className="space-y-6">
                <Alert>
                  <AlertDescription>
                    El PAMA permite a las empresas adecuarse gradualmente a los LMP mediante inversiones 
                    en tecnología de control de emisiones.
                  </AlertDescription>
                </Alert>

                <div className="grid grid-cols-2 gap-4">
                  <div className="p-4 bg-blue-50 rounded-lg">
                    <h4 className="font-semibold mb-2">🎯 Objetivos del PAMA</h4>
                    <ul className="text-sm space-y-1">
                      <li>✓ Cumplir con LMP vigentes</li>
                      <li>✓ Reducir emisiones progresivamente</li>
                      <li>✓ Implementar mejores tecnologías disponibles</li>
                      <li>✓ Mantener operatividad económica</li>
                      <li>✓ Proteger salud pública</li>
                    </ul>
                  </div>

                  <div className="p-4 bg-green-50 rounded-lg">
                    <h4 className="font-semibold mb-2">📅 Plazos Típicos</h4>
                    <ul className="text-sm space-y-1">
                      <li><strong>Diagnóstico:</strong> 3 meses</li>
                      <li><strong>Ingeniería:</strong> 6-9 meses</li>
                      <li><strong>Adquisición:</strong> 6-12 meses</li>
                      <li><strong>Instalación:</strong> 12-18 meses</li>
                      <li><strong>Pruebas:</strong> 3-6 meses</li>
                      <li><strong>Total:</strong> 24-36 meses</li>
                    </ul>
                  </div>
                </div>

                <div>
                  <h4 className="font-semibold mb-3">💰 Costos Estimados de Tecnologías de Control</h4>
                  <div className="overflow-x-auto">
                    <table className="w-full border text-sm">
                      <thead className="bg-indigo-100">
                        <tr>
                          <th className="border p-2">Tecnología</th>
                          <th className="border p-2">Contaminante</th>
                          <th className="border p-2">Eficiencia</th>
                          <th className="border p-2">Costo (USD)</th>
                          <th className="border p-2">Plazo</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr><td className="border p-2">Sistema SCR</td><td className="border p-2">NOx</td><td className="border p-2">&gt;90%</td><td className="border p-2">$2-5 millones</td><td className="border p-2">12-18 meses</td></tr>
                        <tr><td className="border p-2">Desulfuración (FGD)</td><td className="border p-2">SO₂</td><td className="border p-2">&gt;95%</td><td className="border p-2">$5-10 millones</td><td className="border p-2">18-24 meses</td></tr>
                        <tr><td className="border p-2">Quemadores Low-NOx</td><td className="border p-2">NOx</td><td className="border p-2">30-50%</td><td className="border p-2">$500k-1M</td><td className="border p-2">6-12 meses</td></tr>
                        <tr><td className="border p-2">Filtros de mangas</td><td className="border p-2">PM</td><td className="border p-2">&gt;99%</td><td className="border p-2">$1-3 millones</td><td className="border p-2">9-15 meses</td></tr>
                      </tbody>
                    </table>
                  </div>
                </div>

                <div className="p-4 bg-yellow-50 rounded-lg">
                  <h4 className="font-semibold mb-2">⚠️ Caso 2: Central Termoeléctrica</h4>
                  <p className="text-sm mb-2">
                    Tu caso involucra una central que reporta excedencias de LMP de NOx y SO₂ <strong>durante 
                    arranques y paradas programadas</strong>, y alega cumplimiento parcial del PAMA.
                  </p>
                  <p className="text-sm font-semibold">Preguntas clave para análisis:</p>
                  <ul className="text-sm space-y-1 mt-2">
                    <li>1. ¿Las excedencias durante arranques/paradas están contempladas en la normativa?</li>
                    <li>2. ¿El PAMA incluye medidas para estos eventos operacionales?</li>
                    <li>3. ¿Existe reincidencia o es la primera vez?</li>
                    <li>4. ¿Hay atenuantes (inversión en tecnología) o agravantes (impacto en población)?</li>
                    <li>5. ¿Qué medidas técnicas inmediatas se pueden implementar?</li>
                  </ul>
                </div>
              </CardContent>
            </Card>
          </TabsContent>
        </Tabs>

        {/* Footer */}
        <div className="mt-8 p-4 bg-white rounded-lg shadow text-center">
          <p className="text-sm text-gray-600">
            <strong>Universidad Nacional de Moquegua</strong> | Facultad de Ingeniería y Arquitectura
          </p>
          <p className="text-sm text-gray-600">
            Curso: Contaminación y Control Atmosférico | Prof. Dr. José Antonio Valeriano Zapana
          </p>
          <p className="text-xs text-gray-500 mt-2">
            © 2024-2025 | Sistema basado en normativas oficiales de OEFA, OMS, EPA y Canadá
          </p>
        </div>
      </div>
    </div>
  );
};

export default AirQualityApp;
