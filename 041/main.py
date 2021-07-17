# Pandigital prime

# Domain restriction
# 8-digit and 9-digit numbers have their digits add up to a multiple of 9
# so max digits for pandigital prime = 7 digits

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

def is_pandigital(a: int):
  digits: list[str] = [char for char in str(a)]
  num_digits: int = len(digits)
  unique_digits: set[str] = set(digits)
  
  must_have_digits = map(lambda n: str(n), list(range(1, num_digits+1)))

  # Has all digits
  for d in must_have_digits:
    if d not in unique_digits:
      return False

  return True

for i in range(7_654_321, 11, -2):
  if is_pandigital(i) and is_prime(i):
    print(i)
    break
