# Lista de problemas identificados (v1)

Preencha/ajuste esta lista conforme for revisando `v1_com_problemas/app.py`.
Cada item já está mapeado no código-fonte com o comentário `# PROBLEMA:`.

| #   | Problema                                                                                              | Onde está             | Tipo                        |
| --- | ----------------------------------------------------------------------------------------------------- | --------------------- | --------------------------- |
| 1   | Ausência total de validação de entrada (nome, e-mail e idade aceitam qualquer valor, inclusive vazio) | `cadastrar()`         | Falha de validação          |
| 2   | Consulta SQL construída por concatenação de string, vulnerável a SQL Injection                        | `cadastrar()`         | Falha de segurança          |
| 3   | Regra de negócio, acesso a dados e apresentação (HTML) misturados na mesma função/arquivo             | `app.py` inteiro      | Código mal estruturado      |
| 4   | Nomes de variáveis sem significado (`n`, `e`, `i`)                                                    | `cadastrar()`         | Falta de padrão de código   |
| 5   | Nenhum tratamento de exceções — erro do banco ou de tipo derruba a aplicação com erro 500 cru         | `cadastrar()`         | Falha de confiabilidade     |
| 6   | `debug=True` habilitado, expondo detalhes internos (stack trace) para o usuário final                 | `app.run(debug=True)` | Falha de segurança          |
| 7   | Ausência de qualquer teste automatizado                                                               | projeto inteiro       | Falta de qualidade/processo |
