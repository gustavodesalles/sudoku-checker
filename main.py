import sudoku

def checar(tabuleiro):
    linhas = ["L" + linha for linha in sudoku.checar_linhas(tabuleiro)]
    colunas = ["C" + coluna for coluna in sudoku.checar_colunas(tabuleiro)]
    regioes = ["R" + regiao for regiao in sudoku.checar_regioes(tabuleiro)]
    erros = linhas + colunas + regioes
    print(f'{len(erros)} erros encontrados', end=" ")
    if len(erros) > 0:
        print(f"({', '.join(erros)})")

def main(arquivo):
    tabuleiros = sudoku.ler(arquivo)
    for t in tabuleiros:
        checar(t)