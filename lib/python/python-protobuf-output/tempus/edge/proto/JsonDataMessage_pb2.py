# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: JsonDataMessage.proto

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
  name='JsonDataMessage.proto',
  package='com.hashmapinc.tempus.edge.proto',
  syntax='proto3',
  serialized_pb=_b('\n\x15JsonDataMessage.proto\x12 com.hashmapinc.tempus.edge.proto\"\x1f\n\x0fJsonDataMessage\x12\x0c\n\x04json\x18\x01 \x01(\tB\"Z com/hashmapinc/tempus/edge/protob\x06proto3')
)




_JSONDATAMESSAGE = _descriptor.Descriptor(
  name='JsonDataMessage',
  full_name='com.hashmapinc.tempus.edge.proto.JsonDataMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='json', full_name='com.hashmapinc.tempus.edge.proto.JsonDataMessage.json', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=59,
  serialized_end=90,
)

DESCRIPTOR.message_types_by_name['JsonDataMessage'] = _JSONDATAMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

JsonDataMessage = _reflection.GeneratedProtocolMessageType('JsonDataMessage', (_message.Message,), dict(
  DESCRIPTOR = _JSONDATAMESSAGE,
  __module__ = 'JsonDataMessage_pb2'
  # @@protoc_insertion_point(class_scope:com.hashmapinc.tempus.edge.proto.JsonDataMessage)
  ))
_sym_db.RegisterMessage(JsonDataMessage)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z com/hashmapinc/tempus/edge/proto'))
# @@protoc_insertion_point(module_scope)
