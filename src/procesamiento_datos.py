
# Funciones para procesamiento de datos

def filtrar_datos(datos, id_participante):
   """
    Filtrar los datos de un Dataframe por participante a partir de su id. 

    Parameters
    ----------
    datos : DataFrame
      Dataframe con datos de los participantes 
    id_participante: int
      id ingresado que define los datos del participante que quiere filtrar 
      
    Returns
    -------
    Dataframe: datos filtrados 

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
      pregunta = input("Desea seguir buscando un participante? ")
     
      if pregunta.lower() == "no": 
         break 
         
   return datos_filtrados

