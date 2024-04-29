def contador_palabras(texto):
    texto = texto.split()
    palabras={}
    for i in texto:
        if i in palabras:     
            palabras[i]+=1
        else:
            palabras[i]=1
    return palabras
def mas_repetida(palabras):
    max_palabra = ''
    max_frecuencia = 0
    for palabra, frecuencia in  palabras.items():
        if frecuencia > max_frecuencia:
            max_palabra = palabra
            max_frecuencia = frecuencia
    return max_palabra, max_frecuencia

text = 'como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'
print(contador_palabras(text))
print(mas_repetida(contador_palabras(text)))