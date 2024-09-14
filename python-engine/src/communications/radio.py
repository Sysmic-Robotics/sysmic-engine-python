import threading
import time
import serial
import constants
import numpy as np
import pickle


class Radio:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.robotQueue = {'r0': [], 'r1': [], 'r2': [], 'r3': [], 'r4': [], 'r5': []}
        self.robotIds = {'r0': 0, 'r1': 1, 'r2': 2, 'r3': 3, 'r4': 4, 'r5': 5}
        self.verbose = False
        # Format for the queue
        '''
        r_queue = {
                    "drb": dribbler,
                    "kick": kicker,
                    "cb: call_back,
                    "x": x speed,
                    "y": y speed,
                    "r": rotational speed in rad/s}
        '''
        # se enlaza al puerto serial de la base station
        self.serial_port = serial.Serial(port= constants.SERIAL_PORT, baudrate=constants.BAUDRATE, timeout=constants.TIMEOUT)
        if not self.serial_port.is_open:
            raise ValueError("No se pudo abrir el puerto serial")
        
    
    #print data
    def send_data(self):
        packet = b''
        for rIndex in self.robotQueue.keys():
            robot_packet = np.zeros(5, dtype=np.uint8)
            if self.robotQueue[rIndex] != []:
                # Byte 0
                """
                3 bits para el ID del robot a la izquierda del byte
                3 bits para la fuerza del dribbler a la derecha del ID del robot
                1 bit para el kicker a la derecha de la fuerza del dribbler
                1 bit para el callback a la derecha del kicker
                """
                robot_packet[0] = self.robotIds[rIndex] << 5
                robot_packet[0] = robot_packet[0] | (self.robotQueue[rIndex][0]["drb"] << 2)
                robot_packet[0] = robot_packet[0] | (self.robotQueue[rIndex][0]["kick"] << 1)
                robot_packet[0] = robot_packet[0] | self.robotQueue[rIndex][0]["cb"]

                # Byte 1
                """
                1 bit para el signo de la velocidad x del robot a la izquierda del byte
                7 bits para la velocidad x del robot
                """
                if self.robotQueue[rIndex][0]["x"] < 0:
                    self.robotQueue[rIndex][0]["x"] = -self.robotQueue[rIndex][0]["x"]
                    robot_packet[1] = robot_packet[1] | (self.robotQueue[rIndex][0]["x"] & 0x7F)
                else:
                    robot_packet[1] = 1 << 7
                    robot_packet[1] = robot_packet[1] | (self.robotQueue[rIndex][0]["x"] & 0x7F)
                # Byte 2
                """
                1 bit para el signo de la velocia y del robot a la izquierda del byte
                7 bits para la velocidad (solo parte entera) y del robot
                """
                if self.robotQueue[rIndex][0]["y"] < 0:
                    robot_packet[2] = 1 << 7
                    self.robotQueue[rIndex][0]["y"] = -self.robotQueue[rIndex][0]["y"]
                    robot_packet[2] = robot_packet[2] | (self.robotQueue[rIndex][0]["y"] & 0x7F)
                else:
                    robot_packet[2] = robot_packet[2] | (self.robotQueue[rIndex][0]["y"] & 0x7F)
                
                # Byte 3
                """
                1 bit para el signo de la velocia rotacional del robot a la izquierda del byte
                7 bits para la velocidad rotacional del robot
                """
                if self.robotQueue[rIndex][0]["r"] < 0:
                    robot_packet[3] = 1 << 7
                    self.robotQueue[rIndex][0]["r"] = -self.robotQueue[rIndex][0]["r"]
                    robot_packet[3] = robot_packet[3] | (self.robotQueue[rIndex][0]["r"] & 0x7F)
                else:
                    robot_packet[3] = robot_packet[3] | (self.robotQueue[rIndex][0]["r"] & 0x7F)

                # Byte 4
                """
                2 bits de digitos significativos de la velocidad x del robot a la izquierda del byte
                2 bits de digitos significativos de la velocidad y del robot a la derecha de los digitos significativos de la velocidad x
                4 bits de digitos significativos de la velocidad rotacional del robot a la derecha de los digitos significativos de la velocidad y
                """
                # Convertir los digitos significativos a enteros
                robot_packet[4] = robot_packet[4] | ((self.robotQueue[rIndex][0]["x"] >> 7) << 6)
                robot_packet[4] = robot_packet[4] | ((self.robotQueue[rIndex][0]["y"] >> 7) << 4)
                robot_packet[4] = robot_packet[4] | ((self.robotQueue[rIndex][0]["r"] >> 7) & 0x0F)
                # print (robot_packet[4]) in binary
                robot_packet_bytes = bytearray(robot_packet.tobytes())
                self.robotQueue[rIndex].pop(0)
            else:
                # Si el robot no esta activo, enviar un paquete de ceros
                robot_packet[0] = self.robotIds[rIndex] << 5
                robot_packet[1] = 0
                robot_packet[2] = 0
                robot_packet[3] = 0
                robot_packet[4] = 0
            robot_packet_bytes = bytearray(robot_packet.tobytes())
            
            # Convertir el arreglo de bytes a un string
            # Convert each number in the array to its corresponding Unicode character
            # Encode the characters using UTF-8
            packet += robot_packet_bytes
        # Enviar el string al puerto serial
        self.serial_port.write(packet)
        if self.verbose:
            print(chr(27) + "[2J")

            for i in range(0, len(packet), 5):
                print("robot", i//5, "packet: ", end='')
                for j in range(0, 5):
                    print(format(packet[i+j], '08b'), end=' ')
                print()
        



    #print data every 1 second
    def send_loop(self)-> None:
        while True:
            self.send_data()
            time.sleep(.016)

    
    def add_to_robot_queue(self, robot_id, drb, kick, cb, x, y, r)-> None:
        message = {"x": x, "y": y, "r": r, "drb": drb, "kick": kick, "cb": cb}
        id = "r" + str(robot_id)
        self.robotQueue[id].append(message)

    
    def receive_data(self):
        # Recibir datos del puerto serial
        # NOTE: Aun no se aplica un uso definido para esta funcion
        serialized_data = self.serial_port.read(64)
        data = pickle.loads(serialized_data)
        return data


    def list_serial_ports(self)-> None:
        # Listar los puertos seriales disponibles
        ports = serial.tools.list_ports.comports()
        for port in ports:
            print(port.device)
