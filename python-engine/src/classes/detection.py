'''Clases detection SSL Vision'''
import numpy as np
HEIGHT = 600 #altura de cada robot

class Ball:
    '''Clase que representa un balon, con sus atributos de posicion y confianza'''
    def __init__(self):
        #veracidad de los datos recibidos va entre 0 y 1
        self.confidence = .0
        #posicion del balon en el campo
        self.posx = .0
        self.posy = .0
        self.posz = .0
        
class Robot:
    '''Clase que representa un robot, con sus atributos de posicion y confianza'''
    def __init__(self):
        self.id = 0
        #posicion del robot en el campo
        self.posx = .0 #mm
        self.posy = .0 #mm
        self.orientation = .0 #rad
        #equipo al que pertenece
        self.team = 0 #0 para amarillo, 1 para azul

        #veracidad de los datos recibidos
        self.confidence = .0
        self.frame_number = .0

        self.frames_from_last_update = 0

'''
class Frame:
    #Clase que representa un frame
    def __init__(self, frame_number,
                t_capture,t_sent, camera_id,
                balls, robots_yellow, robots_blue):
        #numero de frame
        self.frame_number = 0
        #tiempo de captura
        self.t_capture = np.float16(0)
        #tiempo de envio
        self.t_sent = np.float16(0)
        #id de la camara
        self.camera_id = 0
        #lista de balones
        self.balls = Ball()
        #lista de robots amarillos
        self.robots_yellow = robots_yellow
        #lista de robots azules
        self.robots_blue = robots_blue
'''
