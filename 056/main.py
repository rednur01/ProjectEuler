# Powerful digit sum

def digit_sum(n: int) -> int:
  return sum(int(char) for char in str(n))

highest: int = 0

for a in range(2,100):
  for b in range(2,100):
    ds: int = digit_sum(int(a**b))
    if ds > highest:
      highest = ds

print(highest)