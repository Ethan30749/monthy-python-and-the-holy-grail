def crear_matriz(M,N):
    matriz= []
    for i in range(M):
        matriz.append([])
        for j in range (N):
            value=int(input("ingrese valores: "))
            matriz[i].append(value)
    return matriz
F=int(input("ingrese cantidad de filas: "))
C=int(input("ingrese cantidad de columnas: "))
print(crear_matriz(F,C))
