# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages_robocup_ssl_wrapper.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import messages_robocup_ssl_detection_pb2
from . import messages_robocup_ssl_geometry_pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"messages_robocup_ssl_wrapper.proto\x1a$messages_robocup_ssl_detection.proto\x1a#messages_robocup_ssl_geometry.proto\"\x85\x01\n\x11SSL_WrapperPacket\x12+\n\tdetection\x18\x01 \x01(\x0b\x32\x13.SSL_DetectionFrameH\x00\x88\x01\x01\x12(\n\x08geometry\x18\x02 \x01(\x0b\x32\x11.SSL_GeometryDataH\x01\x88\x01\x01\x42\x0c\n\n_detectionB\x0b\n\t_geometryb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'messages_robocup_ssl_wrapper_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_SSL_WRAPPERPACKET']._serialized_start=114
  _globals['_SSL_WRAPPERPACKET']._serialized_end=247
# @@protoc_insertion_point(module_scope)