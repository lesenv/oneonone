import subprocess, os # just for Terminal
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
    def output(self) -> None: ...

    @abstractmethod
    def get_input(self, str) -> int:...

    @abstractmethod
    def get_new_name(self, str) -> str:...

    @abstractmethod
    def new_menu() -> None: ...

    @abstractmethod
    def print_help() -> None: ...

class Terminal(Viewer):
    def start(self, people: list[Person]) -> None:
        maxtabs = (max( length for length in [len(p.name) for p in people] ))
        tabnum_from_names = {p.name: maxtabs - len(p.name) for p in people}
        self.output(self.header())
        active = people[0]
        sorted_people= sorted(people, key= lambda n: n.joined)
        for p in sorted_people:
            prefix = ">> " if p == active else "   "
            grid = f"{(tabnum_from_names[p.name])*' '}"
            line = prefix + f"{p.joined} {p.name}: {grid}{"O"*p.lives}"
            if not p.lives:
                line = '\033[91m'+line+'\033[0m'
            self.output([line])
        self.output()

    def print_help(self):
        self.output(self.output_help_menu())

    def output(self, txt_list: list[str] = None) -> None:
        # only method to print
        # all the others are returning the strings
        if type(txt_list) == list:
            for txt in txt_list:
                print(f"{txt}")
        else:
            print()

    def new_menu(self):
        self.clear_display()

    def clear_display(self):
        subprocess.call('cls' if os.name == 'nt' else 'clear')
    
    def header(self) -> str:
        self.clear_display()
        txt = ["1x1-Übungen -..-''-..-''# help: type 'hhh'"]
        txt.append("")
        txt.append(self.seperate_line())
        return txt
    
    def seperate_line(self) -> str:
        return "================"
    
    def output_help_menu(self) -> str:
        out = ["hhh - print this menu",
               "ppp - add a player",
               "zzz - exit the game"]
        return out

    def get_input(self, txt: str) -> int:
        try:
            return int(input(txt))
        except ValueError as e:
            return str(e)[-4:-1]
    
    def get_new_name(self, txt: str = "Wie heißt Du? ") -> str:
        self.clear_display()
        return input(txt)

    def get_task(self, task: list = []) -> str:
        return("{} {} {} = ".format(*task))
    
    def closing(self):
        self.clear_display()
        self.output(["", "Schön war's", "Bis zum nächsten Mal!"])