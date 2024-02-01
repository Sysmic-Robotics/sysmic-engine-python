#comunicación con protobuf
from classes.engine import Engine
from communications.vision import Vision
from communications.radio import Radio
from communications.grsim import Grsim
import argparse
import threading
import time
from stp_architecture.stp_manager import STP

#TODO: Agregar FPS

if __name__ == '__main__':

    #capura de flag de equipo (-b o -y)
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--team", help="Team color", choices=['y', 'b'], default='b')
    parser.add_argument("-v", "--vision", help="Verbose mode", action="store_true")

    args = parser.parse_args()
    blue_team = True
    if args.team == 'y':
        blue_team = False

    ########################################################################
    # True = simulación en grsim
    # False = Uso de radio
    ########################################################################
    grsim = True

    if grsim:
        #radio = Grsim()
        #radio_t = threading.Thread(target=radio.comm_loop)
        #radio_t.start() 
        pass
    else:
        #radio = Radio()
        #radio_t = threading.Thread(target=radio.send_loop)
        #radio_t.start()
        pass

    vision = Vision()
    vision.initSocket("224.5.23.2", 10020) #Socket for grSim (10020) or SSL_Vision (10006)
    vision_t = threading.Thread(target=vision.vision_loop)
    vision_t.start()
    # Initialize grsim packets
    #radio = Grsim()
    #radio.communicate_grsim(id=1, isteamyellow=0, spinner=1, velnormal=2)
    
    engine = Engine(vision)

    while engine.running:
        #engine.test_radio()
        engine.test_grsim()
        '''
        if args.vision:
            #radio communication pending
            pass
        else:
            engine.communicate_grsim()
        '''