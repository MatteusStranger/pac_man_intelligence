from tools import estrutura_dados as No


def breadth_first_search(mapa, inicio, fim):
    # Criar listas para nós abertos e nós fechados
    aberto = []
    fechado = []
    # Crie um nó representando o inicio e o objetivo
    inicio_node = No.No(inicio, None)
    objetivo = No.No(fim, None)
    # Adiciona nó inicial
    aberto.append(inicio_node)

    # Repetir até que a lista aberta esteja vazia
    while len(aberto) > 0:
        # Pegue o primeiro nó (FIFO)
        no_atual = aberto.pop(0)
        # Adicione o nó atual à lista fechada
        fechado.append(no_atual)
        # Verifique se atingimos a meta, retorne o caminho
        if no_atual == objetivo:
            caminho = []
            while no_atual != inicio_node:
                caminho.append(no_atual.posicao)
                no_atual = no_atual.pai
                # Retornar caminho invertido
            return caminho[::-1]
        # Pega a posição atual do nó
        (x, y) = no_atual.posicao
        # Pega os vizinhos
        vizinhos = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        # Loop nos vizinhos
        for proximo in vizinhos:
            # Pega valor do mapa
            valor = mapa.get(proximo)
            # Verifique se é uma parede, fantasma ou obstáculo
            if (valor == '#') or (valor == '&') or (valor == ' '):
                continue
            # Crie o nó vizinho
            vizinho = No.No(proximo, no_atual)
            # Checa se o vizinho está em fechado
            if (vizinho in fechado):
                continue
            # Adicione o nó se não estiver aberto
            if (vizinho not in aberto):
                aberto.append(vizinho)

    return None
