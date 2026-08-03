import datetime

from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LogSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOG_SEVERITY_UNSPECIFIED: _ClassVar[LogSeverity]
    LOG_SEVERITY_TRACE: _ClassVar[LogSeverity]
    LOG_SEVERITY_DEBUG: _ClassVar[LogSeverity]
    LOG_SEVERITY_INFO: _ClassVar[LogSeverity]
    LOG_SEVERITY_WARN: _ClassVar[LogSeverity]
    LOG_SEVERITY_ERROR: _ClassVar[LogSeverity]
    LOG_SEVERITY_FATAL: _ClassVar[LogSeverity]
LOG_SEVERITY_UNSPECIFIED: LogSeverity
LOG_SEVERITY_TRACE: LogSeverity
LOG_SEVERITY_DEBUG: LogSeverity
LOG_SEVERITY_INFO: LogSeverity
LOG_SEVERITY_WARN: LogSeverity
LOG_SEVERITY_ERROR: LogSeverity
LOG_SEVERITY_FATAL: LogSeverity

class LogAttributeValue(_message.Message):
    __slots__ = ("string_value", "bool_value", "int_value", "double_value", "bytes_value")
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    BYTES_VALUE_FIELD_NUMBER: _ClassVar[int]
    string_value: str
    bool_value: bool
    int_value: int
    double_value: float
    bytes_value: bytes
    def __init__(self, string_value: _Optional[str] = ..., bool_value: bool = ..., int_value: _Optional[int] = ..., double_value: _Optional[float] = ..., bytes_value: _Optional[bytes] = ...) -> None: ...

class LogAttribute(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: LogAttributeValue
    def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[LogAttributeValue, _Mapping]] = ...) -> None: ...

class LogResource(_message.Message):
    __slots__ = ("service_name", "service_version", "service_instance_id", "environment", "application_type")
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_VERSION_FIELD_NUMBER: _ClassVar[int]
    SERVICE_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    service_name: str
    service_version: str
    service_instance_id: str
    environment: str
    application_type: str
    def __init__(self, service_name: _Optional[str] = ..., service_version: _Optional[str] = ..., service_instance_id: _Optional[str] = ..., environment: _Optional[str] = ..., application_type: _Optional[str] = ...) -> None: ...

class LogSource(_message.Message):
    __slots__ = ("file", "line", "function")
    FILE_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_FIELD_NUMBER: _ClassVar[int]
    file: str
    line: int
    function: str
    def __init__(self, file: _Optional[str] = ..., line: _Optional[int] = ..., function: _Optional[str] = ...) -> None: ...

class LogException(_message.Message):
    __slots__ = ("type", "message", "stack_trace")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STACK_TRACE_FIELD_NUMBER: _ClassVar[int]
    type: str
    message: str
    stack_trace: str
    def __init__(self, type: _Optional[str] = ..., message: _Optional[str] = ..., stack_trace: _Optional[str] = ...) -> None: ...

class LogRecord(_message.Message):
    __slots__ = ("id", "timestamp", "observed_at", "severity", "severity_text", "body", "resource", "attributes", "source", "exception", "logger_name", "sequence_number")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_AT_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_TEXT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    EXCEPTION_FIELD_NUMBER: _ClassVar[int]
    LOGGER_NAME_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    id: str
    timestamp: _timestamp_pb2.Timestamp
    observed_at: _timestamp_pb2.Timestamp
    severity: LogSeverity
    severity_text: str
    body: str
    resource: LogResource
    attributes: _containers.RepeatedCompositeFieldContainer[LogAttribute]
    source: LogSource
    exception: LogException
    logger_name: str
    sequence_number: int
    def __init__(self, id: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., observed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., severity: _Optional[_Union[LogSeverity, str]] = ..., severity_text: _Optional[str] = ..., body: _Optional[str] = ..., resource: _Optional[_Union[LogResource, _Mapping]] = ..., attributes: _Optional[_Iterable[_Union[LogAttribute, _Mapping]]] = ..., source: _Optional[_Union[LogSource, _Mapping]] = ..., exception: _Optional[_Union[LogException, _Mapping]] = ..., logger_name: _Optional[str] = ..., sequence_number: _Optional[int] = ...) -> None: ...

class LogRecords(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[LogRecord]
    def __init__(self, items: _Optional[_Iterable[_Union[LogRecord, _Mapping]]] = ...) -> None: ...
