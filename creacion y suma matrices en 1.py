def crear_matriz(M,N):
    matriz= []
    for i in range(M):
        matriz.append([])
        for j in range (N):
            value=int(input("ingrese valores: "))
            matriz[i].append(value)
    return matriz

def suma_matriz(M,N):
    suma=0
    matriz=crear_matriz(M,N)
    for i in range(M):
        for j in range(N): 
            valor=matriz[i][j]
            suma+=valor
    return suma
    

M=int(input("ingrese cantidad de filas: "))
N=int(input("ingrese cantidad de columnas: "))
print(suma_matriz(M,N))
