import json


def volta_comeco_arquivo():
    return file.seek(0, 0)


# Deleta o arquivo
# import os
# os.remove('abc.txt')

"""
w+ indica escrita e leitura,
r+ indica leitura e escrita,
a+ indica leitura e append sem apagar o arquivo completamente
"""
with open('abc.txt', 'a+') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 5\n')

    volta_comeco_arquivo()
    print('Lendo linhas:')
    print(file.read())

    print('##############')
    volta_comeco_arquivo()
    print(file.readline(), end='')
    print(file.readline(), end='')
    print(file.readline(), end='')

    print('#############')
    volta_comeco_arquivo()
    for linha in file.readlines():
        print(linha, end='')

d1 = {
    'Pessoa 1': {
        'nome': 'Andrew',
        'idade': '26',
    },
    'Pessoa 2': {
        'nome': 'Mae',
        'idade': '51',
    },
}

d1_json = json.dumps(d1, indent=True)
with open('abc.json', 'w+') as file:
    file.write(d1_json)
