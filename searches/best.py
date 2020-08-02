from tools import estrutura_dados as No
from tools import heuristicas as h


def best_first_search(mapa, inicio, fim, heuristica):
    # Criar listas para nós abertos e nós fechados
    aberto = []
    fechado = []
    # Crie um nó representando o inicio e o objetivo
    no_inicio = No.No(inicio, None)
    objetivo = No.No(fim, None)
    # Adiciona nó inicial
    aberto.append(no_inicio)
    # Repetir até que a lista aberta esteja vazia
    while len(aberto) > 0:
        # Ordene a lista aberta para obter o nó com o menor custo primeiro
        aberto.sort()
        # Obtenha o nó com o menor custo
        no_atual = aberto.pop(0)
        # Adicione o nó atual à lista fechada
        fechado.append(no_atual)
        # Verifique se atingimos a meta, retorne o caminho
        if no_atual == objetivo:
            path = []
            while no_atual != no_inicio:
                path.append(no_atual.posicao)
                no_atual = no_atual.pai
                # Retornar caminho invertido
            return path[::-1]
        # Pega a posição atual do nó
        (x, y) = no_atual.posicao
        # Pega os vizinhos
        vizinhos = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        # Loop nos vizinhos
        for proximo in vizinhos:
            # Pega valor do mapa
            valor = mapa.get(proximo)
            # Verifique se é uma parede, fantasma ou obstáculo
            if (valor == '#'):
                continue
            if (valor == '&'):
                continue
            if (valor == ' '):
                continue

            # Crie o nó vizinho
            vizinho = No.No(proximo, no_atual)

            if (vizinho in fechado):
                continue
            # Gera heurísticas
            if (heuristica == 1):
                # Distância de Manhattan
                vizinho.g = h.distancia_manhattan(vizinho.posicao[0], no_inicio.posicao[0], vizinho.posicao[1],
                                                  no_inicio.posicao[1])
                vizinho.h = h.distancia_manhattan(vizinho.posicao[0], objetivo.posicao[0], vizinho.posicao[1],
                                                  objetivo.posicao[1])
            else:
                # Distância de Euclides
                vizinho.g = h.euclidiano(vizinho.posicao[0], no_inicio.posicao[0], vizinho.posicao[1],
                                         no_inicio.posicao[1])
                vizinho.h = h.euclidiano(vizinho.posicao[0], objetivo.posicao[0], vizinho.posicao[1],
                                         objetivo.posicao[1])
            vizinho.f = vizinho.h  # # Custo total recebe o valor da heurística
            # Verifique se o vizinho deve ser adicionado à lista aberta
            for no in aberto:
                if (vizinho == no and vizinho.f > no.f):
                    continue

            aberto.append(vizinho)
    # Retorne vazio, não há caminho
    return None
