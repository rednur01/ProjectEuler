# Factorial digit sum

n: int = 100

def factorial(n: int) -> int:
  if n <= 1:
    return 1
  else:
    return n * factorial(n-1)

digits: list[int] = [int(char) for char in str(factorial(n))]
print(sum(digits))