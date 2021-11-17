#solution for "maze" from https://reeborg.ca/

for i in range (100):
    
    if at_goal():
        done()
    elif right_is_clear():
        turn_left()
        turn_left()
        turn_left()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
