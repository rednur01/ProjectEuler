# Permuted multiples

def is_permutation(first: int, second: int) -> bool:
  first_digits: list[str] = [digit for digit in str(first)]
  second_digits: list[str] = [digit for digit in str(second)]

  for digit in first_digits:
    if first_digits.count(digit) != second_digits.count(digit):
      return False

  return len(first_digits) == len(second_digits)

for x in range(100, 1_000_000_000):
  multiples = [x*2, x*3, x*4, x*5, x*6]

  all_are_permutations = True
  for multiple in multiples:
    if not is_permutation(x, multiple):
      all_are_permutations = False
      break
  
  if all_are_permutations:
    print(x, multiples)
    break