# Powerful digit counts

matching_numbers: list[str] = []

for n in range(1, 10):
  power = 1
  
  while True:
    num_digits = len(str(n ** power))
    
    if num_digits == power:
      matching_numbers.append(f"{n} ** {power}")
    elif num_digits > power:
      break
    elif abs(num_digits - power) > 5:
      break

    power += 1

print(len(matching_numbers))
print(matching_numbers)