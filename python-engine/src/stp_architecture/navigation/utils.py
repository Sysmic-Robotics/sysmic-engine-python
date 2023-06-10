def is_obstructed(start,finish,obstacles):
    # Check if the path from the start coordinate to the finish coordinate
    # is obstructed by an obstacle
    # Return True if it is obstructed, False otherwise
    x1,y1 = start
    x2,y2 = finish

    #asume all robots has max diameter of 1 (temporal)
    robot_diameter = 1

    for obstacle in obstacles:
        x3,y3 = obstacle
        #check collision with circle
        
        if (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1) == 0:
            return True
    return False