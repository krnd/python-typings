from typing import Annotated, Any, Iterable, Literal, Mapping, overload

from _typeshed import SupportsWrite

# ################################ TYPING ######################################

AttributesType = Literal[
    "bold",
    "dark",
    "underline",
    "blink",
    "reverse",
    "concealed",
    "strike",
]
HighlightsType = Literal[
    "on_black",
    "on_grey",
    "on_red",
    "on_green",
    "on_yellow",
    "on_blue",
    "on_magenta",
    "on_cyan",
    "on_light_grey",
    "on_dark_grey",
    "on_light_red",
    "on_light_green",
    "on_light_yellow",
    "on_light_blue",
    "on_light_magenta",
    "on_light_cyan",
    "on_white",
]
ColorsType = Literal[
    "black",
    "grey",
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
    "light_grey",
    "dark_grey",
    "light_red",
    "light_green",
    "light_yellow",
    "light_blue",
    "light_magenta",
    "light_cyan",
    "white",
]

RGBColorTuple = tuple[
    Annotated[int, "red", (0, 255)],
    Annotated[int, "green", (0, 255)],
    Annotated[int, "blue", (0, 255)],
]

# ################################ GLOBALS #####################################

ATTRIBUTES: Mapping[AttributesType, int]
HIGHLIGHTS: Mapping[HighlightsType, int]
COLORS: Mapping[ColorsType, int]

RESET: str

# ################################ FUNCTIONS ###################################

# ############ colored #####################################

@overload
def colored(
    text: Any,
    color: ColorsType | RGBColorTuple | None = None,
    on_color: HighlightsType | RGBColorTuple | None = None,
    attrs: Iterable[AttributesType] | None = None,
    *,
    no_color: bool | None = None,
    force_color: bool | None = None,
) -> str: ...
@overload
def colored(
    text: Any,
    color: str | tuple[int, int, int] | None = None,
    on_color: str | tuple[int, int, int] | None = None,
    attrs: Iterable[str] | None = None,
    *,
    no_color: bool | None = None,
    force_color: bool | None = None,
) -> str: ...

# ############ cprint ######################################

@overload
def cprint(
    text: Any,
    color: ColorsType | RGBColorTuple | None = None,
    on_color: HighlightsType | RGBColorTuple | None = None,
    attrs: Iterable[AttributesType] | None = None,
    *,
    no_color: bool | None = None,
    force_color: bool | None = None,
    # ### builtins.print
    sep: str | None = " ",
    end: str | None = "\n",
    file: SupportsWrite[str] | None = None,
    flush: Literal[False] = False,
) -> None: ...
@overload
def cprint(
    text: Any,
    color: str | tuple[int, int, int] | None = None,
    on_color: str | tuple[int, int, int] | None = None,
    attrs: Iterable[str] | None = None,
    *,
    no_color: bool | None = None,
    force_color: bool | None = None,
    # ### builtins.print
    sep: str | None = " ",
    end: str | None = "\n",
    file: SupportsWrite[str] | None = None,
    flush: Literal[False] = False,
) -> None: ...
