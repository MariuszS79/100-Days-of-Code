from random import randint
print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.")
number=randint(1,100)
print("psst, the correct number is ",number)
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")

attempts=0

if difficulty=="easy":
    attempts=10
    print("You have 10 attempts remaining to guess the number.")
    while attempts !=0:
        guess=(int(input("Make a guess:")))
        attempts-=1
        if guess>number:
            print("Too high.\nGuess again.")
            print(f"You have {attempts} remaining to guess the number.")
        elif guess<number:
            print("Too low.\nGuess again.")
            print(f"You have {attempts} remaining to guess the number.")
        elif guess==number:
            print("Well done, you guessed it")
            attempts=0
            



        
        

