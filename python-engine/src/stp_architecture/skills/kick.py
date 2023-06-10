#Define the kick skill#
import numpy as np
import engine

class kick:
    def __init__(self, scene: engine.Scene, robot_id: int, target, blue: bool):
        #self.robot = scene.get_robot_by_id(robot_id) NOTE: revisar implementacion scene y ambas listas de robots
        if blue:
            self.robot = scene.get_robot_by_id(scene.robots_blue,robot_id)
        else:
            self.robot = scene.get_robot_by_id(scene.robots_yellow,robot_id)
        self.scene = scene

    def execute(self):
        
        current_orientation = self.robot.orientation
        current_position = (self.robot.posx, self.robot.posy)
        dx = self.target[0] - current_position[0]
        dy = self.target[1] - current_position[1]
        rot_angle = np.arctan2(dy,dx) - current_orientation
        # TODO: rotate
        # if robot is facing the target
        # TODO: kick


    def is_done(self, scene: engine.Scene):
        #returns true if the robot complete the behavior successfully
        pass