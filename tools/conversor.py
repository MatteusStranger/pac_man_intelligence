import numpy as np
class conversor:
    def conv_str2int(row, column, maze):
        """Function to convert string to int.

        We have big string with * | breakline caracter is very hard to see 
        how to process this format (not impossible) but more difficult to see.

        Args:
            row (int): number of line (use  number without subtract as index)
            column (int): number of column (use  number without subtract as index)
            maze (str): string with map

        Returns:
            narray: numpy array[row][column]

        """
        ## Map with 31 x 28
        ## Considering . as path == 1 and | as wall == 0
        # We have matrix 31 x 28 but last column == '\n' we use %29 to convert int 1 until 28 line subtract 1 to use numpy array index 
        str2int = np.zeros((row,column))
        line = 0
        for idx, value in enumerate(maze):
            if (idx!=0)&(value=='\n'):
                line = line + 1
            else:
                if (value == '.'):
                    str2int[line][(idx%(column+1))-1] = 1
        return str2int

    def conv_int2str(maze):
        """Function to convert int to string.


        Args:
            narray: numpy array[row][column]

        Returns:
            maze (str): string with map

        """
        ## Map with 31 x 28
        ## Considering . as path == 1 and | as wall == 0
        # We have matrix 31 x 28 but last column == '\n' we use %29 to convert int 1 until 28 line subtract 1 to use numpy array index 
        int2str = ""
        x,y = maze.shape
        for i in range(0,x):
            for j in range(0,y):
                if maze[i][j] == 0:
                    int2str = int2str + '#'
                elif maze[i][j] == 1:
                    int2str = int2str + '.'
                elif maze[i][j] == 2:
                    int2str = int2str + '@'
                elif maze[i][j] == 3:
                    int2str = int2str + ' '
                elif maze[i][j] == 4:
                    int2str = int2str + '#'
                elif maze[i][j] == 5:
                    int2str = int2str + '$'
            int2str = int2str + '\n'
        
        return int2str
        
        
        for idx, value in enumerate(maze):
            if (idx!=0)&(value=='\n'):
                line = line + 1
            else:
                if (value == '.'):
                    str2int[line][(idx%(column+1))-1] = 1
        return str2int

