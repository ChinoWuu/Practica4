from collections.abc import Iterable
lista = [1, 2, 3, 4]
cadena = "Python"
numero = 10
print(isinstance (lista, Iterable)) #True 
print(isinstance (cadena, Iterable)) #True
print(isinstance (numero, Iterable)) #False