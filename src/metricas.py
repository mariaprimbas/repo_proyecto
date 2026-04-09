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
   suma=0
   cantidad=0

   for participante in datos_validos:
     for senal in participante["valor"]:
       senal_int= int(senal)
       suma+=senal_int
       cantidad+=1
       
  
   if cantidad==0:
     return 0
  
   promedio=suma/cantidad
   return promedio

#funcion maximo
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
   maximo = None

   for participante in datos_validos:
     for valor in participante["valor"]:
       valor_int= int(valor)
       if maximo is None or valor>maximo:
         maximo=valor
   return maximo

#funcion minimo
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
   minimo= None

   for participante in datos_validos:
     for valor in participante["valor"]:
       valor_int= int(valor)
       if minimo is None or valor_int<minimo:
         minimo=valor
   return minimo
