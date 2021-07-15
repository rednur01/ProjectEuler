# Distinct powers

terms: set[int] = set()

for a in range(2, 101):
  for b in range(2, 101):
    terms.add(int(a**b))

print(len(terms))