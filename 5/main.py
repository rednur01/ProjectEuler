# Smallest multiple

# The multiple of all the numbers in the range = 1 * 2 * 3 ... * 20
# This isn't the smallest since prime factors are repeated
# For even divisibility we only need to account for the higest prime power
# Smaller prime powers are automatically divisible
# example: anything divisible by 16 (2^4) is also divisible by 8 (2^3) for free

# primes = 2, 3, 5, 7, 11, 13, 17, 19

# non-prime
# 4 = 2^2
# 6 = 2 * 3
# 8 = 2^3
# 9 = 3^2
# 10 = 2 * 5
# 12 = 2^2 * 3
# 14 = 2 * 7
# 15 = 3 * 5
# 16 = 2^4
# 18 = 2 * 3^2
# 20 = 2^2 * 5

N: int = 2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19
print(N)