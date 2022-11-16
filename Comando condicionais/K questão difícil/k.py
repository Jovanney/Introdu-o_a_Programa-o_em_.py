#'lutador 1'
nome_1 = input()

vida_1 = int(input())

ataque_1 = int(input())

defesa_1 = int(input())

vida_apos_2_round = int()


#'lutador 2'
nome_2 = input()

vida_2 = int(input())

ataque_2 = int(input())

defesa_2 = int(input())

vida_apos_1_round = int()

print('Round 1')

golpe_1 = input()

defesal1 = input()

#sem defesa

if golpe_1 == "jab" and defesal1 == 'X':
    vida_apos_1_round = vida_2 - ataque_1
    if vida_apos_1_round <= 0:
        print(f'NOSSO CAMPEAO E {nome_1} COM UM INCRIVEL NOCAUTE NO PRIMEIRO ROUND'.upper())
if golpe_1 == "direto" and defesal1 == 'X':
    vida_apos_1_round = vida_2 - (ataque_1 * 1.4)
    if vida_apos_1_round <= 0:
        print(f'NOSSO CAMPEAO E {nome_1} COM UM INCRIVEL NOCAUTE NO PRIMEIRO ROUND'.upper())

#bloqueio

if golpe_1 == "jab" and defesal1 == 'Bloqueio':
    vida_apos_1_round = vida_2 - (ataque_1 - (ataque_1 * defesa_2/100))
    if vida_apos_1_round <= 0:
        print(f'NOSSO CAMPEAO E {nome_1} COM UM INCRIVEL NOCAUTE NO PRIMEIRO ROUND'.upper())
if golpe_1 == "direto" and defesal1 == 'bloqueio':
    vida_apos_1_round = vida_2 - (ataque_1 * 1.3 - (ataque_1 * defesa_2/100))
    if vida_apos_1_round <= 0:
        print(f'NOSSO CAMPEAO E {nome_1} COM UM INCRIVEL NOCAUTE NO PRIMEIRO ROUND'.upper())

#esquiva

if golpe_1 == "jab" and defesal1 == 'esquiva':
    ataque_2 = ataque_2 + (ataque_2 * 0.1)
    vida_apos_1_round = vida_2

if golpe_1 == "direto" and defesal1 == 'esquiva':
    ataque_2 = ataque_2 + (ataque_2 * 0.2)
    vida_apos_1_round = vida_2

#round 2

if vida_apos_1_round > 0:
    print('Round 2')
    golpe_2 = input()
    defesal2 = input()
    if golpe_2 == "jab" and defesal2 == 'X':
        vida_apos_2_round = vida_1 - ataque_2
        if vida_apos_2_round <= 0:
            print(f'NOSSO CAMPEAO E {nome_2}'.upper())
    if golpe_2 == "direto" and defesal2 == 'X':
        vida_apos_2_round = vida_1 - (ataque_2 * 1.4)
        if vida_apos_2_round <= 0:
            print(f'NOSSO CAMPEAO E {nome_2}'.upper())

#bloqueio

    if golpe_2 == "jab" and defesal2 == 'bloqueio':
        vida_apos_2_round = vida_1 - (ataque_2 - (ataque_2 * defesa_1/100))
        if vida_apos_2_round <= 0:
            print(f'NOSSO CAMPEAO E {nome_2}'.upper())
    if golpe_2 == "direto" and defesal2 == 'bloqueio':
        vida_apos_2_round = vida_1 - (ataque_2 * 1.3 - (ataque_2 * defesa_1/100))
        if vida_apos_2_round <= 0:
            print(f'NOSSO CAMPEAO E {nome_2}'.upper())

#esquiva

    if golpe_2 == "jab" and defesal2 == 'esquiva':
        ataque_1 = ataque_1 + (ataque_1 * 0.1)
        vida_apos_2_round = vida_1
    if golpe_2 == "direto" and defesal2 == 'esquiva':
        ataque_1 = ataque_1 + (ataque_1 * 0.2)
        vida_apos_2_round = vida_1

#round 3
if vida_apos_2_round > 0:
    print('Round 3')

    golpe_3 = input()

    defesal3 = input()

    print(f'{nome_1} SO TEM MAIS UM ROUND PARA DERRUBAR SEU ADVERSARIO'.upper())

    if golpe_3 == "jab" and defesal3 == 'X':
        vida_apos_1_round = vida_2 - ataque_1
        if vida_apos_1_round <= 0:
            print(f'NOSSO CAMPEAO E {nome_1}'.upper())
        else:
            print(f'NOSSO CAMPEAO E {nome_2}'.upper())
    if golpe_3 == "direto" and defesal3 == 'X':
        if vida_apos_1_round <= 0:
            print(f'NOSSO CAMPEAO E {nome_1}'.upper())
        else:
            print(f'NOSSO CAMPEAO E {nome_2}'.upper())


#bloqueio

    if golpe_3 == "jab" and defesal3 == 'bloqueio':
        vida_apos_1_round = vida_2 - (ataque_1 - (ataque_1 * defesa_2 / 100))
        if vida_apos_1_round <= 0:
            print(f'NOSSO CAMPEAO E {nome_1}'.upper())
        else:
            print(f'NOSSO CAMPEAO E {nome_2}'.upper())
    if golpe_3 == "direto" and defesal3 == 'bloqueio':
        vida_apos_1_round = vida_2 - (ataque_1 * 1.3 - (ataque_1 * defesa_2 / 100))
        if vida_apos_1_round <= 0:
            print(f'NOSSO CAMPEAO E {nome_1}'.upper())
        else:
            print(f'NOSSO CAMPEAO E {nome_2}'.upper())


    #esquiva

    if golpe_3 == "jab" and defesal3 == 'esquiva':
        print(f'NOSSO CAMPEAO E {nome_2}'.upper())
    if golpe_3 == "direto" and defesal3 == 'esquiva':
        print(f'NOSSO CAMPEAO E {nome_2}'.upper())
