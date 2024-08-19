from communications.grsim import Grsim
from world.world import World
from world.entities import Robot
import time
from navigation.navigator import Navigator
from communications.wrapper import CommandSender
from stp.move import Move
import math

from control.follow_trajectory import FollowTrajectory
from navigation.trajectory_planning import TrajectoryPlanning

if __name__ == '__main__':
    
    # Initialize essentials components
    world : World = World(1,1)
    nav : Navigator = Navigator(world)
    
    # Main loop
    last_time = time.time()
    running = True
    time.sleep(1)
    radio : Grsim = Grsim()
    radio.communicate_pos_robot(0, 1, -2, 2, 0)
    

    test_path = [[-2, 2], [4,2]]
    tj =  TrajectoryPlanning = TrajectoryPlanning().get_trajectory(test_path)
    follow : FollowTrajectory = FollowTrajectory(0, 0, tj)
    
    radio.communicate_pos_robot(0, 0, -2, 1, 0)

    while running:
        # Calculate delta time
        current_time = time.time()
        delta_time = current_time - last_time
        last_time = current_time

        world._process(delta_time)

        follow._process(delta_time)

        radio.communicate_grsim(0, 0, veltangent = 5)