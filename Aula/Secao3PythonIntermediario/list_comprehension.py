l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ex1 = [variavel for variavel in l1]

ex2 = [v * 2 for v in l1]
ex3 = [(v, v2) for v in l1 for v2 in range(0, v)]

l2 = ['Luiz', 'Andrew', 'Mae']
ex4 = [v.upper().replace('A', '@') for v in l2]

tupla = (
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
)
ex5 = [[y, x] for x, y in tupla]
ex5 = dict(ex5)

l3 = range(100)
ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]

ex7 = [v if v % 3 == 0 else 'Não é' for v in l3]
