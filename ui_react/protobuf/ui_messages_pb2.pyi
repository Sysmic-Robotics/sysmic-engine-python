from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnginePackage(_message.Message):
    __slots__ = ["scene", "ai_environment", "fps"]
    class Scene(_message.Message):
        __slots__ = ["ball", "yellow_robots", "blue_robots"]
        class Ball(_message.Message):
            __slots__ = ["x", "y", "z"]
            X_FIELD_NUMBER: _ClassVar[int]
            Y_FIELD_NUMBER: _ClassVar[int]
            Z_FIELD_NUMBER: _ClassVar[int]
            x: float
            y: float
            z: float
            def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ...) -> None: ...
        class Robot(_message.Message):
            __slots__ = ["id", "x", "y", "orientation", "vel_x", "vel_y"]
            ID_FIELD_NUMBER: _ClassVar[int]
            X_FIELD_NUMBER: _ClassVar[int]
            Y_FIELD_NUMBER: _ClassVar[int]
            ORIENTATION_FIELD_NUMBER: _ClassVar[int]
            VEL_X_FIELD_NUMBER: _ClassVar[int]
            VEL_Y_FIELD_NUMBER: _ClassVar[int]
            id: int
            x: float
            y: float
            orientation: float
            vel_x: float
            vel_y: float
            def __init__(self, id: _Optional[int] = ..., x: _Optional[float] = ..., y: _Optional[float] = ..., orientation: _Optional[float] = ..., vel_x: _Optional[float] = ..., vel_y: _Optional[float] = ...) -> None: ...
        BALL_FIELD_NUMBER: _ClassVar[int]
        YELLOW_ROBOTS_FIELD_NUMBER: _ClassVar[int]
        BLUE_ROBOTS_FIELD_NUMBER: _ClassVar[int]
        ball: EnginePackage.Scene.Ball
        yellow_robots: _containers.RepeatedCompositeFieldContainer[EnginePackage.Scene.Robot]
        blue_robots: _containers.RepeatedCompositeFieldContainer[EnginePackage.Scene.Robot]
        def __init__(self, ball: _Optional[_Union[EnginePackage.Scene.Ball, _Mapping]] = ..., yellow_robots: _Optional[_Iterable[_Union[EnginePackage.Scene.Robot, _Mapping]]] = ..., blue_robots: _Optional[_Iterable[_Union[EnginePackage.Scene.Robot, _Mapping]]] = ...) -> None: ...
    class AIEnvironment(_message.Message):
        __slots__ = ["name", "robot_destinations"]
        class RobotDestination(_message.Message):
            __slots__ = ["id", "x", "y"]
            ID_FIELD_NUMBER: _ClassVar[int]
            X_FIELD_NUMBER: _ClassVar[int]
            Y_FIELD_NUMBER: _ClassVar[int]
            id: int
            x: float
            y: float
            def __init__(self, id: _Optional[int] = ..., x: _Optional[float] = ..., y: _Optional[float] = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        ROBOT_DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
        name: str
        robot_destinations: _containers.RepeatedCompositeFieldContainer[EnginePackage.AIEnvironment.RobotDestination]
        def __init__(self, name: _Optional[str] = ..., robot_destinations: _Optional[_Iterable[_Union[EnginePackage.AIEnvironment.RobotDestination, _Mapping]]] = ...) -> None: ...
    SCENE_FIELD_NUMBER: _ClassVar[int]
    AI_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    FPS_FIELD_NUMBER: _ClassVar[int]
    scene: EnginePackage.Scene
    ai_environment: EnginePackage.AIEnvironment
    fps: int
    def __init__(self, scene: _Optional[_Union[EnginePackage.Scene, _Mapping]] = ..., ai_environment: _Optional[_Union[EnginePackage.AIEnvironment, _Mapping]] = ..., fps: _Optional[int] = ...) -> None: ...

class Command(_message.Message):
    __slots__ = ["command_type", "robot_ids", "destination", "ai_environment"]
    class CommandType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        START_MOVE_TO: _ClassVar[Command.CommandType]
        CHANGE_AI_ENVIRONMENT: _ClassVar[Command.CommandType]
    START_MOVE_TO: Command.CommandType
    CHANGE_AI_ENVIRONMENT: Command.CommandType
    class Position(_message.Message):
        __slots__ = ["x", "y"]
        X_FIELD_NUMBER: _ClassVar[int]
        Y_FIELD_NUMBER: _ClassVar[int]
        x: float
        y: float
        def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ...) -> None: ...
    COMMAND_TYPE_FIELD_NUMBER: _ClassVar[int]
    ROBOT_IDS_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    AI_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    command_type: Command.CommandType
    robot_ids: _containers.RepeatedScalarFieldContainer[int]
    destination: Command.Position
    ai_environment: str
    def __init__(self, command_type: _Optional[_Union[Command.CommandType, str]] = ..., robot_ids: _Optional[_Iterable[int]] = ..., destination: _Optional[_Union[Command.Position, _Mapping]] = ..., ai_environment: _Optional[str] = ...) -> None: ...
