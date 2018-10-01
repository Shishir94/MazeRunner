from maze_generator import *
from maze_plot import *
from depth_first_search import *
from breadth_first_search import *
from a_star import *
from time import time

#Set -1 for traversed Elements

maze_probability = 0.3
maze_dimension = 1500
#maze = maze_generator(maze_dimension, maze_probability)
maze=maze_generator(maze_dimension,maze_probability)
t=time()

#change diplay to True to see the image of the path.
#change second paramater of a_star to either "euclid" or "manhattan"

#### each of the search algorithm returns 
#### i) success_flag: 1 indicates goal was found, 0 indicates otherwise.
#### ii) expanded_nodes: numpy array which holds the list of nodes that were explore/expanded.
#### iii) final_path: numpy array which holds the list of nodes that belong to the path from start to goal. 
####                  The array is empty if success_flag is 0.

#success_flag, expanded_nodes, final_path = depth_first_search(maze, display=True)
success_flag, expanded_nodes, final_path = a_star(maze,"euclid",display=True)
#success_flag, expanded_nodes, final_path = a_star(maze,"manhattan",display=False)
#success_flag, expanded_nodes, final_path = breadth_first_search(maze,display=True)


print("running time: ", time()-t)