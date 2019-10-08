Número=int(input('Ingrese un número: '))
if (Número < 4):
    print('I'*Número)
    
if (Número % 10 == 4 and Número < 44):
    print('X'*int(Número/10)+'IV')
    
if (Número % 10 == 0 and Número < 40):
    print('X'*int(Número/10))
    
if (Número % 50 == 0):
    print('L')
