# TPC2 - Analisador de Obras Musicais

## Descrição
Este programa, `tpc2.py`, analisa um ficheiro CSV contendo informações sobre obras musicais e fornece diferentes tipos de análise, tais como:
- Lista ordenada alfabeticamente dos compositores musicais.
- Distribuição das obras por período.
- Dicionário onde cada período está associado a uma lista alfabética das obras desse período.

O programa lê os dados sem utilizar o módulo `csv` do Python e garante que campos delimitados por `;` dentro de aspas são corretamente processados.


## Como Utilizar
1. Certifica-te de que tens um ficheiro CSV chamado `obras.csv` na mesma pasta que `tpc2.py`.
2. Executa o programa com o seguinte comando:
   ```sh
   python3 tpc2.py
   ```
3. Escolhe uma das opções disponíveis no menu:
   - **1**: Lista de compositores ordenada alfabeticamente.
   - **2**: Distribuição das obras por período.
   - **3**: Dicionário de obras por período.
   - **4**: Sair do programa.


## Autor
- Nome: Diodo Miranda
- Número: a100839


