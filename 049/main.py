# Prime permutations

from math import ceil, sqrt
from itertools import permutations

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

def is_arithmetic_sequence(nums: list[int]) -> bool:
  if len(nums) < 3:
    return False
  
  increment: int = nums[1] - nums[0]
  
  for i in range(1, len(nums)-1):
    if nums[i+1] - nums[i] != increment:
      return False

  return True

def find_gaps(nums: list[int]) -> list[int]:
  assert len(nums) >= 3
  
  gaps: list[int] = []
  for i in range(len(nums) - 1):
    gaps.append(nums[i+1] - nums[i])
  
  return gaps

primes: list[int] = []

for i in range(1023, 9877, 2):
  if is_prime(i):
    primes.append(i)
  
for prime in primes:
  all_permutations = list(permutations(str(prime), 4))
  all_permutations = list(map(lambda p: int("".join(p)), all_permutations))

  for i in range(100, 5000):
    if (prime + i in all_permutations and prime + i in primes and
        prime + 2 * i in all_permutations and prime + 2 * i in primes):
      print(prime, prime+i, prime + 2*i, i)
  
# for prime in primes:
#   all_permutations = permutations(str(prime), 4)
#   all_permutations = map(lambda p: int("".join(p)), all_permutations)
  
#   prime_permutations: set[int] = set([])

#   for permutation in all_permutations:
#     if permutation in primes:
#       prime_permutations.add(permutation)
  
#   ordered_permutations: list[int] = list(prime_permutations)
#   ordered_permutations.sort()

#   if len(ordered_permutations) >= 3:
#     gaps_between_primes: list[int] = find_gaps(ordered_permutations)

