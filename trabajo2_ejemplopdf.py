# Crea lista, elimina un dato y buscar dicho dato.
def buscar_faltante():
    import random
    import lib
    n = lib.valida_entero("Digite un número Entero - Positivo: ")
    lista = lib.llena_lista(n)
    print(lista)
    lista.remove(random.randint(1,len(lista)))

    print(lista)

    for i in range(n):
        pos = lib.busqueda_binaria_recursiva(lista,i+1,0,len(lista)-1)
        if pos < 0:
            print(lista[i-1:i+1])
            print(f"Falta el {i+1}")
            break

    import lib
    lista = lib.llena_lista_aleatoria(500,9999)
    par = 0
    for i in range(len(lista)):
        if lista[i]%2 == 0:
            par += 1

    print(f"Menor: {min(lista)}")
    print(f"Mayor: {max(lista)}")
    print(f"Pares: {par}")
    print(f"Impares: {len(lista)-par}")
    print(f"Promedio: {sum(lista)/len(lista)}")

# simulación y estadística lanzamientos de dados
def estadistica_dados():
    import random
    lista = []
    n = 500
    for i in range(n):
        lista.append((random.randint(1,6),random.randint(1,6)))

    valores = {}
    par = dob = 0
    for i in range(2,13,1):
        valores[i] = 0

    #print(valores)
    for j in range(len(lista)):
        suma = sum(lista[j])
        valores[suma] += 1
        if suma%2 == 0:
            par += 1
        if lista[j][0] == lista[j][1]:
            dob += 1
        
    for i in range(2,13,1):
        print("{0:2} - {1:2} - {2:5.1%}".format(i,valores[i],valores[i]/n))

    print(f"Pares: {par} - {par/n}")
    print(f"Impares: {n-par} - {(n-par)/n}")
    print(f"Dobles: {dob} - {dob/n}")

estadistica_dados()
   
