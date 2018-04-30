# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TrackMetadata.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='TrackMetadata.proto',
  package='com.hashmapinc.tempus.edge.proto',
  syntax='proto3',
  serialized_pb=_b('\n\x13TrackMetadata.proto\x12 com.hashmapinc.tempus.edge.proto\"G\n\rTrackMetadata\x12\x12\n\ntrack_name\x18\x01 \x01(\t\x12\x10\n\x08track_id\x18\x02 \x01(\r\x12\x10\n\x08metadata\x18\x03 \x01(\tB\"Z com/hashmapinc/tempus/edge/protob\x06proto3')
)




_TRACKMETADATA = _descriptor.Descriptor(
  name='TrackMetadata',
  full_name='com.hashmapinc.tempus.edge.proto.TrackMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='track_name', full_name='com.hashmapinc.tempus.edge.proto.TrackMetadata.track_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='track_id', full_name='com.hashmapinc.tempus.edge.proto.TrackMetadata.track_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='com.hashmapinc.tempus.edge.proto.TrackMetadata.metadata', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=128,
)

DESCRIPTOR.message_types_by_name['TrackMetadata'] = _TRACKMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TrackMetadata = _reflection.GeneratedProtocolMessageType('TrackMetadata', (_message.Message,), dict(
  DESCRIPTOR = _TRACKMETADATA,
  __module__ = 'TrackMetadata_pb2'
  # @@protoc_insertion_point(class_scope:com.hashmapinc.tempus.edge.proto.TrackMetadata)
  ))
_sym_db.RegisterMessage(TrackMetadata)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z com/hashmapinc/tempus/edge/proto'))
# @@protoc_insertion_point(module_scope)