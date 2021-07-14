# Amicable numbers

divisor_sum_table: dict[int, int] = {}

def divisor_sum(n: int) -> list[int]:
  total: int = 1 # 1 is divisor

  for i in range(2, n//2 + 1):
    if n % i == 0:
      total += i
  
  return total

# Build table
limit: int = 10_000

for n in range(1, limit):
  divisor_sum_table[n] = divisor_sum(n)

amicable_pairs_sum: int = 0

for num in range(1, limit):
  pair: int = divisor_sum_table[num]
  if pair != num and pair in divisor_sum_table and divisor_sum_table[pair] == num:
    amicable_pairs_sum += num
    # Only add num rather than num + pair
    # since the pair number will also get looped over
    # and counted then

print(amicable_pairs_sum)