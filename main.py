from maze_generator import *
from maze_plot import *
from depth_first_search import *
from breadth_first_search import *
from a_star import *
from time import time
#Set -1 for traversed Elements
#Set -2 for current element being traversed, or for the current wavefront in case of BFS

maze_probability = 0.3
maze_dimension = 5000#int(input("Enter the dimension for maze : \n"))
#maze = maze_generator(maze_dimension, maze_probability)
maze=maze_generator(500,0.2)
t=time()

#each of depth_first_search, breadth_first_search, a_star returns 1 if a path was found and 0 otherwise.
#change diplay to True to see the image of the path.
#change second paramater to either "euclid" or "manhattan"

#print(depth_first_search(maze,display=False))
print("A-Star :")
print(a_star(maze,"euclid",display=True))
#print(a_star(maze,"manhattan",display=True))
#print("BFS :")
#print(breadth_first_search(maze,display=True))

print("running time: ", time()-t)
