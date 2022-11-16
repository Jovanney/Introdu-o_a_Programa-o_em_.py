nome = input()
valor_semestre1 = int(input())
valor_semestre2 = int(input())

media = int((valor_semestre1 + valor_semestre2) /12)

J = ('Jim Halpert')
D = ('Dwight Schrute')
P = ('Phyllis Vance')
S = ('Stanley Hudson')


if nome != J and nome!= D and nome!= P and nome!= S:
    print('Sinto muito, mas so os vendedores eh que vao ganhar a viagem pra matriz.')
elif media <= 50:
    print (f'{nome}, voce so vendeu {media} por mes? Voce ta demitido... Brincadeira!')
elif media <= 100:
    print(f'{nome}, voce mandou mal... Vai ter que pagar meu almoco.')
elif media >= 100:
    print(f'Parabens, {nome}! Voce foi promovido! kkkkk Brincadeira, a matriz que decide!')
