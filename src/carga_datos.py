def cargar_datos(ruta_archivo):
    '''
    Leer un archivo y transformar su contenido en un dataframe

    Parameters
    ----------
    ruta_archivo : str
        Ruta del archivo que contiene los datos.

    Returns
    -------
    list
        Lista con los registros agrupados por participante.
    '''
    import pandas as pd
    df = pd.read_csv("ruta_archivo.csv")
    df_indice = df.set_index("id_inscripcion")
