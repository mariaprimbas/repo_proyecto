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
- metricas: se encarga de revisar que loos valores sean los adecuados para calcular promedio, mínimo, máximo. Percibe algunos de tipo ValueError.
- procesamiento: verificar que el id ingresado sea valido y agregar la informacion a la lista si hay tal.

  Cambios hechos en cargar_datos:

Corregi la lectura del archivo porque el dataset no tiene encabezado.
Corregi el uso de id_participante para que siempre sea un número y no haya errores.
Corregi la validacion de las lineas
Corregi como se guardan los datos para que se agrupen bien por participante.
Corregi un par de errores en el codigo
