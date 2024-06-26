import socket
import proto_compiled.algo_commander_pb2 as algo_commander_pb2
from PySide6.QtNetwork import QUdpSocket,  QHostAddress
from path_planning.path_planning import PathPlanning
from communications.vision import Vision
import time

class AlgoCommander:
    def __init__(self, port, vision) -> None:
        self.host = '127.0.0.1'  # Change this to your desired destination IP address
        self.port = port        # Change this to your desired destination port number
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.vision = vision

        self.server_socket = QUdpSocket()
        #self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind(QHostAddress.AnyIPv4, 5656)
        self.server_socket.readyRead.connect(self.receive_packets)
        print("receiving packet init")

    def update(self):
        while True:
            self.receive_packets()
            robots = self.vision.get_robots()
            for robot in robots:
                if(robot != None):
                    blue_team = robot.team_id == 1
                    self.send_robot_position(robot.id, robot.posx, robot.posy, robot.orientation, blue_team)
            time.sleep(0.016)    

    def receive_packets(self):
        while self.server_socket.hasPendingDatagrams():
 
            datagram = self.server_socket.receiveDatagram()
            packets = []
            packet = algo_commander_pb2.RequestPath()
            
            packet.ParseFromString( datagram.data().data()  )
            if(not packet):
                print('error')
            else:
                self.receive_request_route(packet)
                packets.append(packet)
    
    def receive_request_route(self, request_path : algo_commander_pb2.RequestPath):
        from_point = (request_path.from_point.x, request_path.from_point.y)
        to_point = (request_path.to_point.x, request_path.to_point.y) 
        print(from_point, to_point)
        path_planning = PathPlanning(self.vision)
        self.send_route(0, True,path_planning.get_path(from_point, to_point))

 
    def send_robot_position(self, robot_id, pos_x, pos_y, angle, blue_team):
        wrapper = algo_commander_pb2.WrapperMessage()
        wrapper.commonField = 0
        # Create a RobotPosition message
        robot_position = algo_commander_pb2.RobotPosition()
        robot_position.id = robot_id
        robot_position.pos_x = pos_x
        robot_position.pos_y = pos_y
        robot_position.angle = angle
        robot_position.blue_team = blue_team

        wrapper.robot_position.CopyFrom(robot_position)
        serialized_data = wrapper.SerializeToString()
        try:
            # Send the serialized data
            self.socket.sendto(serialized_data, (self.host, self.port))
        finally:
            pass
            
    def send_route(self, robot_id : int, is_blue_team : bool, new_route : tuple[float,float]):
        wrapper = algo_commander_pb2.WrapperMessage()
        wrapper.commonField = 0
        #Create route
        route = algo_commander_pb2.Route()
        for point in new_route:
            new_point = route.points.add()
            new_point.x = point[0]
            new_point.y = point[1]
        route.robot_id = robot_id
        route.blue_team = is_blue_team
        wrapper.route.CopyFrom(route) 
        serialized_data = wrapper.SerializeToString()   
        try:
            # Send the serialized data
            self.socket.sendto(serialized_data, (self.host, self.port))
        finally:
            pass  
    
    def __del__(self):
        self.socket.close()   