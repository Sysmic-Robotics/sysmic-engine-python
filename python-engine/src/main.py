from communications.grsim import Grsim
from world.world import World
from world.entities import Robot
import time
from navigation.navigator import Navigator
from communications.wrapper import CommandSender
from stp.move import Move
import math

if __name__ == '__main__':
    
    # Initialize essentials components
    world : World = World(1,1)
    comms : CommandSender = CommandSender()
    nav : Navigator = Navigator(world)
    
    # Main loop
    last_time = time.time()
    running = True
    while running:
        # Calculate delta time
        current_time = time.time()
        delta_time = current_time - last_time
        last_time = current_time

        world._process(delta_time)