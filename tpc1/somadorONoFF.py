def processar_texto(texto):
    soma = 0
    numero_atual = 0
    ativado = True
    resultado = []
    
    i = 0
    while i < len(texto):
        char = texto[i]
        
        if char.isdigit():
            numero_atual = numero_atual * 10 + int(char)
        else:
            soma += numero_atual if ativado else 0
            numero_atual = 0
            
            if char == '=':
                resultado.append(str(soma))
            elif texto[i:i+2].lower() == "on":
                ativado = True
                i += 1 #ignora o proximo caracter
            elif texto[i:i+3].lower() == "off":
                ativado = False
                i += 2  #ignora o proximos 2 caracteres
        
        i += 1
    
    soma += numero_atual if ativado else 0  # Adiciona o último número acumulado
    resultado.append(str(soma))
    
    return " ".join(resultado)

# Ler de um ficheiro txt
def ler_ficheiro(nome_ficheiro):
    with open(nome_ficheiro, 'r', encoding='utf-8') as f:
        texto = f.read()
    return processar_texto(texto)


nome_ficheiro = "input.txt"
print(ler_ficheiro(nome_ficheiro))
