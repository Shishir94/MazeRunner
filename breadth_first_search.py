import matplotlib.pyplot as plt
from maze_plot import *
from get_neighbors import *
import numpy as np
from collections import deque

def bfs_path(bfs_maze, cur_node, bfs_parent):
    bfs_maze[len(bfs_maze)-1, len(bfs_maze)-1] = -2
    count = 2
    temp_node = cur_node
    while temp_node != (0,0):
        bfs_maze[temp_node] = -2
        (i,j) = temp_node
        temp_node = bfs_parent[i][j]
        count += 1
    count += 1
    bfs_maze[0,0] = -2
    print("Path length : ",count)
    maze_plot_final(bfs_maze,"b")
    return


def breadth_first_search(bfs_maze,display=True):
    bfs_maze=bfs_maze.copy()
    source = (0,0)
    goal = (len(bfs_maze)-1, len(bfs_maze)-1)
    bfs_maze[source] = -1
    bfs_visited = np.zeros((len(bfs_maze), len(bfs_maze)), dtype = int)
    bfs_queue = deque([source])
    neighbors = []
    flag = 0
    bfs_parent = [[None for _ in range(len(bfs_maze))] for _ in range(len(bfs_maze))]
    #bfs_parent[] = source

    while len(bfs_queue) != 0 and flag == 0:

        cur_node = bfs_queue.popleft()
        bfs_maze[cur_node] = -2
        neighbors = traversable_neighbors(bfs_maze, cur_node)
        if len(neighbors) != 0:
            for node in neighbors:
                (i,j) = node
                if node == goal:
                    flag = 1
                    if display:
                        bfs_path(bfs_maze, cur_node, bfs_parent)
                        break
                    return 1
                if bfs_parent[i][j] == None:
                    bfs_parent[i][j] = cur_node
                    bfs_queue.append(node)
        bfs_maze[cur_node] = -1

    if flag == 0:
        if display:
            print("No Path Found :(")
            maze_plot_final(bfs_maze)
        return 0
