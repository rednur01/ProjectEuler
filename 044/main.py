# Pentagon numbers

# Does not guarantee minimum D
# Only checks upto a large limit

from math import sqrt

def pentagon(n: int) -> int:
  return n * (3 * n - 1) // 2

def is_pentagon(p: int) -> bool:
  n = (sqrt((24 * p + 1)) + 1) / 6
  return n.is_integer()

limit: int = 5000

for i in range(1, limit):
  for j in range(i+i, limit):
    S = pentagon(i) + pentagon(j)
    D = pentagon(j) - pentagon(i)
    if is_pentagon(S) and is_pentagon(D):
      print(f"{i=} {j=} {D=}")