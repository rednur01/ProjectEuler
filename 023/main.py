# Non-abundant sums

def divisor_sum(n: int) -> list[int]:
  total: int = 1 # 1 is divisor

  for i in range(2, n//2 + 1):
    if n % i == 0:
      total += i
  
  return total

def sum_all_ints(n: int) -> int:
  return n * (n + 1) // 2

limit: int = 28_123

abundant_numbers: list[int] = []
abundant_decomposable: list[int] = []

# Make list of all abundant numbers
# In the same pass, check if any number
# is "abundant decomposable" among the abundants already known
# (since decompositions must be smaller)
for n in range(1, limit+1):
  if divisor_sum(n) > n:
    abundant_numbers.append(n)

  for abundant in abundant_numbers:
    abundant_pair: int = n - abundant
    if abundant_pair != n and abundant_pair in abundant_numbers:
      abundant_decomposable.append(n)
      break

sum_non_decomposable: int = sum_all_ints(limit) - sum(abundant_decomposable)
print(sum_non_decomposable)