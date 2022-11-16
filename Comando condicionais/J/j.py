#inputs

NomeVilao1 = input('')

PoderVilao1 = int(input())

LocalVilao1 = int(input())

NomeVilao2 = input ('')

PoderVilao2 = int(input())

LocalVilao2 = int(input())


if PoderVilao1 < 0 or PoderVilao2 < 0:
    print('Nem faco essa comparacao! Quero ser um vingador, busco coisas maiores.')

else:
    Destruicao1 = ((PoderVilao1 ** 2) * LocalVilao1) / 2
    Destruicao2 = ((PoderVilao2 ** 2) * LocalVilao2) / 2
    if Destruicao1 > Destruicao2:
        print(f'Com grandes poderes, vem grandes responsabilidades. Com isso, preciso ir deter o {NomeVilao1}.')
    if Destruicao1 < Destruicao2:
        print(f'Com grandes poderes, vem grandes responsabilidades. Com isso, preciso ir deter o {NomeVilao2}.')
    if Destruicao1 == Destruicao2:
        if (Destruicao1 % 2) == 0:
            print('E quem disse que isso e problema meu? Vou chamar o senhor Stark.')
        else:
            print('Vou chamar uns reforcos de outro universo... rsrs')
