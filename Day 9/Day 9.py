import os
dict={}

def check_biggest_bid():
  biggest_bid=max(dict, key=dict.get)
  all_values=dict.values()
  biggest_value=max(all_values)
  print("The winner is ",biggest_bid, " with a bid of £", biggest_value)

your_name=input("What is your name?: ")
your_bid=input("What is your bid?: £")
dict[your_name]=your_bid
other_bidders=input("Are there any other bidders? Type 'yes' or 'no'.\n")
if other_bidders!="yes":
    check_biggest_bid()

if other_bidders=="yes":
    if os.name=="posix":
        os.system('clear')
    else:
        os.system('cls')

while other_bidders=="yes":
  your_name=input("What is your name?: ")
  your_bid=input("What is your bid?: £")
  dict[your_name]=your_bid
  other_bidders=input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if other_bidders!="yes":
    if os.name=="posix":
          os.system('clear')
    else:
          os.system('cls')
  if other_bidders!="yes":
    check_biggest_bid()