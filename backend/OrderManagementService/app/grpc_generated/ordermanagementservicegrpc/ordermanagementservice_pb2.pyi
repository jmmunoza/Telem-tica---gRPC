from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Order(_message.Message):
    __slots__ = ["amount", "order_id", "produtct_id"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUTCT_ID_FIELD_NUMBER: _ClassVar[int]
    amount: int
    order_id: int
    produtct_id: int
    def __init__(self, order_id: _Optional[int] = ..., produtct_id: _Optional[int] = ..., amount: _Optional[int] = ...) -> None: ...

class OrderRetrieveRequest(_message.Message):
    __slots__ = ["order_id"]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    order_id: int
    def __init__(self, order_id: _Optional[int] = ...) -> None: ...
