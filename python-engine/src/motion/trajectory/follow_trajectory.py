import numpy as np
from utility.object import Object
from communications.wrapper import CommandSender

# FOLLOW TRAJECTORY CLASS

class FollowTrajectory(Object):
    def __init__(self, robot_id : int, is_blue : int, trajectory):
        self.robot_id = robot_id
        self.is_blue = is_blue
        self.trajectory = trajectory

        self.is_completed = False
        self.acc_delta = 0
        self.time_step = 0

        self.comms : CommandSender = CommandSender()

    def _process(self, delta, robot_rotation):
        if self.is_completed:
            return
        # Force to run 60 fps: WARNING THIS ONLY WORK WITH CODE >= 60 FPS
        self.acc_delta += delta
        
        if self.acc_delta < 0.016:
            return
        self.acc_delta = 0

        if len(self.trajectory) <= self.time_step:
            self.is_completed = True
            return
        
        target_velocity = self.trajectory[self.time_step]
        # Define the rotation angle in radians
        theta = robot_rotation

        # Define the rotation matrix
        rotation_matrix = np.array([
            [np.cos(theta), -np.sin(theta)],
            [np.sin(theta), np.cos(theta)]
        ])
        target_velocity = np.dot(rotation_matrix, target_velocity)
        self.comms.send_robot_data(self.robot_id, self.is_blue, velnormal=target_velocity[1], 
                                   veltangent=target_velocity[0])
        self.time_step += 1