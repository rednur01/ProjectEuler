# Lychrel numbers

def reverse(n: int) -> int:
  return int(str(n)[::-1])

def is_palindrome(n: int) -> bool:
  return str(n) == str(n)[::-1]

def is_Lychrel(n: int, max_iters: int = 50) -> bool:
  next_n: int = n
  
  for i in range(max_iters):
    next_n = next_n + reverse(next_n)
    if is_palindrome(next_n):
      return False
  return True


limit: int = 10_000
num_Lychrels: int = 0

for n in range(10, limit):
  if is_Lychrel(n):
    num_Lychrels += 1
    print(n)

print(num_Lychrels)