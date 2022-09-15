#Escribir un programa que pida ingresar coordenadas (x,y) que representan
#puntos en el plano Informar cuántos puntos se han ingresado en el primer,
#segundo, tercer y cuarto cuadrante. Al comenzar el programa se pide que se
#ingrese la cantidad de puntos a procesar.
plano1 = 0
plano2 = 0
plano3 = 0
plano4 = 0
n = int(input("Digite la cantidad de puntos a procesar: "))
for i in range(n):
    x = int(input("Ingrese coordenada x: "))
    y = int(input("Ingrese coordenada y: "))
    if x>0 and y>0:
            plano1 = plano1 + 1
    else:
        if x<0 and y>0:
            plano2 = plano2 + 1
        else:
            if x<0 and y<0:
                plano3 = plano3 + 1
            else:
                if x>0 and y<0:
                    plano4 = plano4 + 1
print(f"Cantidad puntos primer plano {plano1}")
print(f"Cantidad puntos segundo plano {plano2}")
print(f"Cantidad puntos tercer plano {plano3}")
print(f"Cantidad puntos cuarto plano {plano3}")
print("-------------")
#Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
#a) La cantidad de valores ingresados negativos.
#b) La cantidad de valores ingresados positivos.
#c) La cantidad de múltiplos de 5.
#d) El valor acumulado de los números ingresados que son pares.
nega = 0
posi = 0
multi = 0
sumapares = 0
for i in range (10):
    n = int(input("Digite los datos: "))
    if n < 0:
        nega = nega + 1
    else:
        if n > 0:
            posi = posi + 1
    if n%5==0:
        multi = multi + 1
    if n%2==0:
        sumapares = sumapares + n
print (f"La cantidad de negativos es, {nega}")
print (f"La cantidad de positivos es, {posi}")
print (f"La cantidad de multiplos 15 es, {multi}")
print (f"La cantidad de la suma de los pares es, {sumapares}")
print("-------------")

#Se cuenta con la siguiente información:
#Las edades de 5 estudiantes del turno mañana.
#Las edades de 6 estudiantes del turno tarde.
#Las edades de 11 estudiantes del turno noche.
#Las edades de cada estudiante deben ingresarse por teclado.
#a) Obtener el promedio de las edades de cada turno (tres promedios)
#b) Imprimir dichos promedios (promedio de cada turno)
#c) Mostrar por pantalla un mensaje que indique cual de los tres
#turnos tiene un promedio de edades mayor.
prom1 = 0
prom2 = 0
prom3 = 0
for i in range (5):
    edad = int(input("Digite la edad: "))
    prom1 = prom1 + edad
promedio = prom1/5
print (f"El promedio de las edades turno de la mañana es, {promedio}")
for i in range (6):
    edad = int(input("Digite la edad: "))
    prom2 = prom2 + edad
promedio1 = prom2/6
print (f"El promedio de las edades turno de la tarde es, {promedio1}")
for i in range (11):
    edad = int(input("Digite la edad: "))
    prom2 = prom2 + edad
promedio2 = prom2/11
print (f"El promedio de las edades turno de la noche es, {promedio2}")
if promedio > promedio1 and promedio > promedio2:
    print("El promedio de edades de la mañana es mayor")
else:
    if promedio1 > promedio and promedio1 > promedio2:
        print("El promedio de edades de la tarde es mayor")
    else:
        print("El promedio de edades de la noche es mayor")
          


        
