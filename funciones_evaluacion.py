import random
def numeros_a(n,l_i,l_s):
    numeros = {
        "claves": [],
        "numero": []
    }
    num=[]
    for i in range(n):
        numeros["claves"].append(i+1)
        num.append(random.randint(l_i,  l_s))
        numeros["numero"].append(num[i]*num[i])

    for i in range(len(numeros["claves"])):
        print("numero de lista: ",num[i])
        print("clave:", numeros["claves"][i])
        print("numero:", numeros["numero"][i])
    return
numeros_a(7,1,15)