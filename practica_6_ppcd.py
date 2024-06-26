# -*- coding: utf-8 -*-
"""Practica 6 PPCD.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10Q2dBiwxUIuOyr_S61jarEVji5gEJOeU
"""

import numpy as np

# Cargar el archivo CSV en una lista de Py
datos_np = np.genfromtxt('fashion_products.csv', delimiter=',', dtype=str)

datos_lista = datos_np.tolist()

# Convertir la lista en un arreglo NumPy
arreglo_numpy = np.array(datos_lista)
datos_SE = arreglo_numpy[1:]

# Obtener las columnas Price y Rating como arreglos NumPy
precios = datos_SE [:, 5].astype(float)  # Columna 5
ratings = datos_SE [:, 6].astype(float)  # Columna 6

# Realizar operaciones aritméticas en las columnas Price y Rating
precio_doble = precios * 2
rating_cuadrado = ratings ** 2

# Imprimir los resultados
#print("Precio duplicado:", precio_doble)
#print("Rating al cuadrado:", rating_cuadrado)

# Obtener la columna de precios como un arreglo NumPy
precios = datos_SE[:, 5].astype(float)  # La columna de precios es la quinta columna

# Realizar la operación de difusión: multiplicar los precios por un factor
factor = 1.1
precios_difundidos = precios * factor

# Imprimir los primeros 5 precios originales y difundidos para verificar
#print("Precios Originales:")
#print(precios[:5])

#print("\nPrecios Difundidos:")
#print(precios_difundidos[:5])



# Acceder al primer elemento
primer_elemento = datos_SE[0]
print("Primer elemento:", primer_elemento)

# Acceder al último elemento
ultimo_elemento = datos_SE[-1]
print("Último elemento:", ultimo_elemento)



# Segmentar el arreglo para obtener los primeros tres elementos
primeros_tres_elementos = datos_SE[:3]
print("Primeros tres elementos:", primeros_tres_elementos)

# Segmentar el arreglo para obtener los elementos desde el segundo hasta el cuarto
elementos_intermedios = datos_SE[1:4]
print("Elementos intermedios:", elementos_intermedios)

# Segmentar el arreglo para obtener los elementos cada dos elementos
cada_dos_elementos = datos_SE[::2]
print("Cada dos elementos:", cada_dos_elementos)



# Acceder a un elemento específico
elemento =  datos_SE[1, 2]  # Segunda fila, tercer elemento
print("Elemento en la segunda fila y tercer columna:", elemento)

# Segmentar el arreglo multidimensional
primera_fila =  datos_SE[0, :]  # Todos los elementos de la primera fila
print("Primera fila:", primera_fila)

ultima_columna =  datos_SE[:, -1]  # Todos los elementos de la última columna
print("Última columna:", ultima_columna)