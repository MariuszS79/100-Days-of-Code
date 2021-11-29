from random import randint
print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.")
number=randint(1,100)
print("psst, the correct number is ",number)
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")


def guessing_game():
    global attempts
    global guess
    while attempts !=0:
        guess=(int(input("Make a guess: ")))
        attempts-=1
        if guess>number:
            print("Too high.\nGuess again.")
            print(f"You have {attempts} remaining to guess the number.")
        elif guess<number:
            print("Too low.\nGuess again.")
            print(f"You have {attempts} remaining to guess the number.")
        elif guess==number:
            print(f"Well done, you guessed it. It was {number}.")
            attempts=0
    
            
if difficulty=="easy":
    attempts=10
    print(f"You have {attempts} attempts remaining to guess the number.")
    guessing_game()
    if attempts==0 and guess!=number:
        print(f"You didn't guess it. The number was {number}")
else:
    attempts=5
    print(f"You have {attempts} attempts remaining to guess the number.")
    guessing_game()
    if attempts==0 and guess!=number:
        print(f"You didn't guess it. The number was {number}.")       



        
        

