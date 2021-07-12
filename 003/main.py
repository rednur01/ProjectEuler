# Largest prime factor

### Helper function ###
from math import sqrt, ceil

def isPrime(n: int) -> bool:
  if n < 2:
    return False
  elif n == 2:
    return True
  elif n % 2 == 0:
    return False
  else:
    for i in range(3, ceil(sqrt(n))+1, 2): 
    # Only check upto sqrt(n) since at least one prime root must be < sqrt(n)
    # Start at 3 and jump by 2 to skip testing for even factors
      if n % i == 0:
        return False
  
  return True

def isFactor(to_check: int, N: int) -> bool:
  return N % to_check == 0

### Computation ###
def find_prime_factors(N: int):
  
  prime_factors: list[int] = [1]
  factor_reduced_N: int = N

  # For each prime factor found, divide the number by that factor
  # This factor-reduced number becomes the new limit
  # upto which to check for new prime factors

  i: int = 2
  while factor_reduced_N >= max(prime_factors) and i <= factor_reduced_N:
    if isPrime(i) and isFactor(i, N):
      factor_reduced_N /= i
      prime_factors.append(i)
    i += 1

  print(f"{N}: {prime_factors}")

find_prime_factors(600851475143)