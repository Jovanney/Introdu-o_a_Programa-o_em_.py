# entradas
nome_1 = input()
pontuacao_1 = int(input())

nome_2 = input()
pontuacao_2 = int(input())

nome_3 = input()
pontuacao_3 = int(input())

# atribuicoes
menor_nota = int()
menor_nota2 = int()
menor_nota3 = int()

nome_primeiro = ''
nome_segundo = ''
nome_terceiro = ''

# diferentes

if pontuacao_1 != pontuacao_2 and pontuacao_1 != pontuacao_3 and pontuacao_2 != pontuacao_3:
    if pontuacao_1 < pontuacao_2 and pontuacao_1 < pontuacao_3:
        menor_nota = pontuacao_1
        nome_primeiro = nome_1
        if pontuacao_2 < pontuacao_3:
            menor_nota2 = pontuacao_2
            nome_segundo = nome_2
            menor_nota3 = pontuacao_3
            nome_terceiro = nome_3
        else:
            menor_nota2 = pontuacao_3
            nome_segundo = nome_3
            menor_nota3 = pontuacao_2
            nome_terceiro = nome_2
    if pontuacao_2 < pontuacao_1 and pontuacao_2 < pontuacao_3:
        menor_nota = pontuacao_2
        nome_primeiro = nome_2
        if pontuacao_1 < pontuacao_3:
            menor_nota2 = pontuacao_1
            nome_segundo = nome_1
            menor_nota3 = pontuacao_3
            nome_terceiro = nome_3
        else:
            menor_nota2 = pontuacao_3
            nome_segundo = nome_3
            menor_nota3 = pontuacao_1
            nome_terceiro = nome_1

    if pontuacao_3 < pontuacao_1 and pontuacao_3 < pontuacao_2:
        menor_nota = pontuacao_3
        nome_primeiro = nome_3
        if pontuacao_1 < pontuacao_2:
            menor_nota2 = pontuacao_1
            nome_segundo = nome_1
            menor_nota3 = pontuacao_2
            nome_terceiro = nome_2
        else:
            menor_nota2 = pontuacao_2
            nome_segundo = nome_2
            menor_nota3 = pontuacao_1
            nome_terceiro = nome_1

#3 iguais

if pontuacao_1 == pontuacao_2 and pontuacao_1 == pontuacao_3 and pontuacao_2 == pontuacao_3:
    if nome_1 < nome_2 and nome_1 < nome_3:
        menor_nota = pontuacao_1
        nome_primeiro = nome_1
        if nome_2 < nome_3:
            menor_nota2 = pontuacao_2
            nome_segundo = nome_2
            menor_nota3 = pontuacao_3
            nome_terceiro = nome_3
        else:
            menor_nota2 = pontuacao_3
            nome_segundo = nome_3
            menor_nota3 = pontuacao_2
            nome_terceiro = nome_2
    if nome_2 < nome_1 and nome_2 < nome_3:
        menor_nota = pontuacao_2
        nome_primeiro = nome_2
        if nome_1 < nome_3:
            menor_nota2 = pontuacao_1
            nome_segundo = nome_1
            menor_nota3 = pontuacao_3
            nome_terceiro = nome_3
        else:
            menor_nota2 = pontuacao_3
            nome_segundo = nome_3
            menor_nota3 = pontuacao_1
            nome_terceiro = nome_1
    if nome_3 < nome_2 and nome_3 < nome_1:
        menor_nota = pontuacao_3
        nome_primeiro = nome_3
        if nome_2 < nome_1:
            menor_nota2 = pontuacao_2
            nome_segundo = nome_2
            menor_nota3 = pontuacao_1
            nome_terceiro = nome_1
        else:
            menor_nota2 = pontuacao_1
            nome_segundo = nome_1
            menor_nota3 = pontuacao_2
            nome_terceiro = nome_2

# dois diferentes e um igual

