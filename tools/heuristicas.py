import math as m


def distancia_manhattan(x_goal, x, y_goal, y):
    #entre dois pontos num espaço euclidiano com um sistema cartesiano de coordenadas fixo
    # como a soma dos comprimentos da projecção da linha que une os pontos com os eixos das
    # coordenadas.
    # Aqui, é a soma da diferença entre o x, inicial e final, e y, inicial e final, em valores absolutos
    return abs(x_goal - x) + abs(
        y_goal - y)

# Distância euclidiana (ou distância métrica) é a distância entre dois pontos,
# que pode ser provada pela aplicação repetida do teorema de Pitágoras.
# Aplicando essa fórmula como distância, o espaço euclidiano torna-se um espaço métrico.
def euclidiano(x_goal, x, y_goal, y):
    return m.sqrt((x_goal - x) ** 2 + (y_goal - y) ** 2)
