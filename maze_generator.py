"""
This program generates a maze of the given dimensions based on the
entered dimension for the maze and the probability value.
"""

import random
import numpy as np

def maze_generator(maze_dimension, maze_probability):
    data = np.zeros((maze_dimension, maze_dimension), dtype = int)

    for i in range(maze_dimension):
        for j in range(maze_dimension):
            if random.random() <= maze_probability:
                data[i][j] = 1
            
    data[0][0] = 0
    data[maze_dimension-1][maze_dimension-1] = 0
    return data
