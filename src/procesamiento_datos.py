
# Funciones para procesamiento de datos

def filtrar_datos(datos, id_participante):
   """
    Filtrar los datos procesados por participante a partir de su id. 

    Parameters
    ----------
    datos : list
        Lista de datos de participantes
    id_participante : int
        Numero de id del participante

    Returns
    -------
    dict: diccionario con el id del participante y los datos filtrados 

   """

   dicc_filtrados = {}
   id_participantes = int(id_participante)
   if id_participantes <= 0: 
      raise ValueError("id invalido") 
           
   for dato in datos: 
      id_f = dato["id"]
      if id_f == id_participantes: 
         dicc_filtrados.append(dato)
   
    
   return dicc_filtrados


