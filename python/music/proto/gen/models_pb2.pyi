from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetAlbumsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Album(_message.Message):
    __slots__ = ("id", "title", "artist", "price")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ARTIST_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: str
    artist: str
    price: float
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ..., artist: _Optional[str] = ..., price: _Optional[float] = ...) -> None: ...

class GetAlbumsResponse(_message.Message):
    __slots__ = ("albums",)
    ALBUMS_FIELD_NUMBER: _ClassVar[int]
    albums: _containers.RepeatedCompositeFieldContainer[Album]
    def __init__(self, albums: _Optional[_Iterable[_Union[Album, _Mapping]]] = ...) -> None: ...
