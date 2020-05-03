from tools import estrutura_dados as No


def aestrela(mapa, inicio, fim):
    aberto = []
    fechado = []

    inicio_no = No.No(inicio, None)
    objetivo_no = No.No(fim, None)

    aberto.append(inicio_no)

    while len(aberto) > 0:
        aberto.sort()
        no_atual = aberto.pop(0)
        fechado.append(no_atual)
        if no_atual == objetivo_no:
            path = []
            while no_atual != inicio_no:
                path.append(no_atual.posicao)
                no_atual = no_atual.pai
            return path[::-1]

        (x, y) = no_atual.posicao
        vizinhos = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        for prox in vizinhos:
            mapa_valor = mapa.get(prox)
            if ((mapa_valor == '#') or (mapa_valor == '&')):
                continue
            vizinho = No.No(prox, no_atual)

            if (vizinho in fechado):
                continue
            vizinho.g = abs(vizinho.posicao[0] - inicio_no.posicao[0]) + abs(
                vizinho.posicao[1] - inicio_no.posicao[1])
            vizinho.h = abs(vizinho.posicao[0] - objetivo_no.posicao[0]) + abs(
                vizinho.posicao[1] - objetivo_no.posicao[1])
            vizinho.f = vizinho.g + vizinho.h
            for no in aberto:
                if (vizinho == no and vizinho.f > no.f):
                    continue
            aberto.append(vizinho)

    return None
