import datetime

from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from validation.v1 import predefined_string_rules_pb2 as _predefined_string_rules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StorageSeedRecord(_message.Message):
    __slots__ = ("fingerprint", "applied_at")
    FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    APPLIED_AT_FIELD_NUMBER: _ClassVar[int]
    fingerprint: str
    applied_at: _timestamp_pb2.Timestamp
    def __init__(self, fingerprint: _Optional[str] = ..., applied_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class StorageDumpRequest(_message.Message):
    __slots__ = ("object_name",)
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    object_name: str
    def __init__(self, object_name: _Optional[str] = ...) -> None: ...

class StorageDumpResult(_message.Message):
    __slots__ = ("object_name", "size_bytes", "entity_counts", "created_at")
    class EntityCountsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    ENTITY_COUNTS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    object_name: str
    size_bytes: int
    entity_counts: _containers.ScalarMap[str, int]
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, object_name: _Optional[str] = ..., size_bytes: _Optional[int] = ..., entity_counts: _Optional[_Mapping[str, int]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class StorageLoadRequest(_message.Message):
    __slots__ = ("object_name",)
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    object_name: str
    def __init__(self, object_name: _Optional[str] = ...) -> None: ...

class StorageClearRequest(_message.Message):
    __slots__ = ("apply_configured_seeds", "confirmation_instance_id")
    APPLY_CONFIGURED_SEEDS_FIELD_NUMBER: _ClassVar[int]
    CONFIRMATION_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    apply_configured_seeds: bool
    confirmation_instance_id: str
    def __init__(self, apply_configured_seeds: bool = ..., confirmation_instance_id: _Optional[str] = ...) -> None: ...

class StorageInfo(_message.Message):
    __slots__ = ("backend", "instance_id", "size_bytes", "entity_counts", "seed_record", "experimenter_mode", "last_dump_at")
    class EntityCountsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    BACKEND_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    ENTITY_COUNTS_FIELD_NUMBER: _ClassVar[int]
    SEED_RECORD_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENTER_MODE_FIELD_NUMBER: _ClassVar[int]
    LAST_DUMP_AT_FIELD_NUMBER: _ClassVar[int]
    backend: str
    instance_id: str
    size_bytes: int
    entity_counts: _containers.ScalarMap[str, int]
    seed_record: StorageSeedRecord
    experimenter_mode: bool
    last_dump_at: _timestamp_pb2.Timestamp
    def __init__(self, backend: _Optional[str] = ..., instance_id: _Optional[str] = ..., size_bytes: _Optional[int] = ..., entity_counts: _Optional[_Mapping[str, int]] = ..., seed_record: _Optional[_Union[StorageSeedRecord, _Mapping]] = ..., experimenter_mode: bool = ..., last_dump_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class StorageCollectGarbageRequest(_message.Message):
    __slots__ = ("dry_run", "min_age")
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    MIN_AGE_FIELD_NUMBER: _ClassVar[int]
    dry_run: bool
    min_age: _duration_pb2.Duration
    def __init__(self, dry_run: bool = ..., min_age: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class StorageObject(_message.Message):
    __slots__ = ("bucket", "key", "size_bytes")
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    key: str
    size_bytes: int
    def __init__(self, bucket: _Optional[str] = ..., key: _Optional[str] = ..., size_bytes: _Optional[int] = ...) -> None: ...

class StorageCollectGarbageResult(_message.Message):
    __slots__ = ("dry_run", "removed", "removed_bytes", "kept")
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    REMOVED_FIELD_NUMBER: _ClassVar[int]
    REMOVED_BYTES_FIELD_NUMBER: _ClassVar[int]
    KEPT_FIELD_NUMBER: _ClassVar[int]
    dry_run: bool
    removed: _containers.RepeatedCompositeFieldContainer[StorageObject]
    removed_bytes: int
    kept: int
    def __init__(self, dry_run: bool = ..., removed: _Optional[_Iterable[_Union[StorageObject, _Mapping]]] = ..., removed_bytes: _Optional[int] = ..., kept: _Optional[int] = ...) -> None: ...
