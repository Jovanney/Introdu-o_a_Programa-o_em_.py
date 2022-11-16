Nome_1, Nota_1, Duracao_1 =input().split("-")
Nome_2, Nota_2, Duracao_2 =input().split("-")
Nome_3, Nota_3, Duracao_3 =input().split("-")

Nome_1 = str(Nome_1)
Nome_2 = str(Nome_2)
Nome_3 = str(Nome_3)

Nota_1 = float(Nota_1)
Nota_2 = float(Nota_2)
Nota_3 = float(Nota_3)

Duracao_1 = int(Duracao_1)
Duracao_2 = int(Duracao_2)
Duracao_3 = int(Duracao_3)

maior_nota = ''
#caso a nota < 4

if (Nota_1 < 4) and (Nota_2 < 4) and (Nota_3 < 4):
    print("Nota minima nao atingida")

#caso a nota => 4

else:
    if (Nota_1 > Nota_2) and (Nota_1 > Nota_3):
        maior_nota = Nome_1
    elif (Nota_2 > Nota_1) and (Nota_2 > Nota_3):
        maior_nota = Nome_2
    elif (Nota_3 > Nota_2) and (Nota_3 > Nota_1):
        maior_nota = Nome_3

# casos desempate
    if (Nota_1 == Nota_2) and (Nota_1 == Nota_3):
        if (Duracao_1 < Duracao_2) and (Duracao_1 < Duracao_3):
            maior_nota = Nome_1
        if (Duracao_2 < Duracao_1 ) and (Duracao_2 < Duracao_3):
            maior_nota = Nome_2
        if (Duracao_3 < Duracao_2) and (Duracao_3 < Duracao_1):
            maior_nota = Nome_3
# casos com dois maiores e iguais
    if (Nota_1 == Nota_2) and (Nota_1 > Nota_3):
        if Duracao_1 < Duracao_2:
            maior_nota = Nome_1
        else:
            maior_nota = Nome_2
    if (Nota_2 == Nota_3) and (Nota_2 > Nota_1):
        if Duracao_2 < Duracao_3:
            maior_nota = Nome_2
        else:
            maior_nota = Nome_3
    if (Nota_1 == Nota_3) and (Nota_1 > Nota_2):
        if Duracao_1 < Duracao_3:
            maior_nota = Nome_1
        else:
            maior_nota = Nome_3


#output

    print(maior_nota)
