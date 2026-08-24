import random as rand
user_funds =  1000
bag = ["green","green","green","green","green","black","white","red","red","red"]
num_rounds = int(input(f"How many rounds would you like to play? (You have ${user_funds} to start with) "))
for i in range(num_rounds):
    if user_funds < 500:
        print("You have used half of your funds. Game over.")
        break
    bet_amount = int(input(f"Round {i+1}: How much would you like to bet? (You have ${user_funds} remaining) "))
    if bet_amount > user_funds:
        print("You cannot bet more than your current funds. Please enter a valid amount.")
        continue
    elif bet_amount <= 0:
        print("Please enter a positive amount to bet.")
        continue
    marble = rand.choice(bag)
    if marble == "green":
        user_funds += bet_amount
        print(f"The marble was green! You won! Your new balance is ${user_funds}.")
        continue
    elif marble == "black":
        user_funds += 10*bet_amount
        print(f"The marble was black! You won big! Your new balance is ${user_funds}.")
        continue
    elif marble == "red":
        user_funds -= bet_amount
        print(f"The marble was red! You lost! Your new balance is ${user_funds}.")
        continue
    elif marble == "white":
        user_funds -= 5*bet_amount
        print(f"The marble was white! You lost big! Your new balance is ${user_funds}.")
        continue
print(f"Game over! You finished with ${user_funds}.")
