# Crea el archivo y agrega n líneas
archivo = open("datos.txt","w")
for i in range(5):
    archivo.write(f"Línea {i+1}\n")
archivo.close()

# Abre el archivo en modo lectura y muestra contenido
archivo = open("datos.txt","r")
print(archivo.read())
print(" - - - - - - ")
archivo.seek(0)
print(archivo.readline())
print(archivo.readline())
print(archivo.readline())
print(" - - - - - - ")
archivo.seek(0)
contenido = archivo.readlines()
print(contenido)

for i in contenido:
    print(i)

# Método 1 para asegurar el cerrado del archivo
with open("datos.txt","r") as datos:
    print(datos.read())

# Método 2 para asegurar el cerrado del archivo
try:
    datos = open("datos.txt","r")
    print(datos.read())
finally:
    datos.close()

# Abre el archivo y agrega información
archivo = open("datos.txt","a")
archivo.write("Línea 6\n")
archivo.write("Línea 7")
archivo.close()
