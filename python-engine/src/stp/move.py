from world.world import World
from navigation.navigator import Navigator
from communications.wrapper import CommandSender
from world.entities import Robot
from utility.math_utilities import normalize_2d_vector, rotate_2d_vector, dot_product_2d, euclidian_distance

import time
import math

# Moves a robot to a specific position
class Move:
    def __init__(self, world : World, navigator : Navigator, comms : CommandSender, 
                 robot : tuple[int, int] ):
        self.world = world
        self.navigator = navigator
        self.comms = comms 
        self.robot = robot # ("id", is_blue)
        self.MINIMUM_DISTANCE_SHORT = 0.09 # robot radius in meters
        self.MINIMUM_DISTANCE_LONG = 0.18
        self.MOVE_SPEED = 5
    
            
    def motion_to_point(self, robot : Robot, to_point : tuple[float, float]):
        dir_vec : tuple[float, float] = to_point[0] - robot.x,  to_point[1] - robot.y
        # To local coords of the robot
        # Nose porque con negativo funciona si alguien sabe explicar porfavor
        dir_vec = rotate_2d_vector(dir_vec, -robot.orientation)
        dir_vec = normalize_2d_vector(dir_vec)
        self.comms.send_robot_data(id = self.robot[0], is_blue = self.robot[1], 
                                    veltangent= dir_vec[0]*self.MOVE_SPEED,
                                    velnormal = dir_vec[1]*self.MOVE_SPEED
                                    )

    # Use for long distances
    def move_to_point(self, goal : tuple[float, float]):
        robot : Robot = self.world.get_robot(self.robot[1], self.robot[0])
        path = self.navigator.get_path((robot.x, robot.y), goal)
        path = [(0.999980712890625, 1.000019287109375), (1.0788082329634272, 1.0069336567596778), (1.1564338766951163, 1.0085854041998905), (1.232857644085692, 1.0049745294300125), (1.3080795351351546, 0.9961010324500447), (1.382099549843504, 0.9819649132599866), (1.4549176882107404, 0.9625661718598384), (1.5265339502368636, 0.9379048082495998), (1.5969483359218737, 0.907980822429271), (1.6661608452657706, 0.8727942143988521), (1.7341714782685542, 0.8323449841583429), (1.7606760782084598, 0.7585625199114716), (1.7923875100751392, 0.689907411252544), (1.8293057738685912, 0.6263796581815599), (1.8714308695888175, 0.5679792606985201), (1.9187627972358177, 0.5147062188034238), (1.9713015568095913, 0.46656053249627133), (2.0290471483101387, 0.42354220177706264), (2.09199957173746, 0.38565122664579765), (2.1601588270915544, 0.35288760710247646), (2.2335249143724227, 0.32525134314709914), (2.2598176337760787, 0.25142523105186265), (2.2787681320283335, 0.17830010697226967), (2.2903764091291876, 0.10587597090832007), (2.294642465078642, 0.034152822860014025), (2.2915662998766955, -0.03686933717264855), (2.2811479135233483, -0.10719050918966765), (2.2633873060186, -0.17681069319104326), (2.238284477362452, -0.2457298891767755), (2.205839427554903, -0.31394809714686417), (2.1660521565959536, -0.3814653171013093), (2.1251134729310497, -0.4485279931040179), (2.080183932396441, -0.5099530378571042), (2.031263534992125, -0.5657404513605679), (1.9783522807181044, -0.6158902336144096), (1.921450169574378, -0.660402384618629), (1.8605572015609457, -0.699276904373226), (1.795673376677808, -0.7325137928782006), (1.7267986949249645, -0.7601130501335531), (1.6539331563024153, -0.782074676139283), (1.5770767608101603, -0.7983986708953908), (1.528706028166007, -0.8595600736330018), (1.4770766038879597, -0.9131944800366754), (1.4221884879760176, -0.9593018901064113), (1.3640416804301823, -0.9978823038422104), (1.302636181250452, -1.0289357212440722), (1.237971990436828, -1.0524621423119964), (1.17004910798931, -1.0684615670459836), (1.0988675339078975, -1.0769339954460333), (1.0244272681925912, -1.0778794275121457), (0.9467283108433906, -1.0712978632443209), (0.5500867950126525, -1.0195725510703537)]
        next_point = robot.x, robot.y
        while True:
            if len(path) == 0:
                break
            # Update robot
            robot = self.world.get_robot(self.robot[1], self.robot[0])
            # Pass to next point if the robot is nearest enough
            if euclidian_distance((robot.x,robot.y), next_point) < self.MINIMUM_DISTANCE_LONG:
                next_point = path.pop(0)
            # Or pass to the next point if the current_point is already passed
            if len(path) > 1:
                next_point_2 = path[1]
                path_dir = normalize_2d_vector( (next_point_2[0] - next_point[0], next_point_2[1] - next_point[1]) )
                motion_dir = normalize_2d_vector( (next_point[0] - robot.x, next_point[1] - robot.y)  )
                if dot_product_2d(path_dir, motion_dir) < 0:
                    next_point = path.pop(0)
            self.motion_to_point(robot, next_point)
        print("Move to point finalized")
            
    
    def distance(self, point_a : tuple[float, float], point_b : tuple[float, float]) -> float:
        return math.sqrt((point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2)

    def stop():
        pass