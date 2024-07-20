import math
import random
from path_planning.rrt_map import RRTMap


class RRTAlgorithm:
    def __init__(self) -> None:
        pass

    def PathToGoal(self):
        path_indexes = []
        goal_index = len( self.nodes ) - 1
        path_indexes.append(goal_index)
        new_pos_i = self.nodes[goal_index][1] # Get parent
        while(new_pos_i != 0): # Finish when reached start pos
            path_indexes.append(new_pos_i)
            new_pos_i = self.nodes[new_pos_i][1]
        path_indexes.append(0)
        # Convert to coords
        path = []
        for i in path_indexes:
            path.append(self.nodes[i][0])
        return path   

    def GetPath(self, map, start, goal):
        # Initialize
        self.start = start
        self.goal = goal
        self.map = map
            
        self.nodes = [ ( start, 0) ]
        self.edges = []

        #Initial config
        self.max_step = 200
        # Compute path
        K = 800
        goal_reached = False
        for k in range(0, K):
            random_node = self.GetRandomNode()
            if k % 10 == 0:
                random_node = self.goal
            goal_reached = self.Expand(random_node)
            if(goal_reached):
                break
        if goal_reached:        
            return self.PathToGoal()  
        return [] 


    def Expand(self, random_node):
        if(self.IsColliding(random_node)):
            return
        nearest_node_i = self.GetNearestNeighborTo(random_node)
        nearest_node = self.nodes[nearest_node_i][0]
        epsilon = 20
        new_node = None
        if self.Distance(nearest_node, random_node) < epsilon:
            new_node = nearest_node
        else:
            new_node = self.Step(nearest_node, random_node)
        if(self.edgeIsColliding(nearest_node, new_node)):
            return    
        self.edges.append((nearest_node, new_node))  
        #  Coords, Parent
        self.nodes.append( (new_node, nearest_node_i) )

        if self.Distance(self.goal, new_node) < 20:
            return True
        return False

    def edgeIsColliding(self, node_a, node_b):
        for i in range(0, 101):
            u = i / 100
            x = node_a[0] * u + node_b[0] * (1 - u)
            y = node_a[1] * u + node_b[1] * (1 - u)
            if self.IsColliding((x,y)):
                return True
        return False        

    def IsColliding(self, point):
        for obs in self.map.obstacles:
            if self.map.IsColliding(obs, point):
                return True
        return False

    def Step(self, from_node, to_node):
        d = self.Distance(from_node, to_node)
        if d <= self.max_step:
            return to_node
        else:
            theta = math.atan2(to_node[1] - from_node[1],
                               to_node[0] - from_node[0])
            x = from_node[0] + self.max_step * math.cos(theta)
            y = from_node[1] + self.max_step * math.sin(theta)
            return x, y            
        
    def GetNearestNeighborTo(self, new_node):
        min_distance = float('inf')
        nearest_node_i = None
        for node_id in range(0, len(self.nodes)):
            d = self.Distance(new_node, self.nodes[node_id][0])
            if d < min_distance:
                min_distance = d
                nearest_node_i = node_id
        return nearest_node_i
        
    def Distance(self, point_a, point_b):
        return math.sqrt((point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2)

    def GetRandomNode(self):
        x = int(random.uniform(0, self.map.map_w))
        y = int(random.uniform(0, self.map.map_h))
        return x, y         