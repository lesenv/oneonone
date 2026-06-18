import random
from typing import Protocol
#from dataclasses import dataclass
from abc import abstractmethod
import subprocess, os # just for Terminal
from collections import deque as collectionsdeque

EXIT = "EXIT"
NEW_PLAYER = "NEW_PLAYER"

MENU_CODES = [EXIT,
              NEW_PLAYER]

def get_2_ints(_from: int = 1, _to: int = 10) -> list[int]:
    if _from > _to: _from, _to = _to, _from
    return [random.randint(_from, _to), random.randint(_from, _to)]

class Viewer(Protocol):
    @abstractmethod
    def output(self) -> None: ...
    @abstractmethod
    def get_input(self, str) -> int:...
    @abstractmethod
    def get_new_name(self, str) -> str:...

class Terminal(Viewer):
    def start(self, people: list[Person]) -> None:
        maxtabs = (max( length for length in [len(p.name) for p in people] ))
        tabnum_from_names = {p.name: maxtabs - len(p.name) for p in people}
        self.output(self.header())
        active = people[0]
        sorted_people= sorted(people, key= lambda n: n.name)
        for p in sorted_people:
            prefix = ">> " if p == active else "   "
            grid = f"{(tabnum_from_names[p.name])*' '}"
            self.output([prefix + f" {p.name}: {grid}{"O"*p.lives}"])
        self.output()

    def output(self, txt_list: list[str] = None) -> None:
        # only method to print
        # all the others are returning the strings
        if type(txt_list) == list:
            for txt in txt_list:
                print(f"{txt}")
        else:
            print()

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
            return self.controller(str(e))
    
    def controller(self, e: str):
        match e[-4:-1]:
            case "hhh":
                self.output(self.output_help_menu())
            case "ppp":
                return NEW_PLAYER
            case "zzz":
                return EXIT
    
    def get_new_name(self, txt: str = "Wie heißt Du? ") -> str:
        self.clear_display()
        return input(txt)

    def get_task(self, task: list = []) -> str:
        return("{} {} {} = ".format(*task))
    
    def closing(self):
        self.clear_display()
        self.output(["", "Schön war's", "Bis zum nächsten Mal!"])

class Person():
    def __init__(self, name):
        self.lives = 5
        self.name = name

    def change_life(self, change: bool = False):
        if change:
            self.lives += 1
        else:
            self.lives -= 1

class Task(Protocol):
    symbol: str

    def make_task(self, _from: int = 1, _to: int = 10):
        self.a, self.b = get_2_ints(_from, _to)
        return [self.a, self.symbol, self.b]
    
    @abstractmethod
    def get_result(self) -> int:
        ...

class Multiplizieren(Task):
    def __init__(self):
        self.symbol = "x"
    
    def get_result(self):
        return self.a*self.b

class Game():
    def __init__(self, tasker, viewer):
        self.tasker = tasker
        self.viewer = viewer

        self.people = collectionsdeque()
        self.add_Person()

        self.menu_codes = {EXIT: self.break_,
                           NEW_PLAYER: self.add_Person}

        self.start_game()

    def break_(self):
        self.people = []
        self.viewer.closing()

    def add_Person(self):
        self.people.append(Person(self.viewer.get_new_name()))
        print(f"\n...\n...\n...self.people: {[p.name for p in self.people]}")

    def get_answer_3_times(self):
        new_mult_task = self.tasker.make_task()
        for _ in range(3):
            ans = self.viewer.get_input(self.viewer.get_task(new_mult_task))
            if ans in MENU_CODES:
                self.viewer.clear_display()
                l = {v[0]: i for i, v in enumerate(self.menu_codes.items())}
                self.menu_codes[ans]()
                return False
            elif ans == self.tasker.get_result():
                return True
        return False

    def start_game(self):
        while self.people:
            self.people.rotate()
            active_person = self.people[0]
            self.viewer.start(self.people)
            ''' DEBUG
            print("INTERMISSION")
            ap_name = str(active_person.name)
            sp = f"{', '.join(person.name for person in self.people)}"
            print(f"self.people {sp}")
            # in ppp den viewer aktualisieren
            print(f"active_person: {ap_name}")
            '''
            active_person.change_life(self.get_answer_3_times())
            if not active_person.lives:
                self.people.remove(active_person)


def main():
    game = Game(Multiplizieren(), Terminal())

if __name__ == "__main__":
    main()