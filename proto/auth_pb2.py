# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nauth.proto\"\x18\n\x07\x41uthReq\x12\r\n\x05token\x18\x01 \x01(\t\"\x8c\x01\n\x07\x41uthRes\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x14\n\x0cuser_account\x18\x02 \x01(\t\x12\x14\n\x0c\x63reated_date\x18\x03 \x01(\t\x12\x18\n\x10pwd_updated_date\x18\x04 \x01(\t\x12\x13\n\x0bstatus_code\x18\x05 \x01(\x05\x12\x15\n\rresponse_code\x18\x06 \x01(\t2*\n\x04\x41uth\x12\"\n\nTokenCheck\x12\x08.AuthReq\x1a\x08.AuthRes\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'auth_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _AUTHREQ._serialized_start=14
  _AUTHREQ._serialized_end=38
  _AUTHRES._serialized_start=41
  _AUTHRES._serialized_end=181
  _AUTH._serialized_start=183
  _AUTH._serialized_end=225
# @@protoc_insertion_point(module_scope)