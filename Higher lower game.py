from art import logo,vs
from game_data import data
import random
from replit import clear
print(logo)
score =0
choice2=random.choice(data)

def formatdata(account):
  account_name=account["name"]
  account_descr=account["description"]
  account_country=account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"
correct=True
while correct:
  choice1=choice2
  choice2=random.choice(data)
  if choice1==choice2:
    choice2=random.choice(data)

  print(f"Compare A: {formatdata(choice1)}.")
  print(vs)
  print(f"Against B: {formatdata(choice2)}.")
  choose=input("Who has more followers? Type'A' or 'B': ").lower()
  first_follower_count=choice1["follower_count"]
  second_follower_count=choice2["follower_count"]
  clear()
  print(logo)
  
  if choose =="a":
    if first_follower_count>second_follower_count:
      score+=1
      print(f"You got it right. Your score is {score}")
      
    else:
      correct=False
      print(f"Sorry,Your guess is wrong. Your final score is {score}")

  elif choose=="b":
    if first_follower_count<second_follower_count:
      score+=1
      print(f"You got it right. Your score is {score}")

    else:
      correct = False
      print(f"Sorry,your guess is wrong. Your final score is {score}")