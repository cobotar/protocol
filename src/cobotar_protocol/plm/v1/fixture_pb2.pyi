from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FixtureType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FIXTURE_TYPE_UNSPECIFIED: _ClassVar[FixtureType]
FIXTURE_TYPE_UNSPECIFIED: FixtureType

class FixtureMessage(_message.Message):
    __slots__ = ("id", "name", "icon", "description", "type", "accepted_part_ids")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_PART_IDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon: str
    description: str
    type: FixtureType
    accepted_part_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[FixtureType, str]] = ..., accepted_part_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class FixtureMessages(_message.Message):
    __slots__ = ("fixtures",)
    FIXTURES_FIELD_NUMBER: _ClassVar[int]
    fixtures: _containers.RepeatedCompositeFieldContainer[FixtureMessage]
    def __init__(self, fixtures: _Optional[_Iterable[_Union[FixtureMessage, _Mapping]]] = ...) -> None: ...
