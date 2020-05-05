from searches import best
from searches import dfs
from searches import astar
from searches import bfs
from searches import anne
from tools.desenha_mapa import desenha_mapa
from randomfill.generate import map_template
import io
from tools import monitor
from timeit import Timer
from tools import user_interaction as user


def desenha_caminho(path, mapa, largura, altura, inicio, fim):
    if (path != None):
        print()
        print('Nos expandidos')
        print()
        print(path)
        print()
        desenha_mapa(mapa, largura, altura, espaco=1, path=path, inicio=inicio, objetivo=fim)
        print()
        print('Contagem: {0}'.format(len(path)))
        print()
    else:
        print('Não há caminho')


def executa(n_times, mapa, inicio, fim, largura, altura, i):
    if (i == 0):
        print()
        print('DFS')
        print()
        t = Timer(lambda: dfs.depth_first_search(mapa, inicio, fim))
        print(f"Time spend to run  DFS algorithm {t.timeit(number=n_times) / n_times}")
        monitor.monitor()
        path = dfs.depth_first_search(mapa, inicio, fim)
        desenha_caminho(path, mapa, largura, altura, inicio, fim)
        print()

    if (i == 1):
        print()
        print('AStar')
        print()
        heuristica = user.define_heuristica()
        print()
        t2 = Timer(lambda: astar.aestrela(mapa, inicio, fim, heuristica))
        print(f"Time spend to run A* algorithm {t2.timeit(number=n_times) / n_times}")
        monitor.monitor()
        path = astar.aestrela(mapa, inicio, fim, heuristica)
        desenha_caminho(path, mapa, largura, altura, inicio, fim)
    if (i == 2):
        print()
        print('BFS')
        t3 = Timer(lambda: bfs.breadth_first_search(mapa, inicio, fim))
        print(f"Time spend to run BFS algorithm {t3.timeit(number=n_times) / n_times}")
        monitor.monitor()
        path = bfs.breadth_first_search(mapa, inicio, fim)
        desenha_caminho(path, mapa, largura, altura, inicio, fim)
    if (i == 3):
        print()
        print('Best First')
        print()
        heuristica = user.define_heuristica()
        print()
        t4 = Timer(lambda: best.best_first_search(mapa, inicio, fim, heuristica))
        print(f"Time spend to run Best first search algorithm {t4.timeit(number=n_times) / n_times}")
        monitor.monitor()
        path = best.best_first_search(mapa, inicio, fim, heuristica)
        desenha_caminho(path, mapa, largura, altura, inicio, fim)
    if (i == 4):
        print()
        print('Simulated Annealing')
        t5 = Timer(lambda: anne.simulated_annealing(mapa, inicio, fim))
        print(f"Time spend to run anneling algorithm {t5.timeit(number=n_times) / n_times}")
        monitor.monitor()
        path = anne.simulated_annealing(mapa, inicio, fim)
        desenha_caminho(path, mapa, largura, altura, inicio, fim)


def main():
    mapa = {}
    chars = ['c']
    inicio = None
    fim = None
    largura = 0
    altura = 0
    static_map = False

    opcoes = user.inicializa()

    if (opcoes == 1):
        static_map = True
    elif (opcoes == 2):
        static_map = False
    else:
        print('Opção inválida')

    if (opcoes in (1, 2)):
        if static_map:
            fp = open('./maze/maze.in', 'r')
        else:
            fp = io.StringIO(map_template())
        while len(chars) > 0:
            chars = [str(i) for i in fp.readline().strip()]
            largura = len(chars) if largura == 0 else largura
            for x in range(len(chars)):
                mapa[(x, altura)] = chars[x]
                if (chars[x] == '@'):
                    inicio = (x, altura)
                elif (chars[x] == '$'):
                    fim = (x, altura)
            if (len(chars) > 0):
                altura += 1

        fp.close()

        opcoes = user.algoritmo_options()

        path = ''
        if (opcoes == 1):
            for i in range(5):
                executa(100, mapa, inicio, fim, largura, altura, i)
        elif (opcoes == 2):
            i = user.list_algoritmos()
            if (i in range(0, 5)):
                executa(100, mapa, inicio, fim, largura, altura, i)
            else:
                print('Opção inválida')
        else:
            print('Opção Inválida')


if __name__ == "__main__": main()
