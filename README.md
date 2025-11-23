# Game of Life

Conway's Game of Life implemented with Pygame and NumPy.

## Overview
This repository contains a simple, interactive implementation of Conway's Game of Life using Python, Pygame for rendering and input, and NumPy for grid state management. The simulation runs on a toroidal (wrap-around) grid.

## Requirements
- Python 3.8+
- pip
- pygame
- numpy

## Installation
1. Clone the repository:

   ```
   git clone https://github.com/PawelSzeliga23/GameOfLife.git
   cd GameOfLife
   ```

2. (Optional but recommended) Create and activate a virtual environment:

   ```
   # macOS / Linux
   python3 -m venv venv
   source venv/bin/activate

   # Windows (PowerShell)
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```
   pip install numpy pygame
   ```

   If you prefer a requirements file, create one and install:

   ```
   echo "numpy\npygame" > requirements.txt
   pip install -r requirements.txt
   ```

## Running
Start the simulation with:

   ```
   python game.py
   ```

(Or python3 game.py if your system requires it.)

The default grid size and cell size are set at the bottom of game.py:

   ```
   main(120, 80, 10)
   ```

You can change these numbers to adjust the number of cells horizontally, vertically, and the pixel size of each cell.

## Controls
- Left click (when simulation is OFF): toggle a cell alive/dead.
- Space: start / stop the simulation.
- C: clear the grid (all cells dead).
- R: reset to the initial pattern recorded before the simulation started.
- Click the RULES text field to activate it, then type a new rule string and press Enter to apply it.
- Backspace: edit rule text.

## Rules format
The rules are specified as "<survive>/<birth>" (without quotes). Example: "23/3" (the default)
- "23/3" means: an alive cell survives if it has 2 or 3 neighbors; a dead cell becomes alive if it has exactly 3 neighbors.

## Internals / Notes
- The grid wraps around at edges (toroidal topology).
- The rules parsing in game.py expects digits 0-8 on each side of the slash. For example, "135/357" is valid.
- The program uses NumPy arrays for fast neighbor counting and Pygame for drawing.

## Troubleshooting
- If installing pygame fails on your platform, try installing a platform-specific wheel or consult the pygame installation docs: https://www.pygame.org/wiki/GettingStarted
- If you see an ImportError for numpy or pygame, make sure your virtual environment is activated and that you installed the packages into it.

## License
This project is provided as-is. You may add a license file if you wish to apply an open-source license (for example, MIT).