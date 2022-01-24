
import random
choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
if int(choice) ==0:
  print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif int(choice) ==1:
  print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
else  :
  print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
computer = random.randint(0,2)
if int(computer) ==0 :
  print("""Computer chose:

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif int(computer) == 1:
  print(""" Computer chose:  

     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
else:
  print(""" Computer chose:

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
if  int(choice) == 0 and int(computer) ==2:
  print("You win")
elif int(choice) > int(computer):
  print("You win")


elif int(choice) == int(computer):
  print("Draw ")
else:
  print("You lose")
