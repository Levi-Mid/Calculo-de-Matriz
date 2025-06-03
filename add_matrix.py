# Versão Melhorada 

def obtem_matriz(nome_completo_do_arquivo):
    matriz = []
    try:
        with open(nome_completo_do_arquivo, "r") as arquivo:
            for linha in arquivo:
                if linha.strip() == "":
                    continue  # Ignora linhas em branco
                parte = linha.split()
                nova_linha = []
                for item in parte:
                    try:
                        nova_linha.append(float(item))
                    except ValueError:
                        raise ValueError(f"Valor inválido encontrado: '{item}'. Apenas números são permitidos.")
                matriz.append(nova_linha)
    except FileNotFoundError:
        raise ValueError("Arquivo não encontrado.")

    # Verifica se tem pelo menos 2 linhas
    if len(matriz) < 2:
        raise ValueError("Poucas linhas")

    # Verifica se todas as linhas têm o mesmo tamanho
    tamanho_linha = len(matriz[0])
    for idx, linha in enumerate(matriz):
        if len(linha) != tamanho_linha:
            raise ValueError(f"Linhas de tamanhos diferentes. Linha {idx+1} tem tamanho {len(linha)}, esperado {tamanho_linha}.")

    # Verifica se a quantidade de colunas é um a mais do que a de linhas
    if tamanho_linha != len(matriz) + 1:
        raise ValueError("A quantidade de colunas deve ser igual à quantidade de linhas + 1.")

    return matriz
