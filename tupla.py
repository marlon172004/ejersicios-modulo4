# Solicitar el nombre del producto al usuario
nombre = input("Ingresa el nombre del producto: ")

# Solicitar el precio del producto al usuario
precio = float(input("Ingresa el precio del producto: "))

# Crear una tupla con el nombre y el precio del producto
producto = (nombre, precio)

# Mostrar la información del producto en forma de tupla
print("Información del producto:")
print("Nombre: ", producto[0])
print("Precio: ", producto[1])