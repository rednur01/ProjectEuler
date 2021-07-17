# Integer right triangles

### Domain restriction ###

# Inscribe the right-triangle in a half-cirle
# the hypotenuse H becomes the diameter
# The perimeter of this half-circle is always bigger
# than the perimeter of the inscribed right-triangle

# Perimeter of half-circle
# = H + pi*(H/2)
# = H * (1 + pi/2)

# Let triangle sides be A, B, H
# A+B+H = 1000 and
# A+B+H < H * (1+pi/2)
# H * (1+pi/2) > 1000
# H > 1000 / (1+pi/2)
# H > 388.98

# Since A+B+H = 1000 and H > 388.98
# A+B < 1000 - 388.98
# A+B < 611.02

# General formula for perimeter P
# A+B < P-H : H = P / (1+pi/2)

# Perimeter of right triangle is always even 
# From a^2 + b^2 = c^2
# If a and b are both even or both odd, then c is even and perimeter is even
# If a and b are one even one odd, then c will be odd and perimeter is even 

from math import sqrt, floor, ceil

def max_hypotenuse(perimeter: int) -> float:
  return perimeter / (1 + 3.14/2)

def side_upper_bound(perimeter: int) -> int:
  return perimeter - int(max_hypotenuse(perimeter))

def are_right_angle_sides(a: int, b: int, c:int) -> bool:
  c_sq: int = a**2 + b**2
  c: float = sqrt(c_sq)
  return True if ceil(c) == floor(c) else False # if c in an integer

def find_num_right_triangles_at_perimeter(perimeter: int):
  found: int = 0
  
  for a in range(2, side_upper_bound(perimeter)+1):
    for b in range(1,a):
      c_sq: int = a**2 + b**2
      c: float = sqrt(c_sq)
      
      if ceil(c) == floor(c) and a+b+c == perimeter:
        c = int(c)
        found += 1
  
  return found

highest_right_triangles_found: int = 0

for perimeter in range(20, 1001, 2):
  num_right_triangles = find_num_right_triangles_at_perimeter(perimeter)
  if num_right_triangles > highest_right_triangles_found:
    highest_right_triangles_found = num_right_triangles
    print(f"{num_right_triangles} at {perimeter=}")
