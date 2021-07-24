# XOR decryption

# Remove 059/ if running from inside the 059 folder
filename: str = "059/cipher.txt"

open_file = open(filename, 'r')
file_data = open_file.read()
open_file.close()

encrypted_letters = list(map(lambda elem: int(elem), file_data.split(",")))

def word_to_ascii(word: str) -> list[int]:
  return [ord(letter) for letter in word]

def ascii_to_english(ascii: list[int]) -> str:
  return "".join([chr(num) for num in ascii])

def decrypt(encrypted: list[int], key: list[int]) -> list[int]:
  decrypted_sequence: list[int] = []
  
  for index, letter in enumerate(encrypted):
    decrypted_letter: int = letter ^ key[index % len(key)]
    decrypted_sequence.append(decrypted_letter)
  
  return decrypted_sequence

common_words_3 = ["the", "and", "that"]

ascii_lowercase_range = range(97,123)

# Try all keys and look for common words
def find_decrypted_text():
  for key_letter_1 in ascii_lowercase_range:
    for key_letter_2 in ascii_lowercase_range:
      for key_letter_3 in ascii_lowercase_range:
        key: list[int] = [key_letter_1, key_letter_2, key_letter_3]
        decrypted_ascii: list[int] = decrypt(encrypted_letters, key)
        decrypted: str = ascii_to_english(decrypted_ascii)
        
        all_common_words_present = (common_words_3[0] in decrypted and
                                    common_words_3[1] in decrypted and
                                    common_words_3[2] in decrypted)

        if all_common_words_present:
          print(decrypted)
          print(sum(decrypted_ascii))
          return

find_decrypted_text()