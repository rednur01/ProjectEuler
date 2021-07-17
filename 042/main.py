# Coded triangle numbers

# Remove 042/ if running from inside the 042 folder
filename: str = "042/words.txt"

open_file = open(filename, 'r')
file_data = open_file.read()
open_file.close()

letter_values: dict[str, int] = {
  'A': 1,
  'B': 2,
  'C': 3,
  'D': 4,
  'E': 5,
  'F': 6,
  'G': 7,
  'H': 8,
  'I': 9,
  'J': 10,
  'K': 11,
  'L': 12,
  'M': 13,
  'N': 14,
  'O': 15,
  'P': 16,
  'Q': 17,
  'R': 18,
  'S': 19,
  'T': 20,
  'U': 21,
  'V': 22,
  'W': 23,
  'X': 24,
  'Y': 25,
  'Z': 26,
}

# First 1000
triangle_numbers: list[int] = []

for n in range(1, 1001):
  triangle_number: int = int(0.5 * n * n+1)
  triangle_numbers.append(triangle_number)

def is_triangle_number(n: int) -> bool:
  return n in triangle_numbers

def alphabetical_value(word: str) -> int:
  return sum(letter_values[char] for char in word)

words: list[str] = file_data.split(",")
words = list(map(lambda n: n.replace('"', "").replace("'", ""), words))
word_values = list(map(alphabetical_value, words))

num_triangle_words: int = 0

for value in word_values:
  if is_triangle_number(value):
    num_triangle_words += 1

print(num_triangle_words)
