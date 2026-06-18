import random
from collections import deque as collectionsdeque
import view as vw #import Terminal, MENU_CODES, EXIT, NEW_PLAYER
from typing import Protocol
from abc import abstractmethod

def get_2_ints(_from: int = 1, _to: int = 10) -> list[int]:
    if _from > _to: _from, _to = _to, _from
    return [random.randint(_from, _to), random.randint(_from, _to)]

class Person():
    joined = 0

    def __init__(self, name):
        self.lives = 5
        self.name = name
        self.joined = Person.joined
        Person.joined += 1


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

        self.menu_codes = {vw.EXIT: self.break_,
                           vw.NEW_PLAYER: self.add_Person,
                           vw.HELP: self.viewer.print_help}

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
            if ans in vw.MENU_CODES:
                self.viewer.new_menu()
                self.menu_codes[ans]()
                return False
            elif ans == self.tasker.get_result():
                return True
        return False

    def start_game(self):
        while any(f.lives for f in self.people):
            self.people.rotate()
            active_person = self.people[0]
            if not active_person.lives:
                continue
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
        else:
            self.break_()



def main():
    game = Game(Multiplizieren(), vw.Terminal())

if __name__ == "__main__":
    main()