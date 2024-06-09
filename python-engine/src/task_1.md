from communications.grsim import Grsim
import keyboard 
import threading
import time

#para elegir al robot especifico, id y equipo de ejemplo
control = Grsim(1,1)
speed, move_left, move_right, move_down, move_up = 1000, False, False, False, False

def robot_control():
    while True:
        control.communicate_grsim(id=5, isteamyellow=1, veltangent=speed if move_left else -speed if move_right else 0, velnormal=speed if move_down else -speed if move_up else 0)
        time.sleep(0.01)

keyboard.on_press_key('left', lambda e: globals().__setitem__('move_left', True))
keyboard.on_release_key('left', lambda e: globals().__setitem__('move_left', False))
keyboard.on_press_key('right', lambda e: globals().__setitem__('move_right', True))
keyboard.on_release_key('right', lambda e: globals().__setitem__('move_right', False))
keyboard.on_press_key('down', lambda e: globals().__setitem__('move_down', True))
keyboard.on_release_key('down', lambda e: globals().__setitem__('move_down', False))
keyboard.on_press_key('up', lambda e: globals().__setitem__('move_up', True))
keyboard.on_release_key('up', lambda e: globals().__setitem__('move_up', False))

threading.Thread(target=robot_control, daemon=True).start()
print("Usa las flechas del teclado para controlar el robot. Presiona 'esc' para salir.")
keyboard.wait('esc')
