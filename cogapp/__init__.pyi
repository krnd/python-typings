from typing import NoReturn

class CogGenerator:
    inFile: str
    outFile: str
    firstLineNum: int
    previous: str
    def out(
        self,
        sOut: str = "",
        dedent: bool = False,
        trimblanklines: bool = False,
    ) -> None: ...
    def outl(
        self,
        sOut: str = "",
        dedent: bool = False,
        trimblanklines: bool = False,
    ) -> None: ...
    def msg(self, s: str) -> None: ...
    def error(self, msg: str = ...) -> NoReturn: ...
