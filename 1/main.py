# Multiples of 3 and 5

### Brute force approach ###
limit: int = 1000
total: int = sum([n for n in range(limit) if n % 3 == 0 or n % 5 == 0])
print(total)