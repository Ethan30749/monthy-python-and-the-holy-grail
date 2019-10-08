A=int(input('introduzca el primer número: '))
B=int(input('introduzca el segundo número: '))
C=int(input('introduzca el tercer número: '))

if (A < B) and (A < C):
    if (B < C):
        print(A, B, C)
    else:
        print(A, C, B)

if (B < A) and (B < C):
    if (A < C):
        print(B, A, C)
    else:
        print(B, C ,A)

if (C < A) and (C < B):
    if (A < B):
        print(C, A, B)
    else:
        print(C, B, A)