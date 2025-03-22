# Máquina de Venda Automática

Este é um programa em Python que simula uma máquina de venda automática. O utilizador pode listar produtos, inserir moedas, selecionar produtos e sair da aplicação.

## Funcionalidades
- **LISTAR**: Mostra a lista de produtos disponíveis, juntamente com o seu código, nome, quantidade e preço.
- **MOEDA <VALOR>**: Permite inserir dinheiro na máquina, aceitando euros (e) e cêntimos (c). Exemplo: `MOEDA 1e,50c`.
- **SELECIONAR <COD>**: Permite escolher um produto pelo código, descontando o valor do saldo inserido.
- **SAIR**: Encerra a aplicação, devolvendo o troco se houver saldo remanescente.

## Requisitos
- Python 3.x
- Bibliotecas:
  - `ply` (para análise lexical)
  - `tabulate` (para exibição da lista de produtos)


## Como Utilizar
1. Certifica-te de que existe um ficheiro `stock.json` com a estrutura correta (ver exemplo abaixo).
2. Executa o programa:
```sh
python3 maquinaVenda.py
```
3. Insere comandos conforme necessário.

## Exemplo de `stock.json`
```json
[
{
        "cod": "A10",
        "nome": "sumol 0.33L",
        "quant": 9,
        "preco": 1.5
    },
    {
        "cod": "B22",
        "nome": "barrinha de cereais",
        "quant": 6,
        "preco": 1.2
    }
]
```

## Exemplo de Uso
```
Operação: LISTAR
+-----+------+------------+-------+
| COD | NOME | QUANTIDADE | PREÇO |
+-----+------+------------+-------+
| A10  | sumol | 9         | 1.50€ |
| B22  | barrinha | 6         | 1.20€ |
+-----+------+------------+-------+

Operação: MOEDA 2e,50c
Saldo = 2e50c

Operação: SELECIONAR A1
Pode retirar o produto dispensado "Água"

Operação: SAIR
Pode retirar o troco: 2x 1e.
Até à próxima!
```

