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
    # Test to see if expected array is equal to output array, ran using 'pytest' in terminal
    np.testing.assert_array_equal(previous_grid, updated_grid)