import sys
sys.path.append("python-engine/src/")
import numpy as np
import time
import signal


import robot_comunication

robot_comunication.list_serial_ports()

# Si vendor y product no son correctos, corregir en el archivo constants.py
robot_comunication = robot_comunication.USBSerial()

#close serial when ctrl+c is pressed
def signal_handler(sig, frame):
  print('You pressed Ctrl+C!')
  robot_comunication.serial_port.close()
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

while True:
    time.sleep(1)
    robot_comunication.send_data(np.array([1,1,1,1,1,1]), np.array([1,1,1,1,1,1]), np.array([1,1,1,1,1,1]), np.array([1,1,1,1,1,1]), np.array([1,1,1,1,1,1]), np.array([1,1,1,1,1,1]),np.array([1,1,1,1,1,1]))