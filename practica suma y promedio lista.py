def Suma(Lista):
    suma=0
    for i in range(len(Lista)):
        suma+=Lista[i]
    return suma

def Promedio(Lista):
    suma = Suma(Lista)
    N = len(Lista)
    return suma / N

Lista=[]
M=int(input("ingrese cantidad de valores: "))
for i in range(M):
    Valor=int(input("ingrese valores: "))
    Lista.append(Valor)
    
sumatoria= Suma(Lista)
promedio= Promedio(Lista)

print("suma total de valores en la lista: ", sumatoria)
print("promedio de los valores en la lista: ", promedio)
