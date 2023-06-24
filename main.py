import sudoku
import sys
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process, Queue
import threading
import time

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

def checar(tabuleiro, n_threads, processo_id):
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
    
    # print(f'Processo {processo_id}: {num_erros} erros encontrados', end=" ") # imprime a qtd. de erros, as threads que encontraram, e as linhas/colunas/regiões onde há erro
    if num_erros > 0:
        texto = ""
        lista_erros = []
        for i in range(len(valores)):
            if len(valores[i]) < 1:
                continue
            lista_erros.append(f"T{i+1}: {', '.join(valores[i])}")
        # print(f"({'; '.join(lista_erros)})")
    # else:
        # print("")

def processo_trabalhador(queue, processo_id, num_threads):
    while queue.qsize() > 0:
        try:
            tupla_tabuleiro = queue.get()
        except:
            break

        # print(f"Processo {processo_id}: resolvendo quebra-cabeças {tupla_tabuleiro[0]}")
        checar(tupla_tabuleiro[1], num_threads, processo_id)
    # print(f"Processo {processo_id} encerrado.")

def main(x, y):
    arquivo = "input-sample.txt"
    queue = Queue()

    num_processos = x # TODO: remover depois
    num_threads = y

    try:
        sudoku.ler(arquivo, queue)
        # for t in tabuleiros:
        #     checar(t, 5)
        # for p in range(num_processos): #TODO: trocar por sys.argv
        #     processo = Process(target=processo_trabalhador, args=(queue, p + 1, num_threads)) #TODO: trocar por sys.argv
        #     processo.start()
        processos = [Process(target=processo_trabalhador, args=(queue, i + 1, num_threads)) for i in range(num_processos)] # cria os processos, baseado em https://superfastpython.com/multiprocessing-for-loop/

        for processo in processos:
            processo.start()

        for processo in processos:
            processo.join()

    except:
        print("Erro!")

for i in range(1, 10):
    st = time.time()
    main(1, i)
    et = time.time()
    tempo = et - st
    print(f"Tempo com 1 processo e {i} thread(s): {tempo}")

for i in range(1, 5):
    st = time.time()
    main(i, 1)
    et = time.time()
    tempo = et - st
    print(f"Tempo com {i} processo(s) e 1 thread: {tempo}")

for i in range(1, 5):
    for j in range(1, 10):
        st = time.time()
        main(i, j)
        et = time.time()
        tempo = et - st
        print(f"Tempo com {i} processo(s) e {j} thread(s): {tempo}")
# main(1, 1)
# main(1, 2)
# main(1, 3)
# main(1, 4)
# main(1, 5)
# main(1, 6)
# main(1, 7)
# main(1, 8)
# main(1, 9)