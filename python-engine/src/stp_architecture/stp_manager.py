from path_planning.path_planning import PathPlanning
from classes.detection import Robot

class STP:
    def __init__(self, vision) -> None:
        self.path_planning = PathPlanning(vision)

    def go_to_pos(self, robot_id, final_pos : tuple) -> None:
        robot = self.vision.get_robot_by_id(robot_id)
        if(robot is None):
            return
        
        
        
    

