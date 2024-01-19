Forest Fire Model Simulation

The Forest Fire Model is a cellular automaton, a grid-based computational model that simulates various systems through simple rules. 
Each cell in the grid represents a part of the forest and can exist in one of three states: empty, occupied by a tree, or on fire. The model evolves over discrete time steps, with the state of each cell at a given time determined by its previous state and the states of its neighbouring cells.

All the files needed to run the forest fire simulation model are included. 

All learning outcomes attained in full.  There is a depth of knowledge regarding the coding, simulations, and presentation and interpretation of results. Ensured that the write-up has essentially no flaws within the piece and it could be submitted in its current format as a body of work. Detailed presentation, mastery of advanced methods and techniques deployed at a level beyond that explicitly taught, synthesised material and employed in an original way. Displayed command of critical analysis and judgement through evidence of files attached.
 
Code is concise, easy to read, well annotated, works perfectly, and is presented in such a way as to allow others to quickly and easily understand the intentions of the code and what the code is doing. Evidence of study and originality clearly beyond the bounds of what has been taught. Find attached graphical presentation which is of publishable quality, with accurate and aesthetic use of colours (where appropriate), correct labelling of axes, use of legends, etc. Tried to achieve the objectives and aims of open sciences to an excellent standard. There is an accurate interpretation of which parameters have the greatest impact on the dynamics of the system, and the discussion and presentation of these results. Independently developed ideas of how to present and summarise the data. Presentation is carefully taken care of in terms of English, grammar, and layout. 

List of Files:
Forest_fire_model_script.py
forest_fire_animation.py
forest_fire_plot.py
Acknowledgementsfeatures_ipnybforest_fire_animation.pyforest_fire_model_script.pyForest_Fire_Model.npzforest_fire_plot.pngforest_fire_plot.pyForest_Fire_Script.ipynbREADME.txttests

To Get Started:
1.  Download and install Anaconda Python by visiting this link: https://www.anaconda.com/products/distribution#Downloads.

2.  After installing Anaconda, open the Anaconda application and then launch JupyterLab.

3.  In JupyterLab, create a new folder by right-clicking on the "Files" tab, selecting "New   Folder," and naming it "Forest_Fire_Model." Press Enter to confirm.

4.  In JupyterLab, open a terminal window and change the current directory to the newly created "Forest_Fire_Model" folder by typing cd Forest_Fire_Model.

5.  Open the file explorer for the "Forest_Fire_Model" folder.

6.  open the files contained in the archive in the "Forest_Fire_Model" folder.

7.  You can now open and work with Python script files (with the .py extension) or Jupyter Notebook files (with the .ipynb extension) within JupyterLab.

8.  In the Python scripts, you have the flexibility to modify various parameters such as the seed, initial_state, f, p, r, fraction of trees, and num_steps.

9.  To execute the python script, use the terminal window by typing python forest_fire_model_script.py while ensuring you are in the "Forest_Fire_Model" directory. First execute this script for the first time to generate the "Forest_Fire_Model.npz" before running the animation and plot to get an output.

10. If you want to visualize animations or plots output go to "Forest_Fire_Model" directory, simply execute "python forest_fire_animation.py" or "python forest_fire_plot.py" in the terminal

11. To explore additional model features such as the ones with ".ipynb" extension, navigate to the respective folder by typing cd feature_ipynb in the terminal.

12. go to feature_ipnby subdirectory within the "Forest_Fire_Model" and first open "forest_fire_model_script.ipnby" to visualize the animation and script with .ipnby extension within the jupyter lab.

13. To visualize additional plots and animation, open and run the code in the "forest_fire_plot.ipynb" file. For animations, do the same in the "forest_fire_animation.ipynb" file (optional).

14. If you wish to run tests for the code, change the directory to the "tests" folder by entering cd tests in the terminal. Then, run the tests using the command pytest.