def mover(lista,pos):
    v = lista[pos]
    j = pos
    while j>0 and v<lista[j-1]:
        lista[j] = lista[j-1]
        j = j - 1
    lista[j] = v

def ordenar(codigos,cantidades,tivas): 
    for i in range(len(codigos)-1):
        if codigos[i+1] < codigos[i]:
            mover(codigos,i+1)
            mover(cantidades,i+1)
            mover(tivas,i+1)
            print(codigos)
            print(cantidades)
            print(tivas)

articulos = {1:"Lapiz",2:"Cuaderno",3:"Borrador",4:"Regla",5:"ColoresX12",6:"Escuadra",7:"Calculadora",8:"CrayonesX6"}
precios = {1:2500,2:4500,3:1500,4:5000,5:24000,6:4700,7:45000,8:8900}
N = int(input())
codigos = []
cantidades = []
tivas = []
valores = []
ivas = []
valivas = []
t_valor = 0
t_iva = 0
for i in range(N):
    codigos.append(int(input()))
    cantidades.append(int(input()))
    tivas.append(int(input()))
ordenar(codigos,cantidades,tivas)
for i in range(len(codigos)):
    valor = float(cantidades[i] * precios[codigos[i]])
    valores.append(valor)
   
    if tivas[i] == 1:
        iva = valor * 0
    elif tivas[i] == 2:
        iva = valor * 0.05
    else:
        iva = valor * 0.19
    ivas.append(iva)
    valivas.append(valor+iva)
    t_iva += iva 
    t_valor += valor + iva
    print(codigos[i])
    print(articulos[codigos[i]])
    print(valores[i])
    print(valivas[i])
print(t_valor)
print(t_iva)
    
        

