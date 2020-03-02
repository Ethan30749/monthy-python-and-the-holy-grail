def Es_perfecto(n):
    suma=0
    for i in range(1,n):
        if n % i == 0:
            suma+=i
    if suma == n:
        return True
    else:
        return False


def trabaja_lista(lista):
    counter=0
    for i in range (len(lista)):
        value=lista[i]
        if Es_perfecto(value):
            counter+=1
    return counter
lista=[]
N=int(input("ingrese valores a ingresar en lista: "))
for i in range(N):
    Value=int(input("ingrese valor individual: "))
    lista.append(Value)
result=trabaja_lista(lista)
print(result)
