from . import messages_robocup_ssl_detection_pb2 as _messages_robocup_ssl_detection_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Log_Frame(_message.Message):
    __slots__ = ["frame", "refbox_cmd"]
    FRAME_FIELD_NUMBER: _ClassVar[int]
    REFBOX_CMD_FIELD_NUMBER: _ClassVar[int]
    frame: _messages_robocup_ssl_detection_pb2.SSL_DetectionFrame
    refbox_cmd: str
    def __init__(self, frame: _Optional[_Union[_messages_robocup_ssl_detection_pb2.SSL_DetectionFrame, _Mapping]] = ..., refbox_cmd: _Optional[str] = ...) -> None: ...

class Refbox_Log(_message.Message):
    __slots__ = ["log"]
    LOG_FIELD_NUMBER: _ClassVar[int]
    log: _containers.RepeatedCompositeFieldContainer[Log_Frame]
    def __init__(self, log: _Optional[_Iterable[_Union[Log_Frame, _Mapping]]] = ...) -> None: ...
