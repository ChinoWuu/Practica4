##mi_diccionario = {
##"nombre": "Juan",
##"usuario": "jn123",
#}
# Muestra Juan
#print(mi_diccionario["nombre"])
# Muestra jn123
#
mi_diccionario = {
"nombre": "Juan",
"edad": "23",
"usuario": "jn23",
}
# Recorriendo los elementos

for llave in mi_diccionario:
    print(llave, ": ", mi_diccionario[llave], sep='')