from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class grSim_Robot_Command(_message.Message):
    __slots__ = ["id", "kickspeedx", "kickspeedz", "veltangent", "velnormal", "velangular", "spinner", "wheelsspeed", "wheel1", "wheel2", "wheel3", "wheel4"]
    ID_FIELD_NUMBER: _ClassVar[int]
    KICKSPEEDX_FIELD_NUMBER: _ClassVar[int]
    KICKSPEEDZ_FIELD_NUMBER: _ClassVar[int]
    VELTANGENT_FIELD_NUMBER: _ClassVar[int]
    VELNORMAL_FIELD_NUMBER: _ClassVar[int]
    VELANGULAR_FIELD_NUMBER: _ClassVar[int]
    SPINNER_FIELD_NUMBER: _ClassVar[int]
    WHEELSSPEED_FIELD_NUMBER: _ClassVar[int]
    WHEEL1_FIELD_NUMBER: _ClassVar[int]
    WHEEL2_FIELD_NUMBER: _ClassVar[int]
    WHEEL3_FIELD_NUMBER: _ClassVar[int]
    WHEEL4_FIELD_NUMBER: _ClassVar[int]
    id: int
    kickspeedx: float
    kickspeedz: float
    veltangent: float
    velnormal: float
    velangular: float
    spinner: bool
    wheelsspeed: bool
    wheel1: float
    wheel2: float
    wheel3: float
    wheel4: float
    def __init__(self, id: _Optional[int] = ..., kickspeedx: _Optional[float] = ..., kickspeedz: _Optional[float] = ..., veltangent: _Optional[float] = ..., velnormal: _Optional[float] = ..., velangular: _Optional[float] = ..., spinner: bool = ..., wheelsspeed: bool = ..., wheel1: _Optional[float] = ..., wheel2: _Optional[float] = ..., wheel3: _Optional[float] = ..., wheel4: _Optional[float] = ...) -> None: ...

class grSim_Commands(_message.Message):
    __slots__ = ["timestamp", "isteamyellow", "robot_commands"]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ISTEAMYELLOW_FIELD_NUMBER: _ClassVar[int]
    ROBOT_COMMANDS_FIELD_NUMBER: _ClassVar[int]
    timestamp: float
    isteamyellow: bool
    robot_commands: _containers.RepeatedCompositeFieldContainer[grSim_Robot_Command]
    def __init__(self, timestamp: _Optional[float] = ..., isteamyellow: bool = ..., robot_commands: _Optional[_Iterable[_Union[grSim_Robot_Command, _Mapping]]] = ...) -> None: ...
