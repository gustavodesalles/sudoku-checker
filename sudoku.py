TAMANHO_TABULEIRO = 9 # supõe-se que todos os tabuleiros são 9x9

# def ler(arquivo):
#     array_tabuleiros = []
#     with open(arquivo, "r") as a:
#         tabuleiro = []
#         for line in a: # percorre todas as linhas do arquivo
#             if line.strip == '': # se a linha for vazia, é o fim de um tabuleiro
#                 if len(tabuleiro) != TAMANHO_TABULEIRO:
#                     raise Exception("Tabuleiro inválido")
#                 array_tabuleiros.append(tabuleiro.copy()) # adiciona o tabuleiro à lista de tabuleiros
#                 tabuleiro = [] # remove os conteúdos para começar outro tabuleiro
#             else:
#                 linha_sudoku = []
#                 for x in line:
#                     try:
#                         linha_sudoku.append(int(x))
#                     except ValueError:
#                         continue
                
#                 if len(linha_sudoku) != TAMANHO_TABULEIRO:
#                     raise Exception("Número inválido de elementos")
#                 elif any((x < 1 and x > TAMANHO_TABULEIRO) or type(x) is not int for x in linha_sudoku):
#                     raise Exception("Caractere(s) inválido(s) no tabuleiro")
#                 tabuleiro.append(linha_sudoku)

#                 atual = a.tell()
#                 proxima = next(a, 'end')
#                 if proxima == 'end': # se for a última linha, adiciona o último tabuleiro à lista e retorna
#                     array_tabuleiros.append(tabuleiro)
#                     return array_tabuleiros
#                 a.seek(atual)

def ler(arquivo):
    a = open(arquivo, "r")
    linhas_texto = a.readlines()

    array_tabuleiros = []
    tabuleiro = []
    for line in linhas_texto:
        if line.strip() == '': # se a linha for vazia, é o fim de um tabuleiro
            if len(tabuleiro) != TAMANHO_TABULEIRO:
                raise Exception("Tabuleiro inválido")
            array_tabuleiros.append(tabuleiro.copy()) # adiciona o tabuleiro à lista de tabuleiros
            tabuleiro = [] # remove os conteúdos para começar outro tabuleiro
        else:
            linha_sudoku = []
            for x in line:
                try:
                    linha_sudoku.append(int(x))
                except ValueError:
                    continue

            if len(linha_sudoku) != TAMANHO_TABULEIRO:
                raise Exception("Número inválido de elementos")
            elif any((x < 1 and x > TAMANHO_TABULEIRO) or type(x) is not int for x in linha_sudoku):
                raise Exception("Caractere(s) inválido(s) no tabuleiro")
            tabuleiro.append(linha_sudoku)

            # proxima = next(linhas_texto, 'end')
            # if proxima == 'end': # se for a última linha, adiciona o último tabuleiro à lista e retorna
            if linhas_texto.index(line) == len(linhas_texto) - 1:
                if len(tabuleiro) != TAMANHO_TABULEIRO:
                    raise Exception("Tabuleiro inválido")
                array_tabuleiros.append(tabuleiro.copy())
                return array_tabuleiros


def checar_linhas(tabuleiro):
    lista_erros_linha = []
    for i in range(TAMANHO_TABULEIRO): 
        if len(set(tabuleiro[i])) != TAMANHO_TABULEIRO: # se a linha do tabuleiro conter repetições, há um erro na solução
            lista_erros_linha.append(i + 1)
    return lista_erros_linha

def checar_colunas(tabuleiro):
    # transposto = []
    # for i in range(TAMANHO_TABULEIRO):
    #     for j in range(TAMANHO_TABULEIRO):
    #         transposto[j][i] = tabuleiro[i][j] # transpõe o tabuleiro
    transposto = list(map(list, zip(*tabuleiro)))
    return checar_linhas(transposto)

def checar_regioes(tabuleiro):
    lista_regioes = []
    for i in range(0, TAMANHO_TABULEIRO, 3):
        for j in range(0, TAMANHO_TABULEIRO, 3):
            regiao_em_linha = tabuleiro[i][j:j+3] + tabuleiro[i+1][j:j+3] + tabuleiro[i+2][j:j+3] # obtém a região em formato de linha
            lista_regioes.append(regiao_em_linha)
    return checar_linhas(lista_regioes)