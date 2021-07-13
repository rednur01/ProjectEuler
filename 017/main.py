# Number letter counts

### Method ###
# Directly work with the spelling lengths instead of spelling it out
# Example: 342 -> 'three' 'hundred' 'and' 'forty' 'two'
# Directly count 5 + 7 + 3 + 5 + 3 = 23

spelling_length: dict[int, int] = {
  1: 3,
  2: 3,
  3: 5,
  4: 4,
  5: 4,
  6: 3,
  7: 5,
  8: 5,
  9: 4,
  10: 3,
  11: 6,
  12: 6,
  13: 8,
  14: 8,
  15: 7,
  16: 7,
  17: 9,
  18: 8,
  19: 8,
  20: 6,
  30: 6,
  40: 5,
  50: 5,
  60: 5,
  70: 7,
  80: 6,
  90: 6
}

def spell_count(n: int) -> int:
  if n <= 20:
    return spelling_length[n]

  elif n > 20 and n < 100:
    ones: int = n % 10
    tens: int = n - ones

    if ones == 0:
      return spelling_length[tens]
    else:
      return spelling_length[tens] + spelling_length[ones]
  
  elif n >= 100 and n < 1000:
    tens_ones: int = n % 100
    hundreds_digit: int = n // 100
  
    hundreds_count = spelling_length[hundreds_digit] + 7 # 'hundred'
    if tens_ones != 0:
      hundreds_count += spell_count(tens_ones) + 3 # 'and'
    return hundreds_count

  elif n == 1000:
    return 11 # 'one thousand'
  else:
    return 0

total: int = 0

for n in range(1, 1001):
  total += spell_count(n)

print(total)