import sys
import time
#cria uma lista com 6 valores
lista = [0, 1, 2, 3, 4, 5]
#troca o valor de lista por um iteravel da lista
lista = iter(lista)
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))

print(hasattr(lista, '__next__'))

lista = list(range(1000))
print(sys.getsizeof((lista)))


def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)


g = gera()
print(next(g))

l1 = [x for x in range(10000)]
print(type(l1))
print(sys.getsizeof(l1))
l2 = (x for x in range(10000))
print(type(l2))
print(sys.getsizeof(l2))
