#comunicación con protobuf
from classes.engine import Engine
from classes.vision import Vision
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
vision.initSocket(10020) #Socket for grSim (10020) or SSL_Vision (10006)
t = threading.Thread(target=vision.vision_loop)
t.start()

engine.turn_on_off() #Turn on the engine
#engine.initSocket(10021) #10021 -> UI

#define if we are team yellow or blue with a flag
while engine.running:
    engine.test_vision()
    #engine.receive_ui_packets() #función no finalizada
    '''
    if args.vision:
        #radio communication pending
        pass
    else:
        engine.communicate_grsim()
    '''