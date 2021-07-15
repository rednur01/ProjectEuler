# Digit fifth powers

# For a number with n digits, the *maximum* sum of its 
# digits' 5th powers would be when the number is all 9s

# 3-digit: 999 = 9^5 + 9^5 + 9^5 = 3 * 9^5
# n-digit = n * 9^5

# so if this expression is smaller than the smallest n-digit number
# that means there would be no way to sum the fifth powers of those
# digits to get an n-digit number

# 5 * 9^5 = 295 245
# 6 * 9^5 = 354 294
# 7 * 9^5 = 413 343 (!!)

# Even the highest 7-digit number 9,999,999 cannot have its digits' 5th powers
# add up to 1_000_000, the smallest 7 digit number
# So only upto 6-digit numbers have this property
# Max number to check: 999 999

def digits(number: int) -> int:
  return [int(char) for char in str(number)]

def sum_of_digit_nth_powers(digits: list[int], power: int) -> int:
  digit_powers = map(lambda d: int(d**power), digits)
  return sum(digit_powers)

valid_numbers: list[int] = []

for n in range(10, 1_000_000):
  if n == sum_of_digit_nth_powers(digits(n), 5):
    valid_numbers.append(n)

print(valid_numbers)
print(f"sum={sum(valid_numbers)}")