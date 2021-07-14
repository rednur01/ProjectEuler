# Lexicographic permutations

### Method ###

# Example: 1,2,3,4
# Total permutations = 4!
# Each digit as leading = 4!/4 = 3! = 6

# So, in lexicographic order:
# 1 leads first 6 permutations, 2 leads seconds 6, and so on

# Therefore if asked to find the N-th permutation
# we easily know the leading digit
# For example, the 15th permutation in this example must have 3 leading

# And since 3 starts leading from the 13th onwards
# the 15th permutation must be the 3rd permutation with 3 leading
# and {0,1,4} as the remaining digits

# Then we recursively find the 3rd permutation of {0,1,4} and build up the digits
# until we find the full sequence

def factorial(n: int) -> int:
  return 1 if n <= 1 else n * factorial(n - 1)

def nth_permutation(digits: list[int], n: int) -> str:
  assert n <= factorial(len(digits)) - 1

  if len(digits) == 1:
    return str(digits[0])

  digits.sort()
  each_digit_lead_count: int = factorial(len(digits) - 1)
  leading_digit: int = digits[n // each_digit_lead_count]
  inner_permutation_count: int = n % each_digit_lead_count
  inner_permutation_digits = list(filter(lambda d: d != leading_digit, digits))

  return str(leading_digit) + nth_permutation(inner_permutation_digits, inner_permutation_count)

digits: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n: int = 1_000_000

print(nth_permutation(digits, n-1))