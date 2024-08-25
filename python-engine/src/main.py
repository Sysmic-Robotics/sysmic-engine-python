from communications.grsim import Grsim
from world.world import World
from world.entities import Robot
import time
from navigation.navigator import Navigator
from communications.wrapper import CommandSender
from stp.move import Move
import math

def main():
    # Inicializar los componentes necesarios
    grsim = Grsim()
    world = World()
    navigator = Navigator()
    command_sender = CommandSender()

    # Crear un robot y añadirlo al mundo
    robot = Robot(id=1, team='yellow')
    world.add_robot(robot)

    # Definir el punto al que queremos mover el robot
    target_point = (0.5, 0.5)

    # Mover el robot al punto especificado
    Move.move_to_point(robot, target_point, navigator, command_sender)

    # Esperar un tiempo para observar el movimiento
    time.sleep(5)

if __name__ == '__main__':
    main()