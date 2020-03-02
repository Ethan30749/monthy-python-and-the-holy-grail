def crear_matriz(m):
    matriz= []
    M = int(input("ingrese cantidad de matrices deseadas: "))
    N = int(input("ingrese cantidad de valores en cada columna: "))
    for i in range(M):
        matriz.append([])
        for j in range (N):
            value=int(input("ingrese valores: "))
            matriz[i].append(value)
    return matriz
print(crear_matriz("m"))