""" Geometry classes for the python-engine. """
import numpy as np

class Vector2f:
    """ A 2D vector class. """
    def __init__(self, x, y):
        self.x = np.float16(x)
        self.y = np.float16(y)

class FieldLineSegment:
    """ A class that represents a field line segment. """
    def __init__(self,name, p1, p2,
                    thickness, shape):
        self.name = name
        self.p1 = p1
        self.p2 = p2
        self.thickness = thickness
        self.shape = shape

class FieldCircularArc:
    """ A class that represents a field circular arc. """
    def __init__(self,name, center, radius,
                    angle_1, shape):
        self.name = name
        self.center = center
        self.radius = np.float16(radius)
        self.angle_1 = np.float16(angle_1)
        self.shape = shape

class GeometryFieldSize:
    """ A class that represents the field size. """
    def __init__(self,field_length, field_width,
                    goal_width, goal_depth,
                    boundary_width, field_lines,
                    field_arcs,penalty_team_area_depth,
                    penalty_team_area_width):
        self.field_length = np.int16(field_length)
        self.field_width = np.int16(field_width)
        self.goal_width = np.int16(goal_width)
        self.goal_depth = np.int16(goal_depth)
        self.boundary_width = boundary_width
        self.field_lines = field_lines
        self.field_arcs = field_arcs
        self.penalty_team_area_depth = np.int16(penalty_team_area_depth)
        self.penalty_team_area_width = np.int16(penalty_team_area_width)

class GeometryCameraCalibration:
    """ A class that represents the camera calibration. """
    def __init__(self, focal_length, principal_point,
                    distortion, q0, q1, q2, q3,
                    t_x, t_y, t_z,
                    derived_camera_world_tx,
                    derived_camera_world_ty,
                    derived_camera_world_tz,
                    pixel_image_width,
                    pixel_image_height
                    ):
        self.focal_length = focal_length
        self.principal_point = principal_point
        self.distortion = distortion

        self.q0 = np.float16(q0)
        self.q1 = np.float16(q1)
        self.q2 = np.float16(q2)
        self.q3 = np.float16(q3)

        self.t_x = np.float16(t_x)
        self.t_y = np.float16(t_y)
        self.t_z = np.float16(t_z)

        self.derived_camera_world_tx = np.float16(derived_camera_world_tx)
        self.derived_camera_world_ty = np.float16(derived_camera_world_ty)
        self.derived_camera_world_tz = np.float16(derived_camera_world_tz)

        self.pixel_image_width = np.int16(pixel_image_width)
        self.pixel_image_height = np.int16(pixel_image_height)

class GeometryModels:
    """ A class that represents the geometry models. """
    def __init__(self, ball_model_straight_twoPhase,
                 ballModelChipFixedLoss):
        self.ballModelStraightTwoPhase = ball_model_straight_twoPhase
        self.ballModelChipFixedLoss = ballModelChipFixedLoss

class GeometryData:
    """ A class that represents the geometry data. """
    def __init__(self, field_size, camera_calibrations,
                    models):
        self.field_size = field_size
        self.camera_calibrations = camera_calibrations
        self.models = models

class FieldShapeType:
    """ A class that represents the field shape type. """
    def __init__(self, field_shape_type):
        #revisar como se obtiene de proto
        self.field_shape_type = field_shape_type
        
