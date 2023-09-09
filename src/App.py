from Atividade import *
import os

diret_atividade = 'src/atividade'
diret_gabarito = 'src/gabarito'


if not os.path.exists(diret_atividade):
    os.makedirs(diret_atividade)
if not os.path.exists(diret_gabarito):
    os.makedirs(diret_gabarito)


for i in range(1, 36):
    atividade, respostas = criar_atv()

    perguntas = os.path.join(diret_atividade, f'ativ_{i}.txt')
    gabarito = os.path.join(diret_gabarito, f'gabarito_{i}.txt')

    with open(perguntas, 'w', encoding='utf-8') as arquivo:
        arquivo.write(atividade)

    with open(gabarito, 'w', encoding='utf-8') as arquivo:
        for resposta in respostas:
            arquivo.write(str(resposta) + '\n')
    

    