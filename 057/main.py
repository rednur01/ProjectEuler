# Square root convergents

# Following the pattern in each fraction
# n/d -> n+2d / n+d

def num_digits(n: int) -> int:
  return len(str(n))

limit: int = 1_000 + 1

n: int = 2
d: int = 3

total: int = 0

for i in range(2,limit):
  n, d = n + 2 * d, n + d

  if num_digits(n) > num_digits(d):
    total += 1

print(total)