from path_planning.rrt_algorithm import RRTAlgorithm
from path_planning.rrt_map import RRTMap

class PathPlanning:
    def __init__(self, vision) -> None:
        self.vision = vision

    def get_path(self, point_from, point_to):
        offset = (8940/2 , 6662/2)
        map_h = 6662
        map_w = 8940
        point_from =  point_from[0]  + offset[0], point_from[1]  + offset[1]
        point_to = point_to[0]  + offset[0], point_to[1]  + offset[1]
        rtt = RRTAlgorithm()
        obstacles = []
        for robot in self.vision.get_robots():
            obstacles.append( (robot.posx, robot.posy) )
        map = RRTMap(map_h, map_w,  obstacles)

        t_path = rtt.GetPath(map, point_from, point_to) 
        path = []
        for point in t_path:
            path.append( (point[0] - offset[0],point[1] - offset[1]) )  
        return path
