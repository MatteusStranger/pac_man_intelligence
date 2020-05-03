class No:
    def __init__(self, posicao: (), pai: ()):
        self.posicao = posicao
        self.pai = pai
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, outro):
        return self.posicao == outro.posicao

    def __lt__(self, outro):
        return self.f < outro.f

    def __repr__(self):
        return ('({0},{1})'.format(self.posicao, self.f))


class Fila:
    "A container with a first-in-first-out (FIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Enqueue the 'item' into the queue"
        self.list.insert(0,item)

    def pop(self):
        """
          Dequeue the earliest enqueued item still in the queue. This
          operation removes the item from the queue.
        """
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the queue is empty"
        return len(self.list) == 0