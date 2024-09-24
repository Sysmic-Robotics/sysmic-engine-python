from motion.trajectory.trajectory_algorithms.trapezoid_profile import TrapezoidProfile

class TrajectoryPlanning():
    def get_trajectory(self, geometric_path):
        v_max = 5
        a_max = 4.5
        trajectory = TrapezoidProfile(v_max, a_max, 0.016).get_trajectory([[0,0],[1.5,0]])
        return trajectory