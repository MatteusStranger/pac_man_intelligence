from tools import estrutura_dados as No


def depth_first_search(mapa, inicio, fim):
    # Criar listas para nós abertos e nós fechados
    aberto = []
    fechado = []

    # Crie um nó representando o inicio e o objetivo
    no_inicio = No.No(inicio, None)
    no_objetivo = No.No(fim, None)
    # Adiciona nó inicial
    aberto.append(no_inicio)

    # Repetir até que a lista aberta esteja vazia
    while len(aberto) > 0:
        # Obtenha o último nó (LIFO)
        no_atual = aberto.pop(-1)
        # Adicione o nó atual à lista fechada
        fechado.append(no_atual)
        # Verifique se atingimos a meta, retorne o caminho
        if no_atual == no_objetivo:
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
            valor_mapa = mapa.get(proximo)
            # Verifique se é uma parede, fantasma ou obstáculo
            if ((valor_mapa == '#') or (valor_mapa == '&') or (valor_mapa == ' ')):
                continue

            # Crie o nó vizinho
            vizinhos = No.No(proximo, no_atual)
            # Checa se o vizinho está em fechado
            if (vizinhos in fechado):
                continue
            # Adicione o nó se não estiver aberto
            if (vizinhos not in aberto):
                aberto.append(vizinhos)
    # Retorne vazio, não há caminho
    return None
