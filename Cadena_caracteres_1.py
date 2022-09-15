#Realizar la carga del nombre de una persona y luego mostrar
#el primer caracter del nombre y la cantidad de letras que lo componen.
nombre = input("Digite su nombre: ")
print("El primer caracter es", nombre[0])
print("La cantidad de letras es", len(nombre))
print ("---------------")

#Solicitar la carga del nombre de una persona en minúsculas. Mostrar
#un mensaje si comienza con vocal dicho nombre.

def juego(letra):
    vocales = ['a','e','i','o','u']
    nombre = ""
    for palabra in letra.split():
        if palabra[0].lower() in vocales:
            print("nombre inicia con vocal")
        else:
            print ("nombre no inicia con vocal")
    return nombre
letra = input("Digite su nombre: ")
print(juego(letra))
print ("---------------")

#Ingresar un mail por teclado. Verificar si el string ingresado
#contiene solo un caracter "@".
mail=input("Ingrese un mail: ")
cantidad=0
x=0
while x<len(mail):
    if mail[x]=="@":
        cantidad=cantidad+1
    x=x+1
if cantidad==1:
    print("Contiene solo un caracter @ el mail ingresado")
else:
    print("Incorrecto")
print ("---------------")

#Inicializar un string con la cadena "mAriA" luego llamar a sus métodos
#upper(), lower() y capitalize(), guardar los datos retornados en otros
#string y mostrarlos por pantalla.
nombre1="mAriA"
print(nombre1)
nombre2=nombre1.upper()
print(nombre2)
nombre3=nombre1.lower()
print(nombre3)
nombre4=nombre1.capitalize()
print(nombre4)
print ("---------------")

#Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco
#se ingresaron. Tener en cuenta que un espacio en blanco es igual a
#" ", en cambio una cadena vacía es ""
oraci = input("Digite su oración: ")
blanco = 0
x = 0
while x < len(oraci):
    if oraci[x] == " ":
        blanco = blanco + 1
    x = x+1
print (f"La cantidad de espacios vacios son: {blanco}")
print ("---------------")

#Ingresar una oración que pueden tener letras tanto en mayúsculas como
#minúsculas. Contar la cantidad de vocales. Crear un segundo string con
#toda la oración en minúsculas para que sea más fácil disponer la condición
#que verifica que es una vocal.
oraci = input("Ingrese la Oracion")
oraciminus = oraci.lower()
cantidad=0
x=0
while x<len(oraciminus):
    if oraciminus[x]== "a" or oraciminus[x]== "e" or oraciminus[x]== "i" or oraciminus[x]== "o" or oraciminus[x]== "u"
        cantidad = cantidad + 1
    x=x+1
print(f"La cantidad de vocales es {cantidad}")


