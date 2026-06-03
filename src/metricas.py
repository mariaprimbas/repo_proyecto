# Funciones para cálculo de métricas
 
#funcion 1: promedio señal
def calcular_promedio_senal(datos_filtrados):
    """
    Calcula el promedio de los valores de señal.

    Parameters
    ----------
    datos_filtrados : dataframe 
        DataFrame con datos de uno o varios participantes.

    Returns
    -------
    float
        Promedio de la señal.

    Raises
    ------
    ValueError
        Si no hay datos para calcular el promedio.
    """

    if datos_filtrados.empty:
        raise ValueError(
            "ERROR CRITICO: No hay datos para calcular el promedio"
        )

    cantidad = datos_filtrados["valor"].count()

    if cantidad == 0:
        raise ValueError(
            "ERROR CRITICO: No hay valores de señal"
        )
    promedio = datos_filtrados["valor"].mean()

    return promedio
  
#funcion 2: maximo
def calcular_maximo_senal(datos_filtrados):
    """
    Calcula el máximo de los valores de señal.

    Parameters
    ----------
    datos_filtrados : dataframe
        DataFrame con datos de uno o varios participantes.

    Returns
    -------
    float
        Máximo de la señal.

    Raises
    ------
    ValueError
        Si no hay datos para calcular el máximo.
    """

    if datos_filtrados.empty:
        raise ValueError(
            "ERROR CRITICO: No hay datos para calcular el máximo"
        )

    cantidad = datos_filtrados["valor"].count()

    if cantidad == 0:
        raise ValueError(
            "ERROR CRITICO: No hay valores de señal"
        )

    maximo = datos_filtrados["valor"].max()

    return maximo

#funcion 3: minimo
def calcular_minimo_senal(datos_filtrados):
    """
    Calcula el minimo de los valores de señal.

    Parameters
    ----------
    datos_filtrados : dataframe
        DataFrame con datos de uno o varios participantes.

    Returns
    -------
    float
        minimo de la señal.

    Raises
    ------
    ValueError
        Si no hay datos para calcular el minimo.
    """

    if datos_filtrados.empty:
        raise ValueError(
            "ERROR CRITICO: No hay datos para calcular el minimo"
        )

    cantidad = datos_filtrados["valor"].count()

    if cantidad == 0:
        raise ValueError(
            "ERROR CRITICO: No hay valores de señal"
        )

    minimo = datos_filtrados["valor"].min()

    return minimo

#funcion 4: calcular frecuencia y picos
from src.utils_ecg import detectar_picos_qrs
def calcular_fc_desde_datos(datos):
   tiempos = []
   senal = []
   for d in datos:
       try:
           for t in d["tiempo"]:
               tiempos.append(t)
           for s in d["valor"]:
               senal.append(float(s))
    
       except:
               raise ValueError("Error Crítico: las señales deben ser números")
   picos = detectar_picos_qrs(tiempos, senal)
   frecuencia_picos=calcular_frecuencia_cardiaca(picos)
   return frecuencia_picos
 
#funcion 5: calcula frecuencia cardiaca
def calcular_frecuencia_cardiaca(picos):
    """
    Calcula la frecuencia cardíaca a partir de los tiempos de los picos detectados por otra funcion

    Parameters
    ----------
    picos : list
        Lista de tiempos donde ocurren los picos

    Returns
    -------
    float: frecuencia cardíaca en latidos por minuto
    """

    if len(picos) < 2:
        raise ValueError("ERROR CRITICO: No hay suficientes picos para calcular frecuencia cardíaca - Ubicacion: calcular_frecuencia_cardiaca in metricas")

    intervalos = []

    for i in range(1, len(picos)):
        intervalo = picos[i] - picos[i - 1]
        intervalos.append(intervalo)

    promedio_intervalo = sum(intervalos) / len(intervalos)

    if promedio_intervalo == 0:
        raise ValueError("ERROR CRITICO: Intervalo inválido   - Ubicacion: calcular_frecuencia_cardiaca in metricas")
    if promedio_intervalo<0:
        raise ValueError("ERROR CRITICO: Intervalo inválido   - Ubicacion: calcular_frecuencia_cardiaca in metricas")
    frecuencia = 60 / promedio_intervalo
    
    return frecuencia

#cargar datos desde streamlit 

def cargar_datos_streamlit(archivo):

    """
    Carga un archivo CSV subido desde Streamlit
    y realiza validaciones vectorizadas sobre los datos.

    Parámetros:
    ----------
    archivo : UploadedFile
        Archivo CSV cargado mediante st.file_uploader.

    Returns:
    -------
    pandas.DataFrame
        DataFrame validado.

    Raises:
    ------
    ValueError
        Si existen errores o inconsistencias
        en los datos.
    """

    # Cargar CSV desde Streamlit
    df = pd.read_csv(archivo,header=None,
        names=["id_participante","tiempo",
            "valor","fase","condicion_experimental",
            "hit"])

    # Validar valores vacíos
    if df.isna().any().any():
        raise ValueError("El archivo contiene valores vacíos o NaN.")

    # Validar tiempos negativos
    if (df["tiempo"] < 0).any():
        raise ValueError("Existen tiempos negativos inválidos.")

    # Validar señal negativa
    if (df["valor"] < 0).any():
        raise ValueError("Existen valores negativos inválidos en la señal.")

    # Validar orden temporal
    if not df["tiempo"].is_monotonic_increasing:
        print("Advertencia: los tiempos no están completamente ordenados.")

    # Validar fases válidas
    fases_validas = ["baseline","tarea"]

    if not df["fase"].isin(fases_validas).all():
        raise ValueError("Se detectaron fases experimentales inválidas.")

    return df
