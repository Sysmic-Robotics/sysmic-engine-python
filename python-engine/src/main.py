#comunicación con protobuf
from classes.engine import Engine
from communications.vision import Vision
from communications.radio import Radio
import argparse
import threading
import time


#TODO: Agregar FPS

#capura de flag de equipo (-b o -y)
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--team", help="Team color", choices=['y', 'b'], default='b')
parser.add_argument("-v", "--vision", help="Verbose mode", action="store_true")

args = parser.parse_args()
blue_team = True
if args.team == 'y':
    blue_team = False

engine = Engine()
vision = Vision()
radio = Radio()
vision.initSocket(10020) #Socket for grSim (10020) or SSL_Vision (10006)
vision_t = threading.Thread(target=vision.vision_loop)
vision_t.start()
radio_t = threading.Thread(target=radio.send_loop)
radio_t.start()


engine.turn_on_off() #Turn on the engine
#engine.initSocket(10021) #10021 -> UI

#define if we are team yellow or blue with a flag
while engine.running:
    engine.test_vision()
    engine.test_radio()
    #engine.receive_ui_packets() #función no finalizada
    '''
    if args.vision:
        #radio communication pending
        pass
    else:
        engine.communicate_grsim()
    '''