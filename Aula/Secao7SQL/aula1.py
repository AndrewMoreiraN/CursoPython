import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nome TEXT,'
#                'peso REAL'
#                ')')
#
# cursor.execute('INSERT INTO clientes (nome,peso) VALUES (?, ?)', ('Mae', 50))
# cursor.execute('INSERT INTO clientes (nome,peso) VALUES (:nome, :peso)', {'nome': 'Eu', 'peso': 70})
# cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)', {'id': None, 'nome': 'AA', 'peso': 70})
# conexao.commit()
# cursor.execute('UPDATE clientes SET nome=:nome WHERE id=:id', {'nome': 'Marli', 'id': '2'})
# cursor.execute('DELETE FROM clientes WHERE id=:id', {"id": 7})

cursor.execute('SELECT nome, peso FROM clientes WHERE peso < 80')
for linha in cursor.fetchall():
    print(linha)

cursor.close()
conexao.close()
