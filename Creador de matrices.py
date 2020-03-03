def crear_matriz(M,N):
    matriz= []
    #atribuye al valor "matriz" una lista vacía
    for i in range(M):
        matriz.append([])
        #agrega listas vacías a la matriz equivalente al valor M
        for j in range (N):
            value=int(input("ingrese valores: "))
            matriz[i].append(value)
            #agrega N valores a cada lista de la matriz
    return matriz
    #devuelve la matriz completa
M=int(input("ingrese cantidad de filas: "))
N=int(input("ingrese cantidad de columnas: "))
#solicita los valores M y N para construir la matriz
print(crear_matriz(M,N))
