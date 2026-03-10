import re

# Expresión regular para los movimientos permitidos
patron = r"(p->k[1-8]|kbp|X|qn)"

print("Validador de movimientos de ajedrez")
print("Escribe 'salir' para terminar\n")

while True:
    movimiento = input("Ingrese movimiento: ")

    if movimiento.lower() == "salir":
        break

    if re.fullmatch(patron, movimiento):
        print("ACEPTA\n")
    else:
        print("NO ACEPTA\n")