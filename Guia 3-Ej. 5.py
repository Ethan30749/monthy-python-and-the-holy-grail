presion=float(input('introduzca la presión en ATM: '))
volumen=float(input('indique el volumen en L: '))
temperatura=float(input('introduca la temperatura en K: '))
masa= (presion*volumen) / (float(0.37)*(temperatura+460))
print('su masa calculada es: ',masa,'kilos')