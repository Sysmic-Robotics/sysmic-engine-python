# Interfaz de la radio para comunicarse con sim y cancha . 
#Esto es para evitar la divergencia entre codigo simulador y cancha
from communications.grsim import Grsim
from communications.radio import Radio
from constants import *
import math

class CommandSender:
    def __init__(self) -> None:
        self.data_packet = [[0] * 7 for _ in range(6)]  # Lista de listas 5x6 para enviar a los robots
        
        if COMMUNICATION_MODE == 1:
            self.grsim = Grsim()
            self.kickspeedx = 0
            self.kickspeedz = 0
            self.veltangent = 0
            self.wheelsspeed = False
        else:
            self.radio = Radio()
    
    
    # LLena el paquete de datos para enviar a los robots
    def add_robot_data(self, id=0, velangular=0, veltangent=0,
                            velnormal=0, dribbler=0, kicker=0,
                            call_back=0) -> None:
        if id < 0 or id > 5:
            raise ValueError("Robot id out of range")
        
        if COMMUNICATION_MODE == 1:
            self.data_packet[id] = [id, dribbler, kicker, call_back, veltangent, velnormal, velangular]
        else:
            self.radio.add_to_robot_queue(id, dribbler, kicker, call_back, veltangent, velnormal, velangular) 
            
    
        
    
    # Envía el paquete de datos a los robots en cancha o simulador segun corresponda
    def send_robot_packet(self) -> None:
        if COMMUNICATION_MODE == 1:
            for id in range(6):
                self.grsim.communicate_grsim(
                    id=id, 
                    isteamyellow=ISTEAMYELLOW, 
                    velangular=self.data_packet[id][6], 
                    veltangent=self.data_packet[id][4], 
                    velnormal=self.data_packet[id][5], 
                    spinner=self.data_packet[id][1],
                    kickspeedx=self.kickspeedx,
                    kickspeedz=self.kickspeedz,
                    wheelsspeed=self.wheelsspeed
                )

        else:
            self.radio.send_data()

        self.data_packet = [[0] * 7 for _ in range(6)] # Reinicia el paquete de datos

    # Envía un paquete de datos a un solo robot        
    def send_solo_robot_packet(self, id=0, velangular=0, veltangent=0,
                            velnormal=0, dribbler=0, kicker=0,
                            call_back=0) -> None:
        if id < 0 or id > 5:
            raise ValueError("Robot id out of range")
        
        if COMMUNICATION_MODE == 1:
            self.grsim.communicate_grsim(
                id=id, 
                isteamyellow=ISTEAMYELLOW, 
                velangular=velangular, 
                veltangent=veltangent, 
                velnormal=velnormal, 
                spinner=dribbler,
                kickspeedx=self.kickspeedx,
                kickspeedz=self.kickspeedz,
                wheelsspeed=self.wheelsspeed
            )
        else:
            self.radio.add_to_robot_queue(id, dribbler, kicker, call_back, veltangent, velnormal, velangular) 
            self.radio.send_data()
