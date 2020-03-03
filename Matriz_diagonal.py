
matriz=[[2,4,6],[1,3,8],[2,6,5]]
M = 3
N = 3
matriz_diagonal=[]

def diagonales(m):
    for i in range(M):
        for j in range(N):
            if i == j:
                valor=matriz[i][j]
                matriz_diagonal.append(valor)
                
print(matriz_diagonal)
