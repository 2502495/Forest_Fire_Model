import numpy as np

#Forest Fire Model to be executed

# Set the seed for pseudo-randomness
np.random.seed(7)

# Function to initialize the simulation grid
def initialize_simulation(num_steps, initial_state):
    """
    Initialize the grid with the initial state of the system and create an empty array to store the state at each time step.
    
    The function would take the arguments:
        num_steps (int): Number of time steps in the simulation.
        initial_state (np.ndarray): The 2-dimensional initial state of the model.

    The function would Return:
        np.ndarray: A 2-dimensional array to store the state at each time step, starting with the initial state.
    """
    # Create an empty grid with the same shape as the initial state
    simulation_grid = np.zeros((num_steps, *initial_state.shape), dtype=np.int32)
    # Set the initial state as the first step of the simulation
    simulation_grid[0] = initial_state
    return simulation_grid

# Function to update the simulation grid based on forest-fire rules
def update_simulation(previous_grid, lightning_probability, wind_effect_probability, tree_growth_probability):
    """
    Update the state of the grid based on the previous state, following the four forest-fire rules in order.
    
    The function would takes arguments:
        previous_grid (np.ndarray): The previous 2-dimensional state of the grid.
        lightning_probability (float): The probability of a tree catching fire due to lightning strike.
        wind_effect_probability (float): The probability of a fire accelerating due to wind effects.
        tree_growth_probability (float): The probability of an empty space becoming a tree due to tree growth.
    
    Function Return:
        np.ndarray: The new, updated, 2-dimensional state of the grid.
    """
    # Create a copy of the previous grid to store the updated state
    updated_grid = np.copy(previous_grid)
    
    # Loop through each cell in the grid
    for x in range(previous_grid.shape[0]):
        for y in range(previous_grid.shape[1]):
            # Get the current cell state
            current_cell = previous_grid[x, y]
            
            # Determine the state of neighboring cells
            neighbor_above = previous_grid[x-1, y] if x > 0 else 0
            neighbor_below = previous_grid[x+1, y] if x < previous_grid.shape[0]-1 else 0
            neighbor_left = previous_grid[x, y-1] if y > 0 else 0
            neighbor_right = previous_grid[x, y+1] if y < previous_grid.shape[1]-1 else 0
            
            # Create a list of neighbor states
            neighbors = [neighbor_above, neighbor_below, neighbor_left, neighbor_right]
            
            # Apply forest-fire rules to update the cell state
            if current_cell == 2:
                # Rule 1: A burning cell in the previous time step turns into an empty cell
                updated_grid[x, y] = 0
               
            elif current_cell == 1:
                if 2 in neighbors:
                    # Rule 2: A tree will start burning if at least one neighbor is burning
                    updated_grid[x, y] = 2
                elif np.random.random() < lightning_probability:
                    # Rule 3: A tree turns into fire due to lightning probability
                    updated_grid[x, y] = 2
                elif np.random.random() < wind_effect_probability:
                    # Rule 5: The fire will accelerate due to wind effects probability
                    updated_grid[x, y] = 3
            elif np.random.random() < tree_growth_probability:
                # Rule 4: An empty space fills with a tree due to tree growth probability
                updated_grid[x, y] = 1
                    
            else:
                # Cell remains unchanged if no rules match
                updated_grid[x, y] = previous_grid[x, y]
                    
    return updated_grid

# Function to run the simulation for a given number of steps
def run_simulation_steps(num_steps, initial_state, lightning_probability, wind_effect_probability, tree_growth_probability):
    """
    Run the forest fire simulation for a given number of steps.
    
    Function takes arguments:
        num_steps (int): Number of time steps that the simulation will run for.
        initial_state (np.ndarray): The 2-dimensional initial state of the forest.
        lightning_probability (float): The probability of a tree catching fire due to lightning.
        wind_effect_probability (float): The probability of a fire accelerating due to wind effects.
        tree_growth_probability (float): The probability of an empty space becoming a tree due to tree growth.

    Function Returns: 
        np.ndarray: The overall state for the forest fire simulation.
    """
    # Initialize the simulation grid
    simulation_state = initialize_simulation(num_steps, initial_state)
    
    # Iterate through each time step
    for t in range(1, num_steps):
        # Update the simulation grid based on the previous state
        simulation_state[t] = update_simulation(simulation_state[t-1], lightning_probability, wind_effect_probability, tree_growth_probability)
        
    return simulation_state

# Parameters for the forest fire simulation
lightning_probability = 0.2  # Probability of a tree catching fire due to lightning strike.
wind_effect_probability = 0.1 # The probability of a fire accelerating due to wind effects.
tree_growth_probability = 0.5  # Probability of an empty space becoming a tree due to tree growth.

# The fraction of the forest covered by trees
initial_tree_fraction = 0.5

# The initial state of the forest, a 100x100 grid filled with empty (0) and tree (1) cells
initial_forest_state = np.random.binomial(1, initial_tree_fraction, size=(100, 100))

# The number of time steps (t) that the simulation will run for
num_simulation_steps = 200

# Run the forest fire simulation and save the resulting grid
forest_simulation_grid = run_simulation_steps(num_simulation_steps, initial_forest_state, lightning_probability, wind_effect_probability, tree_growth_probability)

# Save the numpy grid to file "forest_simulation.npz"
np.savez_compressed("Forest_Fire_Model", simulation_state=forest_simulation_grid)
#***************************************************************************************************************************************