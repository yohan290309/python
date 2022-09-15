#Desarrollar un programa que permita cargar 5 nombres de personas y sus edades
#respectivas. Luego de realizar la carga por teclado de todos los datos imprimir
#los nombres de las personas mayores de edad (mayores o iguales a 18 años)
nombres=[]
edades=[]
for x in range(5):
    nom=input("Ingrese el nombre de la persona:")
    nombres.append(nom)
    ed=int(input("Ingrese la edad de dicha persona:"))
    edades.append(ed)
print("Los nombres de las personas mayores de 18: ")
for x in range (5):
    if edades[x] > 18:
        nombres.sort()
        print(nombres[x])
print("----------------------------")

#Crear y cargar dos listas con los nombres de 5 productos en una y sus
#respectivos precios en otra. Definir dos listas paralelas. Mostrar cuantos
#productos tienen un precio mayor al primer producto ingresado.
prod = []
prec = []
for x in range (5):
    produc=(input("Digite el producto: "))
    prod.append(produc)
    precio=int(input("Digite el precio: "))
    prec.append(precio)
print("Los productos con mayor precio en diferencia al primero: ")
prem = 0
for x in range (5):
    if prec[x] > prec[0]:
        prem = prem + 1
print(prem)
print("----------------------------")

#En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben
#procesar de acuerdo a lo siguiente:
#a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas
#   paralelas)
#b) Realizar un listado que muestre los nombres, notas y condición del alumno.
#   En la condición, colocar "Muy Bueno" si la nota es mayor o igual a 8,
#   "Bueno" si la nota está entre 4 y 7, y colocar "Insuficiente" si la nota
#   es inferior a 4.
#c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”.
alum = []
nota = []
for x in range (4):
    nom=(input("Digite el nombre: "))
    alum.append(nom)
    notas=int(input("Digite la nota: "))
    nota.append(notas)
conbue = 0
for x in range (4):
    print(alum[x])
    print(nota[x])
    if nota[x] >= 8:
        conbue =  conbue  + 1 
        print("Muy Bueno")
    else:
        if nota[x] > 4: 
            print("Bueno")
        else:
            if nota[x] < 4:
                print("Insuficiente")
print(f"los alumnos con mayor nota fueron {conbue}")            
print("----------------------------")

#Realizar un programa que pida la carga de dos listas numéricas enteras de 4
#elementos cada una. Generar una tercer lista que surja de la suma de los
#elementos de la misma posición de cada lista. Mostrar esta tercer lista.
lis1 = []
lis2 = []
for x in range (4):
    dato1 = int(input("Digite el numero: "))
    lis1.append(dato1)
    dato2 = int(input("Digite el numero: "))
    lis2.append(dato2)
lis3 = []
for x in range (4):
    suma = lis1[x] + lis2[x]
    lis3.append(suma)
print(lis1)    
print(lis2)    
print(f"La nueva lista es {lis3}")



