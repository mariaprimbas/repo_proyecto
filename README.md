# repo_proyecto

Repositorio colaborativo del proyecto - Pulse Lab

Estructura 


Carpetas del repositorio
- src/: funciones del proyecto
- datos/: archivo de datos
- diagramas/: diagramas del flujo
- main.py: programa principal, utiliza las funciones de src

Manejo de errores:
- validacion_datos: Se encarga de validar que los registros sean los correctos, y lo hace identificando si los tipos de datos son los apropiados. Percibe algunos de tipo ValueError y TypeError.
- detectar_picos: se encarga de revisar que los valores de los datos sean los adecuados para llevar a cabo la función. Percibe algunos de tipo ValueError.
- metricas: se encarga de revisar que los valores sean los adecuados para calcular promedio, mínimo, máximo. Percibe algunos de tipo ValueError. Por ejemplo, las listas que recibe deben tener elementos suficientes para realizar el analisis de metricas
- procesamiento: verificar que el id ingresado sea valido y agregar la informacion a la lista si hay tal. 
- cargar_datos:
se corrigio la lectura del archivo porque el dataset no tiene encabezado.
Se corrigio el uso de id_participante para que siempre sea un número y no haya errores.
Se corrigio la validacion de las lineas
Se corrigio como se guardan los datos para que se agrupen bien por participante.
Se corrigio un par de errores en el codigo
Se implementaron validaciones de archivo, formato, tipos de datos, y valores, con manejo de errores

Objetos:
En el caso de la programación orienatda a objetos (POO) plantearíamos 2 clases:
1. Participante
   - Atributos: id, tiempo, valor, fase, condicion experimental y hit
   - Métodos: init, agregar_registro
2. Investigador
   - Atributos: clase Participante
   - Métodos: init, carga_de_datos, filtrado, calcular_promedio, calcular_picos, calcular_frecuencia_cardíaca, mostrar_respuestas

Pandas:
Para introducir la librería Pandas en nuestro trabajo lo haríamos a partir del método pandas.read_csv(). De esta forma se permite acceder al archivo a través de un DataFrame, lo que sintetiza y organiza mejor la información. Como consecuencia, la función parsear_linea() dejaría de requerirse porque la librería Pandas lo realiza por su cuenta. Así pues, la función que se vería más afectada es cargar_datos() que ahora ingresaría a los datos a partir de las columnas del DataFrame. 
En este contexto sería útil la herramienta iloc, ya que nos permitiría poder setear las filas a partir de los id del participante (data.set_index(‘id_participante’) y etiquetar los datos de cada categoría cómo columnas; y así acceder con mayor facilidad. De esta forma, también se sintetiza tareas de la función métricas, cómo sacar el mínimo o máximo que se puede realizar a través de los métodos data[colA].min() o data[colA].max()
