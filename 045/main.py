# Triangular, pentagonal, and hexagonal

from math import sqrt

def triangle(n: int) -> int:
  return n * (n+1) // 2

def is_pentagon(p: int) -> bool:
  n = (sqrt((24 * p + 1)) + 1) / 6
  return n.is_integer()

def is_hexagon(h: int) -> bool:
  n = (sqrt(8 * h + 1) + 1) / 4
  return n.is_integer()


i: int = 285

while True:
  i += 1
  if is_pentagon(triangle(i)) and is_hexagon(triangle(i)):
    print(f"Triangle {i} = {triangle(i)}")
    break