#Confeccionar un programa que permita cargar los nombres de 5 alumnos
#y sus notas respectivas. Luego ordenar las notas de mayor a menor.
#Imprimir las notas y los nombres de los alumnos.
alum=[]
notas=[]
for x in range (5):
    nom = input("Digite el nombre: ")
    alum.append(nom)
    nota = int(input("Digite la nota: "))
    notas.append(nota)
for i in range (4): 
    for x in range (4-i):
       if notas[x] < notas[x+1]:
           aux1=notas[x]       
           notas[x]= notas[x+1]
           notas[x+1] = aux1
           aux2=alum[x]       
           alum[x]= alum[x+1]
           alum[x+1] = aux2
for x in range(5):
    print( alum[x], notas[x])
print("-------------------------")

#Crear y cargar en un lista los nombres de 5 países y en otra lista
#paralela la cantidad de habitantes del mismo. Ordenar alfabéticamente
#e imprimir los resultados. Por último ordenar con respecto a la
#cantidad de habitantes (de mayor a menor) e imprimir nuevamente.
pai=[]
habi=[]
for x in range (5):
    pais = input("Digite el nombre del Pais: ")
    pai.append(pais)
    habitan = int(input("Digite la cantidad de habitantes: "))
    habi.append(habitan)
for i in range (4): 
    for x in range (4-i):
       if pai[x] > pai[x+1]:
           aux1=pai[x]       
           pai[x]= pai[x+1]
           pai[x+1] = aux1
           aux2=habi[x]       
           habi[x]= habi[x+1]
           habi[x+1] = aux2
print("ordenado alfabéticamente")
for x in range (5):           
    print(pai[x], habi[x])
for i in range (4): 
    for x in range (4-i):
       if habi[x] < habi[x+1]:
           aux1=pai[x]       
           pai[x]= pai[x+1]
           pai[x+1] = aux1
           aux2=habi[x]       
           habi[x]= habi[x+1]
           habi[x+1] = aux2
print("ordenado respecto a cantidad de habitantes")
for x in range (5):
    print(pai[x], habi[x])
           


    

