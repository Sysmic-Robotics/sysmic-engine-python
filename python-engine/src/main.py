from communications.grsim import Grsim
from world.world import World
from world.entities import Robot
import time
from navigation.navigator import Navigator
from communications.wrapper import CommandSender
from stp.move import Move
import math

if __name__ == '__main__':
    # Main loop
    last_time = time.time()
    running = True

    while running:
        # Calculate delta time
        current_time = time.time()
        delta_time = current_time - last_time
        last_time = current_time

        # Initialize essentials components
        world : World = World(6,6)
        comms : CommandSender = CommandSender()
        nav : Navigator = Navigator(world)
        
        world._process(delta_time)


        is_blue = 0
        robot_id = 0
        time.sleep(1)
        move : Move = Move( world, nav, comms, (robot_id, is_blue) )
        radio : Grsim = Grsim()
        test_angle = math.pi/2 + math.pi/4
        ''''
        radio.communicate_pos_robot(robot_id, 1 - is_blue, 1,1, dir = test_angle)
        time.sleep(1)
        robot : Robot = world.get_robot(is_blue, robot_id)
        print("Robot pos: " , robot.x, robot.y )
        move.move_to_point((0.4,-1))
        '''