# Prime pair sets

from math import ceil, sqrt
from functools import cache

@cache
def is_prime(n: int) -> bool:
  if n < 2:
    return False
  elif n == 2 or n == 3 or n == 5:
    return True
  elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
    return False
  else:
    for i in range(6, ceil(sqrt(n))+1, 6): 
    # Only check upto sqrt(n) since at least one prime root must be < sqrt(n)
    # Start at 6 and jump by 6
    # Since all primes are 1 mod 6 or 5 mod 6
    # only need to check i + 1 and i + 5 for prime factors
      if n % (i + 1) == 0 or n % (i + 5) == 0:
        return False
  return True

def next_prime(n: int) -> int:
  # assert n % 2 != 0
  while True:
    n = n + 2
    if is_prime(n):
      return n

def pair_concatenations(pair: tuple[int,int]) -> list[int]:
  left = int(str(pair[0]) + str(pair[1]))
  right = int(str(pair[1]) + str(pair[0]))
  return [left, right]

def primes_upto(limit: int) -> list[int]:
  # Exclude 2 and 5 since they cannot be in concatenation pairs
  # Primes must end in 1,3,7,9
  primes: list[int] = [3,7]
  while primes[-1] < limit:
    primes.append(next_prime(primes[-1]))
  return primes



primes = primes_upto(10_000)

def find_prime_set():
  for p1 in primes:
    for p2 in primes:
      if p2 <= p1:
        continue
      pair = (p1,p2)
      concats = pair_concatenations(pair)
      if all(map(is_prime, concats)):
        
        for p3 in primes:
          if p3 <= p2:
            continue
          pair_1 = (p1,p3)
          pair_2 = (p2,p3)
          concats = pair_concatenations(pair_1)
          concats.extend(pair_concatenations(pair_2))
          if all(map(is_prime, concats)):

            for p4 in primes:
              if p4 <= p3:
                continue
              pair_1 = (p1,p4)
              pair_2 = (p2,p4)
              pair_3 = (p3,p4)
              concats = pair_concatenations(pair_1)
              concats.extend(pair_concatenations(pair_2))
              concats.extend(pair_concatenations(pair_3))
              if all(map(is_prime, concats)):

                for p5 in primes:
                  if p5 <= p4:
                    continue
                  pair_1 = (p1,p5)
                  pair_2 = (p2,p5)
                  pair_3 = (p3,p5)
                  pair_4 = (p4,p5)
                  concats = pair_concatenations(pair_1)
                  concats.extend(pair_concatenations(pair_2))
                  concats.extend(pair_concatenations(pair_3))
                  concats.extend(pair_concatenations(pair_4))
                  if all(map(is_prime, concats)):
                    prime_set = (p1,p2,p3,p4,p5)
                    print(f"{sum(prime_set)}: {prime_set}")

find_prime_set()