from replit import clear
your_name=input("What is your name?: ")
your_bid=input("What is your bid?: £")
other_bidders=input("Are there any other bidders? Type 'yes' or 'no'.\n")

if other_bidders=="yes":
    #print("\n"*200) #used as os.system was giving "TERM environment variable not set" on Thonny
    clear()
your_name=input("What is your name?: ")