from math import sqrt as root
x=float(input('Introduzca variable x: '))
y=float(input('introduzca variable y: '))

if (x < 0) or (y < 0):
    print('variables no válidas')
elif (x == 0) and (y == 0):
    print('variables no válidas')
else:
    r=root(3*(x**2)+(6*y))
    print(r)