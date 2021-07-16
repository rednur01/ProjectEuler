# Truncatable primes

### Method ###

# Allowed digits anywhere except the start = [1,3,7,9]
# If the other digits are allowed, such as 2, then during
# right-truncation that digit would eventually be exposed as the last
# digit, and prime numbers cannot end in even digits or 5 or 0
# (Exception: 2 and 5 can be *starting* digits since a right-truncation ending
# in 2 or 5 can still be prime)

# If we start with an N-digit number and truncate once, we have an (N-1) digit
# number left which must be a prime

# We can start by considering all 2-digit primes within this ruleset
# then all 3-digits, and slowly build up a "primes-for-N-digits" ladder

### Optimization ###

# We can build up a right-concatenation-only ladder, which results in primes
# that are already right-truncatable, and we only need to check for left-truncatability

### Domain restriction ###

# Since we're building up a ladder of right-truncatable primes
# and filtering on that list by left-truncatability, if we find a
# rung with no right-truncatable primes then we've found an upper bound

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
primes_per_rung: list[list[int]] = [[2,3,5,7]]

def prime_ladder_next_rung(n: int) -> list[int]:
  right_concats: list[int] = [int(str(n) + str(d)) for d in allowed_digits]
  left_concats: list[int] = [int(str(d) + str(n)) for d in allowed_digits]
  next_rung: list[int] = []

  for rc in right_concats:
    if is_prime(rc):
      next_rung.append(rc)
  
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

truncatable_primes: list[int] = []
current_rung: int = 0
num_primes_last_rung: int = 1

while num_primes_last_rung > 0:
  next_rung: list[int] = []

  for prime in primes_per_rung[current_rung]:
    next_rung.extend(prime_ladder_next_rung(prime))

  next_rung = list(set(next_rung))
  primes_per_rung.append(next_rung)
  
  truncatable = list(filter(is_left_truncatable_prime,next_rung))
  truncatable_primes.extend(truncatable)

  current_rung += 1
  num_primes_last_rung = len(next_rung) #became last rung after increment

print(truncatable_primes)
print(f"sum = {sum(truncatable_primes)}")
