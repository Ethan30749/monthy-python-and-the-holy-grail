N=int(input('Ingrese la cantidad de factoriales: '))
Mult=1
Suma=0
for i in range (1, N+1):
    Mult*=i
    Suma+=Mult
print(Suma)
    