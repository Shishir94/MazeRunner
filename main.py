from maze_generator import *
from maze_plot import *
from depth_first_search import *
from breadth_first_search import *
from a_star import *
#Set -1 for traversed Elements
#Set -2 for current element being traversed, or for the current wavefront in case of BFS

maze_probability = 0.2
maze_dimension = 5#int(input("Enter the dimension for maze : \n"))
maze = maze_generator(maze_dimension, maze_probability)

a_star(maze)
#depth_first_search(maze)
#breadth_first_search(maze)
