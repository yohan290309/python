def juego(frase):
    vocales = ['a','e','i','o','u']
    frase_n = ""
    for palabra in frase.split():
        if palabra[0].lower() in vocales: # vocal
            palabra_n = palabra + 'way'  
        elif palabra[0].isupper(): # mayúscula
            palabra_n = palabra[1:] + palabra[0] + 'ay' 
        else:# consonante
            parte2 = palabra[1:]
            alreves = voltear_palabra(parte2)
            palabra_n = alreves + palabra[0] + 'ay'
        frase_n = agregar_palabras_frase(frase_n,  palabra_n)
    return frase_n.lower() + '.'

def agregar_palabras_frase_spac(frase, palabra):
    if frase == "":
        frase += palabra
    else:
        frase = frase + " " + palabra 

    return frase 
    
def voltear_palabra(palabra):
    alreves = ""
    for caracter in palabra:
        alreves = caracter + alreves

    return alreves


"""frases = input( "Digite su frase: ")
print(juego(frases))"""

print(juego('hello world'))
print(juego('i eat apple'))
print(juego('Hello World'))
print(juego('I Eat World'))


