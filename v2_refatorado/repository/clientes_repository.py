import sqlite3

DB_PATH = 'clientes.db'


def obter_conexao():
    return sqlite3.connect(DB_PATH)


def criar_tabela():
    conn = obter_conexao()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            idade INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def inserir_cliente(nome, email, idade):
    conn = obter_conexao()
    conn.execute('INSERT INTO clientes (nome, email, idade) VALUES (?, ?, ?)', (nome, email, idade))
    conn.commit()
    conn.close()


def listar_clientes():
    conn = obter_conexao()
    linhas = conn.execute('SELECT nome, email, idade FROM clientes').fetchall()
    conn.close()
    return linhas
