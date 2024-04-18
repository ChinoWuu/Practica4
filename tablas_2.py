# Creamos la tabla con listas vacías al comienzo
usuarios = [[], []]
# Definimos un tamaño para las listas de la tabla
# Lo puedes cambiar si quieres

# Leemos los datos y los agregamos a la tabla
while True:
    print("Ingrese los datos de la persona", len(usuarios[0]) + 1)
    nombre = input("Nombre: ")
    identificación = input("Identificación: ")
    # La primera lista es para los nombres
    usuarios[0].append(nombre)
    # La segunda lista es para las identificaciones
    usuarios[1].append(identificación)
    agregar_otro = input("¿Desea agregar otra persona? (s/n): ")
    if agregar_otro.lower() != 's':
        break
# Ahora mostremos los valores en la tabla
for i in range(len(usuarios[0])):
    print("Mostrando los datos de la persona", i + 1)
    print("Nombre:", usuarios[0][i])
    print("Identificación:", usuarios[1][i])