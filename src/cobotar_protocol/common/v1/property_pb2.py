# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: common/v1/property.proto
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
    'common/v1/property.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x63ommon/v1/property.proto\x12\tcommon.v1\"\xcb\x03\n\x08Property\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x12\n\x04icon\x18\x03 \x01(\tR\x04icon\x12 \n\x0b\x64\x65scription\x18\x04 \x01(\tR\x0b\x64\x65scription\x12+\n\x04type\x18\x05 \x01(\x0e\x32\x17.common.v1.PropertyTypeR\x04type\x12\x14\n\x05value\x18\x06 \x01(\tR\x05value\x12\x16\n\x06\x65xtras\x18\x07 \x01(\tR\x06\x65xtras\x12#\n\ruser_editable\x18\x08 \x01(\x08R\x0cuserEditable\x12\x31\n\x06origin\x18\t \x01(\x0e\x32\x19.common.v1.PropertyOriginR\x06origin\x12\x33\n\x07origins\x18\n \x03(\x0e\x32\x19.common.v1.PropertyOriginR\x07origins\x12,\n\x12mirror_property_id\x18\x0b \x01(\tR\x10mirrorPropertyId\x12\x14\n\x05group\x18\x0c \x01(\tR\x05group\x12\x1a\n\x08ordering\x18\r \x01(\x05R\x08ordering\x12\x1d\n\nhide_group\x18\x0e \x01(\x08R\thideGroup*\xde\x02\n\x0cPropertyType\x12\x1d\n\x19PROPERTY_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12PROPERTY_TYPE_BOOL\x10\x01\x12\x15\n\x11PROPERTY_TYPE_INT\x10\x02\x12\x17\n\x13PROPERTY_TYPE_FLOAT\x10\x03\x12\x18\n\x14PROPERTY_TYPE_DOUBLE\x10\x04\x12\x18\n\x14PROPERTY_TYPE_STRING\x10\x05\x12\x19\n\x15PROPERTY_TYPE_VECTOR3\x10\x06\x12\x16\n\x12PROPERTY_TYPE_POSE\x10\x07\x12\x18\n\x14PROPERTY_TYPE_ANCHOR\x10\x08\x12\x17\n\x13PROPERTY_TYPE_COLOR\x10\t\x12\x17\n\x13PROPERTY_TYPE_AGENT\x10\n\x12\x16\n\x12PROPERTY_TYPE_ENUM\x10\x0b\x12\x1c\n\x18PROPERTY_TYPE_ENUM_MULTI\x10\x0c*h\n\x0ePropertyOrigin\x12\x1f\n\x1bPROPERTY_ORIGIN_UNSPECIFIED\x10\x00\x12\x19\n\x15PROPERTY_ORIGIN_FIXED\x10\x01\x12\x1a\n\x16PROPERTY_ORIGIN_MIRROR\x10\x02\x42\xa5\x01\n\rcom.common.v1B\rPropertyProtoP\x01Z7github.com/cobotar/protocol/messages/common/v1;commonv1\xa2\x02\x03\x43XX\xaa\x02\x12Messages.Common.V1\xca\x02\tCommon\\V1\xe2\x02\x15\x43ommon\\V1\\GPBMetadata\xea\x02\nCommon::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common.v1.property_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\rcom.common.v1B\rPropertyProtoP\001Z7github.com/cobotar/protocol/messages/common/v1;commonv1\242\002\003CXX\252\002\022Messages.Common.V1\312\002\tCommon\\V1\342\002\025Common\\V1\\GPBMetadata\352\002\nCommon::V1'
  _globals['_PROPERTYTYPE']._serialized_start=502
  _globals['_PROPERTYTYPE']._serialized_end=852
  _globals['_PROPERTYORIGIN']._serialized_start=854
  _globals['_PROPERTYORIGIN']._serialized_end=958
  _globals['_PROPERTY']._serialized_start=40
  _globals['_PROPERTY']._serialized_end=499
# @@protoc_insertion_point(module_scope)
