num1=int(input("Ingrese un numero:"))

if num1>999 or num1<0:
    print("Numero no valido")
else:
    if num1>99:
        print("Numero de 3 cifras")
    else:
        if num1>9:
            print("Numero de 2 cifras")
        else:
            print("Numero de una cifra")