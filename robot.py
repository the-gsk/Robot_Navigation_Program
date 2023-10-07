class Robot:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.directions = ["N", "E", "S", "W"]
        self.row = 0
        self.col = 0
        self.direction = "S"

    def move(self):
        if self.direction == "N" and self.row > 0:
            self.row -= 1
        elif self.direction == "E" and self.col < self.cols - 1:
            self.col += 1
        elif self.direction == "S" and self.row < self.rows - 1:
            self.row += 1
        elif self.direction == "W" and self.col > 0:
            self.col -= 1

    def turn_left(self):
        current_index = self.directions.index(self.direction)
        self.direction = self.directions[(current_index - 1) % 4]

    def turn_right(self):
        current_index = self.directions.index(self.direction)
        self.direction = self.directions[(current_index + 1) % 4]

    def execute_instructions(self, instructions):
        for instruction in instructions:
            if instruction == "M":
                self.move()
            elif instruction == "L":
                self.turn_left()
            elif instruction == "R":
                self.turn_right()

    def get_position(self):
        return f"({self.row},{self.col},{self.direction})"


if __name__ == "__main__":
    grid_rows = 5
    grid_cols = 4

    robot = Robot(grid_rows, grid_cols)

    initial_instructions = "MSMMEMM"
    robot.execute_instructions(initial_instructions)

    final_position = robot.get_position()
    print(f"Final Position: {final_position}")
