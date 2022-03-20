# add (adiciona), update(atualiza), clear, discard
# union | (une)
# intersection $ (todos os elementos presentes nos dois sets)0
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^(elementos que estão nos dois sets, mas não em ambos)

s0 = set()  # nao é possivel criar um set vazio utilizando s0 = {} pois isto é um dicionario
s1 = {1, 2, 3, 4, 5}
s1.add(('andrew'))
s1.add(('moreira'))
print(s1)
s1.discard('moreira')
for v in s1:
    print(v)

s2 = set()
# update adiciona o elemento iterando por ele e não tendo uma ordem especifica
s2.update('Andrew')
print(s2)

s3 = set()
s3.update([1, 4, 3, 4, 5], (5, 6, 2, 4))
print(s3)
print()

s10 = {1, 2, 3, 4, 5}
s11 = {2, 3, 4, 5, 6}
s12 = {4, 5, 6, 7, 8}

s20 = s10 ^ s12
print(s20)
