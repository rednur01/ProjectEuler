# Goldbach's other conjecture

# Method
# For every odd composite number,
# run up the list of doubles of squares 2 * [1,4,9,16,25,...]
# for all doubles of squares smaller than the number

# Check if the "addition pair" of the square double is a prime
# If a number is found which has no prime addition pair for all
# square doubles, then that number fails the conjecture

from math import sqrt, ceil

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

i = 9

counterexample: int = 0

while counterexample == 0:
  pair_found = False
  i += 2
  
  if is_prime(i):
    continue

  for sq in range(1,i):
    if pair_found:
      break

    additive_pair: int = i - 2*sq*sq
    if is_prime(additive_pair):
      pair_found = True
  
  if not pair_found:
    counterexample = i

print(counterexample)