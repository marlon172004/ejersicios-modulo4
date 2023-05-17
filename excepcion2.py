try:
    #c = 0/5      # Si comentas esto entra en TypeError
    d = 2 + "Hola" # Si comentas esto entra en ZeroDivisionError
except ZeroDivisionError:
    print("No se puede dividir entre cero!")
except TypeError:
    print("Problema de tipos!")