# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: algo_commander.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='algo_commander.proto',
  package='algo_commander',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14\x61lgo_commander.proto\x12\x0e\x61lgo_commander\"[\n\rRobotPosition\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05pos_x\x18\x02 \x01(\x02\x12\r\n\x05pos_y\x18\x03 \x01(\x02\x12\r\n\x05\x61ngle\x18\x04 \x01(\x02\x12\x11\n\tblue_team\x18\x05 \x01(\x08\x62\x06proto3'
)




_ROBOTPOSITION = _descriptor.Descriptor(
  name='RobotPosition',
  full_name='algo_commander.RobotPosition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='algo_commander.RobotPosition.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pos_x', full_name='algo_commander.RobotPosition.pos_x', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pos_y', full_name='algo_commander.RobotPosition.pos_y', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='angle', full_name='algo_commander.RobotPosition.angle', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='blue_team', full_name='algo_commander.RobotPosition.blue_team', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=131,
)

DESCRIPTOR.message_types_by_name['RobotPosition'] = _ROBOTPOSITION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RobotPosition = _reflection.GeneratedProtocolMessageType('RobotPosition', (_message.Message,), {
  'DESCRIPTOR' : _ROBOTPOSITION,
  '__module__' : 'algo_commander_pb2'
  # @@protoc_insertion_point(class_scope:algo_commander.RobotPosition)
  })
_sym_db.RegisterMessage(RobotPosition)


# @@protoc_insertion_point(module_scope)
