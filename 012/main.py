# Highly divisible triangular number

# Example to demonstrate method: 300 -> 2^2 * 3 * 5^2
# From prime factors, all divisors can be found as the terms in this sum:
# (2^0 + 2^1 + 2^2) * (3^0 + 3^1) * (5^0 + 5^1 + 5^2)
# Since there will be 3*2*3=18 terms in this sum, 300 has 18 divisors

# Method
# 1. Find all prime factors
# 2. List the highest power of each factor (and add 1)
# 3. Multiply these numbers to find the total number of divisors

def triangleNumber(n: int) -> int:
  return int(n * (n + 1) / 2)

def prime_factors(n: int) -> list[int]:
  factors: list[int] = []

  i: int = 2
  while i <= n and n > 1:
    if n % i == 0:
      factors.append(i)
      n /= i
      i = 2
    else:
      i += 1
  
  return factors

def list_product(l: list[int]) -> int:
  product: int = 1
  for number in l:
    product *= number
  return product

def num_factors(all_prime_factors: list[int]) -> int:
  factors: set[int] = set([1])

  for i in range(len(all_prime_factors)):
    factors.add(all_prime_factors[i])
    for j in range(i+1, len(all_prime_factors)):
      factors.add(list_product(all_prime_factors[i:j+1]))
  
  return len(factors)

def list_factor_highest_powers(all_prime_factors: list[int]) -> list[int]:
  if len(all_prime_factors) == 1:
    return [1]

  powers: list[int] = []

  last_factor_seen: int = all_prime_factors[1]
  last_factor_count: int = 1

  for i, factor in enumerate(all_prime_factors[1:]):
    if factor == last_factor_seen:
      last_factor_count += 1
    else:
      powers.append(last_factor_count)
      last_factor_seen = factor
      last_factor_count = 1

    if i == len(all_prime_factors[1:]) - 1:
      powers.append(last_factor_count) 

  return powers

def divisor_count_from_factor_powers(factor_powers: list[int]) -> int:
  factor_powers_augmented: list[int] = map(lambda n: n+1, factor_powers)
  divisor_count: int = list_product(factor_powers_augmented)
  return divisor_count

n: int = 2
max_divisors: int = 1

while max_divisors <= 500:
  triangle: int = triangleNumber(n)
  divisors: int = divisor_count_from_factor_powers(list_factor_highest_powers(prime_factors(triangle)))
  
  if divisors > max_divisors:
    max_divisors = divisors
    print(f"Triangle #{n}: {triangle} has {max_divisors} divisors")
  
  n += 1