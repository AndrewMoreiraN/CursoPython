"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
"""

nome = "Andrew"
idade = 26
altura = 1.8
e_maior = idade > 18
peso = 110
imc = peso / altura ** 2

print(nome, 'tem', idade, 'anos e seu imc é', imc)
# F-Strings, em que as variaveis sao colocadas utilizando seus nomes dentro da string.
#:.2f indica que o float deve mostrar apenas 2 casas decimais
print(f'{nome} tem {idade} anos e seu imc é {imc:.2f}')
# format string, as variaveis sao colocadas em ordem dentro das chaves da string
print('{} tem {} anos e seu imc é {:.2f}'.format(nome, idade, imc))
# colocando numeros nas chaves permite identifcar qual chave recebe qual variavel em sua ordem
print('{0} {0}{2}{1} tem {1} anos e seu imc é {2:.2f}'.format(nome, idade, imc))
# pode se nomear as chaves inves de apenas pela posiçao das variaveis
print('{n} tem {i} anos e seu imc é {im:.2f}'.format(n=nome, i=idade, im=imc))
