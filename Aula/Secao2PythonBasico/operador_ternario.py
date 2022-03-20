"""
Operador ternário em Python
"""
logged_usar = False

# if logged_usar:
#     msg = 'Usuário logado.'
# else:
#     msg = 'Usuário precisa logar.'

msg = 'Usuário logado.' if logged_usar else 'Usuário precisa logar.'

print('Usuário logado.' if logged_usar else 'Usuário precisa logar.')
