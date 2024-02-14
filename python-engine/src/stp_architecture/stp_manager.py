from path_planning.path_planning import PathPlanning
from classes.detection import Robot
from communications.grsim import Grsim
from communications.wrapper import RadioWrapper
import math
import time

class STP:
    def __init__(self, vision) -> None:
        self.path_planning = PathPlanning(vision)
        self.vision = vision

    def normalize_2d_vector(self, x,y):
        if abs(x) < 0.001 or abs(y) < 0.001:
            return (0,0)
        return (x / ((x**2 + y**2)**0.5), y / ((x**2 + y**2)**0.5))

    def go_to_pos(self, robot : Robot , final_pos : tuple) -> None:
        #robot = self.vision.get_robot(code)
        radio = Grsim() # Cambiar por una layer que no le importe si esta en sim o cancha real
        if(robot is None):
            return
        distance_f = lambda x1, y1, x2, y2: ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        robot_pos = ( robot.posx, robot.posy )
        min_distance = 50**2
        path = PathPlanning(self.vision).get_path(robot_pos, final_pos)
        
        if(len(path) <= 0):
            return
        current_goal = path.pop()
        
        while len(path) > 0:
            vel_dir = (current_goal[0] - robot.posx, current_goal[1] - robot.posy ) 
            final_vel = self.normalize_2d_vector(vel_dir[0],vel_dir[1])
            final_vel = final_vel[0], final_vel[1]
            #Convert to robot local coordinates
            angle = -robot.orientation 
            #print(math.cos(angle) )
            x = final_vel[0]* math.cos(angle) -  final_vel[1]* math.sin(angle)
            y = final_vel[0]* math.sin(angle) + final_vel[1]* math.cos(angle)
            changed_number = 0 if robot.team_id == 1 else 1
            radio.communicate_grsim( robot.id, changed_number, veltangent = x , velnormal = y  )

            robot_pos = ( robot.posx, robot.posy )
            distance_to_goal = distance_f( robot.posx, robot.posy, current_goal[0], current_goal[1] )

            if (distance_to_goal < 100):
                current_goal = path.pop()

            
        
        
        
        
        
    

