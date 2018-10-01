from maze_plot import *
import matplotlib.pyplot as plt
from get_neighbors import *
import numpy as np

def depth_first_search(dfs_maze, display=True):
    dfs_maze=dfs_maze.copy()
    source = (0,0)
    goal = ((len(dfs_maze)-1), len(dfs_maze)-1)
    dfs_stack = np.array([source],dtype=np.int16)
    dfs_expanded = np.empty((0,2), dtype=np.uint16)
    flag = 0
    
    while len(dfs_stack):
        
        cur_node=dfs_stack[-1]
        dfs_expanded=np.append(dfs_expanded,[cur_node], axis=0)
        dfs_maze[tuple(cur_node)]=-1
        
        # if the current node is the goal, return successful
        if np.array_equal(goal, cur_node): 
            if display:
                print("Path found!")
                # change color of the path for better visualization.
                for node in dfs_stack:
                    dfs_maze[tuple(node)]=-2
                plot_maze(dfs_maze)
            return 1, dfs_expanded, dfs_stack

        neighbors = traversable_neighbors(dfs_maze, cur_node)
        if not(len(neighbors)):
            # if no more unexplored neighbors, remove node from stack, i.e. backtrack.
            dfs_stack=dfs_stack[:-1]
            continue
        else:
            # add next unexplored neighbor to stack.
            dfs_stack=np.append(dfs_stack, np.array([neighbors[0]],dtype=np.int16),axis=0)
            
    # if goal was not reached return unsuccessful.
    if display:
        print("No path found :(")
        plot_maze(dfs_maze)
        #maze_plot_final(dfs_maze)
    return 0, dfs_expanded, []
