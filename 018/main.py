# Maximum path sum I

### Method ###

# Start at the top node and follow the highest value node out of the next 2 reachable ones
# If only highest node followed at each point, then this is "greedy search"
# Does not find the best path, better paths further down the line can be missed if they have poor starts

# Penalize "depth-first" behavior of greedy search by adding a "cost" for depth
# This makes going too deep too early expensive and encourages breadth-wise exploration
# This is "A* search"

# Heuristic for picking best path = sum of node values
# Cost function = x per node in path = best path value penalized by cost

# Next nodes = bottom, bottom-right

### Data ###

string: str = '''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

string_rows: list[str] = [row for row in string[1:].splitlines()]

numbers: list[list[int]] = []
for row in string_rows:
  numbers.append([int(num) for num in row.split()])

### Algorithm ###

class Node:
  def __init__(self, value: int,  path_weight: int, path_length: int, row: int, column: int) -> None:
    self.value = value
    self.path_weight = path_weight
    self.path_length = path_length
    self.row = row
    self.column = column
    self.history: list[int] = [value]

  def reachable_nodes(self) -> list['Node']:
    bottom_num: int = numbers[self.row+1][self.column]
    bottom_right_num: int = numbers[self.row+1][self.column+1]

    b_Node = Node(bottom_num, self.path_weight + bottom_num, self.path_length + 1, self.row+1, self.column)
    br_Node = Node(bottom_right_num, self.path_weight+bottom_right_num, self.path_length + 1, self.row+1, self.column+1)

    b_Node.history = self.history + b_Node.history
    br_Node.history = self.history + br_Node.history

    return [b_Node, br_Node]
  
  def __repr__(self) -> str:
    return f"Node({self.value}, {self.path_weight}, {self.path_length}, {self.row}, {self.column})"

  def __lt__(self, other: 'Node') -> bool:
    return self.path_weight < other.path_weight
  
  def __eq__(self, other: 'Node') -> bool:
    return self.path_weight == other.path_weight

def apply_cost(node: Node) -> Node:
  cost_per_move: int = 50 # Median value node can have
  node.path_weight = node.path_weight - cost_per_move * node.path_length
  return node

def list_has_node(node_list: list[Node], node: Node) -> bool:
  node_values: list[int] = list(map(lambda n: (n.row, n.column), node_list))
  return (node.row, node.column) in node_values

# Search
explored: list[Node] = []
unexplored: list[Node] = []

max_path_length = len(numbers)

start = Node(numbers[0][0], numbers[0][0], 0, 0, 0)
unexplored.append(start)

while len(unexplored) > 0:
  next_node = unexplored.pop()
  explored.append(next_node)

  if (next_node.path_length < max_path_length - 1):
    reachable_nodes = next_node.reachable_nodes()
    reachable_nodes = list(map(apply_cost, reachable_nodes))

    for node in reachable_nodes:
      if not list_has_node(unexplored, node):
        unexplored.append(node)
    unexplored.sort()
  else:
    best_path_endpoint: Node = explored.pop()
    break

print(f"Path: {best_path_endpoint.history}")
print(f"Sum: {sum(best_path_endpoint.history)}")
print(f"Paths searched: {len(unexplored) + len(explored) + 1}/16384")