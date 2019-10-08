Vocal=('a','e','i','o','u')
Consonante=('b','c','d','f','g','h','j','k','l','m','n','ñ','p','q','r','s','t','v','w','x','y','z',)
Letra=(input('ingrese una letra: '))

if Letra in Vocal:
    print('Su letra es la vocal ',Letra)
elif Letra in Consonante:
    print('Su letra es la consonante ',Letra)
else:
    print('letra no válida')