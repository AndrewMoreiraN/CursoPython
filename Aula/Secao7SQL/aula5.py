from contextlib import contextmanager

import pymysql.cursors


@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        conexao.close()


with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT nome,sobrenome FROM clientes ORDER BY id DESC LIMIT 100 ')
        resultado = cursor.fetchall()
        for linha in resultado:
            print(linha['nome'], linha['sobrenome'])
