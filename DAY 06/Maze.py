def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal() == True:
    if right_is_clear() and front_is_clear():
        turn_right()
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()
    elif wall_in_front() and right_is_clear():
        turn_right()
        move()
    elif right_is_clear():
        turn_right()
    else:
        move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
