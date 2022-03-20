"""
For in em Python
Iterando strings com for
Função range (start = 0, stop, step = 1)
"""

texto = 'Python'

# c = 0
# while c < len(texto):
#     print(texto[c])
#     c += 1

for letra in texto:
    print(letra)

for n in range(10):  # range (0, 10, 1)
    print(n)

for n in range(20, 10, -1):  # stop nao é incluído
    print(n)
