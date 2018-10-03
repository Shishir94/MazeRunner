from maze_generator import *
from maze_plot import *
from depth_first_search import *
from breadth_first_search import *
from a_star import *
from time import time
import numpy as np
import pickle
import math
import sys
#Set -1 for traversed Elements
#Set -2 for current element being traversed, or for the current wavefront in case of BFS

def round_no(x):
    return math.ceil(x * 1000.0) / 1000.0



def question1_question3(n):
    
    # This function calculates the running times for different dimensions for all p
    # for each p for each dim, the function takes an average of n mazes
    # The output is a dictionary of the form {p=0.1:{dim=500:{"dfs":(time_avg=20s,count of successful paths=a<n)}}}
    # The dictionary is stored in the file data/q1,3.pickle
    
    final_dict={}
    for p in [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]:
        print("p= ", p)
        stats={}
        for dim in np.arange(2500,7500,500):
                print("----dim= ", dim)    
                #int(input("Enter the dimension for maze : \n"))
                dfs_times=[]
                bfs_times=[]
                a1_times=[]
                a2_times=[]
                dfs_count=0
                bfs_count=0
                a1_count=0
                a2_count=0
                for rep in range(n):
                    maze = maze_generator(dim, p)
                    sys.stdout.write("\r----rep: %i DFS    " %rep)
                    t=time()
                    dfs_success, dfs_expanded, dfs_path=depth_first_search(maze,display=False)
                    dfs_count+=dfs_success
                    dfs_times.append(time()-t)
                    
                    sys.stdout.write("\r----rep: %i A Euclid  " %rep)
                    t=time()
                    a1_success, a1_expanded, a1_path=a_star(maze,"euclid",display=False)
                    a1_count+=a1_success
                    a1_times.append(time()-t)
                    
                    sys.stdout.write("\r---- rep:%i A Manhat  " %rep)
                    t=time()
                    a2_success, a2_expanded, a2_path=a_star(maze,"manhattan", display=False)
                    a2_count+=a2_success
                    a2_times.append(time()-t)
                    
                    sys.stdout.write("\r---- rep: %i BFS      " %rep)
                    t=time()
                    #bfs_success, bfs_expanded, bfs_path=breadth_first_search(maze,display=False)
                    bfs_count+=1
                    bfs_times.append(time()-t)
                    
                stats[dim]={"dfs":(dfs_times,dfs_count), "bfs":(bfs_times,bfs_count), 
                     "a_euclid":(a1_times,a1_count), "a_manhattan":(a2_times, a2_count) }
                print("\n--------dfs= ", round_no(np.mean(dfs_times)), ", ",round_no(np.max(dfs_times)), ",", dfs_count)
                print("--------bfs= ", round_no(np.mean(bfs_times)), ", ",round_no(np.max(bfs_times)), ",", bfs_count)
                print("--------a1= ", round_no(np.mean(a1_times)), ", ",round_no(np.max(a1_times)), ",", a1_count)
                print("--------a2= ", round_no(np.mean(a2_times)), ", ",round_no(np.max(a2_times)), ",", a2_count)
                
        final_dict[p]=stats
    print(final_dict)
    with open("data/q1,3.pickle","wb+") as f:
        pickle.dump(final_dict,f)
            
if __name__=="__main__":
    question1_question3(20)
