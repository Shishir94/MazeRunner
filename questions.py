from maze_generator import *
from maze_plot import *
from depth_first_search import *
from breadth_first_search import *
from a_star import *
from time import time
import numpy as np
import pickle
#Set -1 for traversed Elements
#Set -2 for current element being traversed, or for the current wavefront in case of BFS

def question1_question3(n):
    
    # This function calculates the running times for different dimensions for all p
    # for each p for each dim, the function takes an average of n mazes
    # The output is a dictionary of the form {p=0.1:{dim=500:{"dfs":(time_avg=20s,count of successful paths=a<n)}}}
    # The dictionary is stored in the file data/q1,3.pickle
    
    final_dict={}
    for p in [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]:
        stats={}
        for dim in np.arange(7000,15000,100):
                #int(input("Enter the dimension for maze : \n"))
                dfs_times=[]
                bfs_times=[]
                a_euclid_times=[]
                a_manhattan_times=[]
                dfs_count=0
                bfs_count=0
                a_euclid_count=0
                a_manhattan_count=0
                for rep in range(n):
                    maze = maze_generator(dim, p)
                    t=time()
                    dfs_count+=depth_first_search(maze,display=False)
                    dfs_times.append(time()-t)

                    t=time()
                    a_euclid_count+=a_star(maze,"euclid",display=False)
                    a_euclid_times.append(time()-t)
                    
                    t=time()
                    a_manhattan_count+=a_star(maze,"manhattan", display=False)
                    a_manhattan_times.append(time()-t)
                    
                    t=time()
                    bfs_count+=breadth_first_search(maze,display=False)
                    bfs_times.append(time()-t)
                    
                    
                dfs_avg=np.mean(dfs_times)
                bfs_avg=np.mean(bfs_times)
                a_euclid_avg=np.mean(a_euclid_times)
                a_manhattan_avg=np.mean(a_manhattan_times)
                stats[dim]={"dfs":(dfs_avg,dfs_count), "bfs":(bfs_avg,bfs_count), 
                     "a_euclid":(a_euclid_avg,a_euclid_count), "a_manhattan":(a_manhattan_avg, a_manhattan_count) }
        final_dict[p]=stats
    print(final_dict)
    with open("data/q1,3.pickle","wb+") as f:
        pickle.dump(final_dict,f)
            
if __name__=="__main__":
    question1_question3(1)
