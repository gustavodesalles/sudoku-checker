def ler(arquivo):
    array_tabuleiros = []
    with open(arquivo, "r") as a:
        tabuleiro = []
        for line in a: # percorre todas as linhas do arquivo
            if line.strip == '': # se a linha for vazia, é o fim de um tabuleiro
                array_tabuleiros.append(tabuleiro.copy()) # adiciona o tabuleiro à lista de tabuleiros
                tabuleiro = [] # remove os conteúdos para começar outro tabuleiro
            else:
                linha_sudoku = line.split() # obtém os valores da linha e adiciona ao tabuleiro
                tabuleiro.append(linha_sudoku)
                if next(a, 'end') == 'end': # se for a última linha, adiciona o último tabuleiro à lista e retorna
                    array_tabuleiros.append(tabuleiro)
                    return array_tabuleiros

def checar_linhas(tabuleiro):
    lista_erros_linha = []
    for i in range(len(tabuleiro)): # supõe-se que todos os tabuleiros são 9x9
        if len(set(tabuleiro[i])) != len(tabuleiro): # se a linha do tabuleiro conter repetições, há um erro na solução
            lista_erros_linha.append(i + 1)
    return lista_erros_linha

def checar_colunas(tabuleiro):
    transposto = []
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            transposto[j][i] = tabuleiro[i][j] # transpõe o tabuleiro
    return checar_linhas(transposto)

def checar_regioes(tabuleiro):
    lista_regioes = []
    for i in range(9, 3):
        for j in range(9, 3):
            regiao_em_linha = tabuleiro[i][j:j+3] + tabuleiro[i+1][j:j+3] + tabuleiro[i+2][j:j+3] # obtém a região em formato de linha
            lista_regioes.append(regiao_em_linha)
    return checar_linhas(lista_regioes)