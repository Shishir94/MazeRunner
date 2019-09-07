def traversable_neighbors(maze, node):
    """
    Utility function to obtain all the traversable neighbors of the current cell

    maze :- nxn matrix consisting the randomly generated maze.
    node :- The cell who's traversable neighbors need ot be found
    """

    #Sets the current node and initializes an empty neighbors array
    (i,j) = node
    neighbors = []
    #The outer "if" conditions check for all the boundary conditions
    if i-1 >= 0:
        up = (i-1,j)
        #Checks if the cell is not a wall or already visited.
        if(maze[up] != 1 and maze[up] != -1):
            neighbors.append(up)

    if j-1 >= 0:
        left = (i,j-1)
        #Checks if the cell is not a wall or already visited.
        if(maze[left] != 1 and maze[left] != -1):
            neighbors.append(left)

    if i+1 < len(maze):
        bottom = (i+1,j)
        #Checks if the cell is not a wall or already visited.
        if(maze[bottom] != 1 and maze[bottom] != -1):
            neighbors.append(bottom)

    if j+1 < len(maze):
        right = (i,j+1)
        #Checks if the cell is not a wall or already visited.
        if(maze[right] != 1 and maze[right] != -1):
            neighbors.append(right)

    #Returns the list containing the traversable neighbors
    return neighbors
