import matplotlib.pyplot as plt

def maze_plot(maze):
    fig, ax = plt.subplots()
    ax.cla()
    cmap = plt.cm.get_cmap()
    cmap.set_bad("white")
    ax.imshow(maze, cmap=cmap)
    #plt.show()
    plt.pause(0.1)

def maze_plot_final(maze):
    fig, ax = plt.subplots()
    ax.cla()
    cmap = plt.cm.get_cmap()
    cmap.set_bad("white")
    ax.imshow(maze, cmap=cmap)
    plt.savefig('figs/bfs/foo.png', bbox_inches='tight')
