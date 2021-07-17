# Sub-string divisibility

from itertools import permutations

perm = permutations('0123456789', 10)
nums = map(lambda p: "".join(p), perm)

primes: list[int] = [2,3,5,7,11,13,17]

valid_nums: list[int] = []

for num in nums:
  is_valid: bool = True
  
  for i in range(1,8):
    substring = num[i:i+3]

    if int(substring) % primes[i-1] != 0:
      is_valid = False
      break
  
  if is_valid:
    valid_nums.append(int(num))
    print(num)

print("sum=", sum(valid_nums))