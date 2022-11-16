R1 = int(input())
R2 = int(input())
resultado = str(input())
P = int()

E = 1/(1+10**((R2-R1)/400))

if resultado == str('vitoria'):
    P = 1
if resultado == str('empate'):
    P = 0.5
if resultado == str('derrota'):
    P = 0

R = R1 + 40*(P - E)

r = int(R)
if resultado != str('vitoria') and resultado != str('empate') and resultado != str('derrota'):
    print('Resultado da partida invalido')
else:
    print(f'O novo rating da Beth Harmon é {r}')
