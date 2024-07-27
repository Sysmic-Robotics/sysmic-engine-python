# Interfaz de la radio para comunicarse con sim y cancha . 
#Esto es para evitar la divergencia entre codigo simulador y cancha
from communications.grsim import Grsim
import configparser
from pathlib import Path
import math

class CommandSender:
    def __init__(self) -> None:
        config = configparser.ConfigParser()
        config_path = Path(__file__).parent.parent / 'config.ini'
        config.read(config_path)

        Communication_Mode = config.getint('Network', 'Communication_Mode')
        if Communication_Mode == 1:
            self.grsim = Grsim()

    def send_robot_data(self, id = 0, is_blue = 0, 
                          velangular = 0, kickspeedx = 0, kickspeedz = 0,
                          veltangent = 0, velnormal = 0, spinner = 0,
                          wheelsspeed = False) -> None:
        config = configparser.ConfigParser()
        config_path = Path(__file__).parent.parent / 'config.ini'
        config.read(config_path)

        Communication_Mode = config.getint('Network', 'Communication_Mode')
        if Communication_Mode == 1:
            isteamyellow = 1 - is_blue
            self.grsim.communicate_grsim(id, isteamyellow, velangular, 
                                         kickspeedx, kickspeedz, veltangent, velnormal, spinner,
                                         wheelsspeed)     
    