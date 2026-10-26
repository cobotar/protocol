from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class CatalogStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CATALOG_STATUS_UNSPECIFIED: _ClassVar[CatalogStatus]
    CATALOG_STATUS_ACTIVE: _ClassVar[CatalogStatus]
    CATALOG_STATUS_EXPERIMENTAL: _ClassVar[CatalogStatus]
    CATALOG_STATUS_DEPRECATED: _ClassVar[CatalogStatus]
    CATALOG_STATUS_DISABLED: _ClassVar[CatalogStatus]
CATALOG_STATUS_UNSPECIFIED: CatalogStatus
CATALOG_STATUS_ACTIVE: CatalogStatus
CATALOG_STATUS_EXPERIMENTAL: CatalogStatus
CATALOG_STATUS_DEPRECATED: CatalogStatus
CATALOG_STATUS_DISABLED: CatalogStatus
