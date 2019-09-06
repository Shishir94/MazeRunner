from maze_plot import *
import matplotlib.pyplot as plt
from get_neighbors import *
å

def depth_first_search(dfs_maze, display=True):
    """
    Implements the Depth First Search approach to solve a given maze.

    dfs_maze :- nxn matrix consisting the randomly generated maze.
    display :- control parameter to display the output or not.
    """

    dfs_maze=dfs_maze.copy()
    #Sets the source for the path planning of the maze
    source = (0,0)
    #Sets the end goal that needs to be reached to be successful
    goal = (len(dfs_maze)-1, len(dfs_maze)-1)
    #Intialize the path by setting the source as visited and add it to the stack
    dfs_maze[source] = -1
    dfs_stack = [source]
    dfs_path = []
    #A flag variable to be set to true if a path is found from source to goal
    pathFound = 0

    """
    Loop till :-
    1. The DFS stack gets empty - signifying that all nodes that could be
       travelled have been travelled and we can't reach the goal
    2. pathFound variable is true - signifying that a path has been found from
       source to the goal.
    """
    while len(dfs_stack) != 0 and pathFound == 0:
        #Pops the last visited node from the DFS stack
        cur_node = dfs_stack.pop()
        dfs_path.append(cur_node)
        dfs_maze[cur_node] = -2
        #Obtain all the traversable neighbors of the current node
        neighbors = traversable_neighbors(dfs_maze, cur_node)
        #If the current node is a dead end with no traversable neighbors then
        #remove it from the path.
        if len(neighbors) == 0:
            dfs_path.pop()
        else:
            #Else, check if one of its neighbors is the goal cell.
            for node in neighbors:
                if node == goal:
                    #If the nrighbor is the goal the set pathFound to True and
                    #return the path.
                    dfs_maze[goal] = -2
                    if display:
                        #If the display parameter is set to true the plot the path
                        print("Path found!!!")
                        maze_plot_final(dfs_maze)
                    pathFound = 1
                    return 1
                #Append all the traversable neighbors to the end of the stack
                dfs_stack.append(node)
        #Set to -1 to signify that the node has been visited.
        dfs_maze[cur_node] = -1
    #At the end of while loop if we don't have a path then return false
    if pathFound == 0:
        if display:
            #If display is true then plot the maze with all the visited nodes.
            print("No path found :(")
            maze_plot_final(dfs_maze)
        return 0
