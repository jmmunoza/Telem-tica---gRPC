from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteProductRequest(_message.Message):
    __slots__ = ["product_id"]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    product_id: int
    def __init__(self, product_id: _Optional[int] = ...) -> None: ...

class GetAllProductsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetProductRequest(_message.Message):
    __slots__ = ["product_id"]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    product_id: int
    def __init__(self, product_id: _Optional[int] = ...) -> None: ...

class Product(_message.Message):
    __slots__ = ["name", "price", "product_id", "stock"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    STOCK_FIELD_NUMBER: _ClassVar[int]
    name: str
    price: int
    product_id: int
    stock: int
    def __init__(self, product_id: _Optional[int] = ..., name: _Optional[str] = ..., price: _Optional[int] = ..., stock: _Optional[int] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ["is_successfull", "message"]
    IS_SUCCESSFULL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    is_successfull: bool
    message: str
    def __init__(self, is_successfull: bool = ..., message: _Optional[str] = ...) -> None: ...
