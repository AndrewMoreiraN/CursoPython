hora = input('Digite a  (0-23): ')

if hora.isnumeric() and 0 <= int(hora) <= 23:
    hora = int(hora)
    if hora < 12:
        print('Bom dia!')
    elif 18 > hora >= 12:
        print('Boa tarde!')
    else:
        print('Boa noite!')
else:
    print('Valor digitado não é um horário válido.')
