
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

   filtrados = []
   id_participantes = int(id_participante)
   if id_participantes <= 0: 
           raise ValueError("id invalido") 
           
   for dato in datos: 
       id_f = dato["id"]
       try: 
           if id_f == id_participantes: 
               filtrados.append(dato)
       except KeyError: 
               continue 
            
   dicc_filtrados = {"id_participante": id_participantes, "datos": filtrados}
    
   return dicc_filtrados


