class SudokuGame:
    def __init__(self, size=9):
        self.size = size
        self.grid = self.generate_blank_grid(size)

    def generate_blank_grid(self, size):
        return [[0 for _ in range(size)] for _ in range(size)]

    def print_grid(self):
        for row in self.grid:
            print(" ".join(str(num) if num != 0 else "-" for num in row))

    def is_valid_move(self, row, col, num):
        # Check if placing 'num' at (row, col) violates Sudoku rules
        pass

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
            if self.is_valid_move(row, col, num):
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
