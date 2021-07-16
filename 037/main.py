# Truncatable primes

# Allowed digits = [1,3,7,9]
# If the other digits are allowed, such as 2, then during
# right-truncation that digit would eventually be exposed as the last
# digit, and prime numbers cannot end in even digits or 5 or 0
# (Exception: 2 and 5 can be *starting* digits)

# If we start with an N-digit number and truncate once, we have an (N-1) digit
# number left which must be a prime

# So we can start by considering all 2-digit primes within this ruleset
# then all 3-digits, and slowly build up a "primes-for-N-digits" ladder

# If we reach a digit N where no primes with this ruleset exist then we have
# found all truncatable primes below this limit

# Exceptions to this rule: 23 and 53

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

allowed_digits: list[int] = [1,3,7,9]
primes_per_rung: list[list[int]] = [[3,7]]

def prime_ladder_next_rung(n: int) -> list[int]:
  right_concats: list[int] = [int(str(n) + str(d)) for d in allowed_digits]
  left_concats: list[int] = [int(str(d) + str(n)) for d in allowed_digits]
  next_rung: list[int] = []

  for rc in right_concats:
    if is_prime(rc):
      next_rung.append(rc)

  for lc in left_concats:
    if is_prime(lc):
      next_rung.append(lc)
  
  return next_rung

def is_right_truncatable_prime(n: int) -> bool:
  prime = str(n)
  num_digits: int = len(prime)
  
  for i in range(1, num_digits):
    if not is_prime(int(prime[:-i])):
      return False
  
  return True

def is_left_truncatable_prime(n: int) -> bool:
  prime = str(n)
  num_digits: int = len(prime)
  
  for i in range(1, num_digits):
    if not is_prime(int(prime[i:])):
      return False
  
  return True

def is_either_truncatable_prime(n: int) -> bool:
  return is_left_truncatable_prime(n) or is_right_truncatable_prime(n)

def is_truncatable_prime(n: int) -> bool:
  return is_left_truncatable_prime(n) and is_right_truncatable_prime(n)

truncatable_primes: list[int] = [23, 53]
current_rung: int = 0
num_truncatable_primes_this_rung: int = 2

while num_truncatable_primes_this_rung > 0:
  next_rung: list[int] = []

  for prime in primes_per_rung[current_rung]:
    next_rung.extend(prime_ladder_next_rung(prime))

  next_rung = list(set(next_rung))
  primes_per_rung.append(next_rung)
  
  truncatable = list(filter(is_left_truncatable_prime,next_rung))
  truncatable_primes.extend(truncatable)
  num_truncatable_primes_this_rung = len(truncatable)

  current_rung += 1

truncatable_primes = list(filter(is_right_truncatable_prime, truncatable_primes))

print(truncatable_primes)
print(f"sum = {sum(truncatable_primes)}")