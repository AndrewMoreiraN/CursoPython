usuario = input('Digite o usuário: ')
qtd_char = len(usuario)

if qtd_char < 6:
    print('Digite pelo menos 6 caracteres.')
else:
    print('Você foi cadastrado no sistema.')
print(f'{usuario} tem {qtd_char} caracteres.')
