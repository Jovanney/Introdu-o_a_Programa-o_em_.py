#input

# se o número informado for ímpar designa que a tal arma é atordoante e quando a arma for par, será do tipo cortante.
arma = int(input())

#variaveis

cas = 'Cassetete'

gar = 'Garrafa de Whisky'

soco = 'Soco Ingles'

lam = 'Lamina Escondida'

pe = 'Pe de Cabra'

cani = 'Canivete'

NOME_DA_ARMA = ''

TIPO_DA_ARMA = ''


if arma < 1 or arma > 6:
    print("Numero invalido")
else:
    if (arma % 2) == 1:
        TIPO_DA_ARMA = 'atordoante'
    else:
        TIPO_DA_ARMA = 'cortante'
    if arma == 1:
        NOME_DA_ARMA = cas
    elif arma == 2:
        NOME_DA_ARMA = gar
    elif arma == 3:
        NOME_DA_ARMA = soco
    elif arma == 4:
        NOME_DA_ARMA = lam
    elif arma == 5:
        NOME_DA_ARMA = pe
    elif arma == 6:
        NOME_DA_ARMA = cani
    print(f'A arma corpo a corpo escolhida foi: {NOME_DA_ARMA}')
    print(f'A arma corpo a corpo escolhida e {TIPO_DA_ARMA}')
