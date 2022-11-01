import random

print("*Rock, Paper, Scissors*")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

outcome = [rock, paper, scissors]
com = random.randint(0, 2)
choice = int(input("What's your choice? 0 = rock/ 1 = paper/ 2 = scissors\n..."))
computer = outcome[com]
user = outcome[choice]

print(f"\n\nYour choice:\n {user}")
print(f"Computer's choice:\n {computer}")

if (computer == rock and user == scissors) or (computer == scissors and user == paper) or (computer == paper and user == rock):
  print("you lose!")
elif computer == user:
  print("Draw")
else:
  print("You win!")
  print("\n\nReplay")
