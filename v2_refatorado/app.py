from flask import Flask, request, render_template, redirect, url_for, flash

from services import clientes_service
from services.clientes_service import DadosInvalidosError
from repository import clientes_repository

app = Flask(__name__)
app.secret_key = 'chave-secreta-apenas-para-fins-didaticos'

clientes_repository.criar_tabela()


@app.route('/')
def index():
    clientes = clientes_service.listar_clientes()
    return render_template('index.html', clientes=clientes)


@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form.get('nome')
    email = request.form.get('email')
    idade = request.form.get('idade')

    try:
        clientes_service.cadastrar_cliente(nome, email, idade)
        flash('Cliente cadastrado com sucesso!', 'sucesso')
    except DadosInvalidosError as erro:
        flash(str(erro), 'erro')

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=False)
