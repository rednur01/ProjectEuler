# Number spiral diagonals

# Spirals must have odd side length
# last digit of spiral of side N = N^2

# Outer corners of spiral N
# N^2
# N^2 - (N-1)
# N^2 - 2(N-1)
# N^2 - 3(N-1)

# All diagonals of spiral
# = sum of outer spiral corners + sum of next inner spiral + ... until 1

def spiral_diagonal_sum(side: int) -> int:
  if side == 1:
    return 1
  
  outer_corner_sum: int = (
    side*side + 
    side*side -   (side - 1) +
    side*side - 2*(side - 1) +
    side*side - 3*(side - 1)
    )
  
  return outer_corner_sum + spiral_diagonal_sum(side-2)

print(spiral_diagonal_sum(1001))