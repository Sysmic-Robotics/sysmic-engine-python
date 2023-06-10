from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Vector2f(_message.Message):
    __slots__ = ["x", "y"]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ...) -> None: ...

class SSL_FieldLineSegment(_message.Message):
    __slots__ = ["name", "p1", "p2", "thickness"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    P1_FIELD_NUMBER: _ClassVar[int]
    P2_FIELD_NUMBER: _ClassVar[int]
    THICKNESS_FIELD_NUMBER: _ClassVar[int]
    name: str
    p1: Vector2f
    p2: Vector2f
    thickness: float
    def __init__(self, name: _Optional[str] = ..., p1: _Optional[_Union[Vector2f, _Mapping]] = ..., p2: _Optional[_Union[Vector2f, _Mapping]] = ..., thickness: _Optional[float] = ...) -> None: ...

class SSL_FieldCicularArc(_message.Message):
    __slots__ = ["name", "center", "radius", "a1", "a2", "thickness"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CENTER_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    A1_FIELD_NUMBER: _ClassVar[int]
    A2_FIELD_NUMBER: _ClassVar[int]
    THICKNESS_FIELD_NUMBER: _ClassVar[int]
    name: str
    center: Vector2f
    radius: float
    a1: float
    a2: float
    thickness: float
    def __init__(self, name: _Optional[str] = ..., center: _Optional[_Union[Vector2f, _Mapping]] = ..., radius: _Optional[float] = ..., a1: _Optional[float] = ..., a2: _Optional[float] = ..., thickness: _Optional[float] = ...) -> None: ...

class SSL_GeometryFieldSize(_message.Message):
    __slots__ = ["field_length", "field_width", "goal_width", "goal_depth", "boundary_width", "field_lines", "field_arcs"]
    FIELD_LENGTH_FIELD_NUMBER: _ClassVar[int]
    FIELD_WIDTH_FIELD_NUMBER: _ClassVar[int]
    GOAL_WIDTH_FIELD_NUMBER: _ClassVar[int]
    GOAL_DEPTH_FIELD_NUMBER: _ClassVar[int]
    BOUNDARY_WIDTH_FIELD_NUMBER: _ClassVar[int]
    FIELD_LINES_FIELD_NUMBER: _ClassVar[int]
    FIELD_ARCS_FIELD_NUMBER: _ClassVar[int]
    field_length: int
    field_width: int
    goal_width: int
    goal_depth: int
    boundary_width: int
    field_lines: _containers.RepeatedCompositeFieldContainer[SSL_FieldLineSegment]
    field_arcs: _containers.RepeatedCompositeFieldContainer[SSL_FieldCicularArc]
    def __init__(self, field_length: _Optional[int] = ..., field_width: _Optional[int] = ..., goal_width: _Optional[int] = ..., goal_depth: _Optional[int] = ..., boundary_width: _Optional[int] = ..., field_lines: _Optional[_Iterable[_Union[SSL_FieldLineSegment, _Mapping]]] = ..., field_arcs: _Optional[_Iterable[_Union[SSL_FieldCicularArc, _Mapping]]] = ...) -> None: ...

class SSL_GeometryCameraCalibration(_message.Message):
    __slots__ = ["camera_id", "focal_length", "principal_point_x", "principal_point_y", "distortion", "q0", "q1", "q2", "q3", "tx", "ty", "tz", "derived_camera_world_tx", "derived_camera_world_ty", "derived_camera_world_tz"]
    CAMERA_ID_FIELD_NUMBER: _ClassVar[int]
    FOCAL_LENGTH_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_POINT_X_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_POINT_Y_FIELD_NUMBER: _ClassVar[int]
    DISTORTION_FIELD_NUMBER: _ClassVar[int]
    Q0_FIELD_NUMBER: _ClassVar[int]
    Q1_FIELD_NUMBER: _ClassVar[int]
    Q2_FIELD_NUMBER: _ClassVar[int]
    Q3_FIELD_NUMBER: _ClassVar[int]
    TX_FIELD_NUMBER: _ClassVar[int]
    TY_FIELD_NUMBER: _ClassVar[int]
    TZ_FIELD_NUMBER: _ClassVar[int]
    DERIVED_CAMERA_WORLD_TX_FIELD_NUMBER: _ClassVar[int]
    DERIVED_CAMERA_WORLD_TY_FIELD_NUMBER: _ClassVar[int]
    DERIVED_CAMERA_WORLD_TZ_FIELD_NUMBER: _ClassVar[int]
    camera_id: int
    focal_length: float
    principal_point_x: float
    principal_point_y: float
    distortion: float
    q0: float
    q1: float
    q2: float
    q3: float
    tx: float
    ty: float
    tz: float
    derived_camera_world_tx: float
    derived_camera_world_ty: float
    derived_camera_world_tz: float
    def __init__(self, camera_id: _Optional[int] = ..., focal_length: _Optional[float] = ..., principal_point_x: _Optional[float] = ..., principal_point_y: _Optional[float] = ..., distortion: _Optional[float] = ..., q0: _Optional[float] = ..., q1: _Optional[float] = ..., q2: _Optional[float] = ..., q3: _Optional[float] = ..., tx: _Optional[float] = ..., ty: _Optional[float] = ..., tz: _Optional[float] = ..., derived_camera_world_tx: _Optional[float] = ..., derived_camera_world_ty: _Optional[float] = ..., derived_camera_world_tz: _Optional[float] = ...) -> None: ...

class SSL_GeometryData(_message.Message):
    __slots__ = ["field", "calib"]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    CALIB_FIELD_NUMBER: _ClassVar[int]
    field: SSL_GeometryFieldSize
    calib: _containers.RepeatedCompositeFieldContainer[SSL_GeometryCameraCalibration]
    def __init__(self, field: _Optional[_Union[SSL_GeometryFieldSize, _Mapping]] = ..., calib: _Optional[_Iterable[_Union[SSL_GeometryCameraCalibration, _Mapping]]] = ...) -> None: ...
