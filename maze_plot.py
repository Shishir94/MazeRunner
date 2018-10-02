import matplotlib.pyplot as plt

def maze_plot(maze):
    fig, ax = plt.subplots()
    ax.cla()
    cmap = plt.cm.get_cmap()
    cmap.set_bad("white")
    ax.imshow(maze, cmap=cmap)
    #plt.show()
    plt.pause(0.1)

def maze_plot_final(maze, s):
    fig, ax = plt.subplots()
    ax.cla()
    cmap = plt.cm.get_cmap()
    cmap.set_bad("white")
    plt.xlim(-10,len(maze)+10)
    plt.ylim(len(maze)+10,-10)
    ax.imshow(maze, cmap=cmap)
    plt.draw()
    if(s=="a"):
        plt.savefig('figs/a_star-new.png', dpi=1000, bbox_inches='tight',)
    else:
        plt.savefig('figs/bfs-new.png', dpi=1000, bbox_inches='tight',)
    plt.show()
