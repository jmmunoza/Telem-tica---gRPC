# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inventoryservice.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16inventoryservice.proto\"I\n\x07Product\x12\x12\n\nproduct_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05price\x18\x03 \x01(\x02\x12\r\n\x05stock\x18\x04 \x01(\x05\"?\n\x11\x41\x64\x64ProductRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\x02\x12\r\n\x05stock\x18\x03 \x01(\x05\"\x17\n\x15GetAllProductsRequest\"2\n\x08Response\x12\x15\n\ris_successful\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"\'\n\x11GetProductRequest\x12\x12\n\nproduct_id\x18\x01 \x01(\t\"*\n\x14\x44\x65leteProductRequest\x12\x12\n\nproduct_id\x18\x01 \x01(\t2\xbe\x01\n\x10InventoryService\x12.\n\x06getAll\x12\x16.GetAllProductsRequest\x1a\x08.Product\"\x00\x30\x01\x12%\n\x03\x61\x64\x64\x12\x12.AddProductRequest\x1a\x08.Product\"\x00\x12%\n\x03get\x12\x12.GetProductRequest\x1a\x08.Product\"\x00\x12,\n\x06\x64\x65lete\x12\x15.DeleteProductRequest\x1a\t.Response\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'inventoryservice_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PRODUCT._serialized_start=26
  _PRODUCT._serialized_end=99
  _ADDPRODUCTREQUEST._serialized_start=101
  _ADDPRODUCTREQUEST._serialized_end=164
  _GETALLPRODUCTSREQUEST._serialized_start=166
  _GETALLPRODUCTSREQUEST._serialized_end=189
  _RESPONSE._serialized_start=191
  _RESPONSE._serialized_end=241
  _GETPRODUCTREQUEST._serialized_start=243
  _GETPRODUCTREQUEST._serialized_end=282
  _DELETEPRODUCTREQUEST._serialized_start=284
  _DELETEPRODUCTREQUEST._serialized_end=326
  _INVENTORYSERVICE._serialized_start=329
  _INVENTORYSERVICE._serialized_end=519
# @@protoc_insertion_point(module_scope)
