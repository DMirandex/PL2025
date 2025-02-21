import re
from collections import defaultdict

class AnalisadorCSV:
    def __init__(self, file_path: str):
        with open(file_path, encoding="utf-8") as f:
            self.dataset = self._reconstruct_records(f)

        self.header = self.dataset.pop(0)  # Remover cabeçalho

    def _split_csv_line(self, line):
        # Dividir corretamente ignorando ; dentro de aspas
        fields = re.split(r';(?=(?:[^"]*"[^"]*")*[^"]*$)', line.strip())
        return [field.strip().strip('"') for field in fields]

    def _reconstruct_records(self, linhas):
        records = []
        buffer = []

        for line in linhas:
            buffer.append(line.strip())
            if buffer[-1].count(";") >= 6:  # Pelo menos 7 campos (6 separadores)
                full_line = " ".join(buffer)
                records.append(self._split_csv_line(full_line))
                buffer = []

        return records

    def listar_compositores(self):
        return sorted({linha[4] for linha in self.dataset if len(linha) > 4})

    def distribuicao_obras_por_periodo(self):
        distribuicao = defaultdict(int)
        for linha in self.dataset:
            if len(linha) > 3:
                distribuicao[linha[3]] += 1
        return dict(distribuicao)

    def obras_por_periodo(self):
        obras = defaultdict(list)
        for linha in self.dataset:
            if len(linha) > 3:
                obras[linha[3]].append(linha[0])
        
        # Ordenar os títulos das obras dentro de cada período
        for periodo in obras:
            obras[periodo].sort()
        return dict(obras)


analise = AnalisadorCSV('obras.csv')

while True:
    print("\nEscolhe uma opção:")
    print("1 - Lista ordenada alfabeticamente de compositores musicais")
    print("2 - Distribuição das obras por período")
    print("3 - Dicionário de obras por período")
    print("4 - Sair")

    opcao = input("Digita o número da opção desejada: ")

    match opcao:
        case "1":
            print("\nLista ordenada alfabeticamente de compositores musicais:")
            print(analise.listar_compositores())

        case "2":
            print("\nDistribuição das obras por período:")
            print(analise.distribuicao_obras_por_periodo())

        case "3":
            print("\nDicionário de obras por período:")
            print(analise.obras_por_periodo())

        case "4":
            print("Sair...")
            break

        case _:
            print("Opção inválida. Tenta novamente.")
