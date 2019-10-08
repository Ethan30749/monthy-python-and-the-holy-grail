numero=int(input('Ingrese un numero: '))
if (numero == 0):
    print (0)
if ((2^numero) %2 == 0):
    print('1'+'0'*int(numero/2))