from randomfill.walls import Map
import tools.conversor as conv
import sys



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

if __name__ == "__main__":
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

    # verbosity option (-v)
    if len(sys.argv) > 1 and sys.argv[1] == "-v":
        tileMap.verbose = True

    # generate map by adding walls until there's no more room
    while tileMap.add_wall_obstacle(extend=True):
        pass

    # reflect the first 14 columns to print the map
    for line in str(tileMap).splitlines():
        s = line[:14]
        print (s+s[::-1])