# Combinatoric selections

from functools import cache

@cache
def factorial(n):
  if n <= 1:
    return 1
  else:
    return n * factorial(n-1)

def combinations(n: int, r: int) -> int:
  assert r <= n
  return factorial(n) / (factorial(r) * factorial(n-r))


threshold: int = 1_000_000
count: int = 0


for n in range(1,101):
  for r in range(n+1):
    if combinations(n,r) > threshold:
      count += 1

print(count)

# Note: nCr == nC(r-1) but I wasn't able to get a proper count
# using that symmetry, will have to investigate later