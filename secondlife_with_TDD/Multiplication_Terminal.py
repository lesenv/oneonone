from collections import deque as collectionsdeque
from person import Person
import view as vw
import task as t

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
            self.people.rotate(1)
            active_person = self.people[0]
            if not active_person.lives:
                continue
            self.viewer.start(self.people)
            active_person.change_life(self.get_answer_3_times())
        else:
            self.break_()



def main():
    Game(t.Multiplizieren(), vw.Terminal())

if __name__ == "__main__":
    main()