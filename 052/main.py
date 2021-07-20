# Permuted multiples

def is_permutation(original: int, other: int) -> bool:
  og_digits: list[str] = [digit for digit in str(original)]
  other_digits: list[str] = [digit for digit in str(other)]

  is_same_length = len(og_digits) == len(other_digits)
  have_same_digits = set(og_digits) == set(other_digits)

  return is_same_length and have_same_digits

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