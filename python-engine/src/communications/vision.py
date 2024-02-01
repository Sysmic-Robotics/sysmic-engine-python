from classes.detection import Ball, Robot
from proto_compiled.messages_robocup_ssl_detection_pb2 import SSL_DetectionRobot as ssl_robot
from proto_compiled import messages_robocup_ssl_wrapper_pb2 as ssl_wrapper
from PySide6.QtNetwork import QUdpSocket, QHostAddress
from PySide6.QtCore import QByteArray
import threading, time
#TODO: Ver si es necesario eliminar robots
ListPackets = list[ssl_wrapper.SSL_WrapperPacket]
ListRobot = list[Robot]

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
        self.robots_yellow = robots #Lista de robots amarillos
        self.robots_blue = robots #Lista de robots azules
        self.udp_socket = QUdpSocket()

    def initSocket(self, multi_cast_address, port_ssl):
        self.udp_socket.bind(QHostAddress.AnyIPv4, port_ssl)
        self.udp_socket.joinMulticastGroup(QHostAddress(multi_cast_address))
        self.udp_socket.readyRead.connect(self.receive_vision_packets)

    def get_robots(self):
        return self.robots_blue + self.robots_yellow 

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

            for robot in det.robots_blue:
                robot_act, pos = self.get_robot_by_id(self.robots_blue, robot.robot_id)
                if(not robot_act):
                    new_robot = self.create_robot(robot)
                    self.robots_blue.append(new_robot)
                elif(robot_act.confidence <= robot.confidence):
                    self.robots_blue[pos] = self.update_robot(robot)
                    #self.robots_yellow[pos].frames_from_last_update -= 1

            for robot in det.robots_yellow:
                robot_act, pos = self.get_robot_by_id(self.robots_yellow, robot.robot_id)
                if(not robot_act):
                    new_robot = self.create_robot(robot)
                    self.robots_yellow.append(new_robot)
                elif(robot_act.confidence <= robot.confidence):
                    self.robots_yellow[pos] = self.update_robot(robot)
                    #self.robots_yellow[pos].frames_from_last_update -= 1
            

        self.robots_blue = self.remove_robot(self.robots_blue)
        self.robots_yellow = self.remove_robot(self.robots_yellow)


    def reset_confidence(self):
        self.ball.confidence = .0

        for robot in self.robots_blue:
            robot.confidence = .0

        for robot in self.robots_yellow:
            robot.confidence = .0
    
    # Entrega el robot y la posición de este
    def get_robot_by_id(self, robots: ListRobot, id: int):
        i = 0
        for robot in robots:
            if robot.id == id:
                return robot, i
            i += 1
        return None, 0
    
    def create_robot(self, robot: ssl_robot):
        new_robot = Robot()
        new_robot.confidence = robot.confidence
        new_robot.id = robot.robot_id
        new_robot.posx = robot.x
        new_robot.posy = robot.y
        new_robot.orientation = robot.orientation
        return new_robot

    def update_robot(self, robot: ssl_robot):
        new_robot = Robot()
        new_robot.confidence = robot.confidence
        new_robot.posx = robot.x
        new_robot.posy = robot.y
        new_robot.orientation = robot.orientation
        return new_robot
    
    def remove_robot(self, robots: ListRobot):
        new_robots = []
        i = 0
        for robot in robots:
            if robot.frames_from_last_update <= 3:
                new_robots.append(robot)
            i += 1
        return new_robots
    
    def print_robot(self, index):
        print(self.robots_blue[index].posx,
              self.robots_blue[index].posy,
              self.robots_blue[index].orientation)