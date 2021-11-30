import random
from art import logo, vs
from game_data import data
import os
compare_a = random.choice(data)
score = 0

def game_def():
  global compare_a
  global score
  global game
  print(logo)
 
  if score>0:
    print(f"You are right! Current score: {score}")
  print("Compare A:", compare_a['name'], ", a", compare_a['description'],
          ", from", compare_a['country'])

  print(vs)
  compare_b = random.choice(data)
  print("Compare B:", compare_b['name'], ", a", compare_b['description'],
        ", from", compare_b['country'])
  

  question=input("Who has more followers \"A\" or \"B\": ").lower()
  
  if question=="A".lower():
    if compare_a['follower_count']>compare_b['follower_count']:
      score+=1
      os.system('clear')
    else: 
      os.system('clear')
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}")
      game=False
  elif question=="B".lower():
    if compare_a['follower_count']<compare_b['follower_count']:
      score+=1
      os.system('clear')
    else: 
      os.system('clear')
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}")
      game=False
  
  compare_a = compare_b
 

game = True
while game:
    game_def()
    
    


