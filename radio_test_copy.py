import sys
import time
sys.path.append("python-engine/src/")
from inputs import get_gamepad
import numpy as np
import math
import signal
import keyboard
import threading

import robot_comunication

robot_comunication.list_serial_ports()

# Si vendor y product no son correctos, corregir en el archivo constants.py
robot_comunication = robot_comunication.USBSerial()

def signal_handler(sig, frame):
  print('You pressed Ctrl+C!')
  robot_comunication.serial_port.close()
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

class XboxController(object):
    MAX_TRIG_VAL = math.pow(2, 8)
    MAX_JOY_VAL = math.pow(2, 15)

    def __init__(self):

        self.LeftJoystickY = 0
        self.LeftJoystickX = 0
        self.RightJoystickY = 0
        self.RightJoystickX = 0
        self.LeftTrigger = 0
        self.RightTrigger = 0
        self.LeftBumper = 0
        self.RightBumper = 0
        self.A = 0
        self.X = 0
        self.Y = 0
        self.B = 0
        self.LeftThumb = 0
        self.RightThumb = 0
        self.Back = 0
        self.Start = 0
        self.LeftDPad = 0
        self.RightDPad = 0
        self.UpDPad = 0
        self.DownDPad = 0

        self._monitor_thread = threading.Thread(target=self._monitor_controller, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()


    def read(self): # return the buttons/triggers that you care about in this methode
        lx = self.LeftJoystickX
        ly = self.LeftJoystickY
        rx = self.RightJoystickX
        ry = self.RightJoystickY
        rb = self.RightBumper
        lb = self.LeftBumper
        print("left joystick x: ", lx)
        print("left joystick y: ", ly)
        print("right joystick x: ", rx)
        print("right joystick y: ", ry)
        print("rb: ", rb, "lb: ", lb)
        
        return None


    def _monitor_controller(self):
        while True:
            events = get_gamepad()
            for event in events:
                if event.code == 'ABS_Y':
                    if np.abs(event.state) >= 15000:
                        self.LeftJoystickY = (event.state / XboxController.MAX_JOY_VAL) * -256.0 # normalize between -512 and 512
                    else:
                        self.LeftJoystickY = 0
                elif event.code == 'ABS_X':
                    if np.abs(event.state) >= 15000:
                        self.LeftJoystickX = (event.state / XboxController.MAX_JOY_VAL) * 256.0 # normalize between -512 and 512
                    else:
                        self.LeftJoystickX = 0
                elif event.code == 'ABS_RY':
                    if np.abs(event.state) >= 15000:
                        self.RightJoystickY = (event.state / XboxController.MAX_JOY_VAL) * -1024.0 # normalize between -1024 and 1024
                    else:
                        self.RightJoystickY = 0
                elif event.code == 'ABS_RX':
                    if np.abs(event.state) >= 15000:
                        self.RightJoystickX = (event.state / XboxController.MAX_JOY_VAL) * 1024.0 # normalize between -1024 and 1024
                    else:
                        self.RightJoystickX = 0
                elif event.code == 'ABS_Z':
                    self.LeftTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
                elif event.code == 'ABS_RZ':
                    self.RightTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
                elif event.code == 'BTN_TL':
                    self.LeftBumper = event.state
                elif event.code == 'BTN_TR':
                    self.RightBumper = event.state
                elif event.code == 'BTN_SOUTH':
                    self.A = event.state
                elif event.code == 'BTN_NORTH':
                    self.Y = event.state #previously switched with X
                elif event.code == 'BTN_WEST':
                    self.X = event.state #previously switched with Y
                elif event.code == 'BTN_EAST':
                    self.B = event.state
                elif event.code == 'BTN_THUMBL':
                    self.LeftThumb = event.state
                elif event.code == 'BTN_THUMBR':
                    self.RightThumb = event.state
                elif event.code == 'BTN_SELECT':
                    self.Back = event.state
                elif event.code == 'BTN_START':
                    self.Start = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY1':
                    self.LeftDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY2':
                    self.RightDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY3':
                    self.UpDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY4':
                    self.DownDPad = event.state




if __name__ == '__main__':
    joy = XboxController()
    while True:
        
        #joy.read()
        x_speed = np.full(shape = 6, fill_value = joy.LeftJoystickY, dtype=np.int16)
        y_speed = np.full(shape = 6, fill_value = joy.LeftJoystickX, dtype=np.int16)
        rot_speed = np.full(shape = 6, fill_value = joy.RightJoystickX, dtype=np.int16)
        kick = np.full(shape = 6, fill_value = joy.RightBumper, dtype=np.int8)
        dribble = np.full(shape = 6, fill_value = joy.LeftBumper, dtype=np.int8)
        robot_comunication.send_data(np.array([1,1,1,1,1,1]), x_speed, y_speed, rot_speed, kick, dribble,np.array([1,1,1,1,1,1]))
        time.sleep(.016)
                        #clear the screen




'''
while True:
  if keyboard.is_pressed('a'):
    robot_comunication.send_data(np.array([1,1,1,1,1,1]), np.array([1,1,1,1,1,1]), np.array([1,1,1,1,1,1]), np.array([1,1,1,1,1,1]), np.array([1,1,1,1,1,1]), np.array([1,1,1,1,1,1]),np.array([1,1,1,1,1,1]))
'''    