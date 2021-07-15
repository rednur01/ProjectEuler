# Coin sums

# Given an integer N and a set of coins {c1, c2, ...}
# How do we find how many ways we can combine coins to add upto N

# Example:
# How many ways can we make 20 using coins {5,2}
# Notation for convenience: 20 >> {5,2}

# If we use at least one 5, then we're asking how many ways
# can we make the remaining 15 using coins {5,2}
# Similarly if we use at least one 2, then we need to know 
# how many ways to make the remaining 18 using coins {5,2}
# BUT this would allow repeat combos using 5
# so we remove the highest coins at each step

# 20 >> {5,2} = 15 >> {5,2} + 18 >> {2}

# Useful observations

# CASE 1: n >> {c}
# If n is a multiple of c, then only 1 way to add up coin c 
# n >> {c} = 1
# If n is not a multiple of c, then no way to add up c's to get n
# n >> {c} = 0

# CASE 2: N >> {c1,...} = 1 if N == 0
# No way to add up to 0
# but since 0 was obtained due to the subtraction of a coin
# that subtraction has to be counted
# Example: 5 >> {5} = 0 >> {5}
# 0 was obtained by subtracting 5 once so 1 way to make this combo

# CASE 3: N >> {c1, ...} = 0 if N < 0
# No way to get to a negative value
# and unlike 0 this subtraction cannot be counted since 
# the subtraction that got here didn't divide evenly

def num_additive_combos(num: int, coins: list[int]) -> int:

  if len(coins) == 1:
    if num % coins[0] == 0:
      return 1
    else:
      return 0
  elif num == 0:
    return 1
  elif num < 0:
    return 0
  
  total: int = 0

  for i in range(len(coins)):
    subset = coins[i:]
    remaining = num - coins[i]
    total += num_additive_combos(remaining, subset)
  
  return total

num: int = 200
coins: list[int] =  [200,100,50,20,10,5,2,1]

total = num_additive_combos(num, coins)

print(f"{num} >> {coins} = {total}")