import socket
import proto_compiled.algo_commander_pb2 as algo_commander_pb2
from communications.vision import Vision
import time

class AlgoCommander:
    def __init__(self, port, vision ) -> None:
        self.host = '127.0.0.1'  # Change this to your desired destination IP address
        self.port = port        # Change this to your desired destination port number
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.vision = vision

    def update(self):
        while True:
            robots = self.vision.get_robots()
            for robot in robots:
                if(robot != None):
                    blue_team = robot.team_id == 1
                    self.send_robot_position(robot.id, robot.posx, robot.posy, robot.orientation, blue_team)
            time.sleep(0.02)    

    def send_robot_position(self, robot_id, pos_x, pos_y, angle, blue_team):
        # Create a RobotPosition message
        robot_position = algo_commander_pb2.RobotPosition()
        robot_position.id = robot_id
        robot_position.pos_x = pos_x
        robot_position.pos_y = pos_y
        robot_position.angle = angle
        robot_position.blue_team = blue_team
        # Serialize the message to bytes
        serialized_data = robot_position.SerializeToString()

        try:
            # Send the serialized data
            self.socket.sendto(serialized_data, (self.host, self.port))
        finally:
            pass
            
    def __del__(self):
        self.socket.close()       
