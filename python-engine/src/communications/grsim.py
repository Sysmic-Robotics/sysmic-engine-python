import threading
from proto_compiled.grsim.grSim_Packet_pb2 import grSim_Packet
from proto_compiled.grsim.grSim_Commands_pb2 import grSim_Robot_Command as grSim_Command
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

    def communicate_grsim(self):
        package = grSim_Packet()
        command = grSim_Command()

        command.id = 0
        command.velangular = 10
        command.kickspeedx = 0
        command.kickspeedz = 0
        command.veltangent = 0
        command.velnormal = 0
        command.spinner = 0
        command.wheelsspeed = 0
        
        package.commands.robot_commands.append(command)
        package.commands.timestamp = 0
        package.commands.isteamyellow = 0
            
        data = package.SerializeToString(True)
        if data:
            msg = QByteArray(data)
            self.send_socket.writeDatagram(msg, QHostAddress.SpecialAddress.LocalHost, 20011) 