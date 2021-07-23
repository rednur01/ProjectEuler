# Poker hands

# Remove 054/ if running from inside the 054 folder
filename: str = "054/poker.txt"

open_file = open(filename, 'r')
file_data = open_file.read()
open_file.close()

# Logic

rank_value: dict[str, int] = {
  "2": 2,
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9,
  "T": 10,
  "J": 11,
  "Q": 12,
  "K": 13,
  "A": 14
}

hand_ranks: dict[str, int] = {
  "Royal flush":      10,
  "Straight flush":   9,
  "Four of a kind":   8,
  "Full house":       7,
  "Flush":            6,
  "Straight":         5,
  "Three of a kind":  4,
  "Two pair":         3,
  "One pair":         2,
  "High card":        1,
}

class Card:
  def __init__(self, raw: str) -> None:
    self.rank = rank_value[raw[:-1]]
    self.suit = raw[-1]
  
  def __repr__(self) -> str:
    return f"{self.rank}{self.suit}"

class Hand:
  def __init__(self, cards: list[Card]) -> None:
    self.cards = cards
    self.rank: str
    self.rank_resolver: list[int] = []

    self.__rate()
    self.__find_rank_resolver()
  

  def __repr__(self) -> str:
    return self.rating

  def count_rank_frequency(self) -> dict[int,int]:
    counts: dict[int,int] = {}
    ranks = list(map(lambda card: card.rank, self.cards))
    for rank in ranks:
      if rank not in counts:
        counts[rank] = ranks.count(rank)
    return counts

  def is_royal_flush(self) -> bool:
    ranks = map(lambda card: card.rank, self.cards)
    lowest = min(ranks)
    return self.is_straight_flush() and lowest == rank_value["T"]

  def is_straight_flush(self) -> bool:
    return self.is_straight() and self.is_flush()

  def is_4_of_a_kind(self) -> bool:
    rank_counts: dict[int,int] = self.count_rank_frequency()
    return max(rank_counts.values()) == 4

  def is_full_house(self) -> bool:
    rank_counts: dict[int,int] = self.count_rank_frequency()
    return 2 in rank_counts.values() and 3 in rank_counts.values()

  def is_flush(self) -> bool:
    suits = set(map(lambda card: card.suit, self.cards))
    return len(suits) == 1

  def is_straight(self) -> bool:
    ranks = set(map(lambda card: card.rank, self.cards))
    expected = [min(ranks)+i for i in range(5)]
    
    for e in expected:
      if e not in ranks:
        return False
    
    return True

  def is_3_of_a_kind(self) -> bool:
    rank_counts: dict[int,int] = self.count_rank_frequency()
    return max(rank_counts.values()) == 3 and len(rank_counts) == 3

  def is_2_pair(self) -> bool:
    rank_counts: dict[int,int] = self.count_rank_frequency()
    return max(rank_counts.values()) == 2 and len(rank_counts) == 3

  def is_pair(self) -> bool:
    rank_counts: dict[int,int] = self.count_rank_frequency()
    return max(rank_counts.values()) == 2 and len(rank_counts) == 4

  def is_high_card(self) -> bool:
    rank_counts: dict[int,int] = self.count_rank_frequency()
    return max(rank_counts.values()) == 1

  def __rate(self) -> None:
    if self.is_royal_flush():
      self.rank = "Royal flush"
    elif self.is_straight_flush():
      self.rank = "Straight flush"
    elif self.is_4_of_a_kind():
      self.rank = "Four of a kind"
    elif self.is_full_house():
      self.rank = "Full house"
    elif self.is_flush():
      self.rank = "Flush"
    elif self.is_straight():
      self.rank = "Straight"
    elif self.is_3_of_a_kind():
      self.rank = "Three of a kind"
    elif self.is_2_pair():
      self.rank = "Two pair"
    elif self.is_pair():
      self.rank = "One pair"
    else:
      self.rank = "High card"
  
  def __find_rank_resolver(self) -> None:
    # No way to resolve between two royal flushes in this ruleset
    if self.rank == "Royal flush":
      pass
    
    # Only compare the highest card
    elif (self.rank == "Straight flush" or 
          self.rank == "Straight"):
      self.rank_resolver = [max(self.count_rank_frequency().keys())]

    # Hands that use 4 or 5 cards to rank
    # can only compare their highest frequencies in order
    elif (self.rank == "Four of a kind" or
          self.rank == "Full house"):
      rank_frequencies: list[tuple[int,int]] = sorted(self.count_rank_frequency().items(), key=lambda item: item[1], reverse=True)
      self.rank_resolver: list[int] = list(map(lambda tup: tup[0], rank_frequencies))

    # Hands that use 3 or less cards to rank
    # start by comparing their highest frequency card
    # but if that is equal then they rank by high card
    elif self.rank == "Three of a kind" or self.rank == "One pair":
      rank_frequency = self.count_rank_frequency()

      highest_frequency = max(rank_frequency.values())      
      highest_frequency_card = [item[0] for item in rank_frequency.items() if item[1] == highest_frequency][0]

      self.rank_resolver.append(highest_frequency_card)
      rank_frequency.pop(highest_frequency_card)

      rest_of_hand_high = sorted(rank_frequency, reverse=True)
      self.rank_resolver.extend(rest_of_hand_high)

    # TODO
    elif self.rank == "Two pair":
      rank_frequency = self.count_rank_frequency()

      highest_frequency = max(rank_frequency.values())      
      highest_frequency_cards = [item[0] for item in rank_frequency.items() if item[1] == highest_frequency]
      higher_pair, lower_pair = max(highest_frequency_cards), min(highest_frequency_cards)

      self.rank_resolver.extend([higher_pair, lower_pair])

      rank_frequency.pop(higher_pair)
      rank_frequency.pop(lower_pair)

      rest_of_hand_high = sorted(rank_frequency, reverse=True)
      self.rank_resolver.extend(rest_of_hand_high)
    
    # Flush and high card compare to equal rank
    # by checking all cards high to low
    else:
      self.rank_resolver = list(self.count_rank_frequency().keys())
      self.rank_resolver.sort(reverse=True)

def find_winning_hand(hand1: Hand, hand2: Hand) -> int:
  hand1_value = hand_ranks[hand1.rank]
  hand2_value = hand_ranks[hand2.rank]

  if hand1_value > hand2_value:
    return 1
  elif hand2_value > hand1_value:
    return 2
  else:
    resolvers = zip(hand1.rank_resolver, hand2.rank_resolver)
    for tup in resolvers:
      if tup[0] > tup[1]:
        return 1
      elif tup[1] > tup[0]:
        return 2

games: list[str] = file_data.splitlines()
p1_wins: int = 0

for index, game in enumerate(games):
  cards = list(map(lambda elem: Card(elem), game.split()))
  hand1 = Hand(cards[:5])
  hand2 = Hand(cards[5:])

  if find_winning_hand(hand1, hand2) == 1:
    p1_wins += 1

print(p1_wins)