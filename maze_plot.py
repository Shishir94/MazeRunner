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
    plt.xlim(-10,len(maze)+10)
    plt.ylim(len(maze)+10,-10)
    ax.imshow(maze, cmap=cmap)
    plt.draw()
    plt.savefig('figs/dfs-new.png', dpi=1000, bbox_inches='tight',)
    plt.show()
