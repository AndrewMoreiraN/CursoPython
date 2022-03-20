"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""

###Código
from itertools import count

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Palhoça']

estados = ['SP', 'MG', 'BA']

cidades_estados = zip(estados, cidades)
cidades_estados_longest = zip(indice, estados, cidades)

for indice, estado, cidade in cidades_estados_longest:
    print(indice, estado, cidade)
