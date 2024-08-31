from communications.grsim import Grsim
from world.world import World
from world.entities import Robot
import time
from navigation.navigator import Navigator
from communications.wrapper import CommandSender
from stp.move import Move
import math

def main():
    # Codigo de prueba de wrapper y radio
    command_sender = CommandSender()

    #Enviar mensaje de prueba a robot 0 por radio
    command_sender.send_solo_robot_packet(id=0, veltangent=40)

    # Esperar un tiempo para observar el movimiento
    time.sleep(5)

    
    # Enviar mensaje de parada a robot 0 por radio
    command_sender.send_solo_robot_packet(id=0, veltangent=0)

    

if __name__ == '__main__':
    main()