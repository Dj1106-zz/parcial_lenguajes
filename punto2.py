import re

# Expresión regular para identificadores
patron = r"[A-Za-z][A-Za-z0-9]*"

print("Validador de identificadores")
print("Escribe 'salir' para terminar\n")

while True:
    identificador = input("Ingrese ID: ")

    if identificador.lower() == "salir":
        break

    if re.fullmatch(patron, identificador):
        print("ACEPTE\n")
    else:
        print("NO ACEPTE\n")