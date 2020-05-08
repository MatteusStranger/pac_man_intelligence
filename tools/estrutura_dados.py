class No:
    def __init__(self, posicao: (), pai: ()):
        self.posicao = posicao
        self.pai = pai
        self.g = 0 # Distância para iniciar o nó
        self.h = 0 # Distância ao nó da meta
        self.f = 0 # Custo total

    def __eq__(self, outro):
        return self.posicao == outro.posicao

    def __lt__(self, outro):
        return self.f < outro.f

    def __repr__(self):
        return ('({0},{1})'.format(self.posicao, self.f))


class Fila:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.insert(0, item)

    def pop(self):
        return self.list.pop()

    def isEmpty(self):
        return len(self.list) == 0
