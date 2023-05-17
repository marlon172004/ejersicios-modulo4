try:
    # Forzamos una excepción al dividir entre 0
    x = 2/0
except:
    print("Entra en except, ha ocurrido una excepción")
else:
    print("Entra en else, no ha ocurrido ninguna excepción")

