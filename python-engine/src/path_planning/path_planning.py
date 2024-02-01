from path_planning.rrt_algorithm import RRTAlgorithm
from path_planning.rrt_map import RRTMap

class PathPlanning:
    def __init__(self, vision) -> None:
        self.vision = vision

    def get_path(self, point_from, point_to):
        rtt = RRTAlgorithm()
        obstacles = []
        for robot in self.vision.get_robots():
            obstacles.append( (robot.posx, robot.posy) )
        map = RRTMap(8940, 6662,  obstacles)

        t_path = rtt.GetPath(map, point_from, point_to) 
        path = []
        for point in t_path:
            path.append( (point[0] - 8940/2,point[1] - 6662/2) )  
        return path
