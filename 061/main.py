# Cyclical figurate numbers

triangles: dict[int,int] = {}
squares: dict[int,int] = {}
pentagons: dict[int,int] = {}
hexagons: dict[int,int] = {}
heptagons: dict[int,int] = {}
octagons: dict[int,int] = {}

for n in range(10_000):
  triangle = n * (n + 1) // 2
  square = n * n
  pentagon = n * (3*n - 1) // 2
  hexagon = n * (2*n - 1)
  heptagon = n * (5 * n - 3) // 2
  octagon = n * (3 * n - 2)

  if triangle >= 1000 and triangle < 10_000:
    triangles[n] = triangle
  
  if square >= 1000 and square < 10_000:
    squares[n] = square
  
  if pentagon >= 1000 and pentagon < 10_000:
    pentagons[n] = pentagon
  
  if hexagon >= 1000 and hexagon < 10_000:
    hexagons[n] = hexagon
  
  if heptagon >= 1000 and heptagon < 10_000:
    heptagons[n] = heptagon
  
  if octagon >= 1000 and octagon < 10_000:
    octagons[n] = octagon
  
  if (triangle > 10_000 and 
      square > 10_000 and
      pentagon > 10_000 and
      hexagon > 10_000 and
      heptagon > 10_000 and
      octagon > 10_000):
    break


shapes = {
  "triangles": triangles,
  "squares": squares,
  "pentagons": pentagons,
  "hexagons": hexagons,
  "heptagons": heptagons,
  "octagons": octagons,
}

def last_2_digits(n: int) -> int:
  return n % 100

def first_2_digits(n: int) -> int:
  return n // 100

def find_chains(chain_length: int, starting_shape: str, visited_shapes: list[str] = [], starting_digits: int = -1):
  chains: list[tuple[str,int,int]] = []
  
  if len(visited_shapes) == len(shapes): # no shapes left
    return []
  
  starting_set = shapes[starting_shape]

  if starting_digits != -1:
    starting_set = {key: starting_set[key] for key in starting_set if first_2_digits(starting_set[key]) == starting_digits}

  if len(starting_set) == 0: # no matches
    return []

  if chain_length == 0: # terminal
    for n in starting_set:
      # chains.append(f" >> {starting_shape[:3]} {starting_set[n]}")
      chains.append([(starting_shape[:3], n, starting_set[n])])
  
  else:
    for n in starting_set:
      last = last_2_digits(starting_set[n])      
      shapes_so_far = visited_shapes + [starting_shape]

      for shape in filter(lambda shape: shape not in shapes_so_far, shapes):
        next_chains = find_chains(chain_length-1, shape, shapes_so_far, last)

        for next_chain in next_chains:
          # chains.append(f" >> {starting_shape[:3]} {starting_set[n]} {next_chain}")
          chains.append([(starting_shape[:3], n, starting_set[n])] + next_chain)

  return chains

def find_cyclic_chains_of_shape(starting_shape: str):
  cyclic_chains = []
  linear_chains = find_chains(len(shapes)-1, starting_shape)
  
  for chain in linear_chains:
    first_num = chain[0][2]
    last_num = chain[-1][2]
    if last_2_digits(last_num) == first_2_digits(first_num):
      cyclic_chains.append(chain)
  
  return cyclic_chains

def find_cyclic_chains():
  unique_chains = {}

  for shape in shapes:
    chains = find_cyclic_chains_of_shape(shape)
    
    for chain in chains:
      chain_sum = sum(map(lambda elem: elem[2], chain))
      if chain_sum not in unique_chains:
        unique_chains[chain_sum] = chain

  for chain_sum in unique_chains:
    print(chain_sum, unique_chains[chain_sum])

find_cyclic_chains()