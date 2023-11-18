def turn_right ():
    turn_left()
    turn_left()
    turn_left()
    

while not at_goal():
    if wall_on_right() and not wall_in_front():
        move()
        if not wall_on_right() and not at_goal():
            turn_right()
            move()
            if not wall_on_right() and not at_goal():
                turn_right()
                move()
    elif not wall_on_right() and wall_in_front():
        turn_right()
    elif wall_on_right() and wall_in_front():
        turn_left()
    else:   
        move()
      
           
        
    
        
    
