import random
from art import logo,vs
from game_data import data

def format_data(account):
  account_name = account["name"]
  account_des = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_des},from {account_country}"

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
  def check_answer(guess,a_followers,b_followers):
    if a_followers > b_followers:
      return guess == "a"
    else:
      return guess == "b"
    
  account_a= account_b
  account_b = random.choice(data)
  
  while account_a == account_b:
    account_b = random.choice(data)
  
  #format tha data
  print(f"\nCompare A : {format_data(account_a)}")
  
  print(vs)
  
  print(f"\nAganist B : {format_data(account_b)}")
  
  guess = input("\nWho has more followers? Type 'A'or 'B': ").lower()
  
  a_followers_count= account_a["follower_count"]
  b_followers_count= account_b["follower_count"]
  
  is_correct = check_answer(guess,a_followers_count,b_followers_count)
  
  if is_correct:
    score+=1
    print(f"\nYou're right! Current score: {score}" )
  else:
    game_should_continue = False
    print(f"\nthat's wrong. Final Score {score}")
    








