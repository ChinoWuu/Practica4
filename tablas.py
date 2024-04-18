mi_tabla = [['Juan', 'Laura'], [21, 32]]
# Recorriendo los elementos
# Accedemos a cada fila (que es una lista)
for fila in mi_tabla:
    # Accedemos a cada columna dentro de la fila
    for columna in fila:
        print(columna)
# Recorriendo los índices
# i serían las filas
for i in range(len(mi_tabla)):
    for j in range(len(mi_tabla[i])):
        print(mi_tabla[i][j])
# Con while y los índices
fila = 0

while fila < len(mi_tabla):
    columna = 0
    while columna < len(mi_tabla[fila]):
        print(mi_tabla[fila][columna])
        columna += 1
    fila += 1