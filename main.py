from searches import best
from searches import dfs
from searches import astar
from searches import bfs
from searches import anne
from tools.desenha_mapa import desenha_mapa
from randomfill.generate import map_template
import io
from timeit import Timer

def clear_report():
    f = open("report.txt", "w")
    f.write('')
    f.close()

def write_text(text):
    f = open("report.txt", "a")
    print(text)
    f.write(text + '\n')
    f.close()

def desenha_caminho(path, mapa, largura, altura, inicio, fim):
    if (path != None):
        print()
        print('Nos expandidos')
        print()
        print(path)
        print()
        desenha_mapa(mapa, largura, altura, espaco=1, path=path, inicio=inicio, objetivo=fim)
        print()
        write_text('Contagem: {0}'.format(len(path)))
        print()
    else:
        print('Não há caminho')

def executa(n_times, mapa, inicio, fim, largura, altura, i):
    if (i == 0):
        print()
        write_text('DFS')
        t = Timer(lambda: dfs.depth_first_search(mapa, inicio, fim))
        write_text(f"Time spent to run  DFS algorithm {t.timeit(number=n_times) / n_times}")
        path = dfs.depth_first_search(mapa, inicio, fim)
        desenha_caminho(path, mapa, largura, altura, inicio, fim)
    if (i == 1):
        print()
        write_text('AStar')
        t2 = Timer(lambda: astar.aestrela(mapa, inicio, fim))
        write_text(f"Time spent to run A* algorithm {t2.timeit(number=n_times) / n_times}")
        path = astar.aestrela(mapa, inicio, fim)
        desenha_caminho(path, mapa, largura, altura, inicio, fim)
    if (i == 2):
        print()
        write_text('BFS')
        t3 = Timer(lambda: bfs.breadth_first_search(mapa, inicio, fim))
        write_text(f"Time spent to run BFS algorithm {t3.timeit(number=n_times) / n_times}")
        path = bfs.breadth_first_search(mapa, inicio, fim)
        desenha_caminho(path, mapa, largura, altura, inicio, fim)
    if (i == 3):
        print()
        write_text('Best First')
        t4 = Timer(lambda: dfs.depth_first_search(mapa, inicio, fim))
        write_text(f"Time spent to run Best first search algorithm {t4.timeit(number=n_times) / n_times}")
        path = best.best_first_search(mapa, inicio, fim)
        desenha_caminho(path, mapa, largura, altura, inicio, fim)
    if (i == 4):
        print()
        write_text('Simulated Annealing')
        t5 = Timer(lambda: anne.simulated_annealing(mapa, inicio, fim))
        write_text(f"Time spent to run anneling algorithm {t5.timeit(number=n_times) / n_times}")
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

    print('Pacman, o nosso herói, deve usar todo o seu raciocínio e sagacidade para chegar ao seu objetivo.')
    print('Ele foi colocado em um labirinto com um objetivo final a ser alcançado.')
    print('Para isso, ele deve comer pílulas pelo caminho, vencer fantasmas, desviar de paredes e superar obstáculos.')
    print('Existe o desafio casual, com um mapa estático definido ou o hard, onde um mapa novo é gerado a cada execução.')
    print('Ele tem 5 algoritmos diferentes que podem ser usados para alcançar o objetivo:')
    print('BFS, DFS, AStar, Best First Search e o Simulated Annealing')
    print('It`s time')
    print()
    print('Escolha o tipo de mapa:')
    print('1. Mapa estático')
    print('2. Mapa aleatório')
    opcoes = int(input())

    clear_report()

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

        print()
        print('Os algoritmos executados trazem o tempo de execução')

        # opcoes = int(input())

        print()
        print('1. Executa todos os algoritmos')
        print('2. Escolha o algoritmo')
        opcoes = int(input())
        path = ''

        if (opcoes == 1):
            for i in range(5):
                executa(500, mapa, inicio, fim, largura, altura, i)
        elif (opcoes == 2):
            print('0. DFS')
            print('1. AStar')
            print('2. BFS')
            print('3. Best First Search')
            print('4. Simulated Annealing')
            i = int(input())
            if (i in range(0, 5)):
                executa(500, mapa, inicio, fim, largura, altura, i)
            else:
                print('Opção inválida')
        else:
            print('Opção Inválida')


if __name__ == "__main__": main()
