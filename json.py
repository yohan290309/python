import json

lista = [10,20,30,40,60]

with open("lista.json","w") as archivo:
    json.dump(lista,archivo)

diccionario = {'1':'Lapiz','2':'Borrador','3':'Cuaderno','4':'Lapicero'}

with open("diccionario.json","w") as archivo:
    json.dump(diccionario,archivo)

with open("lista.json","r") as archivo:
    lista = json.load(archivo)

print("Lista: ",lista)
for i in range(len(lista)):
    print(lista[i])

try:
    with open("diccionario.json","r") as archivo:
        diccionario = json.load(archivo)
except:
    print("Se presentó un error en la lectura del archivo.")

print("Diccionario: ", diccionario)

print(diccionario["3"])
    
