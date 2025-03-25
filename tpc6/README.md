# Calculadora LL(1) em Python

Este projeto implementa um analisador léxico e um parser LL(1) para a avaliação de expressões matemáticas simples. Utiliza a biblioteca `ply` para a análise léxica.

## Estrutura do Projeto

O projeto contém os seguintes ficheiros:

- **calc_lex.py**: Responsável pela análise léxica, identificando tokens como números, operadores matemáticos e parênteses.
- **calc_yacc.py**: Implementa um parser LL(1) para analisar e avaliar expressões matemáticas utilizando regras gramaticais definidas.

## Funcionalidades

- Suporta operações de adição (`+`), subtração (`-`), multiplicação (`*`) e divisão (`/`).
- Reconhece números inteiros e parênteses para definir a precedência de operações.
- Utiliza um parser LL(1) para analisar e calcular a expressão.
- Lida com erros sintáticos e divisão por zero.


## Como Utilizar

Executa o ficheiro `calc_yacc.py` para testar expressões matemáticas:

```bash
python calc_yacc.py
```

Exemplo de entrada e saída:

```
Resultado de '2+3': 5
Resultado de '67-(2+3*4)': 53
Resultado de '(9-2)*(13-4)': 63
```

## Explicação do Funcionamento

### Analisador Léxico (`calc_lex.py`)

Define os seguintes tokens:
- `ADD` (`+`)
- `MINUS` (`-`)
- `MULT` (`*`)
- `DIV` (`/`)
- `NUMBER` (números inteiros)
- `AP` (`(`) e `FP` (`)`) para parênteses

O lexer lê a expressão e converte-a numa sequência de tokens.

### Parser LL(1) (`calc_yacc.py`)

O parser segue regras recursivas para interpretar e avaliar expressões:
- `expr`: Expressões com soma e subtração.
- `term`: Termos com multiplicação e divisão.
- `factor`: Números e expressões entre parênteses.

