polinomio=input('¿cual polinomio desea ver?, ¿a o b?: ')
if polinomio == 'a':
    x=float(input('introduzca variable x: '))
    y=float(input('introduzca variable y: '))
    P=5*(x**5)+(6*(x**4)*y)+(7*(x**3)*(y**2))+3*(x**2)-7*x+6*(y**2)
    print(P)
elif polinomio == 'b':
    x=float(input('introduzca variable x: '))
    Q=4*(x**3)-8*(x**2)+12*x-9
    print(Q)