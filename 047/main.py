# Distinct prime factors

def prime_factors(n: int) -> set[int]:
  factors: list[int] = []

  i: int = 2
  while i <= n and n > 1:
    if n % i == 0:
      factors.append(i)
      n /= i
      i = 2
    else:
      i += 1
      
  return set(factors)

i = 3

a = prime_factors(i)
b = prime_factors(i+1)
c = prime_factors(i+2)
d = prime_factors(i+3)

while True:
  a, b, c, d = b, c, d, prime_factors(i+3)

  if len(a) == len(b) == len(c) == len(d) == 4:
    print(f"{i}:{a} | {i+1}:{b} | {i+2}:{c} | {i+3}:{d}")
    break

  i += 1