
import pickle
import numpy as np
import constants
import serial
import serial.tools.list_ports

def list_serial_ports():
    # Listar los puertos seriales disponibles
    ports = serial.tools.list_ports.comports()
    for port in ports:
        print(port.device)

class USBSerial:
    def __init__(self):
        self.serial_port = serial.Serial(port= constants.SERIAL_PORT, baudrate=constants.BAUDRATE, timeout=constants.TIMEOUT)
        if not self.serial_port.is_open:
            raise ValueError("No se pudo abrir el puerto serial")
        else:
            print("Puerto serial abierto")

    def receive_data(self):
        # Recibir datos del puerto serial
        # NOTE: Aun no se aplica un uso definido para esta funcion
        serialized_data = self.serial_port.read(64)
        data = pickle.loads(serialized_data)
        return data

    def send_data(self, active_robot: np.ndarray, x_array: np.ndarray, y_array: np.ndarray, rot_array: np.ndarray, kicker: np.ndarray, dribbler: np.ndarray,call_back: np.ndarray) -> str:
        packet = b''
        for index, robot in enumerate(active_robot):

            robot_packet = np.zeros(5, dtype=np.uint8)
            if robot == 1:
                # Byte 0
                """
                3 bits para el ID del robot a la izquierda del byte
                3 bits para la fuerza del dribbler a la derecha del ID del robot
                1 bit para el kicker a la derecha de la fuerza del dribbler
                1 bit para el callback a la derecha del kicker
                """
                robot_packet[0] = index << 5
                robot_packet[0] = robot_packet[0] | (dribbler[index] << 2)
                robot_packet[0] = robot_packet[0] | (kicker[index] << 1)
                robot_packet[0] = robot_packet[0] | call_back[index]

                # Byte 1
                """
                1 bit para el signo de la velocia x del robot a la izquierda del byte
                7 bits para la velocidad x del robot
                """
                if x_array[index] < 0:
                    x_array[index] = -x_array[index]
                    robot_packet[1] = robot_packet[1] | (x_array[index] & 0x7F)
                else:
                    robot_packet[1] = 1 << 7
                    robot_packet[1] = robot_packet[1] | (x_array[index] & 0x7F)
                # Byte 2
                """
                1 bit para el signo de la velocia y del robot a la izquierda del byte
                7 bits para la velocidad (solo parte entera) y del robot
                """
                if y_array[index] < 0:
                    robot_packet[2] = 1 << 7
                    y_array[index] = -y_array[index]
                    robot_packet[2] = robot_packet[2] | (y_array[index] & 0x7F)
                else:
                    robot_packet[2] = robot_packet[2] | (y_array[index] & 0x7F)
                
                # Byte 3
                """
                1 bit para el signo de la velocia rotacional del robot a la izquierda del byte
                7 bits para la velocidad rotacional del robot
                """
                if rot_array[index] < 0:
                    robot_packet[3] = 1 << 7
                    rot_array[index] = -rot_array[index]
                    robot_packet[3] = robot_packet[3] | (rot_array[index] & 0x7F)
                else:
                    robot_packet[3] = robot_packet[3] | (rot_array[index] & 0x7F)

                # Byte 4
                """
                2 bits de digitos significativos de la velocidad x del robot a la izquierda del byte
                2 bits de digitos significativos de la velocidad y del robot a la derecha de los digitos significativos de la velocidad x
                4 bits de digitos significativos de la velocidad rotacional del robot a la derecha de los digitos significativos de la velocidad y
                """
                sig_digi_x = x_array[index] - np.int32(x_array[index])
                sig_digi_y = y_array[index] - np.int32(y_array[index])
                sig_digi_rot = rot_array[index] - np.int32(rot_array[index])
                # Convertir los digitos significativos a enteros
                robot_packet[4] = robot_packet[4] | ((x_array[index] >> 7) << 6)
                robot_packet[4] = robot_packet[4] | ((y_array[index] >> 7) << 4)
                robot_packet[4] = robot_packet[4] | ((rot_array[index] >> 7) & 0x0F)
                # print (robot_packet[4]) in binary
                robot_packet_bytes = bytearray(robot_packet.tobytes())
            else:
                # Si el robot no esta activo, enviar un paquete de ceros
                robot_packet[0] = index << 5
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
        # print (packet) in binary inserting a line break after every 8 bits and a line break after every 5 bytes and clear the screen before printing

        #screen clear
        print(chr(27) + "[2J")

        for i in range(0, len(packet), 5):
            print("robot", i//5, "packet: ", end='')
            for j in range(0, 5):
                print(format(packet[i+j], '08b'), end=' ')
            print()
        #print(repr(packet))
        return packet
        