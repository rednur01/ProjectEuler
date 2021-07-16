# Digit cancelling fractions

# Euclid's algorithm
def gcd(a: int, b: int) -> int:
  if b > a:
    a, b = b, a
  if b == 0:
    return a
  else:
    return gcd(b, a % b)

class Fraction:
  def __init__(self, numerator: int, denominator: int) -> None:
    self.numerator = numerator
    self.denominator = denominator
  
  def __repr__(self) -> str:
    return f"{self.numerator}/{self.denominator}"

  def reduced(self) -> 'Fraction':
    factor: int = gcd(self.numerator, self.denominator)
    return Fraction(self.numerator//factor, self.denominator//factor)
  
  def __eq__(self, other: 'Fraction') -> bool:
    return (
      self.numerator == other.numerator and 
      self.denominator == other.denominator)
  
  def __mul__(self, other: 'Fraction') -> 'Fraction':
    numerator: int = self.numerator * other.numerator
    denominator: int = self.denominator * other.denominator
    return Fraction(numerator, denominator)

def common_digits_in_numerator_denominator(fraction: Fraction) -> list[str]:
  return [char for char in str(fraction.numerator) if char in str(fraction.denominator)]

def remove_digit(number: int, digit: int):
  pass

digit_cancelling_fractions: list[Fraction] = []

for numerator in range(10,100):
  for denominator in range(numerator, 100):
    fraction = Fraction(numerator, denominator)
    common_digits: list[str] = common_digits_in_numerator_denominator(fraction)
    common_digits = filter(lambda d: d != '0', common_digits)
    
    for digit in set(common_digits):
      digit_cancelled_numerator = int(str(fraction.numerator).replace(digit, '', 1)) # only remove 1 instance of digit in case of duplicate
      digit_cancelled_denominator = int(str(fraction.denominator).replace(digit, '', 1))
      
      if (digit_cancelled_numerator != 0 and digit_cancelled_numerator != 0):
        digit_cancelled_fraction = Fraction(digit_cancelled_numerator, digit_cancelled_denominator)

        if (fraction.reduced() == digit_cancelled_fraction.reduced() and
            fraction.reduced().denominator != 1 and
            digit_cancelled_fraction.reduced().denominator != 1):
          digit_cancelling_fractions.append(fraction)


product = Fraction(1,1)
for fraction in digit_cancelling_fractions:
  product *= fraction

print(digit_cancelling_fractions)
print(product.reduced())