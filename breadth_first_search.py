import matplotlib.pyplot as plt
from maze_plot import *
from get_neighbors import *
import numpy as np
from collections import deque


def bfs_path(bfs_maze, cur_node, bfs_parent):
    """
    Helper function to find the shortest path and plot the path.

    bfs_maze :- nxn matrix consisting the randomly generated maze.
    cur_node :- the last node we've reached before finding the goal
    bfs_parent :- nxn matrix consisting of the parent cell for each cell
    """
    #Sets a darker color to the goal node
    bfs_maze[len(bfs_maze)-1, len(bfs_maze)-1] = -2
    #Initialize the count as 2 -- source and goal
    count = 2
    temp_node = cur_node
    #Start from the goal and move backwards till you reach the source
    while temp_node != (0,0):
        #Set all the nodes on the shortest path to a darker color
        bfs_maze[temp_node] = -2
        (i,j) = temp_node
        temp_node = bfs_parent[i][j]
        count += 1
    #Sets a darker color to the source node
    bfs_maze[0,0] = -2
    #Prints the total number of nodes on the shortest path to goal and plot it
    print("Path length : ",count)
    maze_plot_final(bfs_maze,"b")
    return


def breadth_first_search(bfs_maze,display=True):
    """
    Implements the Depth First Search approach to solve a given maze.

    bfs_maze :- nxn matrix consisting the randomly generated maze.
    display :- control parameter to display the output or not.
    """

    bfs_maze=bfs_maze.copy()
    #Sets the source for the path planning of the maze
    source = (0,0)
    #Sets the end goal that needs to be reached to be successful
    goal = (len(bfs_maze)-1, len(bfs_maze)-1)
    #Intialize the path by setting the source as visited and add it to the queue
    bfs_maze[source] = -1
    #Initialize a queue to implement BFS.
    bfs_queue = deque([source])
    #A flag variable to be set to true if a path is found from source to goal
    pathFound = 0
    #Matrix to store the parent node of current node and hence obtain the path
    bfs_parent = [[None for _ in range(len(bfs_maze))] for _ in range(len(bfs_maze))]

    """
    Loop till :-
    1. The BFS queue gets empty - signifying that all nodes that could be
       travelled have been travelled and we can't reach the goal
    2. pathFound variable is true - signifying that a path has been found from
       source to the goal.
    """
    while len(bfs_queue) != 0 and pathFound == 0:

        #Pops the last entered node in FIFO from the BFS queue
        cur_node = bfs_queue.popleft()
        bfs_maze[cur_node] = -2
        #Obtain all the traversable neighbors of the current node
        neighbors = traversable_neighbors(bfs_maze, cur_node)
        #If there are traversable neighbors
        if len(neighbors) != 0:
            for node in neighbors:
                (i,j) = node
                if node == goal:
                    #If the neighbor is a goal node then set pathFound to True
                    #and return the true
                    pathFound = 1
                    if display:
                        #If the display parameter is set to true the plot the path
                        bfs_path(bfs_maze, cur_node, bfs_parent)
                        break
                    return 1
                #If node hasn't been visited yet then set the current node as
                #its parent. Will be useful later to find the shortest path.
                if bfs_parent[i][j] == None:
                    bfs_parent[i][j] = cur_node
                    bfs_queue.append(node)
        #Set to -1 to signify that the node has been visited.
        bfs_maze[cur_node] = -1
    #At the end of while loop if we don't have a path then return false
    if pathFound == 0:
        if display:
            #If display is true then plot the maze with all the visited nodes.
            print("No Path Found :(")
            maze_plot_final(bfs_maze)
        return 0
