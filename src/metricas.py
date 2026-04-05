# Funciones para cálculo de métricas

#funcion 1: promedio señal
def calcular_promedio_senal(datos_validos):
  suma=0
  cantidad=0

  for participante in datos_validos:
    for senal in participante["valor"]:
      suma+=senal
      cantidad+=1
  
  if cantidad==0:
    return 0
  
  promedio=suma/cantidad
  return promedio

#funcion maximo
def calcular_maximo_senal(datos_validos):
  maximo= None

   for participante in datos_validos:
    for valor in participante["valor"]:
      if maximo is None or valor>maximo:
        maximo=valor
  return maximo

#funcion minimo
def calcular_minimo_senal(datos_validos):
  minimo= None

   for participante in datos_validos:
    for valor in participante["valor"]:
      if minimo is None or valor<minimo:
        minimo=valor
  return minimo

#Programa Principal 
promedio_senal_datos=calcular_promedio_senal(datos_validos)

maximo_senal_datos=calcular_maximo_senal(datos_validos)

minimo_senal_datos=calcular_minimo_senal(datos_validos)