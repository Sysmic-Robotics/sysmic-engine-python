from navigation.algorithms.rrt_star import RRTStar
from navigation.map import Map
from world.world import World

class Navigator:
    def __init__(self, world : World) -> None:
        self.world = world
    
    # Return a list of points
    def get_path(self, start : tuple[float, float], goal : tuple[float, float]) -> list[tuple[float, float]]:
        map : Map = Map(self.world, start)
        rtt : RRTStar = RRTStar(map)
        path = rtt.get_path(start, goal)  
        return path
