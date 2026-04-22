
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
   datos_filtrados=[]
   while True:
      id_participante= input("Ingrese ID del participante o -todos- para analizar todos los participantes: ")
     
      if id_participante=="todos":
         datos_filtrados = datos
         
      elif id_participante.isdigit():
            
      
            id_participante_int = int(id_participante)
            if id_participante_int <= 0: 
               raise ValueError("ERROR CRITICO: id invalido- Ubicacion: filtrar_datos in procesamiento_datos") 
               
            encontrado = False 
         
            for participante in datos: 
               id_f = participante["id_participante"]
               if id_f == id_participante_int: 
                  datos_filtrados.append(participante)
                  encontrado = True
                  break
               
            if encontrado == False: 
               print("ID no encontrado. Intente nuevamente")
                 
      else:
         raise ValueError("ERROR CRITICO: Dato ingresado no valido - Ubicacion: filtrar_datos in procesamiento_datos")
         continue
      pregunta = input("Desea seguir preguntando? ")
     
      if pregunta == "No": 
         break 
         
   return datos_filtrados

