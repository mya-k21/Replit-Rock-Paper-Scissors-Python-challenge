import random
choices = ("rock", "paper", "scissors")
shaggy_rogers = input("rock, paper or scissors?: ").lower()
scooby_doo = random.choice(choices)
print("Scooby chose", scooby_doo)
if shaggy_rogers == scooby_doo:
  print("It's a tie!")
elif shaggy_rogers == "scissors" and scooby_doo == "rock":
  print("Scooby Doo wins!")
elif shaggy_rogers == "paper" and scooby_doo == "rock":
  print("Shaggy Rogers wins!")
elif shaggy_rogers == "rock" and scooby_doo == "scissors":
  print("Shaggy Rogers wins!")
else:
  print("Scooby Doo wins!")