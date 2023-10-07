# Robot Navigation Program

## Problem Description

Your company, iRobot, has created a new robot that can follow instructions to navigate a 5x4 grid. The robot can move in four directions: North (N), East (E), West (W), and South (S). It can also move one step in the direction it is currently facing (M). The robot starts at the position (0,0) facing South (S) in the grid.

## Instructions

- Create a 5x4 grid with coordinates starting from (0,0) to (4,3).
- Implement a robot class that can execute the following instructions:
  - **M:** Move one step in the current direction.
  - **L:** Turn left (change direction anticlockwise).
  - **R:** Turn right (change direction clockwise).

## Robot Class Implementation

```python
class Robot:
    def __init__(self, rows, cols):
        # Constructor to initialize robot's initial position and grid size.
        # ...

    def move(self):
        # Move the robot one step in the current direction.
        # ...

    def turn_left(self):
        # Turn the robot to the left (anticlockwise).
        # ...

    def turn_right(self):
        # Turn the robot to the right (clockwise).
        # ...

    def execute_instructions(self, instructions):
        # Execute a sequence of instructions.
        # ...

    def get_position(self):
        # Get the current position of the robot.
        # ...
```
## Example Usage
```python
if __name__ == "__main__":
    grid_rows = 5
    grid_cols = 4

    # Create a robot instance
    robot = Robot(grid_rows, grid_cols)

    # Example instructions
    initial_instructions = "MMLMRM"
    robot.execute_instructions(initial_instructions)

    # Get the final position
    final_position = robot.get_position()
    print(f"Final Position: {final_position}")
    
```

## Output
The program will output the final position of the robot after executing the given instructions.

## How to Run

Make sure you have Python installed on your system. Save the Python code in a file named robot.py and execute it using the following command:


```
python robot.py
```

This will run the program and display the final position of the robot based on the provided instructions.