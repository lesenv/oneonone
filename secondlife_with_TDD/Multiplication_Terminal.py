from collections import deque as collectionsdeque
from person import Person
import view_terminal as vw
import task as t

WIN_CONDITIION = 10

class Game():
    def __init__(self, tasker, viewer, cond_win = WIN_CONDITIION):
        self.tasker = tasker
        self.viewer = viewer
        self.cond_win = cond_win

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
            self.viewer.closing([f"\033[92m Wow, {p.name} hat gewonnen! \033[0m"])
        else:
            self.people.clear()
            self.viewer.closing()

    def add_Person(self):
        self.people.append(Person(self.viewer.get_new_name()))
    
    def get_answer_3_times(self):
        new_mult_task = self.tasker.make_task()
        for _ in range(3):
            ans = self.viewer.get_input(self.viewer.get_task(new_mult_task))
            if ans in vw.MENU_CODES:
                self.viewer.new_menu()
                self.menu_codes[ans]()
                if ans == vw.HELP:
                    input()
                return False
            elif ans == self.tasker.get_result():
                return True
        return False

    def start_game(self):
        while any(f.lives for f in self.people) and \
              all(f.lives < self.cond_win for f in self.people):
            self.people.rotate(1)
            active_person = self.people[0]
            if not active_person.lives:
                continue
            sorted_names = [str(p.name) for p in sorted(self.people, key= lambda n: n.joined)]
            dict_lives_from_name = {p.name: p.lives for p in self.people}
            self.viewer.out_names(sorted_names,
                                  dict_lives_from_name,
                                  active_person.name)
            active_person.change_life(self.get_answer_3_times())
        else:
            self.break_(p = self.people[0] if active_person.lives == self.cond_win else [])

def main():
    Game(t.Multiplizieren(), vw.Terminal())

if __name__ == "__main__":
    main()