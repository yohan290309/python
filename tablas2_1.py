# Función crea tabla del n
def crea_tabla(n):
    tabla = []
    for i in range(1,9,1):
        tabla.append({"tabla":n,"por":i,"igual":n*i})
    return tabla

def crea_json():
    import json
    # Crea lista y llena llamando a la función crea_tabla(n)
    tablas = []
    for i in range(2,10,1):
        tablas += crea_tabla(i)
    # Crea el archivo JSON con dump
    with open("tablas.json", "w") as datos:
        json.dump(tablas, datos)
    # Abre el archivo JSON y lista su contenido
    with open("tablas.json", "r") as datos:
        contenido = json.load(datos)
    return(contenido)

print(crea_json())
