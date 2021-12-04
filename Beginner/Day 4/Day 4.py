import random

rock_hand = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_hand = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_hand = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices=["rock", "paper", "scissors"]

name=input("Hello, please enter your name: ")
print("Hello "+name+". good luck with your game.")



while True:
    human=input(name+ ",type rock, paper or scissors: ")
    if human not in choices:
      print("are you serious???;-)")
      human=input(name+ ",type rock, paper or scissors: ")
    if human=="rock":
      print(rock_hand)
    elif human=="paper":
      print(paper_hand)
    elif human=="scissors":
      print(scissors_hand)
    
    computer=(random.choice(choices))
    print("computer chose: " +computer)
    if computer=="rock":
      print(rock_hand)
    elif computer=="paper":
      print(paper_hand)
    elif computer=="scissors":
      print(scissors_hand) 
    
    if(human==choices[0] and computer==choices[2]):
        print(name+" won this time, well done "+name)
    elif(human==choices[1] and computer==choices[0]):
        print(name+" won this time, well done "+name)
    elif(human==choices[2] and computer==choices[1]):
        print(name+" won this time, well done "+name)
    elif(human==choices[2] and computer==choices[0]):
        print("Computer won this time, better luck next time")
    elif(human==choices[0] and computer==choices[1]):
        print("Computer won this time, better luck next time")
    elif(human==choices[1] and computer==choices[2]):
        print("Computer won this time, better luck next time")
    else:
        print("Wow, it's a draw ;)")
    
    print("--------------")
    print("Let's try again ;-)\n")



