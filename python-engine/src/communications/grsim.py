import threading
from proto_compiled.grsim.grSim_Packet_pb2 import grSim_Packet
from proto_compiled.grsim.grSim_Commands_pb2 import grSim_Robot_Command as grSim_Command
from proto_compiled.grsim.grSim_Replacement_pb2 import grSim_Replacement, grSim_RobotReplacement
import time
from PySide6.QtNetwork import QHostAddress, QUdpSocket
from PySide6.QtCore import QByteArray
from classes.detection import Robot
import numpy
from scipy.spatial import distance
import math

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

        

    def navigate_robot(self,robot, id = 0, isteamyellow = 0,
                        x_target = 0, y_target = 0)-> None:
        
        x_target = x_target*1000
        y_target = y_target*1000

        ang_actual = robot.orientation #rad
        x_actual = robot.posx #mm
        y_actual = robot.posy #mm
        if y_target -y_actual > 0:
            ang_target =  math.atan2(y_target -y_actual ,x_target-x_actual)#rad
        else:
            ang_target = math.atan2(y_target -y_actual,x_target-x_actual)#rad

        err_angular = ang_target - ang_actual
        if abs(err_angular) > math.pi:
            if err_angular > 0:
                err_angular -= 2*math.pi
            else:
                err_angular += 2*math.pi
            
        #err_x = x_target - x_actual
        #err_y = y_target - y_actual
        err_eucl = distance.euclidean((robot.posx,robot.posy),(x_target,y_target))



        while abs(err_angular) > 0.001:
            
            if err_angular > 0:
                vel_ang=err_angular*0.8+0.1

            else:
                vel_ang=err_angular*0.8-0.1

            self.communicate_grsim(id = id, isteamyellow = isteamyellow, 
                        velangular = vel_ang, kickspeedx = 0, kickspeedz = 0,
                        veltangent = 0, velnormal = 0, spinner = 0,
                        wheelsspeed = False)
                
            err_angular = ang_target - robot.orientation
            if abs(err_angular) > math.pi:
                if err_angular > 0:
                    err_angular -= 2*math.pi
                else:
                    err_angular += 2*math.pi

        self.communicate_grsim(id = id, isteamyellow = isteamyellow, 
                          velangular = 0, kickspeedx = 0, kickspeedz = 0,
                          veltangent = 0, velnormal = 0, spinner = 0,
                          wheelsspeed = False)

        while abs(err_eucl) > 50:
            vel_tan=err_eucl*0.0015
            self.communicate_grsim(id = id, isteamyellow = isteamyellow, 
                            velangular = 0, kickspeedx = 0, kickspeedz = 0,
                            veltangent = vel_tan, velnormal = 0, spinner = 0,
                            wheelsspeed = False)
            err_eucl = distance.euclidean((robot.posx,robot.posy),(x_target,y_target))
            
            
        self.communicate_grsim(id = id, isteamyellow = isteamyellow, 
                          velangular = 0, kickspeedx = 0, kickspeedz = 0,
                          veltangent = 0, velnormal = 0, spinner = 0,
                          wheelsspeed = False)

    def path_navigate_robot(self,robot,path : list=[], id = 0, isteamyellow = 0)-> None:
        for i in path:
            self.navigate_robot(robot, id = id, isteamyellow = isteamyellow,
                        x_target = i[0], y_target = i[1])