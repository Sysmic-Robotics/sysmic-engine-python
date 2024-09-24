# Recibe los packetes de la camara y guarda los datos en crudo
from proto_compiled.messages_robocup_ssl_detection_pb2 import SSL_DetectionRobot
from proto_compiled.messages_robocup_ssl_detection_pb2 import SSL_DetectionBall
from proto_compiled import messages_robocup_ssl_wrapper_pb2 as ssl_wrapper
from PySide6.QtNetwork import QUdpSocket, QHostAddress
import threading, time
from world.world import World

#TODO: Ver si es necesario eliminar robots
ListPackets = list[ssl_wrapper.SSL_WrapperPacket]

class Vision:
    # NOSE QUE HACE ESTO DE ABAJO
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
        return cls._instance
    # ACA NOSE

    def __init__(self, multi_cast_address, port_ssl, world : World):
        self.world = world
        self.ball : SSL_DetectionBall = SSL_DetectionBall()
        self.robots_blue : list[SSL_DetectionRobot] = []
        self.robots_yellow : list[SSL_DetectionRobot] = []
        self.udp_socket = QUdpSocket()
        self.udp_socket.bind(QHostAddress.AnyIPv4, port_ssl)
        self.udp_socket.joinMulticastGroup(QHostAddress(multi_cast_address))


    def loop(self):
        while True:
            self.receive_vision_packets()
            time.sleep(.016)


    def receive_vision_packets(self):
        packets : ListPackets = [] #lista de SSL_WrapperPackets   
        while self.udp_socket.hasPendingDatagrams():
            datagram = self.udp_socket.receiveDatagram()
            packet = ssl_wrapper.SSL_WrapperPacket()
            if(not packet.ParseFromString(datagram.data().data())):
                print('Error receive_vision_packets cant parse packet')
            else:
                packets.append(packet)
        if len(packets) > 0:
            self.update(packets)


    def update(self, packets: ListPackets):
        #self.reset_confidence()
        for packet in packets:
            det = packet.detection # paquete con detección desreferenciado
            # Update ball
            for ball in det.balls:
                if ball.confidence >= self.ball.confidence:
                    self.ball = ball
            # Update robots
            self.robots_blue.clear()
            for robot_data in det.robots_blue:
                self.robots_blue.append(robot_data)
            
            self.robots_yellow.clear()
            for robot_data in det.robots_yellow:
                self.robots_yellow.append(robot_data)
            
            self.update_world(self.robots_blue, self.robots_yellow, self.ball)
    
    def update_world(self, blue, yellow, ball):
        for robot in blue:
            self.world.update_robot(1, robot.robot_id, robot.x, robot.y, robot.orientation, robot.confidence)
        
        for robot in yellow:
            self.world.update_robot(0, robot.robot_id, robot.x, robot.y, robot.orientation, robot.confidence)

    def get_robots_blue(self):
        return self.robots_blue

    def get_robots_yellow(self):
        return self.robots_yellow

    def get_ball(self):
        return self.ball

    #def reset_confidence(self):
    #    self.ball.confidence = .0
    #    for robot in self.get_robots():
    #        robot.confidence = .0
