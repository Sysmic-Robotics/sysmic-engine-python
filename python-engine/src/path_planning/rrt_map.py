# Map abstraction for RRT

# Assumptions
# Obstacles are circles of the same radius

import math

class RRTMap:
    
    def __init__(self, map_h, map_w, obstacles):
        self.map_h = map_h
        self.map_w = map_w
        self.obstacles = obstacles
        self.obstacle_radius = 110

    def IsColliding(self, obstacle, point):
        distance = math.sqrt( (point[0] - obstacle[0])**2 + (point[1] - obstacle[1])**2 )
        if distance <= self.obstacle_radius:
            return True
        return False



