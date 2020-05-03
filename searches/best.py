from tools import estrutura_dados as No


def best_first_search(mapa, inicio, fim):
    aberto = []
    fechado = []

    no_inicio = No.No(inicio, None)
    objetivo = No.No(fim, None)

    aberto.append(no_inicio)

    while len(aberto) > 0:
        aberto.sort()

        no_atual = aberto.pop(0)

        fechado.append(no_atual)

        if no_atual == objetivo:
            path = []
            while no_atual != no_inicio:
                path.append(no_atual.posicao)
                no_atual = no_atual.pai
            return path[::-1]

        (x, y) = no_atual.posicao

        vizinhos = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        for proximo in vizinhos:
            valor = mapa.get(proximo)
            if (valor == '#'):
                continue
            if (valor == '&'):
                continue
            if (valor == ' '):
                continue

            vizinho = No.No(proximo, no_atual)

            if (vizinho in fechado):
                continue
            vizinho.g = abs(vizinho.posicao[0] - no_inicio.posicao[0]) + abs(
                vizinho.posicao[1] - no_inicio.posicao[1])
            vizinho.h = abs(vizinho.posicao[0] - objetivo.posicao[0]) + abs(
                vizinho.posicao[1] - objetivo.posicao[1])
            vizinho.f = vizinho.h

            for no in aberto:
                if (vizinho == no and vizinho.f > no.f):
                    continue

            aberto.append(vizinho)

    return None
