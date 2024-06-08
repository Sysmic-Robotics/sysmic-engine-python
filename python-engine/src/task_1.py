from communications.grsim import Grsim
import keyboard
import threading
import time

radio = Grsim()
velocidad = 1000  # Incrementa la velocidad para un movimiento más rápido

# Variables globales para controlar el movimiento
moving_left = False
moving_right = False
moving_down = False
moving_up = False

def control_robot():
    while True:
        if moving_left:
            radio.communicate_grsim(id=5, isteamyellow=1, veltangent=velocidad)
        elif moving_right:
            radio.communicate_grsim(id=5, isteamyellow=1, veltangent=-velocidad)
        elif moving_down:
            radio.communicate_grsim(id=5, isteamyellow=1, velnormal=velocidad)
        elif moving_up:
            radio.communicate_grsim(id=5, isteamyellow=1, velnormal=-velocidad)
        else:
            # Envía un comando de parada si no se presiona ninguna tecla
            radio.communicate_grsim(id=5, isteamyellow=1, velnormal=0, veltangent=0)
        time.sleep(0.01)  # Disminuye el tiempo de espera para enviar comandos más frecuentemente

def on_left_arrow_down(event):
    global moving_left
    moving_left = True

def on_left_arrow_up(event):
    global moving_left
    moving_left = False

def on_right_arrow_down(event):
    global moving_right
    moving_right = True

def on_right_arrow_up(event):
    global moving_right
    moving_right = False

def on_down_arrow_down(event):
    global moving_down
    moving_down = True

def on_down_arrow_up(event):
    global moving_down
    moving_down = False

def on_up_arrow_down(event):
    global moving_up
    moving_up = True

def on_up_arrow_up(event):
    global moving_up
    moving_up = False

keyboard.on_press_key('left', on_left_arrow_down)
keyboard.on_release_key('left', on_left_arrow_up)

keyboard.on_press_key('right', on_right_arrow_down)
keyboard.on_release_key('right', on_right_arrow_up)

keyboard.on_press_key('down', on_down_arrow_down)
keyboard.on_release_key('down', on_down_arrow_up)

keyboard.on_press_key('up', on_up_arrow_down)
keyboard.on_release_key('up', on_up_arrow_up)

# Inicia el hilo de control del robot
control_thread = threading.Thread(target=control_robot)
control_thread.daemon = True
control_thread.start()

print("Presiona las flechas del teclado. Presiona 'esc' para salir.")
keyboard.wait('esc')
