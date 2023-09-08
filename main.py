from art import logo, vs
from game_data import data
import os
import random

score = 0
is_game_over = False
print(logo)

def generate_account():
  account = random.choice(data)
  account_list = []
  account_followers = account.get('follower_count')
  for key, value in account.items():
    if type(value) == str:
      account_list.append(value)
  account_info = (f"{account_list[0]}, a {account_list[1]} from {account_list[2]}")
  account_info_and_followers = [account_info, account_followers]
  return account_info_and_followers

def check_guess():
  global guess
  global A_followers
  global B_followers
  if A_followers > B_followers:
    return guess == 'A'
  else:
    return guess == 'B'

def play_game():
  global score
  global guess
  global A_followers
  global B_followers
  global is_game_over
  A = generate_account()
  A_account = A[0]
  A_followers = A[1]
  B = generate_account()
  while A == B:
    B = generate_account()
  B_account = B[0]
  B_followers = B[1]
  print(f"Compare A: {A_account}")
  print(vs)
  print(f"Against B: {B_account}")
  guess = input("Who has more followers? Type 'A' or 'B': ")
  is_correct = check_guess()
  os.system('cls')
  print(logo)
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}.")
  else:
    is_game_over = True
    print(f"Sorry, that's wrong. Final score: {score}")

while is_game_over == False:
  play_game()