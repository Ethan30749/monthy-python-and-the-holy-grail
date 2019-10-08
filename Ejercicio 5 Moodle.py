Vocal=('a','e','i','o','u')
Vocales=0
Consonante=('b','c','d','f','g','h','j','k','l','m','n','ñ','p','q','r','s','t','v','w','x','y','z',)
Consonantes=0
Texto=(input('ingrese un texto: '))
for i in Texto:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        Vocales+=1
for j in Texto:
    if (j == 'b' or j == 'c' or j == 'd' or j == 'f' or j == 'g' or j == 'h' or j == 'j' or j == 'k' or j == 'l' or j == 'm' or j == 'n' or j == 'ñ' or j== 'p' or j == 'q' or j == 'r' or j == 's' or j == 't' or j == 'v'
        or j == 'w' or j == 'x' or j == 'y' or j == 'z'):
        Consonantes+=1
print('Su texto tiene ',Vocales,'vocales y ',Consonantes,'consonantes')
