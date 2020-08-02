from randomfill.walls import Map 
import sys
import numpy as np
from tools.conversor import conversor

def generateDefaultRandomMap():
    maze = ""
    tileMap = Map(16,31,"""
    ||||||||||||||||
    |...............
    |...............
    |...............
    |...............
    |...............
    |...............
    |...............
    |...............
    |...............
    |...............
    |...............
    |.........||||||
    |.........||||||
    |.........||||||
    |.........||||||
    |.........||||||
    |...............
    |...............
    |...............
    |...............
    |...............
    |...............
    |...............
    |...............
    |...............
    |...............
    |...............
    |...............
    |...............
    ||||||||||||||||
    """)

    # generate map by adding walls until there's no more room
    while tileMap.add_wall_obstacle(extend=True):
        pass

    # reflect the first 14 columns to print the map
    for line in str(tileMap).splitlines():
        s = line[:14]
        maze += s+s[::-1] + '\n' 
    return maze

def available_path(maze):
    """Identify available path.

    Considering available path equal 1 this function returno all available path as list of tupla.

    Arguments:
        maze: numpy array[row][column]

    Returns:
        suffle_path(list): List of tuple with available position e.g [(0,1),(1,1)...]  
    """
    idx_goals = np.where(maze == 1)
    sff_idx = list()
    for i in range(len(idx_goals[0])):
        sff_idx.append((idx_goals[0][i],idx_goals[1][i]))
    np.random.shuffle(sff_idx)
    return sff_idx    

def add_hole(n_hole,maze,inplace=False):
    """Add hole in the map.

    This function will add hole in random location 

    Arguments:
        n_hole (int): number of hole
        maze (narray): narray: numpy array[row][column]
        inplace(bool): overwrite maze or make copy

    Returns:
        narray: numpy array[row][column]
    """
    if inplace:
        for position in available_path(maze)[:n_hole]:
            maze[position[0]][position[1]] = 3
        return maze
    else:
        maze_copy = maze.copy()
        for position in available_path(maze_copy)[:n_hole]:
            maze_copy[position[0]][position[1]] = 3
        return maze_copy

def add_block(n_block,maze,inplace=False):
    """Add block in the map.

    This function will add 4 as a block 

    Args:
        n_block (int): number of block
        maze (narray): narray: numpy array[row][column]
        inplace(bool): overwrite maze or make copy

    Returns:
        narray: numpy array[row][column]
    """
    if inplace:
        for position in available_path(maze)[:n_block]:
            maze[position[0]][position[1]] = 4
        return maze
    else:
        maze_copy = maze.copy()
        for position in available_path(maze_copy)[:n_block]:
            maze_copy[position[0]][position[1]] = 4
        return maze_copy
  
def map_template(row=31,column=28):
    temp_map = generateDefaultRandomMap()
    np_map = conversor.conv_str2int(row,column,temp_map)
    add_hole(10,np_map,inplace=True)
    add_block(15,np_map,inplace=True)
    start_position = available_path(np_map)[:1][0]
    end_position = available_path(np_map)[:1][0]
    np_map[start_position[0]][start_position[1]] = 2
    np_map[end_position[0]][end_position[1]] = 5
    return conversor.conv_int2str(np_map)