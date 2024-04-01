import random

class SudokuGame:
    def __init__(self, size=9):
        self.size = size
        self.grid = self.generate_blank_grid(size)

    def generate_blank_grid(self, size):
        grid = [[0 for _ in range(size)] for _ in range(size)]
        # You can set the number of pre-filled cells here
        num_prefilled_cells = 20
        for _ in range(num_prefilled_cells):
            row = random.randint(0, size - 1)
            col = random.randint(0, size - 1)
            num = random.randint(1, 9)
            while not self.is_valid_move(row, col, num, grid):
                row = random.randint(0, size - 1)
                col = random.randint(0, size - 1)
                num = random.randint(1, 9)
            grid[row][col] = num
        return grid

    def print_grid(self):
        for row in self.grid:
            print(" ".join(str(num) if num != 0 else "-" for num in row))

    def is_valid_move(self, row, col, num, grid):
        # Check if placing 'num' at (row, col) violates Sudoku rules
        # Check row
        if num in grid[row]:
            return False
        # Check column
        if num in [grid[i][col] for i in range(self.size)]:
            return False
        # Check subgrid (3x3)
        subgrid_row, subgrid_col = row // 3 * 3, col // 3 * 3
        for i in range(subgrid_row, subgrid_row + 3):
            for j in range(subgrid_col, subgrid_col + 3):
                if grid[i][j] == num:
                    return False
        return True

    def is_complete(self):
        # Check if the Sudoku grid is fully filled
        for row in self.grid:
            if 0 in row:
                return False
        return True

    def play(self):
        while not self.is_complete():
            self.print_grid()
            row = int(input("Enter row (1-9): ")) - 1
            col = int(input("Enter column (1-9): ")) - 1
            num = int(input("Enter number (1-9): "))
            if self.is_valid_move(row, col, num, self.grid):
                self.grid[row][col] = num
            else:
                print("Invalid move! Try again.")
        print("Congratulations! You've completed the Sudoku.")

def main():
    size = 9
    game = SudokuGame(size)
    game.play()

if __name__ == "__main__":
    main()
