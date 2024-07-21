from world.world import World
from navigation.navigator import Navigator
from communications.wrapper import CommandSender
from world.entities import Robot
from utility.math_utilities import normalize_2d_vector, rotate_2d_vector

import time
import math

# Moves a robot to a specific position
class Move:
    def __init__(self, world : World, navigator : Navigator, comms : CommandSender, 
                 robot : tuple[int, int] ):
        self.world = world
        self.navigator = navigator
        self.comms = comms 
        self.robot = robot # ("id", is_blue)
        self.MINIMUM_DISTANCE = 0.18 # robot radius in meters
        self.MOVE_SPEED = 1
    
    def move_to_point(self, point : tuple[float, float]):
        while True:
            robot : Robot = self.world.get_robot(self.robot[1], self.robot[0])
            dir_vec : tuple[float, float] = point[0] - robot.x,  point[1] - robot.y
            # To local coords of the robot
            # Nose porque con negativo funciona si alguien sabe explicar porfavor
            dir_vec = rotate_2d_vector(dir_vec, -robot.orientation)
            dir_vec = normalize_2d_vector(dir_vec)
            
            print("robot orientation: ", math.degrees(robot.orientation))
            self.comms.send_robot_data(id = self.robot[0], is_blue = self.robot[1], 
                                       veltangent= dir_vec[0]*self.MOVE_SPEED,
                                       velnormal = dir_vec[1]*self.MOVE_SPEED
                                       )
            if(self.distance((robot.x,robot.y) , point ) < self.MINIMUM_DISTANCE):
                break
    
    def distance(self, point_a : tuple[float, float], point_b : tuple[float, float]) -> float:
        return math.sqrt((point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2)

    def stop():
        pass