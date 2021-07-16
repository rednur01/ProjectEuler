# Double-base palindromes

def to_binary(n: int) -> str:
  return bin(n).removeprefix("0b")

def is_palindrome(word: str) -> bool:
  for i in range(len(word)//2):
    if word[i] != word[len(word) - i - 1]:
      return False
  return True

palindromes: list[int] = []

for i in range(1,1_000_000):
  if is_palindrome(str(i)) and is_palindrome(to_binary(i)):
    palindromes.append(i)

print(palindromes)
print(f"sum={sum(palindromes)}")