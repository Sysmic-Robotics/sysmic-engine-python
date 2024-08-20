from utility.object import Object
from communications.wrapper import CommandSender
from utility.enums import TaskState
# Trajectory Module
from motion.trajectory.follow_trajectory import FollowTrajectory
from motion.trajectory.trajectory_planning import TrajectoryPlanning
# Path Planning module
from motion.geometric_path.path_planning import PathPlanning
from world.entities import Robot
from world.world import World

class Motion(Object):
    def __init__(self, robot_id, is_blue, world : World):
        self.id = robot_id
        self.is_blue = is_blue
        self.world = world

        self.current_task = [[0,0], None]
        self.current_control = None

    
    def is_already_planned(self, task):
        if task[0] != self.current_task[0]:
            return False
        if task[1] != self.current_task[1]:
            return False
        return True

    def move_linear(self, point, delta) -> TaskState:
        robot : Robot = self.world.get_robot(self.is_blue, self.id)
        # Planning
        task = [point, 'move_linear']
        if not self.is_already_planned(task):
            # Then plan the new task
            
            print("Robo pos: ", robot.x, robot.y)
            path = PathPlanning(self.world).linear_path([robot.x, robot.y], point)
            trajectory = TrajectoryPlanning().get_trajectory([[robot.x, robot.y], point])
            print(trajectory)
            self.current_control = FollowTrajectory(self.id, self.is_blue, trajectory)
            self.current_task = task
        # Execute
        
        if self.current_control.is_completed:
            return TaskState.SUCCESS
        
        self.current_control._process(delta, -robot.orientation)
        return TaskState.IN_PROCESS

    def move_free_obstacle(point):
        pass

    def move_around_clockwise(point):
        pass

    def rotate(angle):
        pass