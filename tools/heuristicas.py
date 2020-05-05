import math as m


def distancia_manhattan(x_goal, x, y_goal, y):
    return abs(x_goal - x) + abs(
        y_goal - y)


def euclidiano(x_goal, x, y_goal, y):
    return m.sqrt((x_goal - x) ** 2 + (y_goal - y) ** 2)
