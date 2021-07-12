# 10001st prime

# Uses the fact that all primes are 1 mod 6 or 5 mod 6

from math import sqrt, ceil

def isPrime(n: int) -> bool:
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

found_primes: int = 0
last_found: int = 0
target_index: int = 10_001

i: int = 2

while found_primes < target_index:
  if isPrime(i):
    found_primes += 1
    last_found = i
  i += 1

print(last_found)