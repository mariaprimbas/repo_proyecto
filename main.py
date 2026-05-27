#Programa Principal 

import pandas as pd
from src.carga_datos import cargar_datos
from src.metricas import calcular_minimo_senal
from src.metricas import calcular_maximo_senal
from src.metricas import calcular_promedio_senal
from src.procesamiento_datos import filtrar_datos
from src.metricas import calcular_fc_desde_datos

ruta_archivo = "datos/PulseLab_mock_data.csv"

df = pd.read_csv(ruta_archivo)
df_indice = df.set_index("id_participante")

id_participante = int(input("Ingrese el id del participante del que desea los datos: "))

datos_filtrados= filtrar_datos(df, id_participante)
promedio= calcular_promedio_senal(datos_filtrados)
minimo= calcular_minimo_senal(datos_filtrados)
maximo= calcular_maximo_senal(datos_filtrados)
fc= calcular_fc_desde_datos(datos_filtrados)

resultado= (f"El promedio es {promedio}, el mínimo es {minimo}, el maximo es {maximo}, y la frecuencia cardíaca es {fc}")

print(resultado)
