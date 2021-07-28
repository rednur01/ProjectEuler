# Cubic permutations

def is_permutation(first: str, second: str) -> bool:
  first_digits: list[str] = [digit for digit in first]
  second_digits: list[str] = [digit for digit in second]

  for digit in first_digits:
    if first_digits.count(digit) != second_digits.count(digit):
      return False

  return len(first_digits) == len(second_digits)


# cube_map: dict[int,str] = {}

# for n in range(10_001):
#   cube_map[n] = str(n * n * n)

# cubes = list(cube_map.values())

def cube(n: int) -> str:
  return str(n * n * n)

limit: int = 10_000

def smallest_permutable_cube(num_permutations: int):
  for i in range(limit):
    permuations: list[str] = []

    for j in range(i+1, limit):
      if is_permutation(cube(i), cube(j)):
        permuations.append((j, cube(j)))
    
    if len(permuations) == num_permutations - 1: # counting self
      print((i, cube(i)), len(permuations), permuations)
      return


smallest_permutable_cube(5)