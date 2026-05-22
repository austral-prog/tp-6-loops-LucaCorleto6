# Replace the "ANSWER HERE" for your answer

def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    nueva_lista = []
    for lista in matrix:
        for elemento in lista:
            nueva_lista.append(elemento)
    return nueva_lista


def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """
    nueva_lista = []
    for lista in matrix:
        numero = 0
        for elemento in lista:
            numero += elemento
        nueva_lista.append(numero)
    return nueva_lista




def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """
    nueva_lista = []
    for elemento in range(len(matrix[0])):
        suma = 0
        for lista in range(len(matrix)):
            suma += matrix[lista][elemento]
        nueva_lista.append(suma)
    return nueva_lista
