# Largest palindrome product

# Smallest number in range
# 100 * 100 = 100_000

# Largest number in range
# 999 * 999 = (1000-1) * (1000-1) = 1_000_000 - 2000 + 1 = 998_001

# All palindromes must be 6-digits in this range
# Since the number must be symmetric for the first 3-digits and the last 3-digits
# we can construct them by taking all 3-digit numbers, then reflecting and concatenating them

# Example: 326 -> [326, 623] -> 326_000 + 623 -> 326_623

# The largest palindrome constructible in this range is 997_799
# and the smallest is 101_101

def is_3_digit_number(n: int) -> bool:
  return n >= 100 and n <= 999

def has_factor(N: int, f: int) -> bool:
  if N % f == 0:
    return True
  else:
    return False

def construct_palindrome(n: int) -> int:
  first_3: int = n
  flipped: str = str(n)[::-1]
  last_3: int = int(flipped)
  return 1000 * first_3 + last_3

found: bool = False

for i in range(997,100,-1):
  palindrome: int = construct_palindrome(i)
  
  for f in range(999, 100, -1):
    if has_factor(palindrome, f) and is_3_digit_number(palindrome // f):
      print(f"{palindrome} = {f} * {palindrome//f}")
      found = True
      break
  
  if found:
    break