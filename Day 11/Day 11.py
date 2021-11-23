from graphic import logo
import random
import os

cards={"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10,"A":1}


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
    
    
def pick_computer_card():
    global computer_cards
    global computer_values
    key_card=(random.choice(list(cards.items())))
    computer_cards.append(key_card[0])
    computer_values.append(key_card[1])
    
    
def clear():
    if os.name=="posix":
        os.system('clear')
    else:
        os.system('cls')

game=True
while game:
    clear()
    
    do_you=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    
    if do_you=="y":
        print(logo)
    else: 
        game=False
    
    pick_player_card()
    pick_player_card()
    pick_computer_card()
    pick_computer_card()
    print("Your cards:",(player_cards),"current score: ",sum(player_values))
    print("computer's first card:",computer_cards[0])
    one_more=input("Type 'y' to get another card, type 'n' to pass: ")
    if one_more=="y":
    

