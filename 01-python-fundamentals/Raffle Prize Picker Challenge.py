# 🏆 Raffle Prize Picker — Challenge Steps
#
# 1. Ask how many people are entering the raffle (at least 3 names).
# 2. Use a loop to collect their names into a list.
# 3. Ask for exactly 3 prize names (in order) and store them in a list.
# 4. Randomly pick 3 different winners from the participant list.
# 5. Print out who wins which prize and make sure the final one
#    is clearly marked as the Grand Prize. 🏆
#
# Hint: Use loops, lists, and a tool that picks random items without repeats.
import random as r
entrants = []
while True:
  entrant = input("Enter a name for the Raffle. Please enter at least 3 total. Enter \'done\' to move on.")
  if entrant.strip().lower() == 'done' and len(entrants) >2:
    break
  else:
    entrants += [str(entrant.strip().title())]
    continue

prizes = []
prizes += [str(input("Enter the name of the third place prize."))]
prizes += [str(input("Enter the name of the second place prize."))]
prizes += [str(input("Enter the name of the first place prize."))]

winners = r.sample(entrants,3)
winners_prizes = {winner:prize for winner, prize, in zip(winners,prizes)}
results = list(winners_prizes.items())  # turns the dict into a list of (winner, prize) tuples, in order

print('-----The Raffle Results-----')
print(f"{results[2][0]} wins the {results[2][1]}")
print(f"{results[1][0]} wins the {results[1][1]}")
print(f"{results[0][0]} wins the {results[0][1]}")