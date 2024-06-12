from communications.grsim import Grsim

import keyboard

radio = Grsim()

velocidad = 8


while True:
    if keyboard.is_pressed('left'):
        radio.communicate_grsim(id=5, isteamyellow=1, veltangent=velocidad)
    elif keyboard.is_pressed('right'):
        radio.communicate_grsim(id=5, isteamyellow=1, veltangent=-velocidad)
    elif keyboard.is_pressed('down'):
        radio.communicate_grsim(id=5, isteamyellow=1, velnormal=velocidad)
    elif keyboard.is_pressed('up'):
        radio.communicate_grsim(id=5, isteamyellow=1, velnormal=-velocidad)        
