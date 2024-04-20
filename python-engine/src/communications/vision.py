from classes.detection import Ball, Robot
from proto_compiled.messages_robocup_ssl_detection_pb2 import SSL_DetectionRobot as ssl_robot
from proto_compiled import messages_robocup_ssl_wrapper_pb2 as ssl_wrapper
from PySide6.QtNetwork import QUdpSocket, QHostAddress
from PySide6.QtCore import QByteArray


import threading, time

#TODO: Ver si es necesario eliminar robots
ListPackets = list([ssl_wrapper.SSL_WrapperPacket])
ListRobot = list([Robot])

class Vision:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, robots: ListRobot = []):
        self.ball = Ball()
        self.robots = {}
        self.udp_socket = QUdpSocket()

    def initSocket(self, multi_cast_address, port_ssl):
        self.udp_socket.bind(QHostAddress.AnyIPv4, port_ssl)
        self.udp_socket.joinMulticastGroup(QHostAddress(multi_cast_address))
        self.udp_socket.readyRead.connect(self.receive_vision_packets)

    def get_robots(self):
       # for robot in self.robots.values():
       #     print({"id ": robot.id , "team_id" : robot.team_id} )
        return self.robots.values()

    def get_ball(self):
        return self.ball

    def vision_loop(self):
        while True:
            self.receive_vision_packets()
            time.sleep(.016)

    def receive_vision_packets(self):
        packets = [] #lista de SSL_WrapperPackets   
        
        while self.udp_socket.hasPendingDatagrams():
            datagram = self.udp_socket.receiveDatagram()
            packet = ssl_wrapper.SSL_WrapperPacket()
            if(not packet.ParseFromString(datagram.data().data())):
                print('error')
            else:
                packets.append(packet)
        if len(packets) > 0:
            self.update(packets)

    def update(self, packets: ListPackets):
        self.reset_confidence()

        for packet in packets:
            det = packet.detection # paquete con detección desreferenciado
            #¿conviene mostrar camara_id de det.camera_id() ?
            
            for ball in det.balls:
                if ball.confidence >= self.ball.confidence:
                    self.ball.posx = ball.x
                    self.ball.posy = ball.y
                    self.ball.posz = ball.z
                    self.ball.confidence = ball.confidence
            
            for robot_data in det.robots_blue:
                robot_code = self.get_robot_code(robot_data.robot_id, "blue")
                if( self.robot_exist(robot_code) ):
                    self.update_robot(robot_data, robot_code)
                else:
                    new_robot = self.create_robot(robot_data, 1)
                    self.robots[robot_code] = new_robot 
            for robot_data in det.robots_yellow:
                robot_code = self.get_robot_code(robot_data.robot_id, "yellow")
                if( self.robot_exist(robot_code) ):
                    self.update_robot(robot_data, robot_code)
                else:
                    new_robot = self.create_robot(robot_data, 0)
                    self.robots[robot_code] = new_robot 


    def create_robot(self, robot_data: ssl_robot, team_id : int):
        new_robot = Robot()
        new_robot.team_id = team_id
        new_robot.confidence = robot_data.confidence
        new_robot.id = robot_data.robot_id
        new_robot.posx = robot_data.x
        new_robot.posy = robot_data.y
        new_robot.orientation = robot_data.orientation
        return new_robot

    def get_robot_code(self, robot_id : int, team : str) -> str:
        code = "y"
        if team == "blue":
            code = "b"
        num_zeros = 2 - len(str(robot_id))
        code = code + '0' * num_zeros + str(robot_id)
        return code


    def robot_exist(self, code : str) -> bool:
        if (code in self.robots):
            return True
        return False

    def get_robot(self, robot_code):
        return self.robots[robot_code]

    
    def reset_confidence(self):
        self.ball.confidence = .0
        for robot in self.get_robots():
            robot.confidence = .0
    

    # Entrega el robot y la posición de este
    def get_robot_by_id(self, id: int, team_id : str):
        robot = None
        if(team_id == "blue"):
            for robot in self.robots_yellow:
                if robot.id == id:
                    return robot
        elif(team_id == "yellow"):
            for robot in self.robots_blue:
                if robot.id == id:
                    return robot    
        return robot
    
    def update_robot(self, new_data: ssl_robot, robot_hash : str):
        self.robots[robot_hash].confidence = new_data.confidence
        self.robots[robot_hash].posx = new_data.x
        self.robots[robot_hash].posy = new_data.y
        self.robots[robot_hash].orientation = new_data.orientation

    
    def remove_robot(self, robots: ListRobot):
        new_robots = []
        i = 0
        for robot in robots:
            if robot.frames_from_last_update <= 3:
                new_robots.append(robot)
            i += 1
        return new_robots
