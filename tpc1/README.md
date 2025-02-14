# Somador On/Off

Este programa implementa um somador que processa números em um texto, com a soma ficando ativa ou desligada quando o programa encotra os comandos `On` e `Off`, no input.

## Como funciona
- Os números encontrados no texto são somados quando o modo está ativado.
- `Off` desativa a soma até que `On` seja encontrado novamente.
- `=` exibe o valor da soma atual.
- No final do texto, a soma final é exibida.

## Como usar
1. Crie um arquivo de texto (`input.txt`) e insira o conteúdo desejado.
2. Execute o script:
   ```sh
   python somadorOnOff.py
   ```
3. O resultado será exibido no terminal.

## Exemplo de entrada (`input.txt`)
```
123abc45On67off89=On12=
```

## Exemplo de saída
```
235 247 247
```


