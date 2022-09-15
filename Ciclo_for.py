#Realizar un programa que imprima en pantalla los números del 0 al 100.
#Este problema lo podemos resolver perfectamente con el ciclo while
#pero en esta situación lo resolveremos empleando el for.
for i in range (100):
    print(i)
print("---------------")    
for i in range (50,101):
    print(i)
print("---------------")
for i in range (1,101,2):
    print(i)
print("---------------")
x=1
while x<101:
    print(x)
    x=x+1
print("---------------")
#Desarrollar un programa que permita la carga de 10 valores por teclado
#y nos muestre posteriormente la suma de los valores ingresados y su promedio.
#Este problema ya lo desarrollamos, lo resolveremos empleando la estructura for
#para repetir la carga de los diez valores por teclado.
suma=0
for i in range (10):
    valor = int(input("Digite el valor: "))
    suma = suma + valor
print(f" la Suma es {suma}")
print("El promedio es:")
print(suma/10)
print("---------------")                
#Escribir un programa que solicite por teclado 10 notas de alumnos y nos informe
#cuántos tienen notas mayores o iguales a 7 y cuántos menores.
nmay = 0
nmen = 0
for i in range (10):
    nota = float(input("Digite la nota: "))
    if nota >= 7:
        nmay = nmay + 1
    else:
        nmen = nmen + 1
print (f"Las notas mayores son {nmay}")
print (f"Las notas mayores son {nmen}")
print("---------------")
#Escribir un programa que lea 10 números enteros y luego muestre cuántos valores
#ingresados fueron múltiplos de 3 y cuántos de 5. Debemos tener en cuenta que hay
#números que son múltiplos de 3 y de 5 a la vez.
mul3 = 0
mul5 = 0
for i in range (10):
    valor = int(input("Digite el valor: "))
    if valor%3==0:
        mul3 = mul3 + 1
    if valor%5==0:
        mul5 = mul5 + 1
print(f"Cantidad multiplos de 3 son {mul3}")
print(f"Cantidad multiplos de 5 son {mul5}")
print("---------------")

#Codificar un programa que lea n números enteros y calcule la cantidad
#de valores mayores o iguales a 1000 (n se carga por teclado)
#Este tipo de problemas también se puede resolver empleando la
#estructura repetitiva for. Lo primero que se hace es cargar una variable
#que indique la cantidad de valores a ingresar. Dicha variable se carga
#antes de entrar a la estructura repetitiva for.
nmay = 0
nigu = 0
n = int(input("Digite la cantidad de numeros: "))
for i in range (n):
    valor = int(input("Digite el valor: "))
    if valor >= 1000:
        nmay = nmay + 1
    else:
        nigu = nigu + 1
print(f"Cantidad de numeros mayores son {nmay}")
print(f"Cantidad de numeros iguales son {nigu}")


