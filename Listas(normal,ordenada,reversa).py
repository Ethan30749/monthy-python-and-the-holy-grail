from random import randint

lista=[]
N=randint(3,10)
for i in range(N):
    lista.append(randint(1,9))

lista_ordenada=sorted(lista)
lista_reversa=sorted(lista,reverse=True)
print(lista)

print("-"*N*3)

print(lista_ordenada)

print("-"*N*3)

print(lista_reversa)