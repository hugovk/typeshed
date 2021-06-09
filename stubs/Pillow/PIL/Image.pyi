from _typeshed import SupportsRead, SupportsWrite
from collections.abc import Iterable, Iterator, MutableMapping
from pathlib import Path
from typing import Any, Dict, Protocol, Tuple, Union
from typing_extensions import Literal

from ._imaging import (
    DEFAULT_STRATEGY as DEFAULT_STRATEGY,
    FILTERED as FILTERED,
    FIXED as FIXED,
    HUFFMAN_ONLY as HUFFMAN_ONLY,
    RLE as RLE,
)

_Mode = Literal["1", "CMYK", "F", "HSV", "I", "L", "LAB", "P", "RGB", "RGBA", "RGBX", "YCbCr"]
_Resample = Literal[0, 1, 2, 3, 4, 5]

_ConversionMatrix = Union[
    Tuple[float, float, float, float], Tuple[float, float, float, float, float, float, float, float, float, float, float, float],
]
_Color = Union[float, Tuple[float, ...]]

class _Writeable(SupportsWrite[bytes], Protocol):
    def seek(self, __offset: int) -> Any: ...

# obsolete
NORMAL: Literal[0]
SEQUENCE: Literal[1]
CONTAINER: Literal[2]

class DecompressionBombWarning(RuntimeWarning): ...
class DecompressionBombError(Exception): ...

MAX_IMAGE_PIXELS: int

NONE: Literal[0]

FLIP_LEFT_RIGHT: Literal[0]
FLIP_TOP_BOTTOM: Literal[1]
ROTATE_90: Literal[2]
ROTATE_180: Literal[3]
ROTATE_270: Literal[4]
TRANSPOSE: Literal[5]
TRANSVERSE: Literal[6]

AFFINE: Literal[0]
EXTENT: Literal[1]
PERSPECTIVE: Literal[2]
QUAD: Literal[3]
MESH: Literal[4]

NEAREST: Literal[0]
BOX: Literal[4]
BILINEAR: Literal[2]
LINEAR: Literal[2]
HAMMING: Literal[5]
BICUBIC: Literal[3]
CUBIC: Literal[3]
LANCZOS: Literal[1]
ANTIALIAS: Literal[1]

ORDERED: Literal[1]
RASTERIZE: Literal[2]
FLOYDSTEINBERG: Literal[3]

WEB: Literal[0]
ADAPTIVE: Literal[1]

MEDIANCUT: Literal[0]
MAXCOVERAGE: Literal[1]
FASTOCTREE: Literal[2]
LIBIMAGEQUANT: Literal[3]

ID: list[str]
OPEN: dict[str, Any]
MIME: dict[str, str]
SAVE: dict[str, Any]
SAVE_ALL: dict[str, Any]
EXTENSION: dict[str, str]
DECODERS: dict[str, Any]
ENCODERS: dict[str, Any]

MODES: list[_Mode]

def getmodebase(mode: _Mode) -> Literal["L", "RGB"]: ...
def getmodetype(mode: _Mode) -> Literal["L", "I", "F"]: ...
def getmodebandnames(mode: _Mode) -> Tuple[str, ...]: ...
def getmodebands(mode: _Mode) -> int: ...
def preinit() -> None: ...
def init() -> None: ...
def coerce_e(value) -> _E: ...

class _E:
    def __init__(self, data) -> None: ...
    def __add__(self, other) -> _E: ...
    def __mul__(self, other) -> _E: ...

_ImageState = Tuple[Dict[str, Any], str, Tuple[int, int], Any, bytes]

