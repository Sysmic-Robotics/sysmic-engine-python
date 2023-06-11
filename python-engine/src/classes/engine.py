import time
from PySide6.QtNetwork import QUdpSocket, QHostAddress
from PySide6.QtCore import QByteArray
from proto_compiled import messages_robocup_ssl_wrapper_pb2 as ssl_wrapper
from communications.vision import Vision
from proto_compiled import ui_messages_pb2 as ui_messages
from communications.radio import Radio

from proto_compiled.grsim.grSim_Packet_pb2 import grSim_Packet
from proto_compiled.grsim.grSim_Replacement_pb2 import *

class Engine:

    def __init__(self):
        self.running = False
        self.vision_socket = QUdpSocket()
        self.ui_socket = QUdpSocket()
        self.vision = Vision()
        self.send_socket = QUdpSocket()

    def initSocket(self, port_ui):
        print(self.ui_socket.bind(QHostAddress.SpecialAddress.LocalHost, port_ui)) #UI 

    def test_vision(self):
        print(self.vision.ball.posx)

    def test_radio(self):
        instance = Radio()
        n = 10
        while n != 0:
            timeout = time.time() + 3
            while True:
                instance.recive_message(1,1,1,1,1,1,'r0')
                if time.time() > timeout:
                    break
                time.sleep(.016)
            timeout = time.time() + 3
            while True:
                instance.recive_message(1,1,1,1,1,1,'r1')
                if time.time() > timeout:
                    break
                time.sleep(.016)
            n -= 1


        
        time.sleep(1)
        instance.recive_message(1,1,1,1,1,1,'r1')
        


    # Paquetes recibidos desde UI 
    def receive_ui_packets(self):
        while self.ui_socket.hasPendingDatagrams():
            datagram = self.ui_socket.receiveDatagram()
            
            command = ui_messages.Command()
            if(not command.ParseFromString(datagram.data().data())):
                print('error')
            else:
                #TODO
                print("hacer algo")    

    # Paquetes a enviar
    def communicate_grsim(self):
        # package = ui_messages.EnginePackage.vision()
        package = grSim_Packet()

        package.replacement.ball.x = 0
        package.replacement.ball.y = 0
        package.replacement.ball.vx = 0
        package.replacement.ball.vy = 0

        # TODO: Está hecho para un solo robot

        '''
        i = 0
        for robot in self.vision.robots_blue:
            package.blue_robots[i].id = robot.id
            package.blue_robots[i].x = robot.posx
            package.blue_robots[i].y = robot.posy
            package.blue_robots[i].orientation = robot.orientation
            i += 1
        '''
        robot = grSim_RobotReplacement()

        robot.id = 0
        robot.x = 0
        robot.y = 0
        robot.dir = 90
        robot.yellowteam = False

        package.replacement.robots.append(robot)

        '''
        i = 0
        for robot in self.vision.robots_yellow:
            package.yellow_robots[i].id = robot.id
            package.yellow_robots[i].x = robot.posx
            package.yellow_robots[i].y = robot.posy
            package.yellow_robots[i].orientation = robot.orientation
            i += 1  
        '''
            
        data = package.SerializeToString(True)
        if data:
            msg = QByteArray(data)
            self.send_socket.writeDatagram(msg, QHostAddress.SpecialAddress.LocalHost, 20011)        

    def turn_on_off(self):
        self.running = not self.running
