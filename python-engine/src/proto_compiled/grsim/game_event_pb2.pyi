from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SSL_Referee_Game_Event(_message.Message):
    __slots__ = ["gameEventType", "originator", "message"]
    class GameEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN: _ClassVar[SSL_Referee_Game_Event.GameEventType]
        CUSTOM: _ClassVar[SSL_Referee_Game_Event.GameEventType]
        NUMBER_OF_PLAYERS: _ClassVar[SSL_Referee_Game_Event.GameEventType]
        BALL_LEFT_FIELD: _ClassVar[SSL_Referee_Game_Event.GameEventType]
        GOAL: _ClassVar[SSL_Referee_Game_Event.GameEventType]
        KICK_TIMEOUT: _ClassVar[SSL_Referee_Game_Event.GameEventType]
        NO_PROGRESS_IN_GAME: _ClassVar[SSL_Referee_Game_Event.GameEventType]
        BOT_COLLISION: _ClassVar[SSL_Referee_Game_Event.GameEventType]
        MULTIPLE_DEFENDER: _ClassVar[SSL_Referee_Game_Event.GameEventType]
        MULTIPLE_DEFENDER_PARTIALLY: _ClassVar[SSL_Referee_Game_Event.GameEventType]
        ATTACKER_IN_DEFENSE_AREA: _ClassVar[SSL_Referee_Game_Event.GameEventType]
        ICING: _ClassVar[SSL_Referee_Game_Event.GameEventType]
        BALL_SPEED: _ClassVar[SSL_Referee_Game_Event.GameEventType]
        ROBOT_STOP_SPEED: _ClassVar[SSL_Referee_Game_Event.GameEventType]
        BALL_DRIBBLING: _ClassVar[SSL_Referee_Game_Event.GameEventType]
        ATTACKER_TOUCH_KEEPER: _ClassVar[SSL_Referee_Game_Event.GameEventType]
        DOUBLE_TOUCH: _ClassVar[SSL_Referee_Game_Event.GameEventType]
        ATTACKER_TO_DEFENCE_AREA: _ClassVar[SSL_Referee_Game_Event.GameEventType]
        DEFENDER_TO_KICK_POINT_DISTANCE: _ClassVar[SSL_Referee_Game_Event.GameEventType]
        BALL_HOLDING: _ClassVar[SSL_Referee_Game_Event.GameEventType]
        INDIRECT_GOAL: _ClassVar[SSL_Referee_Game_Event.GameEventType]
        BALL_PLACEMENT_FAILED: _ClassVar[SSL_Referee_Game_Event.GameEventType]
        CHIP_ON_GOAL: _ClassVar[SSL_Referee_Game_Event.GameEventType]
    UNKNOWN: SSL_Referee_Game_Event.GameEventType
    CUSTOM: SSL_Referee_Game_Event.GameEventType
    NUMBER_OF_PLAYERS: SSL_Referee_Game_Event.GameEventType
    BALL_LEFT_FIELD: SSL_Referee_Game_Event.GameEventType
    GOAL: SSL_Referee_Game_Event.GameEventType
    KICK_TIMEOUT: SSL_Referee_Game_Event.GameEventType
    NO_PROGRESS_IN_GAME: SSL_Referee_Game_Event.GameEventType
    BOT_COLLISION: SSL_Referee_Game_Event.GameEventType
    MULTIPLE_DEFENDER: SSL_Referee_Game_Event.GameEventType
    MULTIPLE_DEFENDER_PARTIALLY: SSL_Referee_Game_Event.GameEventType
    ATTACKER_IN_DEFENSE_AREA: SSL_Referee_Game_Event.GameEventType
    ICING: SSL_Referee_Game_Event.GameEventType
    BALL_SPEED: SSL_Referee_Game_Event.GameEventType
    ROBOT_STOP_SPEED: SSL_Referee_Game_Event.GameEventType
    BALL_DRIBBLING: SSL_Referee_Game_Event.GameEventType
    ATTACKER_TOUCH_KEEPER: SSL_Referee_Game_Event.GameEventType
    DOUBLE_TOUCH: SSL_Referee_Game_Event.GameEventType
    ATTACKER_TO_DEFENCE_AREA: SSL_Referee_Game_Event.GameEventType
    DEFENDER_TO_KICK_POINT_DISTANCE: SSL_Referee_Game_Event.GameEventType
    BALL_HOLDING: SSL_Referee_Game_Event.GameEventType
    INDIRECT_GOAL: SSL_Referee_Game_Event.GameEventType
    BALL_PLACEMENT_FAILED: SSL_Referee_Game_Event.GameEventType
    CHIP_ON_GOAL: SSL_Referee_Game_Event.GameEventType
    class Team(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        TEAM_UNKNOWN: _ClassVar[SSL_Referee_Game_Event.Team]
        TEAM_YELLOW: _ClassVar[SSL_Referee_Game_Event.Team]
        TEAM_BLUE: _ClassVar[SSL_Referee_Game_Event.Team]
    TEAM_UNKNOWN: SSL_Referee_Game_Event.Team
    TEAM_YELLOW: SSL_Referee_Game_Event.Team
    TEAM_BLUE: SSL_Referee_Game_Event.Team
    class Originator(_message.Message):
        __slots__ = ["team", "botId"]
        TEAM_FIELD_NUMBER: _ClassVar[int]
        BOTID_FIELD_NUMBER: _ClassVar[int]
        team: SSL_Referee_Game_Event.Team
        botId: int
        def __init__(self, team: _Optional[_Union[SSL_Referee_Game_Event.Team, str]] = ..., botId: _Optional[int] = ...) -> None: ...
    GAMEEVENTTYPE_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    gameEventType: SSL_Referee_Game_Event.GameEventType
    originator: SSL_Referee_Game_Event.Originator
    message: str
    def __init__(self, gameEventType: _Optional[_Union[SSL_Referee_Game_Event.GameEventType, str]] = ..., originator: _Optional[_Union[SSL_Referee_Game_Event.Originator, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...
