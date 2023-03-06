from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Product(_message.Message):
    __slots__ = ["name", "price", "produtct_id"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    PRODUTCT_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    price: int
    produtct_id: int
    def __init__(self, produtct_id: _Optional[int] = ..., name: _Optional[str] = ..., price: _Optional[int] = ...) -> None: ...

class ProductListRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ProductRetrieveRequest(_message.Message):
    __slots__ = ["produtct_id"]
    PRODUTCT_ID_FIELD_NUMBER: _ClassVar[int]
    produtct_id: int
    def __init__(self, produtct_id: _Optional[int] = ...) -> None: ...
