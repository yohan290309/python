#Definir una lista vacía y luego solicitar la carga de 5 enteros por teclado
#y añadirlos a la lista. Imprimir la lista generada.
lista = []
for x in range (5):
    valor = int(input("Digite su numero: "))
    lista.append(valor)
print (lista)
print("----------------------")
"""lista = [] el mismo con while
x=0
while x in range (5):
    valor = int(input("Digite su numero: "))
    lista.append(valor)
    x=x+1
print (lista)
print("----------------------")"""

#Realizar la carga de valores enteros por teclado, almacenarlos en una lista.
#Finalizar la carga de enteros al ingresar el cero. Mostrar finalmente
#el tamaño de la lista.
lista = []
valor = int(input("Ingrese valor, el 0 es para finalizar: "))
while valor != 0:
    lista.append(valor)
    valor = int(input("Ingrese valor, el 0 es para finalizar: "))
print(len(lista))
print("----------------------")

#Almacenar en una lista los sueldos (valores float) de 5 operarios. Imprimir
#la lista y el promedio de sueldos
lista = []
suma = 0
x=0
while x in range (5):
    sueldo = float(input("Ingrese el sueldo: "))
    lista.append(sueldo)
    suma = suma + sueldo
    x = x+1
prome = suma/5
print(lista)
print(prome)
print("----------------------")

#Cargar por teclado y almacenar en una lista las alturas de 5 personas
#(valores float) Obtener el promedio de las mismas. Contar cuántas
#personas son más altas que el promedio y cuántas más bajas.
lista = []
suma = 0
alta = 0
baja = 0
x=0
while x in range (5):
    altu = float(input("Ingrese la altura: "))
    lista.append(altu)
    suma = suma + altu
    x = x+1
prome = suma/5
for x in range (5):
    if prome > lista[x]:
        alta = alta + 1
    else:
        baja = baja + 1
print(baja)
print(alta)
print(prome)
print("----------------------")

#Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados
#(4 por la mañana y 4 por la tarde) Confeccionar un programa que permita
#almacenar los sueldos de los empleados agrupados en dos listas.
#Imprimir las dos listas de sueldos.
suelm = []
print("Sueldos del turno de la mañana")
for x in range (4):
    valor = int(input("Ingrese el sueldo: "))
    suelm.append(suelm)
suelt = []
print("Sueldos del turno de la tarde")
for x in range (4):
    valor = int(input("Ingrese el sueldo: "))
    suelt.append(suelt)    
print(suelm)
print(suelt)






    
