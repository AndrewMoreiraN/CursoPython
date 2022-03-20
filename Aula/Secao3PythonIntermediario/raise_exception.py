def divide(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser 0.')
    try:
        return n1 / n2
    except ZeroDivisionError as erro:
        print(erro, 'dentro')
        raise


try:
    print(divide(2, 0))
except ZeroDivisionError as erro:
    print(erro, 'fora')

try:
    print(divide(2, 0))
except ValueError as erro:
    print(erro)
