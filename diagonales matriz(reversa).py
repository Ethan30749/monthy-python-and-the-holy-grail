matriz=[[2,4,6],[1,3,8],[2,6,5]]
M = 3
N = 3
matriz_diagonal=[]

def diagonales(m):
    count=2
    for i in range(M):
                valor=matriz[i][count]
                matriz_diagonal.append(valor)
                count-=1
    return matriz_diagonal

print(diagonales(matriz))