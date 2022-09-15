#Confeccionar una función que le enviemos como parámetro el valor del lado
#de un cuadrado y nos retorne su superficie.
def retornar_superficie(lado):
    sup=lado*lado
    return sup
# bloque principal del programa
va=int(input("Ingrese el valor del lado del cuadrado:"))
superficie=retornar_superficie(va)
print("La superficie del cuadrado es",superficie)
print("-------------------------------------------")
#Confeccionar una función que le enviemos como parámetros dos enteros y
#nos retorne el mayor.
def mostrar_mayor(nu1,nu2,):
    print("El valor mayor de los dos numeros es: ")
    if nu1 > nu2: 
        mayor = nu1
    else:
        mayor = nu2
    return  nu2       
# bloque principal
valor1=int(input("Ingrese el primer valor:"))
valor2=int(input("Ingrese el segundo valor:"))
print(mostrar_mayor(valor1,valor2))
print("------------------------------------")