class Image:
    format: Any
    format_description: Any
    im: Any
    mode: str
    palette: Any
    info: dict[Any, Any]
    readonly: int
    pyaccess: Any
    @property
    def category(self) -> int: ...  # obsolete
    @property
    def width(self) -> int: ...
    @property
    def height(self) -> int: ...
    @property
    def size(self) -> tuple[int, int]: ...
    def __enter__(self) -> Image: ...
    def __exit__(self, *args: Any) -> None: ...
    def close(self) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    @property
    def __array_interface__(self) -> dict[str, Any]: ...
    def __getstate__(self) -> _ImageState: ...
    def __setstate__(self, state: _ImageState) -> None: ...
    def tobytes(self, encoder_name: str = ..., *args) -> bytes: ...
    def tobitmap(self, name: str = ...) -> bytes: ...
    def frombytes(self, data: bytes, decoder_name: str = ..., *args) -> None: ...
    def load(self): ...
    def verify(self) -> None: ...
    def convert(
        self,
        mode: str | None = ...,
        matrix: _ConversionMatrix | None = ...,
        dither: int | None = ...,
        palette: Literal[0, 1] = ...,
        colors: int = ...,
    ) -> Image: ...
    def quantize(
        self,
        colors: int = ...,
        method: Literal[0, 1, 2, 3] | None = ...,
        kmeans: int = ...,
        palette: Image | None = ...,
        dither: int = ...,
    ) -> Image: ...
    def copy(self) -> Image: ...
    __copy__ = copy
    def crop(self, box=...) -> Image: ...
    def draft(self, mode, size) -> None: ...
    def filter(self, filter): ...
    def getbands(self) -> Tuple[str, ...]: ...
    def getbbox(self) -> tuple[int, int, int, int] | None: ...
    def getcolors(self, maxcolors: int = ...): ...
    def getdata(self, band=...): ...
    def getextrema(self): ...
    def getexif(self) -> Exif: ...
    def getim(self): ...
    def getpalette(self): ...
    def getpixel(self, xy): ...
    def getprojection(self): ...
    def histogram(self, mask=..., extrema=...): ...
    def entropy(self, mask=..., extrema=...): ...
    def paste(
        self, im: Image, box: tuple[float, float] | tuple[float, float, float, float] | None = ..., mask: Image | None = ...
    ) -> None: ...
    def alpha_composite(self, im: Image, dest: tuple[int, int] = ..., source: tuple[int, int] = ...) -> None: ...
    def point(self, lut, mode=...): ...
    def putalpha(self, alpha): ...
    def putdata(self, data, scale: float = ..., offset: float = ...): ...
    def putpalette(self, data, rawmode=...): ...
    def putpixel(self, xy, value): ...
    def remap_palette(self, dest_map, source_palette=...): ...
    def resize(
        self, size: tuple[int, int], resample: _Resample = ..., box: tuple[float, float, float, float] | None = ...
    ) -> Image: ...
    def reduce(self, factor, box=...): ...
    def rotate(
        self,
        angle: float,
        resample: _Resample = ...,
        expand: bool = ...,
        center: tuple[float, float] | None = ...,
        translate: tuple[float, float] | None = ...,
        fillcolor: _Color | None = ...,
    ) -> Image: ...
    def save(self, fp: str | bytes | Path | _Writeable, format: str | None = ..., **params: Any) -> None: ...
    def seek(self, frame): ...
    def show(self, title=..., command=...): ...
    def split(self): ...
    def getchannel(self, channel): ...
    def tell(self) -> int: ...
    def thumbnail(self, size: tuple[int, int], resample: _Resample = ..., reducing_gap: float = ...) -> None: ...
    def transform(
        self, size, method: Literal[0, 1, 2, 3, 4], data=..., resample: _Resample = ..., fill: int = ..., fillcolor=...
    ) -> None: ...
    def transpose(self, method: Literal[0, 1, 2, 3, 4, 5, 6]): ...
    def effect_spread(self, distance): ...
    def toqimage(self): ...
    def toqpixmap(self): ...

class ImagePointHandler: ...
class ImageTransformHandler: ...

def new(mode: _Mode, size: tuple[int, int], color: float | Tuple[float, ...] = ...) -> Image: ...
def frombytes(mode: _Mode, size: tuple[int, int], data, decoder_name: str = ..., *args) -> Image: ...
def frombuffer(mode: _Mode, size: tuple[int, int], data, decoder_name: str = ..., *args) -> Image: ...
def fromarray(obj, mode: _Mode = ...) -> Image: ...
def fromqimage(im) -> Image: ...
def fromqpixmap(im) -> Image: ...
def open(fp: str | bytes | Path | SupportsRead[bytes], mode: _Mode = ..., formats=...) -> Image: ...
def alpha_composite(im1: Image, im2: Image) -> Image: ...
def blend(im1: Image, im2: Image, alpha) -> Image: ...
def composite(image1: Image, image2: Image, mask) -> Image: ...
def eval(image: Image, *args): ...
def merge(mode, bands): ...
def register_open(id: str, factory, accept=...) -> None: ...
def register_mime(id: str, mimetype: str) -> None: ...
def register_save(id: str, driver) -> None: ...
def register_save_all(id: str, driver) -> None: ...
def register_extension(id: str, extension: str) -> None: ...
def register_extensions(id: str, extensions: Iterable[str]) -> None: ...
def registered_extensions() -> dict[str, str]: ...
def register_decoder(name: str, decoder) -> None: ...
def register_encoder(name: str, encoder) -> None: ...
def effect_mandelbrot(size: tuple[int, int], extent, quality) -> Image: ...
def effect_noise(size: tuple[int, int], sigma) -> Image: ...
def linear_gradient(mode) -> Image: ...
def radial_gradient(mode) -> Image: ...

class Exif(MutableMapping[int, Any]):
    def load(self, data: bytes) -> None: ...
    def tobytes(self, offset: int = ...) -> bytes: ...
    def get_ifd(self, tag: int): ...
    def __len__(self) -> int: ...
    def __getitem__(self, tag: int): ...
    def __contains__(self, tag: object) -> bool: ...
    def __setitem__(self, tag: int, value) -> None: ...
    def __delitem__(self, tag: int) -> None: ...
    def __iter__(self) -> Iterator[int]: ...
