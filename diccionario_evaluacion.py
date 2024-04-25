def main():
    fruteria = {"Fruta": ["manzana","platano","naranja","uva","piña","fresas"],
    "Precio": [19,13,12,30,16,20],}

    fruta=str(input("Que fruta compro:"))
    #fruta=(input("Que fruta compro:"))

    for i in range(len(fruteria["Fruta"])):

        if fruta == fruteria["Fruta"][i]:
            can=int(input("Cuanta fruta compro: "))
            p_f=can*fruteria["Precio"][i]
            print("El precio a pagar por la fruta ",fruteria["Fruta"][i]," es de: ",p_f)
            agregar_otro = input("¿Desea agregar otro fruta? (s/n): ")
            if agregar_otro.lower() != "s":
                exit()
            else:
                restart()

        if i == len(fruteria["Fruta"])-1:
            print("Parece que no tenemos esa fruta agregue otra")
            restart()

def restart():
    main()
    exit()
main()

