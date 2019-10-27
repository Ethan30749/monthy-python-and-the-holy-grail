N=int(input('Ingrese su número: '))
if N > 1:
    for i in range (2, N):
        if (N % i == 0):
            print('su número no es primo')
            break
    else:
        print('su número es primo')
elif N == 1:
    print('su número no es primo')