#comunicación con protobuf
from classes.engine import Engine
from communications.vision import Vision
from communications.radio import Radio
from communications.grsim import Grsim
from classes.detection import Robot
import argparse
import threading
import time
from stp_architecture.stp_manager import STP
from communications.algo_commander import AlgoCommander

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

    vision : Vision = Vision()
    vision.initSocket("224.5.23.2", 10020) #Socket for grSim (10020) or SSL_Vision (10006)
    vision_t = threading.Thread(target=vision.vision_loop)
    vision_t.start()

    # Initialize grsim packets
    radio = Grsim()
    radio.communicate_grsim(id=1, isteamyellow=0, spinner=1, velnormal=2)
    
    # Algo Commander: Visualization system
    algo_commander = AlgoCommander(12345, vision)
    algo_commander_t = threading.Thread(target=algo_commander.update)
    algo_commander_t.start()

    stp = STP(vision, algo_commander)
    engine = Engine(vision, stp)

    # Test path planning

    radio.communicate_pos_robot(id=0, yellowteam=0 ,x = 4.000, y= 0)
    time.sleep(1) # Wait for vision to start get data
    
    code = vision.get_robot_code(0, "blue")
    robot : Robot = vision.get_robot(code)
    path_planning : PathPlanning = PathPlanning(vision)
    path : tuple[float, float] = path_planning.get_path( (robot.posx,robot.posy) , (0,0) )
    algo_commander.send_route( 0, True, path ) 

    stp.follow_path(robot , path)
    while engine.running:
        break
    #    engine.test_grsim()
