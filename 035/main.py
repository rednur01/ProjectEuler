# Circular primes

# Domain restriction
# Numbers with 2,4,6,8,0,5 as digits can be discarded
# since a permutation of this number would have those as the ending digit
# and primes cannot end with those digits

# For speed, first list all candidate primes
# Then loop through this list and check that all their rotations
# are also in this list

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

def circular_rotations(n: int) -> list[int]:
  assert n >= 0
  if n < 10:
    return [n]
  
  digits: list[str] = [char for char in str(n)]
  rotations: set[int] = set([])

  for i in range(len(digits)-1):
    rotating_digit: str = digits[0]
    digits = digits[1:]
    digits.append(rotating_digit)
    rotations.add(int("".join(digits)))
  
  return list(rotations)

def contains_any_of_digits(num: int, digits: list[int]) -> bool:
  for digit in digits:
    if str(digit) in str(num):
      return True
  return False

primes: list[int] = [2, 3, 5]
circular_primes: list[int] = []

for i in range(7, 1_000_000, 2):
  if not contains_any_of_digits(i, [2,4,6,8,0,5]) and is_prime(i):
    primes.append(i)

for prime in primes:
  rotations: list[int] = circular_rotations(prime)
  
  all_rotations_are_prime: bool = True
  for rotation in rotations:
    if not rotation in primes:
      all_rotations_are_prime = False
      break
  
  if all_rotations_are_prime:
    circular_primes.append(prime)

print(f"{len(circular_primes)}: {circular_primes}")