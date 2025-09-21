from typing import (
    AbstractSet,
    Any,
    Literal,
    Sequence,
    Tuple,
    TypedDict,
    overload,
)

from packaging.version import Version
from pandas import DataFrame
from PIL.Image import Image

# ################################ TYPING ######################################

_PandasConfigDict = dict[str, Any]

# ###################### OUTPUT ############################

class _ImageToStringDict(TypedDict):
    text: str

_FileToDict = dict[str, Any]

class _OSDToDict(TypedDict):
    page_num: int
    orientation: int
    rotate: int
    orientation_conf: float
    script: str
    script_conf: float

# ################################ GLOBALS #####################################

tesseract_cmd: str

SUPPORTED_FORMATS: AbstractSet[str]

class Output:
    BYTES: Literal["bytes"]
    DATAFRAME: Literal["dataframe"]
    DICT: Literal["dict"]
    STRING: Literal["string"]

# ################################ EXCEPTIONS ##################################

class PandasNotSupported(EnvironmentError):
    def __init__(self) -> None: ...

class TesseractError(RuntimeError):
    status: int
    message: str
    args: Tuple[int, str]
    def __init__(self, status: int, message: str) -> None: ...

class TesseractNotFoundError(EnvironmentError):
    def __init__(self) -> None: ...

class TSVNotSupported(EnvironmentError):
    def __init__(self) -> None: ...

class ALTONotSupported(EnvironmentError):
    def __init__(self) -> None: ...

# ################################ FUNCTIONS ###################################

# ############ get_languages ###############################

def get_languages(
    config: str = "",
) -> Sequence[str]: ...

# ############ get_tesseract_version #######################

def get_tesseract_version(
    #
) -> Version: ...

# ############ run_and_get_multiple_output #################

@overload
def run_and_get_multiple_output(
    image: Image,
    extensions: list[str],
    *,
    lang: str | None = None,
    nice: int = 0,
    timeout: int = 0,
    return_bytes: Literal[False] = False,
) -> Sequence[str]: ...
@overload
def run_and_get_multiple_output(
    image: Image,
    extensions: list[str],
    *,
    lang: str | None = None,
    nice: int = 0,
    timeout: int = 0,
    return_bytes: Literal[True],
) -> Sequence[bytes]: ...
@overload
def run_and_get_multiple_output(
    image: Image,
    extensions: list[str],
    *,
    lang: str | None = None,
    nice: int = 0,
    timeout: int = 0,
    return_bytes: bool = False,
) -> Sequence[str] | Sequence[bytes]: ...

# ############ run_and_get_output ##########################

@overload
def run_and_get_output(
    image: Image,
    *,
    extension: str = "",
    lang: str | None = None,
    config: str = "",
    nice: int = 0,
    timeout: int = 0,
    return_bytes: Literal[False] = False,
) -> str: ...
@overload
def run_and_get_output(
    image: Image,
    *,
    extension: str = "",
    lang: str | None = None,
    config: str = "",
    nice: int = 0,
    timeout: int = 0,
    return_bytes: Literal[True],
) -> bytes: ...
@overload
def run_and_get_output(
    image: Image,
    *,
    extension: str = "",
    lang: str | None = None,
    config: str = "",
    nice: int = 0,
    timeout: int = 0,
    return_bytes: bool = False,
) -> str | bytes: ...

# ############ image_to_string #############################

@overload
def image_to_string(
    image: Image,
    *,
    lang: str | None = None,
    config: str = "",
    nice: int = 0,
    output_type: Literal["bytes"],
    timeout: int = 0,
) -> bytes: ...
@overload
def image_to_string(
    image: Image,
    *,
    lang: str | None = None,
    config: str = "",
    nice: int = 0,
    output_type: Literal["dict"],
    timeout: int = 0,
) -> _ImageToStringDict: ...
@overload
def image_to_string(
    image: Image,
    *,
    lang: str | None = None,
    config: str = "",
    nice: int = 0,
    output_type: Literal["string"] = "string",
    timeout: int = 0,
) -> str: ...
@overload
def image_to_string(
    image: Image,
    *,
    lang: str | None = None,
    config: str = "",
    nice: int = 0,
    output_type: str = "string",
    timeout: int = 0,
) -> Any: ...