if pontuacao_1 == pontuacao_2 and (pontuacao_1 != pontuacao_3 or pontuacao_2 != pontuacao_3):
    if pontuacao_1 < pontuacao_3 or pontuacao_2 < pontuacao_3:
        if nome_1 < nome_2:
            menor_nota = pontuacao_1
            nome_primeiro = nome_1
            menor_nota2 = pontuacao_2
            nome_segundo = nome_2
            menor_nota3 = pontuacao_3
            nome_terceiro = nome_3
        elif nome_2 < nome_1:
            menor_nota = pontuacao_2
            nome_primeiro = nome_2
            menor_nota2 = pontuacao_1
            nome_segundo = nome_1
            menor_nota3 = pontuacao_3
            nome_terceiro = nome_3

if pontuacao_2 == pontuacao_3 and (pontuacao_2 != pontuacao_1 or pontuacao_3 != pontuacao_1):
    if pontuacao_2 < pontuacao_1 or pontuacao_3 < pontuacao_1:
        if nome_2 < nome_3:
            menor_nota = pontuacao_2
            nome_primeiro = nome_2
            menor_nota2 = pontuacao_3
            nome_segundo = nome_3
            menor_nota3 = pontuacao_1
            nome_terceiro = nome_1
        else:
            menor_nota = pontuacao_3
            nome_primeiro = nome_3
            menor_nota2 = pontuacao_2
            nome_segundo = nome_2
            menor_nota3 = pontuacao_1
            nome_terceiro = nome_1

if pontuacao_3 == pontuacao_1 and (pontuacao_3 != pontuacao_2 or pontuacao_1 != pontuacao_2):
    if pontuacao_3 < pontuacao_2 or pontuacao_1 < pontuacao_2:
        if nome_3 < nome_1:
            menor_nota = pontuacao_3
            nome_primeiro = nome_3
            menor_nota2 = pontuacao_1
            nome_segundo = nome_1
            menor_nota3 = pontuacao_2
            nome_terceiro = nome_2
        else:
            menor_nota = pontuacao_1
            nome_primeiro = nome_1
            menor_nota2 = pontuacao_3
            nome_segundo = nome_3
            menor_nota3 = pontuacao_2
            nome_terceiro = nome_2
if pontuacao_1 == pontuacao_2 and (pontuacao_1 != pontuacao_3 or pontuacao_2 != pontuacao_3):
    if pontuacao_1 > pontuacao_3 or pontuacao_2 > pontuacao_3:
            menor_nota = pontuacao_3
            nome_primeiro = nome_3
            if nome_1 < nome_2:
                menor_nota2 = pontuacao_1
                nome_segundo = nome_1
                menor_nota3 = pontuacao_2
                nome_terceiro = nome_2
            else:
                menor_nota = pontuacao_3
                nome_primeiro = nome_3
                menor_nota2 = pontuacao_2
                nome_segundo = nome_2
                menor_nota3 = pontuacao_1
                nome_terceiro = nome_1
if pontuacao_2 == pontuacao_3 and (pontuacao_2 != pontuacao_1 or pontuacao_3 != pontuacao_1):
    if pontuacao_2 > pontuacao_1 or pontuacao_3 > pontuacao_1:
            menor_nota = pontuacao_1
            nome_primeiro = nome_1
            if nome_2 < nome_3:
                menor_nota2 = pontuacao_2
                nome_segundo = nome_2
                menor_nota3 = pontuacao_3
                nome_terceiro = nome_3
            else:
                menor_nota = pontuacao_1
                nome_primeiro = nome_1
                menor_nota2 = pontuacao_3
                nome_segundo = nome_3
                menor_nota3 = pontuacao_2
                nome_terceiro = nome_2
if pontuacao_1 == pontuacao_3 and (pontuacao_1 != pontuacao_2 or pontuacao_3 != pontuacao_2):
    if pontuacao_1 > pontuacao_2 or pontuacao_3 > pontuacao_2:
        menor_nota = pontuacao_2
        nome_primeiro = nome_2
        if nome_1 < nome_3:
            menor_nota2 = pontuacao_1
            nome_segundo = nome_1
            menor_nota3 = pontuacao_3
            nome_terceiro = nome_3
        else:
            menor_nota = pontuacao_2
            nome_primeiro = nome_2
            menor_nota2 = pontuacao_1
            nome_segundo = nome_1
            menor_nota3 = pontuacao_3
            nome_terceiro = nome_3

print(f'{nome_primeiro} {menor_nota}')
print(f'{nome_segundo} {menor_nota2}')
print(f'{nome_terceiro} {menor_nota3}')