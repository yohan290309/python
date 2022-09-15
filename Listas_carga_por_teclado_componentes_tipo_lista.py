"""Crear y cargar una lista con los nombres de tres alumnos. Cada alumno tiene
#dos notas, almacenar las notas en una lista paralela. Cada componente de la
#lista paralela debe ser también una lista con las dos notas. Imprimir luego
alum=[]
notas=[]
for x in range (3):
    nom=input("Ingrese el nombre del alumno:")
    alum.append(nom)
    no1=int(input("Ingrese la primer nota:"))
    no2=int(input("Ingrese la segunda nota:"))
    notas.append([no1,no2])
for x in range(3):
    print(alum[x], notas[x][0], notas[x][1])
print("-------------------------------------------------")"""
#Se tiene que cargar la siguiente información:
#· Nombres de 3 empleados
#· Ingresos en concepto de sueldo, cobrado por cada empleado,
#en los últimos 3 meses.
#Confeccionar el programa para:
#a) Realizar la carga de los nombres de empleados y los tres sueldos por cada
#   empleado.
#b) Generar una lista que contenga el ingreso acumulado en sueldos en los
#   últimos 3 meses para cada empleado.
#c) Mostrar por pantalla el total pagado en sueldos a cada empleado en los
#   últimos 3 meses
#d) Obtener el nombre del empleado que tuvo el mayor ingreso acumulado
"""nom=[]
suel=[]
tosuel=[]
for x in range (3):
    nombr=input("Ingrese el nombre del empleado:")
    nom.append(nombr)
    su1=int(input("Ingrese el primer sueldo:"))
    su2=int(input("Ingrese el segundo sueldo:"))
    su3=int(input("Ingrese el tercer sueldo:"))
    suel.append([su1,su2,su3])
for x in range (3):
    total=suel[x][0] + suel[x][1] + suel[x][2]
    tosuel.append(total)
for x in range (3):
    print(nom[x], tosuel[x])
posmay=0
mayor=tosuel[0]
for x in range(1,3):
    if tosuel[x]>mayor:
        mayor=tosuel[x]
        posmay=x
print("Empleado con mayores ingresos en los ultimos tres meses")
print(f"{nom[posmay]},con un ingreso de, {mayor}")
print("-------------------------------------------------")"""

#Solicitar por teclado dos enteros. El primer valor indica la cantidad de
#elementos que crearemos en la lista. El segundo valor indica la cantidad de
#elementos que tendrá cada una de las listas internas a la lista principal.
#Mostrar la lista y la suma de todos sus elementos.
"""lista =[]
elemen = int(input("Cuantos elementos tendra la lista: "))
subele = int(input("Cuantos elementos tendra la lista interna: "))
for k in range(elemen):
    lista.append([])
    for x in range(subele):
        valor=int(input("Ingrese valor:"))
        lista[k].append(valor)
print(lista)
suma=0
for k in range (len(lista)):
    for x in range(len(lista[k])):
        suma= suma + lista[k][x]
print("La suma de todos sus elementos:",suma)
print("-------------------------------------------------")"""
#Definir dos listas de 3 elementos.
#La primer lista cada elemento es una sublista con el nombre del padre y
#la madre de una familia. La segunda lista está constituida por listas con
#los nombres de los hijos de cada familia. Puede haber familias sin hijos.
#Imprimir los nombres del padre, la madre y sus hijos. También imprimir solo
#el nombre del padre y la cantidad de hijos que tiene dicho padre.

padres=[]
hijos=[]
for k in range(3):
    pa=input("Los nombres de los padres: ")
    ma=input("Los nombres de las madres: ")
    padres.append([pa,ma])
    can= int(input("Cuantos hijos tienen esta familia:"))
    hijos.append([])
    for x in range (can):
        nom=input("Ingrese el nombre del hijo:")
        hijos[k].append(nom)
print("Listado del padre, madre y sus hijos")
for k in range(3):
    print("Padre:",padres[k][0])
    print("Madre:",padres[k][1])
    for x in range(len(hijos[k])):
        print("Hijo:",hijos[k][x])
print("Listado del padre y cantidad de hijos que tiene")
for x in range(3):
    print("padre:",padres[x][0])
    print("Cantidad de hijos:",len(hijos[x]))

