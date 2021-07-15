# Quadratic primes

# We can find some bounds on n, a and b
# to restrict the domain of the problem


### b bounds ###

# since n starts at 0, the first prime of the sequence must be
# 0^2 + 0*a + b = b
# Therefore b must be prime
# 2 < b < 1000


### a bounds ###

# [N^2 + aN] + [b] 
#  ^^^^^^^      ^
#   gaps       prime
#  between    constant
#  primes

# Since N^2 + aN are gaps between primes, and all primes
# are of the form 6k+1 or 6k+5, gaps between primes must always be
# gaps between these forms
# Which turn out to be 4 mod 6, 2 mod 6, or 0 mod 6
# which are all even numbers

# So (N^2 + aN) = N(N+a) must be even
# If N even, this expression is even for all a
# If N odd, then a must be odd for the expression to be even
# Therefore a must be odd


### n bounds ###

# n starts at 0 and increments by 1
# As we generate the next number, we can check if it's prime
# and only increment n if a prime was produced

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

def expression(n: int, a: int, b: int) -> int:
  return n*n + a*n + b

a_range = range(-999, 1000 , 2)
b_values: list[int] = [b for b in range(2, 1000) if isPrime(b)]

largest_sequence: list[int] = []
best_a: int = 0
best_b: int = 0

for b in b_values:
  for a in a_range:
    
    seq: list[int] = []

    n: int = 0
    nth_term: int = expression(n, a, b)
    
    while isPrime(nth_term):
      seq.append(nth_term)
      n += 1
      nth_term = expression(n, a, b)
    
    if len(seq) > len(largest_sequence):
      largest_sequence = seq
      best_a = a
      best_b = b


a = best_a
b = best_b
print(f"{a=}, {b=} : n^2 + {a}n + {b} : {len(largest_sequence)} consecutive primes")
print(f"a * b = {a*b}")