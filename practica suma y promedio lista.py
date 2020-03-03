Lista=[]
M=int(input("ingrese cantidad de valores: "))
suma=0
promedio=0
for i in range(M):
    N=int(input("ingrese valores: "))
    Lista.append(N)
for i in range (1, len(Lista)):
    suma+=Lista[i]
promedio=suma/len(Lista)
print("suma total de valores en la lista: ", suma)
print("promedio de los valores en la lista: ", promedio)