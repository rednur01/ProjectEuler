# Longest Collatz sequence

def Collatz_next(n: int) -> int:
  if n % 2 == 0:
    return n // 2
  else:
    return 3 * n + 1
  
class ChainList:
  def __init__(self) -> None:
    self.nums = {1: 1}

  def add(self, num: int, length: int) -> None:
    self.nums[num] = length

  def has_chain(self, n: int) -> bool:
    return n in self.nums
  
  def chain_length_of(self, n: int) -> int:
    return self.nums[n]
  
  def __repr__(self) -> str:
    stringified: str = ""
    for key in self.nums:
      stringified += f"({key}, {self.nums[key]})" + "\n"
    return stringified

chain_list = ChainList()

def find_chain_length(n: int) -> int:
  if chain_list.has_chain(n):
    return chain_list.chain_length_of(n)
  else:
    c_next: int = Collatz_next(n)
    length: int = 1 + find_chain_length(c_next)
    chain_list.add(n, length)
  
  return length

max_length: int = 1

for n in range(2, 1_000_000):
  length: int = find_chain_length(n)
  if length > max_length:
    max_length = length
    print(f"New max chain: ({n}, {length})")
