print("Welcome to Treasure Island.\nYour mission is to find treasure\n")
print("----------")
step_1=input("You just landed on shore of the Treasure Island. \nWhere would you like to go? left or right?: ")

if step_1=="right":
  print("\nBad luck. You fell into hole and broke your legs. GAME OVER!")
elif step_1=="left":
  step_2=input("\nYou approach a river. Do you swim or try to find a boat? swim/boat?: ")
  if step_2=="swim":
    print("\nBad luck. You were eaten by aligator. GAME OVER!")
  elif step_2=="boat":
    print("\nYou crossed the river. You found weird building with 4 doors.")
    step_3=input("Which doors do you choose? red, blue, yellow or pink?: ") 
    if step_3=="red":
      print("\nBad luck. You were burnt alive. GAME OVER!")
    elif step_3=="blue":
      print("\nBad luck. You were eaten by lions. GAME OVER!")
    elif step_3=="pink":
      print("\nBad luck. You were shot by skeleton archer. GAME OVER!")
    elif step_3=="yellow":
      print("Well done, you found the treasure. Enjoy")


  
