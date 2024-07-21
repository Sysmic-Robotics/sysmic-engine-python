# Interfaz de la radio para comunicarse con sim y cancha . 
#Esto es para evitar la divergencia entre codigo simulador y cancha
from communications.grsim import Grsim
from constants import *
import math

class CommandSender:
    def __init__(self) -> None:
        if COMMUNICATION_MODE == 1:
            self.grsim = Grsim()

    def send_robot_data(self, id = 0, is_blue = 0, 
                          velangular = 0, kickspeedx = 0, kickspeedz = 0,
                          veltangent = 0, velnormal = 0, spinner = 0,
                          wheelsspeed = False) -> None:
        if COMMUNICATION_MODE == 1:
            isteamyellow = 1 - is_blue
            self.grsim.communicate_grsim(id, isteamyellow, velangular, 
                                         kickspeedx, kickspeedz, veltangent, velnormal, spinner,
                                         wheelsspeed)     
    
