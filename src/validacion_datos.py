

# Funciones para validación de datos
def validar_numero(num):
    '''
    función que verifica si el valor ingresado corresponde a un valor numérico.

    Parameters
    ----------
    num : puede ser str / int o float
        DESCRIPTION: valor a analizar

    Returns
    -------
    bool
        DESCRIPTION: True si se puede convertir a un número
	False en caso contrario

    '''
    try:
        float(num)
        return True
    except ValueError as e:
        print("Error, ingreso inválido", e)
        return False
	
def validar_registro(registro):
    '''
    función que valida el tipo de dato y los valores de un diccionario

    Parameters
    ----------
    registro : dicc
        DESCRIPTION: diccionario que contiene 6 claves para analizar información

    Returns
    -------
    bool
        DESCRIPTION: True si la informacion esta validada y False en caso contrario

    '''
    ### validar que las claves son las correctas
    claves_inicio = ["id_participante", "tiempo", "valor", "fase", "condicion_experimental", "hit"]
    for claves in claves_inicio:
        if claves not in registro:
            return False
        
        id_p = registro["id_participante"]
        tiempo = registro["tiempo"]
        valor = registro["valor"]
        fase = registro["fase"]
        cond_exp = registro["condicion_experimental"]
        hit = registro["hit"]
        listas = [tiempo, valor, fase, cond_exp, hit]
    ### validar tipos de datos 
        if not validar_numero(id_p):
            return False
        
        for lista in listas:
            try: 
                if len(lista) == 0:
                    return False
            except TypeError as e:
                print("Los datos deben ser listas",e)
                return False
         
     ### validar valores
        for t in tiempo:
            if not validar_numero(t):
                return False
            if float(t) <= 0:
                return False
        for v in valor:
            if not validar_numero(v):
                return False
        
        return True



        
