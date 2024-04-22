usuarios = {
    "nombres": [],
    "identificaciones": []
}

while True:
    print("Ingrese los datos de la persona:")
    nombre = input("Nombre: ")
    identificación = input("Identificación: ")
    usuarios["nombres"].append(nombre)
    usuarios["identificaciones"].append(identificación)

    agregar_otro = input("¿Desea agregar otro empleado? (s/n): ")
    if agregar_otro.lower() != "s":
        break

# Mostrar los valores en el diccionario
for i in range(len(usuarios["nombres"])):
    print("Mostrando los datos de la persona", i + 1)
    print("Nombre:", usuarios["nombres"][i])
    print("Identificación:", usuarios["identificaciones"][i])

