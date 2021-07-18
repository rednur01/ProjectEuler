# Consecutive prime sum

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

primes: list[int] = [i for i in range(2, 1_000_000) if is_prime(i)]

longest_window: list[int] = []
check_length: int = 21

for window_index in range(len(primes) - check_length - 1):
  for window_length in range(check_length, len(primes) - window_index):
    window = primes[window_index: window_index+window_length]
    window_sum = sum(window)
    
    if window_sum > 1_000_000:
      break
    elif window_sum in primes and len(window) > len(longest_window):
      longest_window = window
      check_length = len(longest_window)
      print(len(longest_window), sum(window))