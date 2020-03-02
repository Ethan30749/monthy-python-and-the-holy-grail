def impar_matriz(matriz):
    counter=0
    for i in range(M):
        for j in range(N):
            valor=matriz[i][j]
            if valor % 2 != 0:
                counter+=1
    return counter







matriz= []
M = int(input("ingrese cantidad de matrices deseadas: "))
N = int(input("ingrese cantidad de valores en cada columna: "))
for i in range(M):
    matriz.append([])
    for j in range (N):
            value=int(input("ingrese valores: "))
            matriz[i].append(value)
print(impar_matriz(matriz))