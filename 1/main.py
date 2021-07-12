# Multiples of 3 and 5

### Analytical Approach ###

# In every block of 15 numbers, the multiples of 3 and 5 are
# 15k
# 15k + 3
# 15k + 5
# 15k + 6
# 15k + 9
# 15k + 10
# 15k + 12

# The sum of these multiples M = 105k + 45

# Let 15n + r = 1000
# and 
# M = 105k + 45 ; sum for k=0 to k=n-1
# R = [15nk, 15nk + 3, ... 15nk + 12] ; filter down to the numbers < 1000 and sum

# Sum = M + R

### Analytical approach code ###
# n: int = 1000 // 15
# r: int = 1000 % 15

# M: int = 0
# for k in range(n):
#   M += 105 * k + 45

# remaining_nums: list[int] = [15*n, 15*n + 3, 15*n + 5, 15*n + 6, 15*n + 9, 15*n + 10, 15*n + 12]
# R: int = sum(list(filter(lambda num: num < 1000, remaining_nums)))

# total: int = M + R
# print(total)



### Brute force approach ###
limit: int = 1000
total: int = 0

for i in range(limit):
  if i % 3 == 0 or i % 5 == 0:
    total += i

print(total)