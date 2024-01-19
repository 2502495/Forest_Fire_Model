import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as seabn
import forest_fire_model_script
import importlib


#Forest Fire Model Plot
#Run cell to get plot
# Reload the script each time to update any changes made to probability f
importlib.reload(forest_fire_model_script)
with np.load("Forest_Fire_Model.npz") as forest_grid:
    forest_grid = forest_grid["simulation_state"]

# Creating empty list for trees and fires
num_trees_array = []
num_fires_array = []

# looping over each time step in state (grid)
for grid_state in forest_grid:
    # Calculating total number of cells in the grid 
    total_cells = grid_state.shape[0]*grid_state.shape[1]
    
    # Counting trees, then calculating percentage coverage
    trees = np.count_nonzero(grid_state == 1)/(total_cells)*100
    num_trees_array.append(trees)
    
    # Counting fires, then calculating percentage coverage
    fires = np.count_nonzero(grid_state == 2)/(total_cells)*100
    num_fires_array.append(fires)

# Lightning rate (probility f) calculated as a percentage
lightning_strike = lightning_probability*100

# wind_effect rate (probility w) calculated as a percentage
wind_effect = wind_effect_probability*100

# Creating dataframe
forestfire_model = pd.DataFrame({"Trees" : num_trees_array, "Fires" : num_fires_array, "Lightning rate" : lightning_strike, "Wind-effect rate" : wind_effect})
forestfire_model.index.name = "Time step"

# Setting size of figure, style and font size 
seabn.set(style = "white", font_scale=1.5)

# Plotting the data
plot = seabn.relplot(data=forestfire_model, kind="line").set(
    xlim=(0, None), 
    ylim=(0, None), 
    ylabel="Proportion of Cells (%)"
)

# Set figure size (inches)
plot.fig.set_size_inches(8, 4)

# Saving output as a png (picture) file
plt.savefig('forest_fire_plot.png')