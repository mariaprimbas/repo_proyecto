#Programa Principal 


from src.carga_datos import cargar_datos
from src.validacion_datos import validar_registro
from src.metricas import calcular_minimo_senal
from src.metricas import calcular_maximo_senal
from src.metricas import calcular_promedio_senal
from src.procesamiento_datos import filtrar_datos
from src.utils_ecg import detectar_picos_qrs
from src.metricas import calcular_frecuencia_cardiaca

datos= cargar_datos("datos/PulseLab_mock_data.csv")

datos_validos= []

for registro in datos:
    if validar_registro(registro):
        datos_validos.append(registro)

id_participante = input("Ingrese un id: ")

datos_filtrados= filtrar_datos(datos_validos, id_participante)
promedio= calcular_promedio_senal(datos_filtrados)
minimo= calcular_minimo_senal(datos_filtrados)
maximo= calcular_maximo_senal(datos_filtrados)
picos= detectar_picos_qrs()
fc= calcular_frecuencia_cardiaca(picos)

resultado= (promedio, minimo, maximo)

print(resultado)
