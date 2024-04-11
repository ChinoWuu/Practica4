num1=int(input("Ingrese un numero:"))
num2=int(input("Ingrese un numero:"))
num3=int(input("Ingrese un numero:"))

if num1==num2 or num2==num3 or num1==num3:
    print("No se puede continuar hay numero iguales")
else:
    if num1>num2 and num1>num3:
        print("El numero ",num1," es el mayor.")
    if num2>num1 and num2>num3:
        print("El numero ",num2," es el mayor.")
    else:
        print("El numero ",num3," es el mayor.")