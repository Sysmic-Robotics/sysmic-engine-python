from communications.grsim import Grsim
from world.world import World
import threading
import time

if __name__ == '__main__':
    # Initialize grsim packets
    radio = Grsim()
    # Por alguna razon grsim no envia packetes sin haber recibido ninguno
    radio.communicate_pos_robot(id=0, yellowteam=0,x = 0, y= 0)

    world : World = World(6,6)


    
    time.sleep(1) # Wait for vision to start get data

