from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class WorkerPermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WORKER_PERMISSION_UNSPECIFIED: _ClassVar[WorkerPermission]
    WORKER_PERMISSION_BASIC: _ClassVar[WorkerPermission]
    WORKER_PERMISSION_COSMETIC: _ClassVar[WorkerPermission]
    WORKER_PERMISSION_FULL: _ClassVar[WorkerPermission]
    WORKER_PERMISSION_NONE: _ClassVar[WorkerPermission]
WORKER_PERMISSION_UNSPECIFIED: WorkerPermission
WORKER_PERMISSION_BASIC: WorkerPermission
WORKER_PERMISSION_COSMETIC: WorkerPermission
WORKER_PERMISSION_FULL: WorkerPermission
WORKER_PERMISSION_NONE: WorkerPermission
