# Special Pythagorean triplet

# Find all Pythagorean triples
# where a + b + c < 1000

from math import sqrt, floor, ceil

def isInt(n: float) -> bool:
  return floor(n) == ceil(n)

limit: int = 1000
a: int = 1

for a in range(1, limit):
  for b in range(a+1, limit-a):
    c_sq: float = a**2 + b**2
    c_float: float = sqrt(c_sq)
    c: int = int(c_float)

    if isInt(c_float) and a + b + c == 1000:
      product: int = a * b * c
      print(f"{a}^2 + {b}^2 = {c}^2 | {a} + {b} + {c} = 1000 | {a} * {b} * {c} = {product}")