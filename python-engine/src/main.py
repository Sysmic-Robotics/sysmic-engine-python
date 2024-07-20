from communications.grsim import Grsim
from world.world import World
from world.entities import Robot
import time
from navigation.navigator import Navigator

if __name__ == '__main__':
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
    for point in test_path:
        print("to ", point)
        radio.communicate_pos_robot(id=0, yellowteam=0, x = point[0], y = point[1])
        time.sleep(0.2)
