# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: service/v1/status.proto
# Protobuf Python Version: 6.31.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    1,
    '',
    'service/v1/status.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17service/v1/status.proto\x12\nservice.v1\"\xa5\x01\n\rServiceStatus\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x12\n\x04type\x18\x04 \x01(\tR\x04type\x12\x0e\n\x02ip\x18\x05 \x01(\tR\x02ip\x12*\n\x06status\x18\x06 \x01(\x0e\x32\x12.service.v1.StatusR\x06status*G\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x12\n\x0eSTATUS_OFFLINE\x10\x01\x12\x11\n\rSTATUS_ONLINE\x10\x02\x42\xaa\x01\n\x0e\x63om.service.v1B\x0bStatusProtoP\x01Z9github.com/cobotar/protocol/messages/service/v1;servicev1\xa2\x02\x03SXX\xaa\x02\x13Messages.Service.V1\xca\x02\nService\\V1\xe2\x02\x16Service\\V1\\GPBMetadata\xea\x02\x0bService::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service.v1.status_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\016com.service.v1B\013StatusProtoP\001Z9github.com/cobotar/protocol/messages/service/v1;servicev1\242\002\003SXX\252\002\023Messages.Service.V1\312\002\nService\\V1\342\002\026Service\\V1\\GPBMetadata\352\002\013Service::V1'
  _globals['_STATUS']._serialized_start=207
  _globals['_STATUS']._serialized_end=278
  _globals['_SERVICESTATUS']._serialized_start=40
  _globals['_SERVICESTATUS']._serialized_end=205
# @@protoc_insertion_point(module_scope)
