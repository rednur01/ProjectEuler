# Lattice paths

### Method ###
# Represent a NxN grid as the vertices, making it a (N+1) * (N+1) lattice
# . . .
# . . .
# . . x

# Starting at the destination (bottom-right),
# mark each adjacent vertex with the number of route choices that can be
# made at that vertex (2 for inner points, since only down/right are valid moves,
# and 1 for edge points since they can only travel along the edge)

# Example with only some points marked
# . . 1
# . 2 1
# 1 1 x

# Let's call each marking a weight. The weight at each vertex now represents
# the number of routes from that path to the destination. So for any point that
# comes into one of these points, their total number of routes increases by 
# that vertex's route. Therefore we can calculate the other vertices
# as the sum of their neighbors' total weight

# 4x4 lattice example

# 20 10 4 1 
# 10  6 3 1
#  4  3 2 1
#  1  1 1 x

# Since the lattice is symmetric along the diagonal, we can only compute
# half of it, as long as we double the weights at the diagonal to account
# for the missing neighbor across the diagonal

# 4x4 example, mirrored horizontally and vertically

# x
# 1 2
# 1 3 6
# 1 4 10 20

# Memoize for speed
def path_length(row: int, column: int) -> int:
  if column > row:
    column, row = row, column
  
  square_side = max(row, column)
  
  lattice = []
  for i in range(square_side):
    lattice.append([0] * square_side)
  
  for r in range(1,row):
    for c in range(r+1):
      if c == 0:
        lattice[r][c] = 1
      elif r == c:
        lattice[r][c] = 2 * lattice[r][c-1]
      else:
        lattice[r][c] = lattice[r-1][c] + lattice[r][c-1]

  return lattice[row-1][column-1]

print(path_length(21,21))