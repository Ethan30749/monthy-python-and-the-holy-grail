lista=[3,4,1,2,6,5]
mitad_izquierda=[]
mitad_derecha=[]

print(lista)

for i in range(len(lista)//2):
    mitad_izquierda.append(lista[i])
    mitad_izquierda.sort()
    
print(mitad_izquierda)

for j in range(3, len(lista)):
    mitad_derecha.append(lista[j])
    mitad_derecha.sort(reverse=True)
    
print(mitad_derecha)

lista_mixta=mitad_izquierda+mitad_derecha

print(lista_mixta)
