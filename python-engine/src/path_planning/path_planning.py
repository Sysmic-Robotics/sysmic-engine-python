from path_planning.rrt_algorithm import RRTAlgorithm
from path_planning.rrt_map import RRTMap
import math
# Se trabajan con coordenadas donde x -> y \/ son positivos
# el origen esta en la esquina superior izquierda 

class PathPlanning:
    def __init__(self, vision) -> None:
        self.vision = vision

    def convert_to_local_coords(self , global_x , global_y):
        map_l = 9000 # In cm
        map_w = 6000 # In cm
        point_x = global_x
        point_y = global_y*-1
        point_x += map_l/2
        point_y += map_w/2
        return (point_x, point_y)
    
    def convert_to_global_coords(self, local_x, local_y):
        map_l = 9000 # In cm
        map_w = 6000 # In cm
        point_y = local_y
        point_x = local_x
        point_x -= map_l/2
        point_y -= map_w/2
        point_y = point_y*-1
        return (point_x, point_y)

    def get_path(self, point_from, point_to):
        rtt = RRTAlgorithm()
        obstacles = []
        for robot in self.vision.get_robots():
            if math.sqrt(( (robot.posx - point_from[0])**2 + (robot.posy - point_from[1])**2 ) ) > 110:
                obstacles.append( self.convert_to_local_coords(robot.posx, robot.posy) )

        point_to = self.convert_to_local_coords(point_to[0], point_to[1] )
        point_from = self.convert_to_local_coords(point_from[0], point_from[1] )    
        map = RRTMap(6000, 9000,  obstacles)

        t_path = rtt.GetPath(map, point_from, point_to) 
        
    
        path = []
        for point in t_path:
            path.append( self.convert_to_global_coords(point[0], point[1]) )  
        return path
