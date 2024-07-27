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
    test_angle = math.pi/2 + math.pi/4
    
    radio.communicate_pos_robot(robot_id, 1 - is_blue, 1,1, dir = test_angle)
    time.sleep(1)
    robot : Robot = world.get_robot(is_blue, robot_id)
    print("Robot pos: " , robot.x, robot.y )
    move.move_to_point((0.4,-1))

    ''' 
    # Initialize grsim packets
    radio = Grsim()
    # Por alguna razon grsim no envia packetes sin haber recibido ninguno
    radio.communicate_pos_robot(id=0, yellowteam=0, x = 1, y = 1.2)
    world : World = World(6,6)
    nav : Navigator = Navigator(world)
    time.sleep(1)
    # test path
    robot : Robot = world.get_robot(1, 0)
    test_path = nav.get_path((robot.x, robot.y), (1.5,-3))
    print("robot pos: ", robot.x, robot.y)
    # follow the path
    print("path to follow: ", test_path)
    for point in test_path:
        print("to ", point)
        radio.communicate_pos_robot(id=0, yellowteam=1, x = point[0], y = point[1])
        time.sleep(0.2)
    '''