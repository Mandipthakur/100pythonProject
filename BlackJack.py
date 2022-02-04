import random
from replit import clear
from art import logo
def deal_card():
  cards  = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card= random.choice(cards)
  return card

def calculate_score(cards):
  if sum(cards)==21 and len(cards)==2:
    return 0
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)
def compare(user_score,computer_score):
  if user_score==computer_score:
    return "Draw"
  elif computer_score==0:
    return "Lose, opponent has Blackjack"
  elif user_score==0:
    return "win with a black jack"
  elif user_score>21:
    return "you went over. You lose"
  elif computer_score >21:
    return"Opponent went over. You win"
  elif user_score >computer_score:
    return "you win"
  else:
    return "You lose"

def play_game():
  print(logo)   
  user_cards=[]
  computer_cards=[]
  is_game_over= False
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f"Your card: {user_cards}, your score {user_score}")
    print(f"Computer card: {computer_cards[0]}")
    if user_score==0 or computer_score==0 or user_score>21:
      is_game_over= True
    else:
      user_should_deal= input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal=="y":
        user_cards.append(deal_card())
      else:
        is_game_over=True
  while computer_score !=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)

  print(f"Your final hand: {user_cards}, final_score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final_score: {computer_score}")
  print(compare(user_score,computer_score))

while input("Do you want to play the game of BlackJack? Type 'y' to play or 'n' to end.  ")=="y":
  clear()
  play_game()