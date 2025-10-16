import React, { useState } from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { Alert, AlertDescription } from '@/components/ui/alert';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, LineChart, Line, ScatterChart, Scatter } from 'recharts';

const AirQualityApp = () => {
  const [activeTab, setActiveTab] = useState('oms');

  const airStandards = {
    pm25: [
      { entidad: 'OMS 2021', anual: 5, dia24h: 15 },
      { entidad: 'OEFA Peru', anual: 25, dia24h: 50 },
      { entidad: 'EPA USA', anual: 9, dia24h: 35 },
      { entidad: 'Canada', anual: 8.8, dia24h: 27 }
    ],
    pm10: [
      { entidad: 'OMS 2021', anual: 15, dia24h: 45 },
      { entidad: 'OEFA Peru', anual: 50, dia24h: 100 },
      { entidad: 'EPA USA', anual: null, dia24h: 150 },
      { entidad: 'Canada', anual: null, dia24h: 50 }
    ],
    no2: [
      { entidad: 'OMS 2021', anual: 10, dia24h: 25, hora1: null },
      { entidad: 'OEFA Peru', anual: 100, dia24h: null, hora1: 200 },
      { entidad: 'EPA USA', anual: 53, dia24h: null, hora1: 100 },
      { entidad: 'Canada', anual: null, dia24h: null, hora1: 60 }
    ],
    so2: [
      { entidad: 'OMS 2021', dia24h: 40 },
      { entidad: 'OEFA Peru', dia24h: 250 },
      { entidad: 'EPA USA', hora1: 75 },
      { entidad: 'Canada', hora1: 70 }
    ],
    o3: [
      { entidad: 'OMS 2021', hora8: 100 },
      { entidad: 'OEFA Peru', hora8: 100 },
      { entidad: 'EPA USA', hora8: 70 },
      { entidad: 'Canada', hora8: 62 }
    ]
  };

  const lmpThermoelectric = [
    { contaminante: 'NOx', gasNatural: 320, diesel: 850, residual: 2000, unidad: 'mg/Nm3' },
    { contaminante: 'SO2', gasNatural: null, diesel: 1700, residual: 3500, unidad: 'mg/Nm3' },
    { contaminante: 'PM', gasNatural: 50, diesel: 150, residual: 350, unidad: 'mg/Nm3' }
  ];

  const timeline = [
    { año: 2001, evento: 'D.S. 074-2001-PCM - Primeros ECA Aire Peru', entidad: 'OEFA' },
    { año: 2005, evento: 'OMS - Guias Calidad del Aire', entidad: 'OMS' },
    { año: 2010, evento: 'D.S. 003-2010-MINAM - LMP Termoelectricas', entidad: 'OEFA' },
    { año: 2013, evento: 'EPA - PM2.5 Anual reducido a 12 ug/m3', entidad: 'EPA' },
    { año: 2017, evento: 'D.S. 003-2017-MINAM - ECA Aire mas estrictos', entidad: 'OEFA' },
    { año: 2019, evento: 'D.S. 010-2019-MINAM - Modificatoria ECA', entidad: 'OEFA' },
    { año: 2020, evento: 'EPA - Fortalece PM2.5', entidad: 'EPA' },
    { año: 2021, evento: 'OMS - Nuevas Directrices (50% mas estrictas)', entidad: 'OMS' },
    { año: 2022, evento: 'Canada - Actualizacion CAAQS', entidad: 'Canada' },
    { año: 2024, evento: 'EPA - PM2.5 Anual a 9.0 ug/m3', entidad: 'EPA' }
  ];

  const plantasComparacion = [
    { tipo: 'Hidroelectrica', emisionNOx: 0, emisionSO2: 0, emisionPM: 0, impactoAire: 'Nulo' },
    { tipo: 'Termoelectrica Gas', emisionNOx: 280, emisionSO2: 0, emisionPM: 40, impactoAire: 'Moderado' },
    { tipo: 'Termoelectrica Diesel', emisionNOx: 750, emisionSO2: 1500, emisionPM: 130, impactoAire: 'Alto' },
    { tipo: 'Termoelectrica Carbon', emisionNOx: 1800, emisionSO2: 3200, emisionPM: 320, impactoAire: 'Muy Alto' }
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-6">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-indigo-900 mb-2">
            Sistema Integral de Normativas de Calidad del Aire
          </h1>
          <p className="text-lg text-gray-700">
            Caso 2: Central Termoelectrica - Analisis de LMP en NOx/SO2
          </p>
          <p className="text-sm text-gray-600 mt-2">
            Universidad Nacional de Moquegua | Prof. Dr. Jose Antonio Valeriano Zapana
          </p>
        </div>

        <Tabs value={activeTab} onValueChange={setActiveTab} className="w-full">
          <TabsList className="grid w-full grid-cols-7 mb-6">
            <TabsTrigger value="oms">OMS</TabsTrigger>
            <TabsTrigger value="oefa">OEFA Peru</TabsTrigger>
            <TabsTrigger value="epa">EPA USA</TabsTrigger>
            <TabsTrigger value="canada">Canada</TabsTrigger>
            <TabsTrigger value="linea">Linea Tiempo</TabsTrigger>
            <TabsTrigger value="plantas">Plantas</TabsTrigger>
            <TabsTrigger value="pama">PAMA</TabsTrigger>
          </TabsList>

          <TabsContent value="oms">
            <Card>
              <CardHeader>
                <CardTitle className="text-2xl">Organizacion Mundial de la Salud (OMS)</CardTitle>
              </CardHeader>
              <CardContent className="space-y-6">
                <Alert>
                  <AlertDescription>
                    Las directrices de la OMS 2021 son las mas estrictas del mundo. Representan niveles 
                    de calidad del aire que protegen la salud publica segun la mejor evidencia cientifica disponible.
                  </AlertDescription>
                </Alert>

                <div>
                  <h3 className="text-xl font-semibold mb-3 text-indigo-800">Material Particulado PM2.5</h3>
                  <ResponsiveContainer width="100%" height={300}>
                    <BarChart data={airStandards.pm25}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="entidad" />
                      <YAxis label={{ value: 'ug/m3', angle: -90, position: 'insideLeft' }} />
                      <Tooltip />
                      <Legend />
                      <Bar dataKey="anual" fill="#4f46e5" name="Anual" />
                      <Bar dataKey="dia24h" fill="#818cf8" name="24 horas" />
                    </BarChart>
                  </ResponsiveContainer>
                  <div className="mt-4 p-4 bg-blue-50 rounded-lg">
                    <p className="text-sm"><strong>OMS 2021:</strong> Anual 5 ug/m3, 24h 15 ug/m3</p>
                    <p className="text-sm mt-2"><strong>Impacto en salud:</strong> Enfermedades cardiovasculares, 
                    cancer de pulmon, muerte prematura. PM2.5 es el contaminante mas peligroso por su tamano microscopico.</p>
                  </div>
                </div>

                <div>
                  <h3 className="text-xl font-semibold mb-3 text-indigo-800">Material Particulado PM10</h3>
                  <ResponsiveContainer width="100%" height={300}>
                    <BarChart data={airStandards.pm10}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="entidad" />
                      <YAxis label={{ value: 'ug/m3', angle: -90, position: 'insideLeft' }} />
                      <Tooltip />
                      <Legend />
                      <Bar dataKey="anual" fill="#10b981" name="Anual" />
                      <Bar dataKey="dia24h" fill="#6ee7b7" name="24 horas" />
                    </BarChart>
                  </ResponsiveContainer>
                </div>

                <div>
                  <h3 className="text-xl font-semibold mb-3 text-indigo-800">Dioxido de Nitrogeno (NO2)</h3>
                  <div className="grid grid-cols-3 gap-4">
                    <div className="p-4 bg-yellow-50 rounded-lg text-center">
                      <p className="text-2xl font-bold text-yellow-700">10</p>
                      <p className="text-sm">ug/m3 Anual</p>
                      <p className="text-xs text-gray-600">OMS 2021</p>
                    </div>
                    <div className="p-4 bg-orange-50 rounded-lg text-center">
                      <p className="text-2xl font-bold text-orange-700">25</p>
                      <p className="text-sm">ug/m3 24h</p>
                      <p className="text-xs text-gray-600">OMS 2021</p>
                    </div>
                    <div className="p-4 bg-red-50 rounded-lg text-center">
                      <p className="text-2xl font-bold text-red-700">100</p>
                      <p className="text-sm">ug/m3 Anual</p>
                      <p className="text-xs text-gray-600">OEFA Peru</p>
                    </div>
                  </div>
                  <p className="text-sm mt-3 text-gray-700">
                    <strong>Fuente principal:</strong> Trafico vehicular, termoelectricas. 
                    <strong> Efectos:</strong> Irritacion respiratoria, asma, precursor de ozono.
                  </p>
                </div>

                <div>
                  <h3 className="text-xl font-semibold mb-3 text-indigo-800">Dioxido de Azufre (SO2)</h3>
                  <ResponsiveContainer width="100%" height={250}>
                    <BarChart data={airStandards.so2}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="entidad" />
                      <YAxis label={{ value: 'ug/m3', angle: -90, position: 'insideLeft' }} />
                      <Tooltip />
                      <Bar dataKey="dia24h" fill="#ef4444" name="24 horas" />
                      <Bar dataKey="hora1" fill="#f87171" name="1 hora" />
                    </BarChart>
                  </ResponsiveContainer>
                  <p className="text-sm mt-3 text-gray-700">
                    <strong>Fuente:</strong> Quema de carbon, refinacion de petroleo, fundicion de metales.
                    <strong> Impacto:</strong> Lluvia acida, irritacion respiratoria severa.
                  </p>
                </div>

                <div>
                  <h3 className="text-xl font-semibold mb-3 text-indigo-800">Ozono Troposferico (O3)</h3>
                  <ResponsiveContainer width="100%" height={250}>
                    <BarChart data={airStandards.o3}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="entidad" />
                      <YAxis label={{ value: 'ug/m3', angle: -90, position: 'insideLeft' }} />
                      <Tooltip />
                      <Bar dataKey="hora8" fill="#8b5cf6" name="8 horas" />
                    </BarChart>
                  </ResponsiveContainer>
                  <p className="text-sm mt-3 text-gray-700">
                    <strong>Contaminante secundario:</strong> No se emite directamente, se forma por reaccion 
                    fotoquimica entre NOx y VOCs bajo luz solar. Niveles mas altos en dias soleados.
                  </p>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          <TabsContent value="oefa">
            <Card>
              <CardHeader>
                <CardTitle className="text-2xl">OEFA - Organismo de Evaluacion y Fiscalizacion Ambiental</CardTitle>
              </CardHeader>
              <CardContent className="space-y-6">
                <Alert className="bg-indigo-50 border-indigo-200">
                  <AlertDescription>
                    <strong>Marco legal principal:</strong> D.S. N 003-2017-MINAM (ECA Aire) y 
                    D.S. N 003-2010-MINAM (LMP para Termoelectricas)
                  </AlertDescription>
                </Alert>

                <div>
                  <h3 className="text-xl font-semibold mb-3">Estandares de Calidad Ambiental (ECA) - Aire</h3>
                  <div className="overflow-x-auto">
                    <table className="w-full border-collapse border border-gray-300">
                      <thead className="bg-indigo-100">
                        <tr>
                          <th className="border p-2">Contaminante</th>
                          <th className="border p-2">Periodo</th>
                          <th className="border p-2">Valor ECA</th>
                          <th className="border p-2">Unidad</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr><td className="border p-2">PM2.5</td><td className="border p-2">24 horas</td><td className="border p-2 font-bold">50</td><td className="border p-2">ug/m3</td></tr>
                        <tr><td className="border p-2">PM2.5</td><td className="border p-2">Anual</td><td className="border p-2 font-bold">25</td><td className="border p-2">ug/m3</td></tr>
                        <tr><td className="border p-2">PM10</td><td className="border p-2">24 horas</td><td className="border p-2 font-bold">100</td><td className="border p-2">ug/m3</td></tr>
                        <tr><td className="border p-2">PM10</td><td className="border p-2">Anual</td><td className="border p-2 font-bold">50</td><td className="border p-2">ug/m3</td></tr>
                        <tr className="bg-yellow-50"><td className="border p-2">NO2</td><td className="border p-2">1 hora</td><td className="border p-2 font-bold">200</td><td className="border p-2">ug/m3</td></tr>
                        <tr className="bg-yellow-50"><td className="border p-2">NO2</td><td className="border p-2">Anual</td><td className="border p-2 font-bold">100</td><td className="border p-2">ug/m3</td></tr>
                        <tr className="bg-red-50"><td className="border p-2">SO2</td><td className="border p-2">24 horas</td><td className="border p-2 font-bold">250</td><td className="border p-2">ug/m3</td></tr>
                        <tr><td className="border p-2">O3</td><td className="border p-2">8 horas</td><td className="border p-2 font-bold">100</td><td className="border p-2">ug/m3</td></tr>
                        <tr><td className="border p-2">CO</td><td className="border p-2">8 horas</td><td className="border p-2 font-bold">10,000</td><td className="border p-2">ug/m3</td></tr>
                        <tr><td className="border p-2">CO</td><td className="border p-2">1 hora</td><td className="border p-2 font-bold">30,000</td><td className="border p-2">ug/m3</td></tr>
                      </tbody>
                    </table>
                  </div>
                </div>

                <div>
                  <h3 className="text-xl font-semibold mb-3">Limites Maximos Permisibles (LMP) - Termoelectricas</h3>
                  <p className="text-sm mb-3 text-gray-700">
                    D.S. N 003-2010-MINAM | Se miden en la chimenea (punto de emision)
                  </p>
                  <div className="overflow-x-auto">
                    <table className="w-full border-collapse border border-gray-300">
                      <thead className="bg-green-100">
                        <tr>
                          <th className="border p-2">Contaminante</th>
                          <th className="border p-2">Gas Natural</th>
                          <th className="border p-2">Diesel</th>
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
                      <strong>Caso 2:</strong> Tu central termoelectrica reporta excedencias de LMP de NOx 
                      y SO2 durante arranques y paradas programadas. Estos valores aplican en condiciones normales de operacion.
                    </AlertDescription>
                  </Alert>
                </div>

                <div className="grid grid-cols-2 gap-4">
                  <div className="p-4 bg-blue-50 rounded-lg">
                    <h4 className="font-bold text-blue-900 mb-2">ECA (Receptor)</h4>
                    <ul className="text-sm space-y-1">
                      <li>Se mide en el ambiente</li>
                      <li>Protege salud publica</li>
                      <li>Puede tener multiples fuentes</li>
                      <li>Ejemplo: Estacion de monitoreo en poblacion</li>
                    </ul>
                  </div>
                  <div className="p-4 bg-green-50 rounded-lg">
                    <h4 className="font-bold text-green-900 mb-2">LMP (Fuente)</h4>
                    <ul className="text-sm space-y-1">
                      <li>Se mide en la chimenea</li>
                      <li>Responsabilidad del titular</li>
                      <li>Control de emisiones industriales</li>
                      <li>Ejemplo: Chimenea de termoelectrica</li>
                    </ul>
                  </div>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          <TabsContent value="epa">
            <Card>
              <CardHeader>
                <CardTitle className="text-2xl">EPA - Environmental Protection Agency (USA)</CardTitle>
              </CardHeader>
              <CardContent className="space-y-6">
                <Alert className="bg-blue-50 border-blue-200">
                  <AlertDescription>
                    <strong>NAAQS (National Ambient Air Quality Standards):</strong> Estandares primarios 
                    (salud) y secundarios (bienestar publico, visibilidad, ecosistemas)
                  </AlertDescription>
                </Alert>

                <div className="grid grid-cols-2 gap-6">
                  <div>
                    <h3 className="text-lg font-semibold mb-3">Estandares Actuales</h3>
                    <div className="space-y-2">
                      <div className="p-3 bg-purple-50 rounded">
                        <p className="font-semibold">PM2.5</p>
                        <p className="text-sm">Anual: <strong>9.0 ug/m3</strong> (2024)</p>
                        <p className="text-sm">24h: <strong>35 ug/m3</strong></p>
                      </div>
                      <div className="p-3 bg-blue-50 rounded">
                        <p className="font-semibold">PM10</p>
                        <p className="text-sm">24h: <strong>150 ug/m3</strong></p>
                      </div>
                      <div className="p-3 bg-yellow-50 rounded">
                        <p className="font-semibold">O3</p>
                        <p className="text-sm">8h: <strong>0.070 ppm</strong></p>
                      </div>
                      <div className="p-3 bg-red-50 rounded">
                        <p className="font-semibold">SO2</p>
                        <p className="text-sm">1h: <strong>75 ppb</strong></p>
                      </div>
                    </div>
                  </div>

                  <div>
                    <h3 className="text-lg font-semibold mb-3">Evolucion PM2.5 Anual</h3>
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
                      Reduccion del 40% desde 1997 basada en evidencia cientifica
                    </p>
                  </div>
                </div>

                <div className="p-4 bg-green-50 rounded-lg">
                  <h4 className="font-semibold text-green-900 mb-2">Implementacion</h4>
                  <ul className="text-sm space-y-1">
                    <li>Estados desarrollan SIP (State Implementation Plans)</li>
                    <li>Zonas de no cumplimiento requieren medidas adicionales</li>
                    <li>Sistema de permisos de emision</li>
                    <li>Monitoreo continuo obligatorio</li>
                  </ul>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          <TabsContent value="canada">
            <Card>
              <CardHeader>
                <CardTitle className="text-2xl">Canada - CAAQS (Canadian Ambient Air Quality Standards)</CardTitle>
              </CardHeader>
              <CardContent className="space-y-6">
                <Alert>
                  <AlertDescription>
                    Sistema de gestion por <strong>Air Zones</strong> con mejora continua. 
                    Estandares se actualizan cada 5 años.
                  </AlertDescription>
                </Alert>

                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <h3 className="text-lg font-semibold mb-3">Estandares 2020-2025</h3>
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
                          <tr><td className="border p-2">O3 (8h)</td><td className="border p-2">62</td><td className="border p-2">60</td></tr>
                          <tr><td className="border p-2">NO2 (1h)</td><td className="border p-2">60</td><td className="border p-2">50</td></tr>
                          <tr><td className="border p-2">SO2 (1h)</td><td className="border p-2">70</td><td className="border p-2">65</td></tr>
                        </tbody>
                      </table>
                    </div>
                  </div>

                  <div>
                    <h3 className="text-lg font-semibold mb-3">Gestion por Air Zones</h3>
                    <div className="space-y-2">
                      <div className="p-3 bg-green-100 rounded">
                        <p className="font-semibold">Verde - Achievement</p>
                        <p className="text-xs">Cumple estandares</p>
                      </div>
                      <div className="p-3 bg-yellow-100 rounded">
                        <p className="font-semibold">Amarillo - Management</p>
                        <p className="text-xs">Requiere gestion</p>
                      </div>
                      <div className="p-3 bg-orange-100 rounded">
                        <p className="font-semibold">Naranja - Action</p>
                        <p className="text-xs">Acciones requeridas</p>
                      </div>
                      <div className="p-3 bg-red-100 rounded">
                        <p className="font-semibold">Rojo - Critical</p>
                        <p className="text-xs">Intervencion urgente</p>
                      </div>
                    </div>
                  </div>
                </div>

                <div className="p-4 bg-blue-50 rounded-lg">
                  <h4 className="font-semibold mb-2">Innovacion Canadiense</h4>
                  <p className="text-sm">
                    Canada es lider en monitoreo satelital de calidad del aire, modelamiento atmosferico 
                    avanzado, y gestion de incendios forestales. Enfoque de mejora continua con 
                    estandares progresivamente mas estrictos basados en evidencia cientifica.
                  </p>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          <TabsContent value="linea">
            <Card>
              <CardHeader>
                <CardTitle className="text-2xl">Linea de Tiempo - Evolucion de Normativas de Aire</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-3">
                  {timeline.map((item, idx) => (
                    <div key={idx} className={`p-3 rounded-lg border-l-4 ${
                      item.entidad === 'OEFA' ? 'bg-purple-50 border-purple-500' :
                      item.entidad === 'OMS' ? 'bg-green-50 border-green-500' :
                      item.entidad === 'EPA' ? 'bg-blue-50 border-blue-500' :
                      'bg-orange-50 border-orange-500'
                    }`}>
                      <p className="font-semibold">{item.año} - {item.entidad}</p>
                      <p className="text-sm text-gray-700">{item.evento}</p>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          <TabsContent value="plantas">
            <Card>
              <CardHeader>
                <CardTitle className="text-2xl">Comparacion: Plantas Hidroelectricas vs Termoelectricas</CardTitle>
              </CardHeader>
              <CardContent className="space-y-6">
                <Alert className="bg-blue-50">
                  <AlertDescription>
                    Las plantas hidroelectricas NO emiten contaminantes atmosfericos, mientras que las 
                    termoelectricas son una fuente significativa de NOx, SO2 y PM.
                  </AlertDescription>
                </Alert>

                <div>
                  <h3 className="text-lg font-semibold mb-3">Emisiones por Tipo de Planta (mg/Nm3)</h3>
                  <ResponsiveContainer width="100%" height={300}>
                    <BarChart data={plantasComparacion}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="tipo" />
                      <YAxis />
                      <Tooltip />
                      <Legend />
                      <Bar dataKey="emisionNOx" fill="#fbbf24" name="NOx" />
                      <Bar dataKey="emisionSO2" fill="#ef4444" name="SO2" />
                      <Bar dataKey="emisionPM" fill="#6b7280" name="PM" />
                    </BarChart>
                  </ResponsiveContainer>
                </div>

                <div className="grid grid-cols-2 gap-4">
                  <div className="p-4 bg-green-50 rounded-lg border-2 border-green-500">
                    <h4 className="font-bold text-green-900 mb-3">Hidroelectrica</h4>
                    <p className="text-sm mb-2"><strong>Ventajas ambientales:</strong></p>
                    <ul className="text-sm space-y-1">
                      <li>Cero emisiones atmosfericas</li>
                      <li>Energia renovable</li>
                      <li>No requiere LMP de aire</li>
                      <li>No contribuye al cambio climatico</li>
                    </ul>
                  </div>

                  <div className="p-4 bg-red-50 rounded-lg border-2 border-red-500">
                    <h4 className="font-bold text-red-900 mb-3">Termoelectrica</h4>
                    <p className="text-sm mb-2"><strong>Caracteristicas:</strong></p>
                    <ul className="text-sm space-y-1">
                      <li>Alta emision de NOx y SO2</li>
                      <li>Contribuye a lluvia acida</li>
                      <li>Requiere cumplir LMP estrictos</li>
                      <li>Emisiones de CO2</li>
                    </ul>
                  </div>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          <TabsContent value="pama">
            <Card>
              <CardHeader>
                <CardTitle className="text-2xl">Plan de Adecuacion y Manejo Ambiental (PAMA)</CardTitle>
              </CardHeader>
              <CardContent className="space-y-6">
                <Alert>
                  <AlertDescription>
                    El PAMA permite a las empresas adecuarse gradualmente a los LMP mediante inversiones 
                    en tecnologia de control de emisiones.
                  </AlertDescription>
                </Alert>

                <div className="grid grid-cols-2 gap-4">
                  <div className="p-4 bg-blue-50 rounded-lg">
                    <h4 className="font-semibold mb-2">Objetivos del PAMA</h4>
                    <ul className="text-sm space-y-1">
                      <li>Cumplir con LMP vigentes</li>
                      <li>Reducir emisiones progresivamente</li>
                      <li>Implementar mejores tecnologias disponibles</li>
                      <li>Mantener operatividad economica</li>
                      <li>Proteger salud publica</li>
                    </ul>
                  </div>

                  <div className="p-4 bg-green-50 rounded-lg">
                    <h4 className="font-semibold mb-2">Plazos Tipicos</h4>
                    <ul className="text-sm space-y-1">
                      <li><strong>Diagnostico:</strong> 3 meses</li>
                      <li><strong>Ingenieria:</strong> 6-9 meses</li>
                      <li><strong>Adquisicion:</strong> 6-12 meses</li>
                      <li><strong>Instalacion:</strong> 12-18 meses</li>
                      <li><strong>Pruebas:</strong> 3-6 meses</li>
                      <li><strong>Total:</strong> 24-36 meses</li>
                    </ul>
                  </div>
                </div>

                <div>
                  <h4 className="font-semibold mb-3">Costos Estimados de Tecnologias de Control</h4>
                  <div className="overflow-x-auto">
                    <table className="w-full border text-sm">
                      <thead className="bg-indigo-100">
                        <tr>
                          <th className="border p-2">Tecnologia</th>
                          <th className="border p-2">Contaminante</th>
                          <th className="border p-2">Eficiencia</th>
                          <th className="border p-2">Costo (USD)</th>
                          <th className="border p-2">Plazo</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr><td className="border p-2">Sistema SCR</td><td className="border p-2">NOx</td><td className="border p-2">&gt;90%</td><td className="border p-2">$2-5 millones</td><td className="border p-2">12-18 meses</td></tr>
                        <tr><td className="border p-2">Desulfuracion (FGD)</td><td className="border p-2">SO2</td><td className="border p-2">&gt;95%</td><td className="border p-2">$5-10 millones</td><td className="border p-2">18-24 meses</td></tr>
                        <tr><td className="border p-2">Quemadores Low-NOx</td><td className="border p-2">NOx</td><td className="border p-2">30-50%</td><td className="border p-2">$500k-1M</td><td className="border p-2">6-12 meses</td></tr>
                        <tr><td className="border p-2">Filtros de mangas</td><td className="border p-2">PM</td><td className="border p-2">&gt;99%</td><td className="border p-2">$1-3 millones</td><td className="border p-2">9-15 meses</td></tr>
                      </tbody>
                    </table>
                  </div>
                </div>

                <div className="p-4 bg-yellow-50 rounded-lg">
                  <h4 className="font-semibold mb-2">Caso 2: Central Termoelectrica</h4>
                  <p className="text-sm mb-2">
                    Tu caso involucra una central que reporta excedencias de LMP de NOx y SO2 <strong>durante 
                    arranques y paradas programadas</strong>, y alega cumplimiento parcial del PAMA.
                  </p>
                  <p className="text-sm font-semibold">Preguntas clave para analisis:</p>
                  <ul className="text-sm space-y-1 mt-2">
                    <li>1. Las excedencias durante arranques/paradas estan contempladas en la normativa?</li>
                    <li>2. El PAMA incluye medidas para estos eventos operacionales?</li>
                    <li>3. Existe reincidencia o es la primera vez?</li>
                    <li>4. Hay atenuantes (inversion en tecnologia) o agravantes (impacto en poblacion)?</li>
                    <li>5. Que medidas tecnicas inmediatas se pueden implementar?</li>
                  </ul>
                </div>
              </CardContent>
            </Card>
          </TabsContent>
        </Tabs>

        <div className="mt-8 p-4 bg-white rounded-lg shadow text-center">
          <p className="text-sm text-gray-600">
            <strong>Universidad Nacional de Moquegua</strong> | Facultad de Ingenieria y Arquitectura
          </p>
          <p className="text-sm text-gray-600">
            Curso: Contaminacion y Control Atmosferico | Prof. Dr. Jose Antonio Valeriano Zapana
          </p>
          <p className="text-xs text-gray-500 mt-2">
            2024-2025 | Sistema basado en normativas oficiales de OEFA, OMS, EPA y Canada
          </p>
        </div>
      </div>
    </div>
  );
};

export default AirQualityApp;
