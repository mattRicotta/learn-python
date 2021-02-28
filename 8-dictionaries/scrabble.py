letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters, points)}
letter_to_points.update({" ": 0})

def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter.upper(), 0)
  return point_total

player_to_words = {}
player_to_words.update({"player1":["BLUE", "TENNIS", "EXIT"]})
player_to_words.update({"wordNerd":["EARTH", "EYES", "MACHINE"]})
player_to_words.update({"Lexi Con":["ERASER", "BELLY", "HUSKY"]})
player_to_words.update({"Prof Reader":["ZAP", "COMA", "PERIOD"]})

def play_word(player, word):
  player_to_words[player].append(word)

player_to_points = {}
def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points.update({player: player_points})
  return player_to_points

print(update_point_totals())