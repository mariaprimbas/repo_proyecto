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
   Calcular el maximo de los valores de la señal del participante. 

   Parameters
   ----------
   datos_filtrados : dict
        diccionario de datos del participante
        
   
   Returns   
   -------
   float: numero que representa el maximo de la señal del participante

   """
   if len(datos_filtrados) == 0:
        raise ValueError("ERROR CRITICO: No hay datos para calcular el máximo - Ubicacion: calcular_maximo_senal in metricas")

   maximo= None
   for elemento in datos_filtrados:
       valores = elemento["valor"]
       for valor in valores: 
           valor_int= int(valor)
           if maximo is None or valor_int>maximo:
               maximo=valor_int
   return maximo

#funcion 3: minimo
def calcular_minimo_senal(datos_filtrados):

   """
   Calcular el minimo de los valores de la señal del participante

   Parameters
   ----------
   datos_filtrados : dict
        diccionario de datos del participante
   
   Returns
   -------
   float: numero que representa el minimo de la señal del participante

   """
   if len(datos_filtrados) == 0:
        raise ValueError("ERROR CRITICO: No hay datos para calcular el minimo- Ubicacion: calcular_minimo_senal in metricas")

   minimo= None
   for elemento in datos_filtrados:
       valores = elemento["valor"]
       for valor in valores: 
           valor_int = int(valor)
           if minimo is None or valor_int<minimo:
               minimo=valor_int
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

