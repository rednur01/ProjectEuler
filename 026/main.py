# Reciprocal cycles

### Method ###

# Example: 1/7 = (142857)...
# Create 2 adjacent windows and check for equality
# Window size 1 = [1][4]2857142..
# Window size 2 = [14][28]57142...
# Window size 6 = [142857][142857]... = match

# Since decimal places are limited and inaccurate I multiplied the number
# by a large power of 10 to shift to the left of the decimal
# Sometimes there are "extra" digits before the repeat sequence that could
# disrupt the search, so some digits at the start were thrown out

# Decide on a suitable maximum size for the check window
# The size of the repeating decimal cannot exceed N in 1/N so that's the maximum
# (since the repeating demical must evenly divide into 10^N - 1)

limit: int = 1_000
max_check_length: int = limit
junk_clearance: int = 10
big_ten_power: int = 10**(2*max_check_length+junk_clearance)


def rep_sequence(n: str, check_length_limit: int) -> str:
  n = n[10:] # Remove some starting digits, often masks pattern

  for check_length in range(1, check_length_limit+1):
    window_1: str = n[:check_length]
    window_2: str = n[check_length: 2*check_length]
    if window_1 == window_2:
      return window_1
  
  return ""

highest_rep_found: str = ""

for n in range(2, limit+1):
  r = rep_sequence(str(big_ten_power//n), n)
  if r != "":
    if len(r) > len(highest_rep_found):
      highest_rep_found = r
      print(f"{n=}, size={len(r)}")