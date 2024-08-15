from communications.grsim import Grsim
from world.world import World
from world.entities import Robot
import time
from navigation.navigator import Navigator
from communications.wrapper import CommandSender
from stp.move import Move
import math

if __name__ == '__main__':
    # Initialize principal components
    world : World = World(6,6)
    nav : Navigator = Navigator(world)
    comms : CommandSender = CommandSender()

    is_blue = 0
    robot_id = 0
    time.sleep(1)
    move : Move = Move( world, nav, comms, (robot_id, is_blue) )
    radio : Grsim = Grsim()
