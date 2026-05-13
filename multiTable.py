# 1x1 program
import subprocess, os
import random

# mit 5 Leben starten
class Person:
    def __init__(self):
        self.lives = 5
        self.set_name()

    def set_name(self):
        self.name = input("Wie heißt Du?")

    def get_name(self):
        return self.name
    
    def get_lives(self):
        return self.lives
    
    def add_life(self):
        self.lives += 1

    def rem_life(self):
        self.lives -= 1
        
        
# show multiply-task
def show_task():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    print(f"{a} x {b} = ?")
    return a * b

# asking 3 times if the answer was wrong
# richtige Antwort: +1 Leben
# falsche Antwort: -1 Leben gewonnen
# bei 0 Leben verloren, bei 10 
class Game:
    def __init__(self):
        self.people = []
        self.addPerson()

        self.play = True

        while self.play:
            self.loop_start()

    def addPerson(self):
        new_person = Person()
        self.people.append(new_person)

    def new_task(self):
        a = random.randint(1,10)
        b = random.randint(1,10)
        return [a, b]

    def print_header(self):
        subprocess.call('cls' if os.name == 'nt' else 'clear')
        print(f"\n1x1-Übungen    -  Schluss mit 'zzz', 'ppp' ist neuer Spieler")
        for p in self.people:
            print(">" if p is self.active_player else " ", p.get_name(), "\t", "O"*p.get_lives())
        print(f"================")
        return
    
    def print_task(self, args):
        a, b = args
        c = input(f"{a} * {b} = ")
        try:
            d = int(c)
        except ValueError:
            if c == "zzz": self.play = False
            elif c == "ppp": self.addPerson()
            return False
        return d == a*b
    
    def loop_start(self):
        for p in self.people:
            self.active_player = p
            self.print_header()
            new = self.new_task()
            for i in range(3):
                q = self.print_task(new)
                if q or not self.play:
                    p.add_life()
                    break
                if i==2 and not q:
                    p.rem_life()
            


if __name__ == "__main__":
    g = Game()
