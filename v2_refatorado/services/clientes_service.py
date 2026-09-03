import re

from repository import clientes_repository

EMAIL_REGEX = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')
IDADE_MINIMA = 0
IDADE_MAXIMA = 130


class DadosInvalidosError(Exception):
    pass


def validar_dados(nome, email, idade):
    if not nome or not nome.strip():
        raise DadosInvalidosError('Nome é obrigatório.')

    if not email or not EMAIL_REGEX.match(email):
        raise DadosInvalidosError('E-mail inválido.')

    try:
        idade_numerica = int(idade)
    except (TypeError, ValueError):
        raise DadosInvalidosError('Idade deve ser um número.')

    if idade_numerica < IDADE_MINIMA or idade_numerica > IDADE_MAXIMA:
        raise DadosInvalidosError(f'Idade deve estar entre {IDADE_MINIMA} e {IDADE_MAXIMA}.')

    return nome.strip(), email.strip(), idade_numerica


def cadastrar_cliente(nome, email, idade):
    nome_validado, email_validado, idade_validada = validar_dados(nome, email, idade)
    clientes_repository.inserir_cliente(nome_validado, email_validado, idade_validada)


def listar_clientes():
    return clientes_repository.listar_clientes()
