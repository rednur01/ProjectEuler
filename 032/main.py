# Pandigital products

# Since the total number of digits must equal 9 (by definition)
# the sum of digits of the 3 terms A * B = C must equal 9

# This rules out most combinations of A * B where the total digit count of 9
# does not fall within the multiplication range

# Example: if A is 2-digit and B is 5-digit then C has to be 2-digit
# But a multiple of a 2-digit and a 5-digit number cannot be 2-digit
# Similarly if A and B are both 1-digit, then C has be 7-digit
# but the highest product AB can be 9*9 = 81 = 2-digit

# Using this check, only the following digit combinations are found to be valid
# 1-digit * 4-digit
# 2-digit * 3-digit

def is_pandigital(a: int, b: int, c: int):
  joined: str = str(a) + str(b) + str(c)
  digits: list[int] = [int(char) for char in joined]
  unique_digits: set[int] = set(digits)
  
  return (
    0 not in unique_digits
    and len(digits) == len(unique_digits) # no duplicates in original
    and len(unique_digits) == 9 # has all 9 digits
  )
  
range_1_digit = range(0,10)
range_2_digit = range(10,100)
range_3_digit = range(100,1_000)
range_4_digit = range(1_000,10_000)

pandigital_identities: list[tuple[int, int, int]] = []

for a in range_1_digit:
  for b in range_4_digit:
    c: int = a * b
    if is_pandigital(a,b,c):
      pandigital_identities.append((a,b,c))

for a in range_2_digit:
  for b in range_3_digit:
    c: int = a * b
    if is_pandigital(a,b,c):
      pandigital_identities.append((a,b,c))


products: list[int] = list(map(lambda t: t[2], pandigital_identities))

print(pandigital_identities)
print(sum(set(products)))