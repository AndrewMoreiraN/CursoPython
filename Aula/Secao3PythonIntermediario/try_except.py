try:
    a = 0
    try:
        a = 1 / 0
    except:
        print('Erro')
except NameError as erro:
    print('Erro:', erro)
except (IndexError, KeyError) as erro:
    print('Erro de indice ou chave', erro)
except Exception as erro:
    print('Ocorreu um erro inesperado:', erro)
else:
    # print('Seu codigo foi executado com sucesso!')
    # print(a)
    pass
finally:
    a = ''
    # print('Finalmente.')
print(a)
