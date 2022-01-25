import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [ '0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')']
print("Welcome to password Generator")
in_letter= int(input("How many alphabet would you like to have.\n"))
in_numbers = int(input("How many numbers would you like to have. \n"))
in_symbols = int(input("How many symbols woul dyou like to have.\n"))
password_list = []
for char in range(1, in_letter +1):
  password_list.append( random.choice(letters))
for char in range(1,in_numbers +1):
  password_list +=random.choice(numbers)
for char in range (1, in_symbols+1):
  password_list += random.choice(symbols)

random.shuffle(password_list)

password=""
for char in password_list:
  password+=char
print(f"Your password is: {password}")