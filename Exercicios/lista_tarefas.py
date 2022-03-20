"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    lista tarefas
    opçao de defazer (a cada vez que chamarmos, desfaz a ultima açao)
    opcao de refazer (a cada vez que cahamarmos, refaz a ultima açao)

    ['Tarefa 1', 'Tarefa 2']
    ['Tarefa 1'] <- Desfazer
    ['Tarefa 1', 'Tarefa 2'] <- refazer

    input <- nova tarefa
"""

todo_list = []
redo_list = []


def show_op(todo_list):
    print()
    print('Tarefas: ')
    print(todo_list)
    print()


def add(lista_tarefas, str):
    lista_tarefas.append(str)
    return


def undo(lista_tarefas, redo_list):
    if not lista_tarefas:
        print('Nada a remover')
        return
    ultima_tarefa = lista_tarefas.pop()
    redo_list.append(ultima_tarefa)


def redo(lista_tarefas, redo_list):
    if not redo_list:
        print('Nada a refazer')
        return
    lista_tarefas.append(redo_list.pop())


while (True):
    menu = input('Digite undo, redo, add, ls ou sair: ')
    if menu == 'undo':
        undo(todo_list, redo_list)
    elif menu == 'redo':
        redo(todo_list, redo_list)
    elif menu == 'add':
        add(todo_list, input('Digite a tarefa a adicionar: '))
    elif menu == 'ls':
        show_op(todo_list)
    elif menu == 'sair':
        break
    else:
        print('Valor inválido.')
