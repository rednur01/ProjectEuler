# Prime digit replacements

# Prime numbers can only end in 1,3,7,9
# If the ending digit is replaced, the family size would be max 4 (we're looking for 8)

# We"ll start with the lowest number of digits and incrementally
# replace more and more of their digits with rep-digits

# We"ll use notation <D,R> where D = # of digits and R = # of rep-digits
# The example of *3 would be <2,1> and 56**3 would be <5,2> under this notation

# For <3,1>, we have the numbers **1 | **3 | **7 | **9
# For <3,2>, we have 1*1, 2*1 ... 9*1, 1*3, ... 9*3, ... 9*9
# and also *01, *21, ...*91, *13, *23, ...*99

# If we exclude the last digit then we have 1*, 2*, ... 9*, *0, *1, *2, ... *9
# which is all permutations of the characters

# We can then append back the last digit and swap out the wildcard for each rep-digit
# combination possible and check for primality

# We"ll use the notation d = D - 1
# and E<d,r> where E = ending digit

# The given examples according to this notation:
# *3 = 3<1,1>
# 56**3 = 3<4,2>

from itertools import product
from math import ceil, sqrt

end_digits: list[str] = ["1", "3", "7", "9"]
all_digits: list[str] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "*"]
wildcard = "*"

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

def digit_rep_combos(digits: int, reps: int) -> list[str]:
  assert digits >= reps

  all_combos_of_digit_size = product(all_digits, repeat=digits)
  correct_wildcard_no = filter(lambda elem: elem.count(wildcard) == reps, all_combos_of_digit_size)
  stringified = map(lambda elem: "".join(elem), correct_wildcard_no)

  return list(stringified)

def fill_wildcard(stringified: str, digit: int) -> str:
  return stringified.replace(wildcard, str(digit))


def search():
  longest_prime_family: list[int] = []
  looking_for_family_size: int = 8

  for d in range(1,12+1):
    for r in range(1,d+1):
      for end_digit in end_digits:
        combos = digit_rep_combos(d,r)

        for combo in combos:
          primes_this_family: list[int] = []
          combo_family: str = f"{combo}{end_digit}"
          
          for i in range(10):
            rep_digit_number = fill_wildcard(combo, i) + end_digit
            if rep_digit_number[0] != "0" and is_prime(int(rep_digit_number)):
              primes_this_family.append(rep_digit_number)
          
          if len(primes_this_family) > len(longest_prime_family):
            longest_prime_family = primes_this_family
            print(f"{combo_family} = {len(primes_this_family)} : {primes_this_family}")

            if len(primes_this_family) == looking_for_family_size:
              return          


search()