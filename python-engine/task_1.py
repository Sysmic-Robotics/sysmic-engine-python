import keyboard


def move_robot():
    # Main loop
    running = True
    while running:
        # Detect arrow key presses
        if keyboard.is_pressed('up'):
            print("Up arrow key pressed")
        elif keyboard.is_pressed('down'):
            print("Down arrow key pressed")
        elif keyboard.is_pressed('left'):
            print("Left arrow key pressed")
        elif keyboard.is_pressed('right'):
            print("Right arrow key pressed")
    
    # Stop the loop if 'q' is pressed
    if keyboard.is_pressed('q'):
        break

    pass