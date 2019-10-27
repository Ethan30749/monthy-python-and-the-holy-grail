pi=float(3.1416)
r=float(input('introduzca el radio en cm: '))
h=float(input('introduzca la altura en cm: '))
if (r > 0) and (h > 0):
    area=2*pi*r*(h+r)
    volumen=pi+(r**2)*h
    print('el área de su tarro de conservas es: ',area,'cm cuadrados', '\ny su volumen es: ',volumen,'cm cúbicos')