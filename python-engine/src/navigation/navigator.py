from navigation.algorithms.rrt_star import RRTStar
from navigation.algorithms.bezier import Bezier
from navigation.map import Map
from world.world import World
from navigation.algorithms.fast_planning import FastPlanning

class Navigator:
    def __init__(self, world : World) -> None:
        self.world = world
    
    # Return a list of points
    def get_path(self, start : tuple[float, float], goal : tuple[float, float]) -> list[tuple[float, float]]:
        map : Map = Map(self.world, start)
        fast_planning : FastPlanning = FastPlanning(map)
        planning = fast_planning.get_path(start, goal)
        #path = Bezier().calculate_points(planning)
        return planning
