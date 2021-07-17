# Champernowne's constant

# Method
# Start at n=1 and increment by 1 
# and keep track of how many digits are going by
# when the desired digit number is reached, store the
# digit at that index

d_to_check: list[int] = [1,10,100,1_000,10_000,100_000,1_000_000]
d_indices: dict[int, int] = {}

n : int = 1
d: int = 1

while len(d_to_check) > 0:
  n_str = str(n)
  num_digits: int = len(n_str)

  next_d_to_check = d_to_check[0]
  d_after_this_step = d + num_digits

  if d_after_this_step > next_d_to_check:
    position_to_check = next_d_to_check - d
    digit: str = n_str[position_to_check]
    
    d_indices[next_d_to_check] = int(digit)
    d_to_check = d_to_check[1:]

  d += num_digits
  n += 1


product: int = 1
for key in d_indices:
  product *= d_indices[key]

print(d_indices)
print(product)