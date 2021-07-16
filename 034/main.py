# Digit factorials

# 8-digit numbers cannot have this property since the
# highest 8-digit number 99_999_999 has factorial sum = 8*9! = 2_903_040
# which is 7-digits

# Largest 7-digit number has factorial sum = 7*9! = 2_540_160
# So only check upto this number

# Use a factorial table for fast lookup
factorial: dict[int, int] = {
  0: 1,
  1: 1,
  2: 2,
  3: 6,
  4: 24,
  5: 120,
  6: 720,
  7: 5_040,
  8: 40_320,
  9: 362_880,
}

def sum_of_digit_factorials(n: int) -> int:
  return sum([factorial[int(char)] for char in str(n)])

total: int = 0
upper_bound: int = 2_540_160

for i in range(10,upper_bound+1):
  if i == sum_of_digit_factorials(i):
    total += i
    print(i)

print(f"{total=}")