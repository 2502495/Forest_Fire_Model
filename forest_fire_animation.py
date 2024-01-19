import numpy as np
import matplotlib.pyplot as plt
from IPython.display import HTML
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap


#Forest Fire Model Animation

# Loading forest fire simulation
with np.load("Forest_Fire_Model.npz") as forest_grid:
    forest_grid = forest_grid["simulation_state"]
    
# Setting up the initial figure and axes
fig, ax = plt.subplots(constrained_layout=True)
ax.axis("off")

# Set colours for states 0 (empty), 1 (tree) and 2 (fire) respectively
cmap = ListedColormap(["black", "darkgreen", "red"])

# Plot the initial grid
grid_plot = ax.imshow(
    forest_grid[0],
    vmin=forest_grid.min(),
    vmax=forest_grid.max(),
    animated=True,
    cmap=cmap
)

# Animating the state of each grid (number of grids dependent on number of steps)
def animate(xy):
    grid_plot.set_array(forest_grid[xy])
    return [grid_plot]

# Creating animation object, interval set to 100ms 
anim = FuncAnimation(fig, animate, frames=len(forest_grid), interval=100)

# Displaying animation in Jupyter Notebook
HTML(anim.to_jshtml())