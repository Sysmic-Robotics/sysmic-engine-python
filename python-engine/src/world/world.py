#The World class is what we use to represent the state of the world at any given time.
# # In this context, the world includes the positions and orientations of all robots on the field, #
# the position and velocity of the ball, the dimensions of the field being played on, and the current 
# referee commands.
# Altogether, it's the information we have at any given time that we can use to make decisions.

# Otorga la informacion necesario del juego
import threading
from world.entities import Robot, Ball
from world.vision.vision import Vision
from proto_compiled.messages_robocup_ssl_detection_pb2 import SSL_DetectionRobot, SSL_DetectionBall
from utility.observer import Observer

class World(Observer):
    def __init__(self, n_blues : int, n_yellow : int) -> None:
        self.robots_blue : dict[Robot] = {}
        self.robots_yellow : dict[Robot] = {}
        # Init vision
        self.vision : Vision = Vision("224.5.23.2", 10020, self)
        vision_t = threading.Thread(target=self.vision.loop)
        vision_t.start()
        
        self.ball : Ball
        # Create robots
        for id in range(0, n_blues):
            self.robots_blue[id] = self.create_robot(1) 
        for id in range(0, n_yellow):
            self.robots_yellow[id] = self.create_robot(0)
        
        print("-- World succefully initiated --")
        print(" Blue team size ", len(self.robots_blue.keys()))
        print(" Yellow team size ", len(self.robots_yellow.keys()))

    def update_world(self, blue : list[SSL_DetectionRobot], yellow : list[SSL_DetectionRobot], ball : SSL_DetectionBall):
        # Update robots
        for robot in blue:
            self.update_robot(1, robot.robot_id, robot.x, robot.y, robot.orientation, robot.confidence)
        for robot in yellow:
            self.update_robot(0, robot.robot_id, robot.x, robot.y, robot.orientation, robot.confidence)
        # Update ball
        

    # Create a robot from raw data
    def create_robot(self, is_blue : int) -> Robot:
        new_robot = Robot()
        new_robot.team_id = is_blue
        return new_robot


    def update_ball(self, x : float, y : float, confidence : float):
        self.ball.x = x
        self.ball.y = y
        self.ball.confidence = confidence


    def update_robot(self, is_blue : int, id : int, x : float, y : float, orientation : float, confidence : float):
        if(not self.robot_exist(is_blue, id)):
            team = 'yellow'
            if(is_blue == 1):
                team = 'blue'
            print(" Trying to update robot that doenst exist: id: ", id," team: ", team)
            return
        
        robot : Robot = Robot()
        robot.id = id
        robot.team_id = is_blue
        # Hot fix, por alguna razon las posiciones se estan recibiendo en mm
        robot.x = x/1000
        robot.y = y/1000
        robot.orientation = orientation
        robot.confidence = confidence

        if(is_blue == 1):
            self.robots_blue[id] = robot
        else:
            self.robots_yellow[id] = robot


    # Return the robot index from its respective list
    def get_robot_index(self, is_blue : int, id : int) -> int:
        if(is_blue == 1):
            for i in range(0, len(self.robots_blue)):
                if self.robots_blue[i].id == id:
                    return i
        else:
            for i in range(0, len(self.robots_yellow)):
                if self.robots_yellow[i].id == id:
                    return i
        return -1


    def robot_exist(self, is_blue : int, id : int) -> bool:
        if(is_blue == 1):
            return id in self.robots_blue.keys()
        else:
            return id in self.robots_yellow.keys()
    
    # Public function
    def get_robot(self, is_blue : int, id : int) -> Robot:
        if(not self.robot_exist(is_blue, id)):
            return None
        if(is_blue == 1):
            return self.robots_blue[id]
        else:
            return self.robots_yellow[id]
    
    def get_robots(self) -> list[Robot]:
        b = list(self.robots_blue.values()) if isinstance(self.robots_blue, dict) else self.robots_blue
        y = list(self.robots_yellow.values()) if isinstance(self.robots_yellow, dict) else self.robots_yellow
        f = b + y
        return f
