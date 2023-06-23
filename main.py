import sudoku
import sys
from concurrent.futures import ThreadPoolExecutor
import threading

# def checar(tabuleiro):
#     linhas = ["L" + str(linha) for linha in sudoku.checar_linhas(tabuleiro)]
#     colunas = ["C" + str(coluna) for coluna in sudoku.checar_colunas(tabuleiro)]
#     regioes = ["R" + str(regiao) for regiao in sudoku.checar_regioes(tabuleiro)]
#     erros = linhas + colunas + regioes
#     print(f'{len(erros)} erros encontrados', end=" ")
#     if len(erros) > 0:
#         print(f"({', '.join(erros)})")
#     else:
#         print("")

def checar(tabuleiro, n_threads):
    erros = {}
    transposto = sudoku.transpor(tabuleiro)
    tab_em_blocos = sudoku.obter_regioes_como_linhas(tabuleiro)

    def checar_wrapper(aux): # usado para passar um único parâmetro nos submits
        id_thread = threading.get_ident()
        sudoku.checar_linha(aux[0], id_thread, aux[1], erros, aux[2])

    with ThreadPoolExecutor(max_workers=n_threads) as executor:
        for i in range(9):
            executor.submit(checar_wrapper, (tabuleiro[i], i, "L"))
            executor.submit(checar_wrapper, (transposto[i], i, "C"))
            executor.submit(checar_wrapper, (tab_em_blocos[i], i, "R"))
    
    num_erros = 0
    valores = list(erros.values())
    for v in valores:
        num_erros += len(v)
    
    print(f'{num_erros} erros encontrados', end=" ") # imprime a qtd. de erros, as threads que encontraram, e as linhas/colunas/regiões onde há erro
    if num_erros > 0:
        texto = ""
        lista_erros = []
        for i in range(len(valores)):
            if len(valores[i]) < 1:
                continue
            lista_erros.append(f"T{i+1}: {', '.join(valores[i])}")
        print(f"({'; '.join(lista_erros)})")
    else:
        print("")

def main():
    arquivo = "input-sample.txt"
    try:
        tabuleiros = sudoku.ler(arquivo)
        for t in tabuleiros:
            checar(t, 5)
    except:
        print("Erro!")

main()