from communications.grsim import Grsim
from world.world import World
from world.entities import Robot
import time
import math

from motion.motion import Motion

if __name__ == '__main__':
    
    # Initialize essentials components
    world : World = World(1,1)
    
    # Main loop
    last_time = time.time()
    running = True
    time.sleep(2)

    radio : Grsim = Grsim()
    
    motion : Motion = Motion(0,1,world)
    while running:
        # Calculate delta time
        current_time = time.time()
        delta_time = current_time - last_time
        if delta_time > 0.016:
            print("LOW 60 FPS!")
        last_time = current_time

        world._process(delta_time)

        
        motion.move_linear([0,0], delta_time)

        #radio.communicate_grsim(0, 0, veltangent = 5)