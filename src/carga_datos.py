def cargar_datos(ruta_archivo):
    '''
    Leer un archivo y transformar su contenido en una lista de diccionarios.

    Parameters
    ----------
    ruta_archivo : str
        Ruta del archivo que contiene los datos.

    Returns
    -------
    list
        Lista con los registros agrupados por participante.
    '''

    datos = []
    participantes = {}

    try:
        archivo = open(ruta_archivo, "r", encoding="utf-8")
        lineas = archivo.readlines()
        archivo.close()
    except FileNotFoundError:
        print("ERROR CRITICO: no se encontró el archivo.- Ubicacion: carga_datos")
        return []

    for linea in lineas:
        if linea.strip() == "":
            continue

        partes = parsear_linea(linea)

        if len(partes) != 6:
            print("ERROR CRITICO: línea mal formada:", linea.strip())
            continue

        id_participante = int(partes[0])
        tiempo = float(partes[1])
        valor = float(partes[2])
        fase = partes[3]
        condicion_experimental = partes[4]
        hit = partes[5]

        if id_participante not in participantes:
            participantes[id_participante] = {
                "id_participante": id_participante,
                "tiempo": [],
                "valor": [],
                "fase": [],
                "condicion_experimental": [],
                "hit": []
            }

        participantes[id_participante]["tiempo"].append(tiempo)
        participantes[id_participante]["valor"].append(valor)
        participantes[id_participante]["fase"].append(fase)
        participantes[id_participante]["condicion_experimental"].append(condicion_experimental)
        participantes[id_participante]["hit"].append(hit)

    for participante in participantes:
        datos.append(participantes[participante])

    return datos


def parsear_linea(linea):
    '''
    Transformar una línea del archivo en una lista de valores.
    '''
    return linea.strip().split(",")
