from searches import best
from searches import dfs
from searches import astar
from searches import bfs
from searches import anne
from tools.desenha_mapa import desenha_mapa
from randomfill.generate import map_template
import io
from timeit import Timer

def main():
    mapa = {}
    chars = ['c']
    inicio = None
    fim = None
    largura = 0
    altura = 0
    static_map = False
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
    # path = dfs.depth_first_search(mapa, inicio, fim)
    # path = astar.aestrela(mapa, inicio, fim)
    # path = bfs.breadth_first_search(mapa,inicio,fim)
    # path = best.best_first_search(mapa, inicio, fim)
    path =anne.simulated_annealing(mapa, inicio, fim)
    n_times = 500
    t = Timer(lambda: dfs.depth_first_search(mapa, inicio, fim))
    print(f"Time spend to run  DFS algorithm{t.timeit(number=n_times)/n_times}")
    t2 = Timer(lambda: astar.aestrela(mapa, inicio, fim))
    print(f"Time spend to run A* algorithm{t2.timeit(number=n_times)/n_times}")
    t3 = Timer(lambda: bfs.breadth_first_search(mapa, inicio, fim))
    print(f"Time spend to run BFS algorithm{t3.timeit(number=n_times)/n_times}")
    t4 = Timer(lambda: dfs.depth_first_search(mapa, inicio, fim))
    print(f"Time spend to run Best first search algorithm{t4.timeit(number=n_times)/n_times}")
    t5 = Timer(lambda: anne.simulated_annealing(mapa, inicio, fim))
    print(f"Time spend to run anneling algorithm{t5.timeit(number=n_times)/n_times}")

    if (path != None):
        print()
        print('Nos expandidos')
        print()
        desenha_mapa(mapa, largura, altura, espaco=1, path=path, inicio=inicio, objetivo=fim)
        print()
        print('Contagem: {0}'.format(len(path)))
        print()
    else:
        print('Não há caminho')


if __name__ == "__main__": main()
