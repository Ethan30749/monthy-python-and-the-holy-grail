def Roman(N):
    Ten=0
    Unit=0
    if (N / 10 != 0):
        if (N / 10 < 4):
            Ten='X'*int(N /10)
        
        elif (N / 10 >= 4) and (N / 10 < 5):
            Ten='XL'
        
        elif (N / 10 == 5):
            Ten='L'
        
        elif (N / 10 > 5) and (N / 10 < 9):
            Ten='L'+'X'*int((N/ 10)-5)
    
        elif (N / 10 >= 9) and (N / 10 < 10):
            Ten='XC'
        elif (N / 10 == 10):
            Ten='C'
        
        number=str(Ten)
    
    if (N / 10 != 0):
        Unit=0
        
        if (N % 10 < 4):
            Unit='I'*int(N % 10)
            
        elif (N % 10 == 4):
            Unit='IV'
            
        elif (N % 10 == 5):
            Unit='V'
            
        elif (N % 10 > 5) and (N % 10 < 9):
            Unit='V'+'I'*int((N %10)-5)
            
        elif (N % 10 == 9):
            Unit='IX'
            
        number=str(Ten)+str(Unit)
            
    return number
print(Roman(int(input('Ingrese un número: '))))