# Creamos las listas (vacías al comienzo)
nombres = []
identificaciones = []

while True:
    print("Ingrese los datos de la persona", len(nombres) + 1)
    nombre = input("Nombre: ")
    identificación = input("Identificación: ")
    nombres.append(nombre)
    identificaciones.append(identificación)
    
    agregar_otro = input("¿Desea agregar otra persona? (s/n): ")
    if agregar_otro.lower() != 's':
        break

# Ahora mostremos las listas
for i in range(len(nombres)):
    print("Mostrando los datos de la persona", i + 1)
    print("Nombre:", nombres[i])
    print("Identificación:", identificaciones[i])
