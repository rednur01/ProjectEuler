# 1000-digit Fibonacci number

# Keep memory of two fibonacci numbers [a, b]
a: int = 1
b: int = 1
fib_index = 2

target_digit_count: int = 1_000

# Start going up fibonacci ladder
while True:
  a, b = b, a + b
  fib_index += 1

  if len(str(b)) >= target_digit_count:
    print(fib_index)
    break