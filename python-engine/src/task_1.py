from communications.grsim import Grsim
import keyboard

# Crear el objeto para comunicarse con GrSim
radio = Grsim()

vel_x = 2
vel_y = 2

# Función para mover el robot
def move_robot():
    global vel_x, vel_y
    print(f"Moviendo el robot con vel_x: {vel_x}, vel_y: {vel_y}")  # Mensaje de depuración
    radio.communicate_grsim(id=3, isteamyellow=0, velnormal=vel_x, veltangent=vel_y)

# Función para detectar las teclas
def handle_keys():
    global vel_x, vel_y
    if keyboard.is_pressed('up'):
        vel_y = 1
    elif keyboard.is_pressed('w'):
        vel_y = 1
    elif keyboard.is_pressed('down'):
        vel_y = -1
    elif keyboard.is_pressed('s'):
        vel_y = -1
    else:
        vel_y = 0

    if keyboard.is_pressed('left'):
        vel_x = -1
    elif keyboard.is_pressed('a'):
        vel_y = -1
    elif keyboard.is_pressed('right'):
        vel_x = 1
    elif keyboard.is_pressed('d'):
        vel_y = 1
    else:
        vel_x = 0

    # Detener el robot si se presiona ESC
    if keyboard.is_pressed('esc'):
        print("Programa detenido")
        exit()  # Salir del programa

# Bucle principal
while True:
    handle_keys()  # Leer las teclas
    move_robot()   # Mover el robot
