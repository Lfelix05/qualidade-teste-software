# Propostas de melhoria (v1 → v2)

| # | Problema (v1) | Melhoria proposta (v2) |
|---|---------------|--------------------------|
| 1 | Sem validação de entrada | Função `validar_dados()` centralizada em `services/clientes_service.py`, valida nome, e-mail (regex) e idade (numérica, faixa 0–130) |
| 2 | SQL Injection via concatenação de string | Query parametrizada (`?`) em `repository/clientes_repository.py` |
| 3 | Tudo misturado em um arquivo só | Separação em 3 camadas: rota (`app.py`) → regra de negócio (`services/`) → acesso a dados (`repository/`) |
| 4 | Nomes de variável ruins | Nomes descritivos (`nome`, `email`, `idade`) em todo o código |
| 5 | Nenhum tratamento de erro | Exceção customizada `DadosInvalidosError`, capturada na rota e exibida como mensagem amigável (`flash`) |
| 6 | `debug=True` em execução | `debug=False` por padrão |
| 7 | Nenhum teste automatizado | 4 testes com `pytest` cobrindo os principais cenários de validação (ver `tests/test_cadastro.py`) |

