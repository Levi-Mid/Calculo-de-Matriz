def divideIndice(matriz, primeiraLista, segundaLista):
    resultadoPar = []
    for i in range(len(matriz[primeiraLista])): 
        denominador = matriz[segundaLista][i]
        numerador = matriz[primeiraLista][i]
        if i == 3:
            break
        if denominador != 0:
            resultado1 = numerador / denominador
            resultadoPar.append(resultado1)
        else:
            resultadoPar.append("∞")
    return resultadoPar
   
def criaPares(matriz, qtdLinhas):
    pares=[]
    for l in range(qtdLinhas-1):
        for i in range(1, qtdLinhas):
            if not l==i:
                pares.append([l,i])
    return pares

def verificaMatrizValida(matriz):
    qtdLinhas = len(matriz)
    pares = criaPares(matriz, qtdLinhas)
    matriz_resultados = []
    for p in pares:
        matriz_resultados.append(divideIndice(matriz,p[0],p[1]))
    print(matriz_resultados)
    for resultado in matriz_resultados:
        for numero in  range(len(resultado)):
            for comparar in range(len(resultado)):
                print(resultado[comparar])
                if comparar != numero and resultado[comparar] == resultado[numero]:
                    return [False, qtdLinhas]
    for lista in matriz:
        if len(lista)-1 != qtdLinhas:
            return [False, qtdLinhas]
    return [True, qtdLinhas]

'''
TESTE

matriz=[[0,3,2,28],\
        [4,0,2,24],\
        [2,0,2,16]]

result=verificaMatrizValida(matriz)
print(result[0])
'''
