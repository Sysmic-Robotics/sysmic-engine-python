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
        self.robots = {}
        self.udp_socket = QUdpSocket()

    def initSocket(self, multi_cast_address, port_ssl):
        self.udp_socket.bind(QHostAddress.AnyIPv4, port_ssl)
        self.udp_socket.joinMulticastGroup(QHostAddress(multi_cast_address))
        self.udp_socket.readyRead.connect(self.receive_vision_packets)

    def get_robots(self):
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

            n_robots_blue = len(det.robots_blue)
            robots = det.robots_yellow
            robots.extend(det.robots_blue)
            team_id = 0 # Yellow
            i = 0
            #clean_deprecated_robots()
            for robot in robots:
                if(i > n_robots_blue - 1):
                    team = 1
                robot_act = self.get_robot_by_id(robot.robot_id)
                if(not robot_act):
                    new_robot = self.create_robot(robot, team_id)
                    self.robots[robot.robot_id] = new_robot
                elif(robot_act.confidence <= robot.confidence):
                    self.update_robot(robot, robot.robot_id)
                i += 1    

    def reset_confidence(self):
        self.ball.confidence = .0
        for id in self.robots:
            self.robots[id].confidence = .0

    # Entrega el robot y la posición de este
    def get_robot_by_id(self, id: int):
        if( id in self.robots ):
            return self.robots[id]
        return None
    
    def create_robot(self, robot: ssl_robot, team_id):
        new_robot = Robot()
        new_robot.confidence = robot.confidence
        new_robot.id = robot.robot_id
        new_robot.posx = robot.x
        new_robot.posy = robot.y
        new_robot.orientation = robot.orientation
        new_robot.team_id = team_id
        return new_robot

    def update_robot(self, robot: ssl_robot, id : int):
        new_robot = self.robots[id]
        new_robot.confidence = robot.confidence
        new_robot.posx = robot.x
        new_robot.posy = robot.y
        new_robot.orientation = robot.orientation
        return new_robot
    
    def clean_outdated_robots(self):
        pass
    
    def print_robot(self, index):
        print(self.robots_blue[index].posx,
              self.robots_blue[index].posy,
              self.robots_blue[index].orientation)