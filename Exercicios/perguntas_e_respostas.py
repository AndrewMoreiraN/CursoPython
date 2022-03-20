perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2?',
        'resposta': {'a': '1', 'b': '3', 'c': '4', 'd': '22', },
        'resposta_certa': 'c',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 6 * 8?',
        'resposta': {'a': '68', 'b': '48', 'c': '86', 'd': '42', },
        'resposta_certa': 'b',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 2 + 3 * 4?',
        'resposta': {'a': '234', 'b': '20', 'c': '14', 'd': '24', },
        'resposta_certa': 'c',
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 6 / 2 + 4?',
        'resposta': {'a': '1', 'b': '7', 'c': '5', 'd': '624', },
        'resposta_certa': 'b',
    },
}
respostas_certas = 0
quantidade_perguntas = len(perguntas)
print()
for pk, pv in perguntas.items():
    print(f'{pk}:{pv["pergunta"]}')

    print('Respostas:')
    for rk, rv in pv['resposta'].items():
        print(f'[{rk}]:{rv}')

    resposta = input('Sua resposta: ')
    if (resposta == pv['resposta_certa']):
        print('Resposta correta.')
        respostas_certas += 1
    else:
        print('Resposta incorreta.')

porcentagem_acertos = respostas_certas / quantidade_perguntas * 100
print(f'Você acertou {respostas_certas} questões.')
print(f'Sua porcentagem de acertos foi de {porcentagem_acertos}%')
