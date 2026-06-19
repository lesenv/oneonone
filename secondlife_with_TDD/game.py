from collections import deque as collectionsdeque
from person import Person
import view_terminal as vw
import task as t

WIN_CONDITION = 10

class Game():
    def __init__(self, tasker, viewer, cond_win = WIN_CONDITION):
        self.tasker = tasker
        self.viewer = viewer
        self.cond_win = cond_win

        self.title="1x1-Übungen -..-''-..-''# help: type 'hhh'"

        self.people = collectionsdeque()
        self.add_Person()

        self.menu_codes = {vw.EXIT: self.break_,
                           vw.NEW_PLAYER: self.add_Person,
                           vw.HELP: self.print_help}

        self.start_game()

    def print_help(self):
        self.viewer.output(self.output_help_menu)

    def output_help_menu(self) -> str:
        out = ["hhh - print this menu",
               "ppp - add a player",
               "zzz - exit the game"]
        input(out)
        return out

    def break_(self, p: Person= None) -> None:
        if p:
            # p won
            self.viewer.closing([f"\033[92m    Wow, {p.name} hat gewonnen! \033[0m"])
        else:
            # break manually
            self.people.clear()
            self.viewer.closing(["", "Schön war's", "Bis zum nächsten Mal!"])

    def add_Person(self):
        self.people.append(Person(self.viewer.get_new_name()))
    
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

    def out_names(self, active) -> None:
        outlist = []
        maxtabs = (max( length for length in [len(p.name) for p in self.people] ))
        for p in sorted(self.people, key = lambda d: d.joined):
            prefix = ">>>> " if p == active else "     "
            grid = f"{(maxtabs - len(p.name))*' '}"
            line = prefix + f"{p.name}: {grid}{"O"*p.lives}"
            if not p.lives:
                line = '\033[91m' + line + '\033[0m' # line in red
            outlist.append(line)
        return outlist

    def start_game(self):
        while any(f.lives for f in self.people) and \
              all(f.lives < self.cond_win for f in self.people):
            self.viewer.output(self.viewer.header(self.title))
            self.people.rotate(1)
            active_person = self.people[0]
            if not active_person.lives:
                continue
            self.viewer.output(self.out_names(active_person))
            active_person.change_life(self.get_answer_3_times())
        else:
            self.break_(p = self.people[0] if active_person.lives == self.cond_win else [])