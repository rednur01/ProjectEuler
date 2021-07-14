# Names scores

# Remove 022/ if running from inside the 022 folder
filename: str = "022/names.txt"

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

def alphabetical_value(name: str) -> int:
  return sum([letter_values[char] for char in name])

names: list[str] = file_data.split(",")
names = list(map(lambda n: n.replace('"', "").replace("'", ""), names))
names.sort()

ordered_names: dict[int, str] = {}

for index, name in enumerate(names):
  ordered_names[index+1] = alphabetical_value(name)

total_sum: int = 0

for index in ordered_names:
  total_sum += index * ordered_names[index]

print(total_sum)