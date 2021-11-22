import os

def operators():
    if operator=="+":
        return (first+next)
    elif operator=="-":
        return (first-next)
    elif operator=="*":
        return (first*next)
    elif operator=="/":
        return (first/next)


def program():
    global operator
    global next
    global first
    print("C A L C U L A T O R")
    first=float(input("What's the first number?: "))
    print("+\n-\n*\n/")
    score=0


    count=True
    while count:
        global cont
        operator=input("Pick an operation: ")
        next=float(input("What's the next number?: "))
        score=operators()
        print (first,operator,next,"=",score)
        cont=str(input(f"Type 'y' to continue calculating with {score} or type 'n' to start a new calculation: "))
        if cont =="n":
            count=False
            if os.name=="posix":
                os.system('clear')
            else:
                os.system('cls')
            program()
                                                            
        first=score
             
program()


