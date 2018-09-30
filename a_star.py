import math
import numpy as np


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


def a_star(a_star_maze):
    source = (0,0)
    goal = (len(a_star_maze)-1, len(a_star_maze)-1)
    euclid_heuristic = euclidean_distance(a_star_maze)
    manhattan_heuristic = manhattan_distance(a_star_maze)
    print(euclid_heuristic)
    print(manhattan_heuristic)
