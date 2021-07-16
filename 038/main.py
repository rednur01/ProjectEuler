# Pandigital multiples

# Domain restriction
# Since the pandigital number is 9-digits and the smallest
# multiplier set n allowed is {1,2}
# the largest number which can form the pandigit from its multiples
# must be 4-digit or less
# Since a 5-digit number N cannot concatenate N and 2N to form a 9-digit number

def is_pandigital(a: str):
  digits: list[str] = [char for char in a]
  unique_digits: set[str] = set(digits)
  
  return (
    '0' not in unique_digits
    and len(digits) == len(unique_digits) # no duplicates
    and len(unique_digits) == 9 # has all 9 digits
  )

limit: int = 10_000
largest: int = 0

for i in range(1, limit):
  products_concatenated: str = ""
  
  for n in range(1, 10):
    products_concatenated += str(i * n)
    if len(products_concatenated) >= 9:
      break
  
  if is_pandigital(products_concatenated):
    if int(products_concatenated) > largest:
      largest = int(products_concatenated)

print(largest)