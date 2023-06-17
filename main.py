import sudoku
import sys

def checar(tabuleiro):
    linhas = ["L" + str(linha) for linha in sudoku.checar_linhas(tabuleiro)]
    colunas = ["C" + str(coluna) for coluna in sudoku.checar_colunas(tabuleiro)]
    regioes = ["R" + str(regiao) for regiao in sudoku.checar_regioes(tabuleiro)]
    erros = linhas + colunas + regioes
    print(f'{len(erros)} erros encontrados', end=" ")
    if len(erros) > 0:
        print(f"({', '.join(erros)})")
    else:
        print("")

def main():
    arquivo = "input-sample.txt"
    try:
        tabuleiros = sudoku.ler(arquivo)
        for t in tabuleiros:
            checar(t)
    except:
        print("Erro!")

main()