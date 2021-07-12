# Sum square difference

# Sum of numbers 1 to n
# Gauss method: n * (n+1) / 2

# Sum of square numbers 1 to n
# n * (n + 1) * (2n + 1) / 6

def square_of_sum(n: int) -> int:
  return int((n * (n + 1) / 2) ** 2)

def sum_of_squares(n: int) -> int:
  return n * (n + 1) * (2 * n + 1) // 6

print(square_of_sum(100) - sum_of_squares(100))