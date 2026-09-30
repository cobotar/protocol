from buf.validate import validate_pb2 as _validate_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ARContentOrigin(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AR_CONTENT_ORIGIN_UNSPECIFIED: _ClassVar[ARContentOrigin]
    AR_CONTENT_ORIGIN_AUTHOR: _ClassVar[ARContentOrigin]
    AR_CONTENT_ORIGIN_STRATEGY: _ClassVar[ARContentOrigin]

class AdaptiveParticipation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ADAPTIVE_PARTICIPATION_UNSPECIFIED: _ClassVar[AdaptiveParticipation]
    ADAPTIVE_PARTICIPATION_FIXED: _ClassVar[AdaptiveParticipation]
    ADAPTIVE_PARTICIPATION_AVAILABLE: _ClassVar[AdaptiveParticipation]
    ADAPTIVE_PARTICIPATION_MANAGED: _ClassVar[AdaptiveParticipation]
AR_CONTENT_ORIGIN_UNSPECIFIED: ARContentOrigin
AR_CONTENT_ORIGIN_AUTHOR: ARContentOrigin
AR_CONTENT_ORIGIN_STRATEGY: ARContentOrigin
ADAPTIVE_PARTICIPATION_UNSPECIFIED: AdaptiveParticipation
ADAPTIVE_PARTICIPATION_FIXED: AdaptiveParticipation
ADAPTIVE_PARTICIPATION_AVAILABLE: AdaptiveParticipation
ADAPTIVE_PARTICIPATION_MANAGED: AdaptiveParticipation

class ARContentProvenance(_message.Message):
    __slots__ = ("origin", "participation", "source_strategy_id")
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    PARTICIPATION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_STRATEGY_ID_FIELD_NUMBER: _ClassVar[int]
    origin: ARContentOrigin
    participation: AdaptiveParticipation
    source_strategy_id: str
    def __init__(self, origin: _Optional[_Union[ARContentOrigin, str]] = ..., participation: _Optional[_Union[AdaptiveParticipation, str]] = ..., source_strategy_id: _Optional[str] = ...) -> None: ...
