#Programa Principal 


from src.carga_datos import cargar_datos
from src.metricas import calcular_minimo_senal
from src.metricas import calcular_maximo_senal
from src.metricas import calcular_promedio_senal
from src.procesamiento_datos import filtrar_datos
from src.metricas import calcular_fc_desde_datos

datos= cargar_datos("datos/PulseLab_mock_data.csv")

datos_validos= []

for registro in datos:
    datos_validos.append(registro)
    
datos_filtrados= filtrar_datos(datos_validos)
promedio= calcular_promedio_senal(datos_filtrados)
minimo= calcular_minimo_senal(datos_filtrados)
maximo= calcular_maximo_senal(datos_filtrados)
fc= calcular_fc_desde_datos(datos_filtrados)

resultado= (f"El promedio es {promedio}, el mínimo es {minimo}, el maximo es {maximo}, y la frecuencia cardíaca es {fc}")

print(resultado)
