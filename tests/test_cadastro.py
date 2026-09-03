import pytest

from services.clientes_service import validar_dados, DadosInvalidosError


def test_dados_validos_sao_aceitos():
    nome, email, idade = validar_dados('Maria Silva', 'maria@email.com', '30')

    assert nome == 'Maria Silva'
    assert email == 'maria@email.com'
    assert idade == 30


def test_nome_vazio_gera_erro():
    with pytest.raises(DadosInvalidosError):
        validar_dados('', 'maria@email.com', '30')


def test_email_invalido_gera_erro():
    with pytest.raises(DadosInvalidosError):
        validar_dados('Maria Silva', 'email-invalido', '30')


@pytest.mark.parametrize('idade_invalida', ['abc', '-1', '200'])
def test_idade_invalida_gera_erro(idade_invalida):
    with pytest.raises(DadosInvalidosError):
        validar_dados('Maria Silva', 'maria@email.com', idade_invalida)
