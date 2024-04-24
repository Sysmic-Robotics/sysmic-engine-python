import keyboard
from communications.grsim import Grsim

def move_robot():
    radio = Grsim()
    # Main loop
    running = True
    while running:
        # Detect arrow key presses
        final_velocity = [0,0]
        if keyboard.is_pressed('up'):
            final_velocity[1] += 1
        if keyboard.is_pressed('down'):
            final_velocity[1] += -1
        if keyboard.is_pressed('left'):
            final_velocity[0] += -1
        if keyboard.is_pressed('right'):
            final_velocity[0] += 1
        radio.communicate_grsim(id=1, isteamyellow=0, 
                                velnormal=final_velocity[1],
                                veltangent=final_velocity[0])

        if keyboard.is_pressed('q'):
            break

move_robot()