import matplotlib.pyplot as plt
from maze_plot import *
from get_neighbors import *
from breadth_first_search import *
import math
import numpy as np
import heapq

def a_star_path(a_star_maze, cur_node, a_star_parent):
    a_star_maze[len(a_star_maze)-1, len(a_star_maze)-1] = -2
    count = 2
    temp_node = cur_node
    while temp_node != (0,0):
        a_star_maze[temp_node] = -2
        (i,j) = temp_node
        temp_node = a_star_parent[i][j]
        count += 1
    a_star_maze[0,0] = -2
    print("Path length : ",count)
    maze_plot_final(a_star_maze,"a")
    return


def euclidean_distance(a_star_maze):
    euclid_heuristic = np.zeros((len(a_star_maze), len(a_star_maze)), dtype = int)
    (x, y) = (len(a_star_maze)-1, len(a_star_maze)-1)
    for i in range(len(a_star_maze)):
        for j in range(len(a_star_maze)):
            euclid_heuristic[i,j] = math.sqrt(math.pow((x - i), 2)+ math.pow((y-j),2))
    return euclid_heuristic


def manhattan_distance(a_star_maze):

    manhattan_heuristic = np.zeros((len(a_star_maze), len(a_star_maze)), dtype = int)
    (x, y) = (len(a_star_maze)-1, len(a_star_maze)-1)
    for i in range(len(a_star_maze)):
        for j in range(len(a_star_maze)):
            manhattan_heuristic[i,j] = abs(x-i)+abs(y-j)
    return manhattan_heuristic


#def a_star_manhattan(a_star_maze):


def a_star(a_star_maze,h, display=True):
    a_star_maze=a_star_maze.copy()
    source = (0,0)
    goal = (len(a_star_maze)-1, len(a_star_maze)-1)
    if h=="euclid":
        heuristic = euclidean_distance(a_star_maze)
    else:
        heuristic = manhattan_distance(a_star_maze)

    a_star_maze[source] = -1
    a_star_visited = np.zeros((len(a_star_maze), len(a_star_maze)), dtype = int)
    a_star_parent = [[None for _ in range(len(a_star_maze))] for _ in range(len(a_star_maze))]
    a_star_p_queue = []
    heapq.heappush(a_star_p_queue, (heuristic[source],0,source))
    flag = 0

    while len(a_star_p_queue) != 0 and flag == 0:

        cur_heuristic, cur_cost, cur_node = heapq.heappop(a_star_p_queue)
        a_star_maze[cur_node] = -2
        if(cur_node == goal):
            flag = 1
            a_star_maze[cur_node] = -1
            a_star_maze[goal] = -2
            if display:
                print("Path Found!!!!")
                maze_plot_final(a_star_maze,"a")
                a_star_path(a_star_maze, cur_node, a_star_parent)
            return 1
        """
        #Mistake in the final goal condition, the condition has to be if the
        #goal node is popped from  the heap queue and not in the neighboring nodes
        #as implemented currently
        """
        neighbors = traversable_neighbors(a_star_maze, cur_node)
        if len(neighbors) != 0:
            for node in neighbors:
                (i,j) = node
                if a_star_parent[i][j] == None:
                    a_star_parent[i][j] = cur_node
                    heapq.heappush(a_star_p_queue, ((heuristic[i,j])+cur_cost,cur_cost+1,node))

        a_star_maze[cur_node] = -1

    if(flag == 0):
        a_star_maze[source] = -2

        if display:
            print("No Path found :(")
            maze_plot_final(a_star_maze,"a")
        return 0
