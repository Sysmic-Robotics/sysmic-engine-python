from world.world import World
from navigation.navigator import Navigator
from communications.wrapper import CommandSender
from world.entities import Robot
from utility.math_utilities import normalize_2d_vector, rotate_2d_vector, dot_product_2d, euclidian_distance

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
        self.MINIMUM_DISTANCE_SHORT = 0.09 # robot radius in meters
        self.MINIMUM_DISTANCE_LONG = 0.18
        self.MOVE_SPEED = 5
    
            
    def motion_to_point(self, robot : Robot, to_point : tuple[float, float]):
        dir_vec : tuple[float, float] = to_point[0] - robot.x,  to_point[1] - robot.y
        # To local coords of the robot
        # Nose porque con negativo funciona si alguien sabe explicar porfavor
        dir_vec = rotate_2d_vector(dir_vec, -robot.orientation)
        dir_vec = normalize_2d_vector(dir_vec)
        self.comms.send_robot_data(id = self.robot[0], is_blue = self.robot[1], 
                                    veltangent= dir_vec[0]*self.MOVE_SPEED,
                                    velnormal = dir_vec[1]*self.MOVE_SPEED
                                    )

    # Use for long distances
    def move_to_point(self, goal : tuple[float, float]):
        robot : Robot = self.world.get_robot(self.robot[1], self.robot[0])
        path = self.navigator.get_path((robot.x, robot.y), goal)
       
        next_point = robot.x, robot.y
        while True:
            if len(path) == 0:
                break
            # Update robot
            robot = self.world.get_robot(self.robot[1], self.robot[0])
            # Pass to next point if the robot is nearest enough
            if euclidian_distance((robot.x,robot.y), next_point) < self.MINIMUM_DISTANCE_LONG:
                next_point = path.pop(0)
            # Or pass to the next point if the current_point is already passed
            if len(path) > 1:
                next_point_2 = path[1]
                path_dir = normalize_2d_vector( (next_point_2[0] - next_point[0], next_point_2[1] - next_point[1]) )
                motion_dir = normalize_2d_vector( (next_point[0] - robot.x, next_point[1] - robot.y)  )
                if dot_product_2d(path_dir, motion_dir) < 0:
                    next_point = path.pop(0)
            self.motion_to_point(robot, next_point)
        print("Move to point finalized")
            
    
    def distance(self, point_a : tuple[float, float], point_b : tuple[float, float]) -> float:
        return math.sqrt((point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2)

    def stop():
        pass