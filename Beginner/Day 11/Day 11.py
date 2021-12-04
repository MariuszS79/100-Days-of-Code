from graphic import logo
import random
import os



cards={"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10,"A":11}


player_cards=[]
player_values=[]
computer_cards=[]
computer_values=[]


def pick_player_card():
    global player_cards
    global player_values
    key_card=(random.choice(list(cards.items())))
    player_cards.append(key_card[0])
    player_values.append(key_card[1])
    if "A" in player_cards[0:-1] and "A" in player_cards[-1]:
        player_values.append(-10)
    elif sum(player_values)>21 and "A" in player_cards[-1]:
        player_values.append(-10)
    
    
def pick_computer_card():
    global computer_cards
    global computer_values
    key_card=(random.choice(list(cards.items())))
    computer_cards.append(key_card[0])
    computer_values.append(key_card[1])
    if "A" in computer_cards[0:-1] and "A" in computer_cards[-1]:
        computer_values.append(-10)
    elif sum(computer_values)>21 and "A" in computer_cards[-1]:
        computer_values.append(-10)


def your_cards():
    print("\nYour cards:",(player_cards),"current score: ",sum(player_values))


def opponents_cards():
    print("Computer's first card:",computer_cards[0])


def check_score():
    global final
    if sum(player_values)>=21 or sum(computer_values)>=21:
        print(f"\nYour final hand: {player_cards}, final score: {sum(player_values)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_values)}")

        if sum(player_values)<=21 and sum(computer_values)>21:
            print("---Opponent went over. You win.---")
            final=1
        elif sum(player_values)>21 and sum(computer_values)<=21:
            print("---You went over. You lose!---")
            final=1
        elif sum(player_values)>21 and sum(computer_values)>21:
            print("---You both went over.---")
            final=1
        elif sum(player_values)>sum(computer_values):
            print("---You win!---")
            final=1
        elif sum(player_values)<sum(computer_values):
            print("---You lose!---")
            final=1
        elif sum(player_values)==sum(computer_values):
            print("---You scored same.---")
            final=1    

        
def ask_score():
    global final
    print(f"\nYour final hand: {player_cards}, final score: {sum(player_values)}")
    print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_values)}")
    
    if sum(player_values)<=21 and sum(computer_values)>21:
        print("---Opponent went over. You win!---")
        final=1  
    elif sum(player_values)>21 and sum(computer_values)<=21:
        print("---You went over. You lose!---")
        final=1
    elif sum(player_values)>21 and sum(computer_values)>21:
        print("---You both went over!---")
        final=1
    elif sum(player_values)>sum(computer_values):
        print("---You win!!!---")
        final=1
    elif sum(player_values)<sum(computer_values):
        print("---You lose!---")
        final=1
    elif sum(player_values)==sum(computer_values):
        print("---You scored same.---")
        final=1
    
    
def clear():
    if os.name=="posix":
        os.system('clear')
    else:
        os.system('cls')



game=True
while game:
    global final
    final=0
    player_cards=[]
    player_values=[]
    computer_cards=[]
    computer_values=[]
    
    do_you=input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")
  
    if do_you=="y":
      clear()
      print(logo)
    else: 
      game=False
      continue    
    
    pick_player_card()
    pick_player_card()
    pick_computer_card()
    pick_computer_card()
    your_cards()
    opponents_cards()
    check_score()
    
    if final==0:
      one_more=input("\nType 'y' to get another card, type 'n' to pass: ")
      if one_more!="y":
          ask_score()
          if final==1:
            one_more!="y"
         
    
      while one_more=="y" and final==0:
          pick_player_card()
          pick_computer_card()
          your_cards()
          opponents_cards()
          check_score()
          if final==1:
            one_more!="y"
            continue
              
          one_more=input("\nType 'y' to get another card, type 'n' to pass: ")
          if one_more!="y":
            ask_score()
            if final==1:
              one_more!="y"
          
            

