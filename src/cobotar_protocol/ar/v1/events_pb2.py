# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: ar/v1/events.proto
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
    'ar/v1/events.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x61r/v1/events.proto\x12\x05\x61r.v1\"B\n\x16SupportedEventsMessage\x12(\n\x06\x65vents\x18\x01 \x03(\x0e\x32\x10.ar.v1.EventTypeR\x06\x65vents*\xeb\x02\n\tEventType\x12\x1a\n\x16\x45VENT_TYPE_UNSPECIFIED\x10\x00\x12\x1c\n\x18\x45VENT_TYPE_TASK_COMPLETE\x10\n\x12\x18\n\x14\x45VENT_TYPE_TASK_UNDO\x10\x0b\x12\x1a\n\x16\x45VENT_TYPE_TASK_ASSIGN\x10\x0c\x12\x1d\n\x19\x45VENT_TYPE_TASK_HIGHLIGHT\x10\r\x12\x18\n\x14\x45VENT_TYPE_TASK_HELP\x10\x0e\x12\x18\n\x14\x45VENT_TYPE_ROBOT_TCP\x10\x64\x12!\n\x1d\x45VENT_TYPE_ROBOT_JOINT_ANGLES\x10\x65\x12!\n\x1d\x45VENT_TYPE_ROBOT_FORCE_TORQUE\x10\x66\x12\x1a\n\x16\x45VENT_TYPE_ROBOT_STATE\x10n\x12\x19\n\x15\x45VENT_TYPE_ROBOT_PATH\x10x\x12\x1e\n\x1a\x45VENT_TYPE_ROBOT_WAYPOINTS\x10yB\x87\x01\n\tcom.ar.v1B\x0b\x45ventsProtoP\x01Z/github.com/cobotar/protocol/messages/ar/v1;arv1\xa2\x02\x03\x41XX\xaa\x02\x0eMessages.AR.V1\xca\x02\x05\x41r\\V1\xe2\x02\x11\x41r\\V1\\GPBMetadata\xea\x02\x06\x41r::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ar.v1.events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\tcom.ar.v1B\013EventsProtoP\001Z/github.com/cobotar/protocol/messages/ar/v1;arv1\242\002\003AXX\252\002\016Messages.AR.V1\312\002\005Ar\\V1\342\002\021Ar\\V1\\GPBMetadata\352\002\006Ar::V1'
  _globals['_EVENTTYPE']._serialized_start=98
  _globals['_EVENTTYPE']._serialized_end=461
  _globals['_SUPPORTEDEVENTSMESSAGE']._serialized_start=29
  _globals['_SUPPORTEDEVENTSMESSAGE']._serialized_end=95
# @@protoc_insertion_point(module_scope)
