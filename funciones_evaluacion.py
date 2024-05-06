import random   #importamos random
def numeros_a(n,l_i,l_s):   #creamos la funcion
    numeros = {     #definimos el diccionario
        "claves": [],
        "numero": []
    }
    num=[]      #creamos la lista
    for i in range(n):  #creamos un range para crear los numeros aleatorios
        numeros["claves"].append(i+1)   #sera el indice
        num.append(random.randint(l_i,  l_s))   #guardamos el valor de random en la lista con los rangos que definimos
        numeros["numero"].append(num[i]*num[i]) #guardamos el valor del random al cuadrado

    for i in range(len(numeros["claves"])): #imprimimos los valores
  
        print("clave:", numeros["claves"][i])
        print("numero de lista: ",num[i])
        print("numero:", numeros["numero"][i])
    return
numeros_a(7,1,15)   #mandamos llamar la funcion