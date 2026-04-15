# Funciones para cálculo de métricas
 
#funcion 1: promedio señal
def calcular_promedio_senal(datos_validos):
   """
    Calcular el promedio de los valores de la señal entre todos los participantes. 

    Parameters
    ----------
    datos_validos : list
        Lista de datos de participantes (cada participante es un diccionario)
   
    Returns
    -------
    float: numero que representa el promedio de la señal de todos los participantes, o 0 si no hay datos válidos.

   """
   if len(datos_validos) == 0:
        raise ValueError("No hay datos para calcular el promedio") 

   suma=0
   cantidad=0

   for participante in datos_validos:
    if "valor" not in participante:
            raise ValueError("Falta la clave 'valor' en los datos")

     for senal in participante["valor"]:
       suma+=senal
       cantidad+=1
       
  
   if cantidad == 0:
        raise ValueError("No hay valores de señal")
  
   promedio=suma/cantidad
   return promedio

#funcion 2: maximo
def calcular_maximo_senal(datos_validos):
   """
   Calcular el maximo de los valores de la señal entre todos los participantes. 

   Parameters
   ----------
   datos_validos : list
        Lista de datos de participantes (cada participante es un diccionario)
   
   Returns
   -------
   float: numero que representa el maximo de la señal de todos los participantes.

   """
   if len(datos_validos) == 0:
        raise ValueError("No hay datos para calcular el máximo")

   maximo = None

   for participante in datos_validos:
     for valor in participante["valor"]:
       if maximo is None or valor>maximo:
         maximo=valor
   return maximo

#funcion 3: minimo
def calcular_minimo_senal(datos_validos):

   """
   Calcular el minimo de los valores de la señal entre todos los participantes. 

   Parameters
   ----------
   datos_validos : list
        Lista de datos de participantes (cada participante es un diccionario)
   
   Returns
   -------
   float: numero que representa el minimo de la señal de todos los participantes.

   """
   if len(datos_validos) == 0:
        raise ValueError("No hay datos para calcular el minimo")

   minimo= None

   for participante in datos_validos:
     for valor in participante["valor"]:
       valor_int= int(valor)
       if minimo is None or valor_int<minimo:
         minimo=valor
   return minimo
#funcion 4: calcular frecuencia y picos
from src.utils_ecg import detectar_picos_qrs
def calcular_fc_desde_datos(datos):
   tiempos = []
   senal = []
   for d in datos:
     tiempos.append(d["tiempo"])
     senal.append(d["valor"])
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
        raise ValueError("No hay suficientes picos para calcular frecuencia cardíaca")

    intervalos = []

    for i in range(1, len(picos)):
        intervalo = picos[i] - picos[i - 1]
        intervalos.append(intervalo)

    promedio_intervalo = sum(intervalos) / len(intervalos)

    if promedio_intervalo == 0:
        raise ValueError("Intervalo inválido")

    frecuencia = 60 / promedio_intervalo

    return frecuencia

