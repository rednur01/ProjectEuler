# Even Fibonacci numbers

limit: int = 4_000_000

pair: list[int, int] = [1, 2]
sum_of_evens: int = 2 # Start with 2 since we'll be moving up the fibonacci ladder

while True:
  next_num: int = pair[0] + pair[1]
  pair = [pair[1], next_num]

  if next_num > limit:
    break

  if next_num % 2 == 0:
    sum_of_evens += next_num
  

print(sum_of_evens)