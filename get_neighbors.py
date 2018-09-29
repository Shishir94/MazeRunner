def traversable_neighbors(dfs_maze, node):
    (i,j) = node
    neighbors = []

    if i-1 >= 0:
        up = (i-1,j)
        if(dfs_maze[up] != 1 and dfs_maze[up] != -1):
            neighbors.append(up)

    if j-1 >= 0:
        left = (i,j-1)
        if(dfs_maze[left] != 1 and dfs_maze[left] != -1):
            neighbors.append(left)

    if i+1 < len(dfs_maze):
        bottom = (i+1,j)
        if(dfs_maze[bottom] != 1 and dfs_maze[bottom] != -1):
            neighbors.append(bottom)

    if j+1 < len(dfs_maze):
        right = (i,j+1)
        if(dfs_maze[right] != 1 and dfs_maze[right] != -1):
            neighbors.append(right)

    return neighbors
