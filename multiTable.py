# 1x1 program
import subprocess, os
import random
from abc import ABC

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
        
class Math(ABC):
    def new_task():
        # return new list [given, solution]
        ...
    def get_answer():
        #return bool wether the answer was correct
        ...

class Mulitplier(Math):
    def new_task(self, i : int = 1, j : int = 10):
        a = random.randint(i, j)
        b = random.randint(i, j)
        return [[a, b], a*b]
    
    def get_answer(self, args):
        [a, b], c = args
        d = input(f"{a} * {b} = ")
        try:
            e = int(d)
        except ValueError:
            raise
        return e == c


# asking 3 times if the answer was wrong
# richtige Antwort: +1 Leben
# falsche Antwort: -1 Leben gewonnen
# bei 0 Leben verloren, bei 10 
class Game:
    def __init__(self, math):
        self.people = []
        self.addPerson()

        self.play = True
        self.math = math

        while self.play:
            self.loop_start()

    def addPerson(self):
        new_person = Person()
        self.people.append(new_person)

    def print_header(self):
        subprocess.call('cls' if os.name == 'nt' else 'clear')
        print(f"\n1x1-Übungen    -  Schluss mit 'zzz', 'ppp' ist neuer Spieler")
        for p in self.people:
            print(">" if p is self.active_player else " ", p.get_name(), "\t", "O"*p.get_lives())
        print(f"================")
        return
    
    def loop_start(self):
        for p in self.people:
            self.active_player = p
            self.print_header()
            new = self.math.new_task()
            for i in range(3):
                try:
                    q = self.math.get_answer(new)
                except ValueError as e:
                    if e == "zzz": self.play = False
                    elif e == "ppp": self.addPerson()
                    else: raise
                # if right answer, get a life
                if q:
                    p.add_life()
                    break
                # if after three false guesses removing a life
                elif i==2:
                    p.rem_life()
                # if stopped to play (during game), remove the player
                if not self.play:
                    self.people.remove(p)
                    # as long as there is at least one person left, continue to play
                    if self.people:
                        self.play = True
                    break
            


if __name__ == "__main__":
    mult = Mulitplier()
    g = Game(mult)
