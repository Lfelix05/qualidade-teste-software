from flask import Flask, request
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('clientes.db', check_same_thread=False)
conn.execute('CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, idade TEXT)')
conn.commit()


@app.route('/')
def index():
    linhas = conn.execute('SELECT nome, email, idade FROM clientes').fetchall()

    html = '<h1>Cadastro de Clientes</h1>'
    html += '<form method="POST" action="/cadastrar">'
    html += 'Nome: <input name="nome"><br>'
    html += 'Email: <input name="email"><br>'
    html += 'Idade: <input name="idade"><br>'
    html += '<input type="submit" value="Cadastrar">'
    html += '</form>'
    html += '<h2>Clientes cadastrados</h2><ul>'
    for linha in linhas:
        html += f'<li>{linha[0]} - {linha[1]} - {linha[2]}</li>'
    html += '</ul>'
    return html


@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    n = request.form['nome']
    e = request.form['email']
    i = request.form['idade']

    query = "INSERT INTO clientes (nome, email, idade) VALUES ('" + n + "', '" + e + "', '" + i + "')"
    conn.execute(query)
    conn.commit()

    return f'<p>Cliente {n} cadastrado com sucesso!</p><a href="/">Voltar</a>'


if __name__ == '__main__':
    app.run(debug=True)
