def operators():
    if operator=="+":
        return (first+next)
    elif operator=="-":
        return (first-next)
    elif operator=="*":
        return (first*next)
    elif operator=="/":
        return (first/next)
cont=""
operator=""
next=float(0)
first=float(0)


print("C A L C U L A T O R")
first=float(input("What's the first number?: "))
print("+\n-\n*\n/")
score=0


count=True
while count:
    operator=input("Pick an operation: ")
    next=float(input("What's the next number?: "))
    score=operators()
    print (first,operator,next,"=",score)
    cont=input("Type 'y' to continue calculating with, or type 'n' to start a new calculation: ")
    if cont =="n":
        count=False
        break
    first=score
             



