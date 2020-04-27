from searches import best
from searches import dfs
from searches import astar
from tools.desenha_mapa import desenha_mapa

def main():
    mapa = {}
    chars = ['c']
    inicio = None
    fim = None
    largura = 0
    altura = 0

    fp = open('./maze/maze.in', 'r')
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
    #path = dfs.depth_first_search(mapa, inicio, fim)
    #path = astar.aestrela(mapa, inicio, fim)
    #path = dfs.depth_first_search(mapa,inicio,fim)
    path = best.best_first_search(mapa, inicio, fim)

    if (path != None):
        print()
        print('Nos expandidos')
        print(path)
        print()
        desenha_mapa(mapa, largura, altura, espaco=1, path=path, inicio=inicio, objetivo=fim)
        print()
        print('Contagem: {0}'.format(len(path)))
        print()
    else:
        print('Não há caminho')


if __name__ == "__main__": main()
