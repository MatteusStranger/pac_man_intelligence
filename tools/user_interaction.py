# Os dois métodos abaixo manipulam o relatório de execução

def clear_report():
    f = open("report.docx", "w")
    f.write('')
    f.close()


def write_text(text):
    f = open("report.docx", "a")
    f.write(str(text) + '\n')
    f.close()

# Interações com o usuário
def inicializa():
    print('Pacman, o nosso herói, foi colocado em um calabouço na forma de labirinto por um terrível mago ')
    print('E só pode sair se alcançar o objetivo $. ')
    print('Ele deve usar todo o seu raciocínio e sagacidade para chegar ao objetivo.')
    print(
        'Para isso, Pacman deve comer pílulas pelo caminho, vencer fantasmas, desviar de paredes e superar obstáculos.')
    print('Existe um labirinto estático, que o mago usa como referência, e o aleatório.')
    print('Pacman tem a opção de cinco 5 algoritmos diferentes para usar para alcançar o objetivo:')
    print('Breadth First Search (BFS), Depth First Search (DFS), AStar, Best First Search e o Simulated Annealing')
    print('Vamos começar')
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
    print('Vai executar um algoritmo por vez, ou todos eles, em sequência?')
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
    print('Esse algoritmo requer uma heurística, que serve de dica, para o nosso herói.\n\n')
    print('Escolha sua heurística\n\n')
    print('1. Distância de Manhattan')
    print('2. Distância Euclidiana')
    print()
    return int(input())
