def passo_gauss(matriz, linha_pivo):
    n = len(matriz)
    m = len(matriz[0])
    pivo = matriz[linha_pivo][linha_pivo]
    if pivo == 0:
        raise ValueError(f"Pivô zero na linha {linha_pivo+1}.")
    # Normaliza a linha do pivô
    for j in range(m):
        matriz[linha_pivo][j] /= pivo
    # Zera a coluna do pivô nas outras linhas
    for i in range(n):
        if i != linha_pivo:
            fator = matriz[i][linha_pivo]
            for j in range(m):
                matriz[i][j] -= fator * matriz[linha_pivo][j]
    return matriz
