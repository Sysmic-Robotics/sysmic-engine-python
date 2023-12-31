import time
from PySide6.QtNetwork import QUdpSocket, QHostAddress
from communications.vision import Vision
from proto_compiled import ui_messages_pb2 as ui_messages
from communications.radio import Radio
from communications.grsim import Grsim

class Engine:

    def __init__(self):
        self.running = False
        self.vision_socket = QUdpSocket()
        self.ui_socket = QUdpSocket()
        self.vision = Vision()
        self.grsim = Grsim()

    def initSocket(self, port_ui):
        print(self.ui_socket.bind(QHostAddress.SpecialAddress.LocalHost, port_ui)) #UI 

    def test_vision(self):
        print(self.vision.ball.posx)

    def test_grsim(self):
        positioned = False

        if not positioned:
            self.grsim.communicate_pos_robot(id=1, yellowteam=0, x=0.8, y=-0.3, dir=180)
            positioned = True
        
        self.grsim.communicate_grsim(id=1, isteamyellow=0, spinner=1)
        self.grsim.communicate_grsim(id=0, isteamyellow=0, kickspeedx=4)
        
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
       

    def turn_on_off(self):
        self.running = not self.running
