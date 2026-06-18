import random
from collections import deque as collectionsdeque
from view import Terminal, MENU_CODES, EXIT, NEW_PLAYER
from typing import Protocol
from abc import abstractmethod

def get_2_ints(_from: int = 1, _to: int = 10) -> list[int]:
    if _from > _to: _from, _to = _to, _from
    return [random.randint(_from, _to), random.randint(_from, _to)]

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

    def controller(self, e: str):
        match e[-4:-1]:
            case "hhh":
                self.output(self.output_help_menu())
            case "ppp":
                return NEW_PLAYER
            case "zzz":
                return EXIT
    
    def get_answer_3_times(self):
        new_mult_task = self.tasker.make_task()
        for _ in range(3):
            ans = self.viewer.get_input(self.viewer.get_task(new_mult_task))
            print(ans)
            if ans in MENU_CODES:
                self.viewer.clear_display()
                self.controller(ans)
                print(self.controller(ans))
                print(self.menu_codes[ans])
                '''          DEBUG
                l = {v[0]: i for i, v in enumerate(self.menu_codes.items())}
                '''
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