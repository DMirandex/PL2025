# Analisador Lexical com PLY

## Descrição
O `analisadorLex.py` é um analisador lexical desenvolvido em Python que utiliza a biblioteca [PLY (Python Lex-Yacc)](https://www.dabeaz.com/ply/).

## Funcionalidades
- Identifica diferentes tipos de tokens, incluindo variáveis, inteiros, URIs, strings, tags de idioma e palavras-chave reservadas.
- Suporta reconhecimento de palavras-chave como `SELECT`, `WHERE` e `LIMIT`.
- Ignora espaços em branco e tabs.
- Trata erros lexicais identificando caracteres inesperados.

## Tokens Reconhecidos
O analisador léxico identifica os seguintes tokens:

| Token    | Exemplo |
|----------|---------|
| COMMENT  | `# Comentário` |
| VAR      | `?nome`, `?desc` |
| INT      | `1000` |
| URI      | `dbo:MusicalArtist` |
| STRING   | `"Chuck Berry"` |
| LANG     | `@en`, `@pt` |
| A        | `a` |
| DOT      | `.` |
| LCB      | `{` |
| RCB      | `}` |
| ID       | `foaf:name`, `dbo:artist` |
| SELECT, WHERE, LIMIT | Palavras-chave reservadas |

## Implementação
- Expressões regulares definem os padrões para reconhecimento dos tokens.
- Funções `t_<TOKEN>` definem as regras para cada token.
- A função `t_error` lida com caracteres inesperados.
- Um exemplo de entrada é fornecido para testes.

## Como Executar
Para executar o analisador lexico:

1. Execute o script `analisadorLex.py`:
   ```sh
   python3 analisadorLex.py
   ```

O output será a lista de tokens reconhecidos no texto de input presente no script.
