def desenha_mapa(mapa, largura, altura, espaco=2, **kwargs):
    for y in range(altura):
        for x in range(largura):
            print('%%-%ds' % espaco % desenho(mapa, (x, y), kwargs), end='')
        print()


def desenho(mapa, posicao, kwargs):
    valor = mapa.get(posicao)

    if 'path' in kwargs and posicao in kwargs['path']: valor = '+'

    if 'inicio' in kwargs and posicao == kwargs['inicio']: valor = '@'

    if 'objetivo' in kwargs and posicao == kwargs['objetivo']: valor = '$'

    return valor
