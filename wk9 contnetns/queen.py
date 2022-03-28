"""The Environment"""


class Environment(object):
    def __init__(self, size):
        self.size = size
        self.solutions = 0


"""Agent Behaviour"""
# Depth First Search


class Agent(Environment):

    def __init__(self, Environment, location):
        positions = [-1] * Environment.size  # create a list of size N
        self.visited_rows = 0
        self.put_queen(Environment, positions, location)
        print("Found", Environment.solutions, "solutions.")

    def put_queen(self, Environment, positions, target_row):
        # Try to place a queen on row
        # If valid recurse to place on the next row until N queens are placed
        # Base (stop) case - when you visit N rows
        self.visited_rows += 1
        if target_row == Environment.size:
            self.show_full_board(Environment, positions)
            Environment.solutions += 1
        else:
            # For all N columns positions in the row try to place a queen
            for column in range(Environment.size):
                # Reject all invalid positions
                if self.check_place(positions, target_row, column):
                    positions[target_row] = column
                    self.put_queen(Environment, positions, target_row+1)

    def check_place(self, positions, ocuppied_rows, column):
        """
        Check if a given position is under attack from any of
        the previously placed queens (check column and diagonal positions)
        """
        for i in range(ocuppied_rows):
            if positions[i] == column or \
                    positions[i] - i == column - ocuppied_rows or \
                    positions[i] + i == column + ocuppied_rows:
                return False
        return True

    def show_full_board(self, Environment, positions):
        """Show the full NxN board"""
        for row in range(Environment.size):
            line = ""
            for column in range(Environment.size):
                if positions[row] == column:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("\n")


"""Create the agent"""
# Maximum number of queens are equal to No of rows
boardsize = 4
location = 0
theEnvironment = Environment(boardsize)
theAgent = Agent(theEnvironment, location)


# sliding tiles
