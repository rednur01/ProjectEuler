# Powerful digit counts

# Method
# For n > 10, the number of digits always exceeds
# the power of n
# Only check 1 through 10, and stop when then number of digits
# deviates too far from the power (indicating divergence)

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