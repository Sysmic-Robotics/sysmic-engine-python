# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages_robocup_ssl_refbox_log.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import messages_robocup_ssl_detection_pb2 as messages__robocup__ssl__detection__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%messages_robocup_ssl_refbox_log.proto\x1a$messages_robocup_ssl_detection.proto\"C\n\tLog_Frame\x12\"\n\x05\x66rame\x18\x01 \x01(\x0b\x32\x13.SSL_DetectionFrame\x12\x12\n\nrefbox_cmd\x18\x02 \x01(\t\"%\n\nRefbox_Log\x12\x17\n\x03log\x18\x01 \x03(\x0b\x32\n.Log_Frameb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'messages_robocup_ssl_refbox_log_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_LOG_FRAME']._serialized_start=79
  _globals['_LOG_FRAME']._serialized_end=146
  _globals['_REFBOX_LOG']._serialized_start=148
  _globals['_REFBOX_LOG']._serialized_end=185
# @@protoc_insertion_point(module_scope)