#Definir una lista que almacene 5 enteros. Sumar todos sus
#elementos y mostrar dicha suma.
lista=[10,7,3,7,2]
suma = 0
x = 0
while x < len(lista):
    suma = suma + lista[x]
    x = x +1
print(f"La suma es {suma}")
print("------------------")

#Definir una lista por asignación que almacene los nombres de los
#primeros cuatro meses de año. Mostrar el primer y último elemento
#de la lista solamente.
lista=["Enero","Febrero","Marzo","Abril"]
print(lista[0])
print(lista[3])
print("------------------")

#Definir una lista por asignación que almacene en la primer componente el
#nombre de un alumno y en las dos
#siguientes sus notas. Imprimir luego el nombre y el promedio de las dos notas.
lista=["ana",7,9]
prome = (lista[1] + lista[2])/2
print(f"Nombre de estudiante, {lista[0]}")
print(f"Promedio es, {prome}")
print("------------------")

#Definir por asignación una lista con 8 elementos enteros. Contar cuantos
#de dichos valores almacenan un valor superior a 100
lista=[50,20,105,250,300,500,50,20]
may = 0
x = 0
while x < len(lista):
    if lista[x] > 100:
        may = may + 1
    x= x+1
print(f"Los numero mayores a 100 son, {may}")
print("------------------")

#Definir una lista por asignación con 5 enteros. Mostrar por pantalla solo los
#elementos con valor iguales o superiores a 7.
lista=[5,7,8,6,9]
mayigua = 0
x = 0
while x < len(lista):
    if lista[x] >= 7:
        mayigua = mayigua + 1
    x= x+1
print(f"Los numero mayores iguales a 7 son, {mayigua}")
print("------------------")

#Definir una lista que almacene por asignación los nombres de 5 personas. Contar
#cuantos de esos nombres tienen 5 o más caracteres
lista=["andres","Carlos","Pedro","Juan","Ana"]
mayCar = 0
x = 0
while x < len(lista):
    if len(lista[x]) >= 5:
        mayCar = mayCar + 1
    x= x+1
print(f"Los nombres con 5 o mas caracteres son, {mayCar}")
print("------------------")
