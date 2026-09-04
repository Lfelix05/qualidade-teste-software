# Refatoração ISO 25010 — Cadastro de Clientes

Trabalho da disciplina **Qualidade e Teste de Software** (UNESC, campus
Colatina — Sistemas de Informação, 7º/8º período). Professor: Riciere
Massariol.

## O que é este projeto

Um sistema simples de cadastro de clientes, criado em duas versões
propositalmente:

- **`v1_com_problemas/`** — versão inicial, com defeitos de qualidade
  inseridos de propósito (falta de validação, SQL Injection, código mal
  estruturado, tratamento de erro inexistente). Cada defeito está marcado
  no código com o comentário `# PROBLEMA:`.
- **`v2_refatorado/`** — versão corrigida, com os problemas da v1
  resolvidos: validação de dados, consultas parametrizadas, separação em
  camadas (rota / regra de negócio / acesso a dados) e tratamento de erro.

## Estrutura do repositório

```
.
├── docs/
│   ├── problemas-identificados.md   # lista de problemas da v1
│   ├── melhorias-propostas.md       # propostas de melhoria v1 -> v2
│   └── iso25010.md                  # relação de cada melhoria com a ISO/IEC 25010
├── v1_com_problemas/
│   └── app.py                       # versão com defeitos propositais
├── v2_refatorado/
│   ├── app.py                       # rota Flask (somente HTTP)
│   ├── services/clientes_service.py # validação e regra de negócio
│   ├── repository/clientes_repository.py # acesso ao banco (SQLite)
│   └── templates/index.html
├── tests/
│   └── test_cadastro.py             # casos de teste (pytest) da v2
├── requirements.txt
└── README.md
```

## Como rodar

Requer Python 3.10+.

```bash
python -m venv .venv
source .venv/bin/activate      # no Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

**Rodar a v1 (com problemas):**
```bash
cd v1_com_problemas
python app.py
# abrir http://127.0.0.1:5000
```

**Rodar a v2 (refatorada):**
```bash
cd v2_refatorado
python app.py
# abrir http://127.0.0.1:5000
```

**Rodar os testes:**
```bash
pytest tests/ -v
```

## Sobre a escolha técnica

Optou-se por uma aplicação web simples com back-end em Flask (em vez de um
script puramente em linha de comando) porque isso permite demonstrar de
forma mais concreta características da ISO/IEC 25010 como Usabilidade e
Segurança, além de servir como prática de desenvolvimento web em Python.
