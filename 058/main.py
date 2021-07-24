# Spiral primes

from math import ceil, sqrt

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


n: int = 1
num_diagonal_primes: int = 0
ratio: float = 1.0 

while ratio > 0.1:
  n += 1

  nth_odd: int = 2*n - 1
  corners: list[int] = [int(nth_odd**2), int(nth_odd**2 - (nth_odd-1)), int(nth_odd**2 - 2*(nth_odd-1)), int(nth_odd**2 - 3*(nth_odd-1))]
  corner_primes: int = list(filter(lambda corner: is_prime(corner), corners))
  num_diagonal_primes += len(corner_primes)

  diagonal_size: int = 4*(n-1) + 1
  ratio = num_diagonal_primes / diagonal_size

print(nth_odd)