"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
"""

nome = "Andrew"
idade = 26
altura = 1.8
e_maior = idade > 18
peso = 110
imc = peso / altura ** 2

print("Nome:", nome, type(nome))
print("Idade:", idade, type(idade))
print("Altura:", altura, type(altura))
print("É maior:", e_maior, type(e_maior))
print("IMC =", imc)
