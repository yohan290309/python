#import modulos
#n = modulos.valida_entero_rango("Entero (1-9)",1,9)
n = int(input("Digite un número entre 1 y 9: "))
tabla = open(f"tabla-{n}.txt","w")
for i in range(10):
    tabla.write(f"{n} * {i+1} = {n*(i+1)}\n")
    print(f"{n} * {i+1} = {n*(i+1)}")
tabla.close()
