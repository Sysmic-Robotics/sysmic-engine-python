from communications.grsim import Grsim
from world.world import World
from world.entities import Robot
import time
from communications.wrapper import CommandSender
import math
from motion.motion import Motion
from world.vision.vision import Vision
import threading

def fix_grsim():
    radio : Grsim = Grsim()
    radio.communicate_pos_robot(0,0 ,1,0)
    robot : Robot = world.get_robot(1,0)
    while True:
        #radio.communicate_pos_robot(0,0 ,1,0)
        robot = world.get_robot(1,0)
        radio.communicate_grsim(0,0,1)
        print(robot.x)
        if robot.x != 0:
            return
        

if __name__ == '__main__':
    world : World = World(1,1)
    # Init vision
    vision : Vision = Vision("224.5.23.2", 10020, world)
    vision_t = threading.Thread(target= vision.loop)
    vision_t.start()

    last_time = time.time()
    
    
    fix_grsim()
    motion : Motion = Motion(0,1,world)
    running = True
    print("Running...")
    while running:
        # Calculate delta time
        current_time = time.time()
        delta_time = current_time - last_time
        last_time = current_time

        world._process(delta_time)
        motion.move_linear((-1.500, 0.01), delta_time)
        