# Sudoku 
def print_grid(grid):
  for row in grid:
    print(" ".join(str(num) if num !=0 else "-" for num in row))

def generate_blank_grid(size):
  return[[0 for _ in range(size)] for _ in range(size)]

if __name__ == "__main__":
  size = 9 
  sudoku_grid = generate_blank_grid(size)
  print("Blank Sudoku Grid:")
  print_grid(sudoku_grid)
