from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AddProductRequest(_message.Message):
    __slots__ = ["name", "price", "stock"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    STOCK_FIELD_NUMBER: _ClassVar[int]
    name: str
    price: float
    stock: int
    def __init__(self, name: _Optional[str] = ..., price: _Optional[float] = ..., stock: _Optional[int] = ...) -> None: ...

class DeleteProductRequest(_message.Message):
    __slots__ = ["product_id"]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    def __init__(self, product_id: _Optional[str] = ...) -> None: ...

class GetAllProductsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetProductRequest(_message.Message):
    __slots__ = ["product_id"]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    def __init__(self, product_id: _Optional[str] = ...) -> None: ...

class Product(_message.Message):
    __slots__ = ["name", "price", "product_id", "stock"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    STOCK_FIELD_NUMBER: _ClassVar[int]
    name: str
    price: float
    product_id: str
    stock: int
    def __init__(self, product_id: _Optional[str] = ..., name: _Optional[str] = ..., price: _Optional[float] = ..., stock: _Optional[int] = ...) -> None: ...

class ProductResponse(_message.Message):
    __slots__ = ["is_successful", "message"]
    IS_SUCCESSFUL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    is_successful: bool
    message: str
    def __init__(self, is_successful: bool = ..., message: _Optional[str] = ...) -> None: ...
