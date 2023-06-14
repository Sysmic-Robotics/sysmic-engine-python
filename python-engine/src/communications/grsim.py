import threading
from proto_compiled.grsim.grSim_Packet_pb2 import grSim_Packet
from proto_compiled.grsim.grSim_Commands_pb2 import grSim_Robot_Command as grSim_Command
from proto_compiled.grsim.grSim_Replacement_pb2 import grSim_Replacement, grSim_RobotReplacement
import time
from PySide6.QtNetwork import QHostAddress, QUdpSocket
from PySide6.QtCore import QByteArray

class Grsim:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self) -> None:
        self.send_socket = QUdpSocket()

    def comm_loop(self):
        while True:
            self.communicate_grsim()
            time.sleep(0.016)

    def communicate_grsim(self, id = 0, isteamyellow = 0, 
                          velangular = 0, kickspeedx = 0, kickspeedz = 0,
                          veltangent = 0, velnormal = 0, spinner = 0,
                          wheelsspeed = False) -> None:
        
        package = grSim_Packet()
        command = grSim_Command()

        command.id = id
        command.velangular = velangular
        command.kickspeedx = kickspeedx
        command.kickspeedz = kickspeedz
        command.veltangent = veltangent
        command.velnormal = velnormal
        command.spinner = spinner
        command.wheelsspeed = wheelsspeed
        
        package.commands.robot_commands.append(command)
        package.commands.timestamp = 0
        package.commands.isteamyellow = isteamyellow
            
        data = package.SerializeToString(True)
        if data:
            msg = QByteArray(data)
            self.send_socket.writeDatagram(msg, QHostAddress.SpecialAddress.LocalHost, 20011) 

    # dir es con ángulo

    def communicate_pos_robot(self, id = 0, yellowteam = 0, 
                        x = 0, y = 0, dir = 0) -> None:
        
        package = grSim_Packet()
        command = grSim_RobotReplacement()

        command.id = id
        command.x = x
        command.y = y
        command.dir = dir
        command.yellowteam = yellowteam

        package.replacement.robots.append(command)
            
        data = package.SerializeToString(True)
        if data:
            msg = QByteArray(data)
            self.send_socket.writeDatagram(msg, QHostAddress.SpecialAddress.LocalHost, 20011) 