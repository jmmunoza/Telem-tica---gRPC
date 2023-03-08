from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateOrderRequest(_message.Message):
    __slots__ = ["amount", "product_id"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    amount: int
    product_id: str
    def __init__(self, product_id: _Optional[str] = ..., amount: _Optional[int] = ...) -> None: ...

class GetAllOrdersRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Order(_message.Message):
    __slots__ = ["amount", "order_id", "product_id"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    amount: int
    order_id: str
    product_id: str
    def __init__(self, order_id: _Optional[str] = ..., product_id: _Optional[str] = ..., amount: _Optional[int] = ...) -> None: ...

class OrderRequest(_message.Message):
    __slots__ = ["order_id"]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    order_id: str
    def __init__(self, order_id: _Optional[str] = ...) -> None: ...

class OrderResponse(_message.Message):
    __slots__ = ["is_successful", "message"]
    IS_SUCCESSFUL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    is_successful: bool
    message: str
    def __init__(self, is_successful: bool = ..., message: _Optional[str] = ...) -> None: ...
