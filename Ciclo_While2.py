# Realizar un programa que imprima 25 términos de la serie 11 - 22 - 33 - 44,
# etc. (No se ingresan valores por teclado)
x=1
while x<=25:
    termino = x * 11
    print(termino)
    x=x+1
print("----------------")
#Mostrar los múltiplos de 8 hasta el valor 500.
#Debe aparecer en pantalla 8 - 16 - 24, etc
ocho=8
while ocho <= 500:
    print (ocho)
    ocho = ocho + 8
    
print("----------------")
#Realizar un programa que permita cargar dos listas de 15 valores cada una.
#Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor
#(mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
#Tener en cuenta que puede haber dos o más estructuras repetitivas
#en un algoritmo.
lista1 = 0
lista2 = 0
x = 1
print ("Carga de la primera lista")
while x <= 15:
    valor = int(input("Ingrese el valor: "))
    lista1 = lista1 + valor
    x = x + 1
x=1
print ("Carga de la segunda lista")
while x <= 15:
    valor = int(input("Ingrese el valor: "))
    lista2 = lista2 + valor
    x = x + 1
if lista1 > lista2:
    print(f"lista uno tiene {lista1} mayor")
else:
    if lista2 > lista1:
        print(f"lista dos tiene {lista2} mayor")
    else:
        print(f"lista uno y lista dos {lista1}, {lista1} son iguales")
        
print("----------------")
#Desarrollar un programa que permita cargar n números enteros y luego
#nos informe cuántos valores fueron pares y cuántos impares.
#Emplear el operador “%” en la condición de la estructura condicional
#(este operador retorna el resto de la división de dos valores, por
#ejemplo 11%2 retorna un 1):
par = 0
imp = 0
x = 1
n = int(input("cuantos Numeros va a digitar: "))
while x<=n:
    numero = int(input("Digite los numeros: "))
    if numero % 2 == 0:
         par = par + 1
    else:
         imp = imp + 1
    x = x + 1        
print(f"La cantidad de pares es {par}")
print(f"La cantidad de impares es {imp}")

    
