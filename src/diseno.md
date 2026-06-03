
Diseño del Sistema PulseLab
Descripción General
El sistema PulseLab permite analizar señales fisiológicas registradas en archivos CSV. El programa carga los datos experimentales, realiza validaciones defensivas, calcula métricas descriptivas y genera visualizaciones para facilitar el análisis de los participantes.

El proyecto posee dos formas de ejecución:

main.py: ejecución por consola.

app.py: dashboard web desarrollado con Streamlit.

Arquitectura del Sistema
Frontend
Streamlit (app.py)

Interfaz web para carga de archivos CSV.

Visualización de métricas mediante tarjetas KPI.

Visualización de gráficos generados por el backend.

Backend
Implementado mediante módulos independientes dentro de src/.

procesamiento_datos.py
Responsable de: Filtrar registros por participante. Preparar subconjuntos de datos para análisis.

metricas.py
Responsable de:
calcular promedio de señal. Calcular máximos y mínimos. Detectar picos QRS. Estimar frecuencia cardíaca.

Flujo de Ejecución
El usuario carga un archivo CSV. El sistema valida los datos. Si existe un error, se muestra un mensaje mediante st.error().
Si los datos son válidos: Se muestran los primeros registros.Se selecciona un participante.Se calculan métricas descriptivas.Se generan gráficos. Se muestran KPIs y visualizaciones en la interfaz.

Tecnologías Utilizadas
Python, Pandas, Matplotlib, Streamlit

Estructura del Proyecto
TA_programacion/
│
├── app.py
├── main.py
├── README.md
├── datos/
├── diagramas/
└── src/
    ├── diseño.md
    ├── procesamiento_datos.py
    ├── metricas.py
    └── utils_ecg.py
    ├── graficos/
