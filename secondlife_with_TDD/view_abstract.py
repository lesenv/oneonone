from typing import Protocol
from abc import abstractmethod

EXIT       = "zzz"
NEW_PLAYER = "ppp"
HELP       = "hhh"

MENU_CODES = [EXIT,
              NEW_PLAYER,
              HELP]



class Viewer(Protocol):
    @abstractmethod
    def read_input_number(self) -> None: ...

    @abstractmethod
    def get_input(self, str) -> int:...

    @abstractmethod
    def get_new_name(self, str) -> str:...

    @abstractmethod
    def new_menu() -> None: ...

    @abstractmethod
    def closing(self, lst: list[str]) -> None: ...
    