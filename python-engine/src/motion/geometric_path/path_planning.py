from motion.geometric_path.algorithms.rrt_star import RRTStar
from motion.geometric_path.algorithms.bezier import Bezier
from motion.geometric_path.algorithms.map import Map
from world.world import World
from motion.geometric_path.algorithms.fast_planning import FastPlanning
import numpy as np

class PathPlanning:
    def __init__(self, world : World) -> None:
        self.world = world
    
    def free_obstacle_path(self, start : tuple[float, float], goal : tuple[float, float]) -> list[tuple[float, float]]:
        map : Map = Map(self.world, start)
        fast_planning : FastPlanning = FastPlanning(map)
        planning = fast_planning.get_path(start, goal)
        return planning
    
    # Return a linear path with no constraints
    def linear_path(self, start, goal) -> list[tuple[float, float]]:
        path = []
        n_points = 10
        start = np.array(start)
        goal = np.array(goal)
        direction = (goal - start) / np.linalg.norm(goal - start)
        for i in range(0, n_points):
            t = i/(n_points - 1)
            point = goal*t + start*(1-t)
            path.append(point)
        return path
