import numpy as np

class TrapezoidProfile:
    def __init__(self, v_max, a_max, time_steps):
        self.v_max = v_max
        self.a_max = a_max
        self.dt = time_steps

    def get_trajectory(self, geometric_path):
        trajectory = np.array([]).reshape(0, 2)  # Initialize an empty 2D array with shape (0, 2)
        for i in range(len(geometric_path) - 1):
            start = np.array(geometric_path[i])
            end = np.array(geometric_path[i + 1])
            segment = [start, end]
            velocities = self.trapezoidal_trajectory_2d(segment)
            # Append the velocities to the trajectory array
            trajectory = np.concatenate((trajectory, velocities), axis=0)
        return trajectory
        

    def trapezoidal_trajectory_2d(self, segment):
        
        times = []

        direction = (segment[1] - segment[0]) / np.linalg.norm(segment[1] - segment[0])
        distance = np.linalg.norm(segment[1] - segment[0])
            
        # Time to accelerate to max_velocity
        t_accel = self.v_max / self.a_max
            
        # Distance covered during acceleration (and deceleration)
        d_accel = 0.5 * self.a_max * t_accel ** 2
            
        # If distance is too short to reach max_velocity
        if 2 * d_accel > distance:
            t_accel = np.sqrt(distance / self.a_max)
            t_decel = t_accel
            t_constant = 0
            self.v_max = self.a_max * t_accel
        else:
            d_constant = distance - 2 * d_accel
            t_constant = d_constant / self.v_max
            t_decel = t_accel
            
        t_total = t_accel + t_constant + t_decel
            
        # Time intervals
        t = np.arange(0, t_total, self.dt)
        velocities = []
        # Velocity profile
        a = self.a_max
        for time in t:
            if time < t_accel:
                velocity = direction * a * time
            elif time < t_accel + t_constant:
                velocity = direction * self.v_max
            else:
                velocity = direction * (self.v_max - a * (time - t_accel - t_constant))
            velocities.append(velocity)
            times.append(time)
        
        return np.array(velocities)