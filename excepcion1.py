# Definir un diccionario
diccionario = {"a": 1, "b": 2, "c": 3}

try:
    # Intentar acceder a una clave inexistente
    valor = diccionario["d"]
    print(valor)
except KeyError:
    print("La clave no existe en el diccionario.")