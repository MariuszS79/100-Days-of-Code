import random

letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
digits=["0","1","2","3","4","5","6","7","8","9"]
symbols=["£","$","%","^","&","*","(",")","|","<",">","@","?"]

print("-=RANDOM PASSWORD GENERATOR=-\n")

letters2=int(input("How many letters would you like in your password?: "))
symbols2=int(input("How many symbols?: "))
digits2=int(input("How many digits?: "))

pass1=[]

for i in range(letters2):
  pass1.append(random.choice(letters))

for i in range(symbols2):
  pass1.append(random.choice(symbols))

for i in range(digits2):
  pass1.append(random.choice(digits))


random.shuffle(pass1)

print("\nYour password is: ", *pass1, sep="")

