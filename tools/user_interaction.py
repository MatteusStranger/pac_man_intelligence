def clear_report():
    f = open("report.docx", "w")
    f.write('')
    f.close()

def write_text(text):
    f = open("report.docx", "a")
    #print(text)
    f.write(str(text) + '\n')
    f.close()

def inicializa():
    print('Pacman, o nosso herói, deve usar todo o seu raciocínio e sagacidade para chegar ao seu objetivo.')
    print('Ele foi colocado em um labirinto com um objetivo final a ser alcançado.')
    print('Para isso, ele deve comer pílulas pelo caminho, vencer fantasmas, desviar de paredes e superar obstáculos.')
    print(
        'Existe o desafio casual, com um mapa estático definido ou o hard, onde um mapa novo é gerado a cada execução.')
    print('Ele tem 5 algoritmos diferentes que podem ser usados para alcançar o objetivo:')
    print('BFS, DFS, AStar, Best e o Simulated Annealing')
    print('It`s time')
    print()
    print('Escolha o tipo de mapa:')
    print('1. Mapa estático')
    print('2. Mapa aleatório')
    print()
    mapa = int(input())
    clear_report()
    return mapa


def algoritmo_options():
    print()
    print('Os algoritmos executados trazem o tempo de execução')
    print()
    print('1. Executa todos os algoritmos')
    print('2. Escolha o algoritmo')
    print()
    return int(input())


def list_algoritmos():
    print()
    print('0. DFS')
    print('1. AStar')
    print('2. BFS')
    print('3. Best')
    print('4. Simulated Annealing')
    print()
    return int(input())


def define_heuristica():
    print()
    print('Esse algoritmo requer uma heurística como guia para o nosso herói.')
    print('Escolha sua heurística')
    print('1. Distância de Manhattan')
    print('2. Distância Euclidiana')
    print()
    return int(input())
