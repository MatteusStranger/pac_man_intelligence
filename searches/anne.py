import numpy as np
from tools import estrutura_dados as No

def simulated_annealing(mapa, inicio, fim, T0=1000, M=20000, N=15, alpha=0.999, k=1):
    inicio_no = No.No(inicio, None)
    objetivo_no = No.No(fim, None)
    path = []
    no_atual = inicio_no
    (x, y) = no_atual.posicao
    (goal_x,goal_y) = objetivo_no.posicao
    path.append(no_atual.posicao)
    while T0 > 2:  
        for j in range(N):  
    while T0 > 2:
        for j in range(N):
            rand_amp = np.random.rand()
            choose_x_y = np.random.rand()
            step_x = 0
            step_y = 0
            if choose_x_y >= 0.5:
                step_x = k * (1 if rand_amp < 0.5 else -1)
            else:
                step_y = -k * (1 if rand_amp < 0.5 else -1)

            x_temporary = x + step_x
            y_temporary = y + step_y

            obj_mov_possible = (x_temporary - goal_x) ** 2 + (y_temporary - goal_y) ** 2

            obj_val_current = (x_temporary - x) ** 2 + (y_temporary - y) ** 2

            rand_factor = np.random.rand()

            probality_eq = 1 / (np.exp((obj_mov_possible - obj_val_current) / T0))

            content = mapa.get((x_temporary, y_temporary))
            if ((content == '#') or (content == '&')):
                continue

            if (obj_mov_possible <= obj_val_current) | (rand_factor <= probality_eq):  
                no_atual = No.No((x,y),(x_temporary,y_temporary))
                x = x_temporary
                y = y_temporary 
                path.append(no_atual.posicao)
            else:  
            if (obj_mov_possible <= obj_val_current) | (rand_factor <= probality_eq):
                no_atual = No.No((x,y),(x_temporary,y_temporary))
                x = x_temporary
                y = y_temporary
                path.append(no_atual.posicao)
            else:
                x = x
                y = y

            if no_atual == objetivo_no:
                return path[::-1]

            T0 = alpha * T0
    return None