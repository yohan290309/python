#Confeccionar un programa que lea n pares de datos, cada par de datos
#corresponde a la medida de la base y la altura de un triángulo.
#El programa deberá informar:
#a) De cada triángulo la medida de su base, su altura y su superficie.
#b) La cantidad de triángulos cuya superficie es mayor a 12.

tmay = 0
n = int(input("Digite la cantidad de triangulos: "))
for i in range (n):
    base = int(input("Digite la base del triangulo: "))
    altu = int(input("Digite la altura del triangulo: "))
    superfi = base * altu / 2
    print("La superficie es")
    print (superfi)
    if superfi > 12:
        tmay = tmay + 1
print(f"La cantidad de triangulos de mayor superficie a 12 es {tmay}")
print ("---------------")
#Desarrollar un programa que solicite la carga de 10 números e imprima la
#suma de los últimos 5 valores ingresados.
resul = 0
for i in range (10):
    n = int(input("Digite 10 numeros: "))
    if i >=5:#Los ultimos cinco
    #if n >=5:  #Los numero mayores = a cinco  
        resul = resul + n
print (resul)
print ("---------------")
#Desarrollar un programa que muestre la tabla de multiplicar del 5 (del 5 al 50)
for f in range (5, 51, 5):
    print (f)
print ("---------------")
#Confeccionar un programa que permita ingresar un valor del 1 al 10 y nos
#muestre la tabla de multiplicar del mismo (los primeros 12 términos)
#Ejemplo: Si ingreso 3 deberá aparecer en pantalla los valores 3, 6, 9,
#hasta el 36.
mult = int(input("Digite un numero del 1 al 10: "))
for f in range (1, 13):
    tabla = mult * f
    print (tabla)
print ("---------------")
#Realizar un programa que lea los lados de n triángulos, e informar:
#a) De cada uno de ellos, qué tipo de triángulo es: equilátero
#(tres lados iguales), isósceles (dos lados iguales), o escaleno
#(ningún lado igual) b) Cantidad de triángulos de cada tipo.
equ = 0
iso = 0
esc = 0
n = int(input("Digite la cantidad de triangulos: "))
for i in range (n):
    lado1 = int(input("Digite tamaño lado1: "))
    lado2 = int(input("Digite tamaño lado2: "))
    lado3 = int(input("Digite tamaño lado3: "))
    if lado1 == lado2 and lado2 == lado3:
        equ = equ + 1
        print ("Triangulo equilatero")
    else:
        if lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
            iso = iso + 1
            print ("Triangulo isósceles")
        else:
            esc = esc + 1
            print ("escaleno")
print (f"la cantidad de trinagulos equilateros es, {equ}")
print (f"la cantidad de trinagulos isósceles es, {equ}")
print (f"la cantidad de trinagulos escaleno es, {equ}") 
    
