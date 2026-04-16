
# Funciones para procesamiento de datos

def filtrar_datos(datos):
   """
    Filtrar los datos procesados por participante a partir de su id. 

    Parameters
    ----------
    datos : list
        Lista de datos de un participante, o todos los participantes

    Returns
    -------
    dict: diccionario con los datos filtrados del id buscado

   """

   while True:
      id_participante= input("Ingrese ID del participante o -todos- para analizar todos los participantes")
      if id_participante=="todos":
         return datos
      elif id_participante.isdigit():
      
            id_participante_int = int(id_participante)
            if id_participante_int <= 0: 
               raise ValueError("id invalido") 
           
            for participante in datos: 
               id_f = participante["id"]
               if id_f == id_participante_int: 
                  return [participante]
               else:
                  print("ID no encontrado. Intente nuevamente")
                  continue
      else:
         raise ValueError("Dato ingresado no valido")
         continue
   
    


