"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudação e nome.
"""


def exer1(saudacao, nome):
    print(f'{saudacao}, {nome}, Exer1')


exer1('Boa noite', 'Andrew')

"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma 
entre eles.
"""


def exer2(num1, num2, num3):
    print(f'Soma é igual a {num1 + num2 + num3} Exer2')


exer2(1, 5, 8)

"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo 
um percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""


def exer3(num1, num2):
    return num1 * (1 + num2 / 100)


print(exer3(100, 15), 'Exer3')
"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro 
da função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, 
retorne o número enviado.
"""


def exer4(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return num


print(exer4(45), 'Exer4')
