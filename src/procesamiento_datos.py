
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
   
   if id_participante <= 0: 
           raise ValueError("id invalido") 
           
   for dato in datos: 
       id_f = dato["id"]
       try: 
           if id_f == id_participante: 
               filtrados.append(dato)
       except KeyError: 
               continue 
            
   dicc_filtrados = {"id_participante": id_participante, "datos": filtrados}
    
   return dicc_filtrados


