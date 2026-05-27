
# Funciones para procesamiento de datos

def filtrar_datos(df, id_participante):
   """
    Filtrar los datos de un Dataframe por participante a partir de su id. 

    Parameters
    ----------
    df : DataFrame
      Dataframe con datos de los participantes 
    id_participante: int
      id ingresado que define los datos del participante que quiere filtrar 
      
    Returns
    -------
    Dataframe: datos filtrados 

   """
   if id_participante=="todos":
      datos_filtrados = df

   else: 
      datos_filtrados = df[df["id_participante"] == id_participante]

   return datos_filtrados 
         
   
