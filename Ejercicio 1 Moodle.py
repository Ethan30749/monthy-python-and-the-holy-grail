H=int(input('introducir hora: '))
M=int(input('introducir minutos: '))
S=int(input('introducir segundos: '))

Hora=(H*3600)+(M*60)+(S)
if (H < 0) or (M < 0) or (S < 0):
    print('valores no válidos')
else:
    print('el tiempo introducido es:', Hora, 'segundos')