# ############ image_to_pdf_or_hocr ########################

def image_to_pdf_or_hocr(
    image: Image,
    lang: str | None = None,
    config: str = "",
    nice: int = 0,
    extension: str = "pdf",
    timeout: int = 0,
) -> bytes: ...

# ############ image_to_alto_xml ###########################

def image_to_alto_xml(
    image: Image,
    lang: str | None = None,
    config: str = "",
    nice: int = 0,
    timeout: int = 0,
) -> bytes: ...

# ############ image_to_boxes ##############################

@overload
def image_to_boxes(
    image: Image,
    *,
    lang: str | None = None,
    config: str = "",
    nice: int = 0,
    output_type: Literal["bytes"],
    timeout: int = 0,
) -> bytes: ...
@overload
def image_to_boxes(
    image: Image,
    *,
    lang: str | None = None,
    config: str = "",
    nice: int = 0,
    output_type: Literal["dict"],
    timeout: int = 0,
) -> _FileToDict: ...
@overload
def image_to_boxes(
    image: Image,
    *,
    lang: str | None = None,
    config: str = "",
    nice: int = 0,
    output_type: Literal["string"] = "string",
    timeout: int = 0,
) -> str: ...
@overload
def image_to_boxes(
    image: Image,
    *,
    lang: str | None = None,
    config: str = "",
    nice: int = 0,
    output_type: str = "string",
    timeout: int = 0,
) -> Any: ...

# ############ image_to_data ###############################

@overload
def image_to_data(
    image: Image,
    *,
    lang: str | None = None,
    config: str = "",
    nice: int = 0,
    output_type: Literal["bytes"],
    timeout: int = 0,
) -> bytes: ...
@overload
def image_to_data(
    image: Image,
    *,
    lang: str | None = None,
    config: str = "",
    nice: int = 0,
    output_type: Literal["dataframe"],
    timeout: int = 0,
    pandas_config: _PandasConfigDict | None = None,
) -> DataFrame: ...
@overload
def image_to_data(
    image: Image,
    *,
    lang: str | None = None,
    config: str = "",
    nice: int = 0,
    output_type: Literal["dict"],
    timeout: int = 0,
) -> _FileToDict: ...
@overload
def image_to_data(
    image: Image,
    *,
    lang: str | None = None,
    config: str = "",
    nice: int = 0,
    output_type: Literal["string"] = "string",
    timeout: int = 0,
) -> str: ...
@overload
def image_to_data(
    image: Image,
    *,
    lang: str | None = None,
    config: str = "",
    nice: int = 0,
    output_type: str = "string",
    timeout: int = 0,
    pandas_config: _PandasConfigDict | None = None,
) -> Any: ...

# ############ image_to_osd ################################

@overload
def image_to_osd(
    image: Image,
    *,
    lang: str = "osd",
    config: str = "",
    nice: int = 0,
    output_type: Literal["bytes"],
    timeout: int = 0,
) -> bytes: ...
@overload
def image_to_osd(
    image: Image,
    *,
    lang: str = "osd",
    config: str = "",
    nice: int = 0,
    output_type: Literal["dict"],
    timeout: int = 0,
) -> _OSDToDict: ...
@overload
def image_to_osd(
    image: Image,
    *,
    lang: str = "osd",
    config: str = "",
    nice: int = 0,
    output_type: Literal["string"] = "string",
    timeout: int = 0,
) -> str: ...
@overload
def image_to_osd(
    image: Image,
    *,
    lang: str = "osd",
    config: str = "",
    nice: int = 0,
    output_type: str = "string",
    timeout: int = 0,
) -> Any: ...
