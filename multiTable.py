# 1x1 program
import subprocess, os
import random
from typing import Protocol
from abc import abstractmethod

# mit 5 Leben starten
class Person:
    def __init__(self, name):
        self.lives = 5
        self.set_name(name)

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
    def get_lives(self):
        return self.lives
    
    def add_life(self):
        self.lives += 1

    def rem_life(self):
        self.lives -= 1

# seperating terminal and browser and so forth
class OnScreen(Protocol):
    @abstractmethod
    def write_on(self, msg: str) -> None: ...
    @abstractmethod
    def get_input(self, msg: str = "") -> str: ...

class OnTerminal(OnScreen):
    def write_on(self, msg: str):
        print(msg)

    def get_input(self,msg: str = "") -> str:
        return input(msg)

# abstracting different mathematical problems
class Math(Protocol):
    def new_task() -> None:
        # stores in self.: givens, solution
        ...
    def get_question() -> str:
        # return problemquestion as text
        ...
    def is_correct(self, guess: int):
        #return bool wether the answer was correct
        ...

class Mulitplier(Math):
    def new_task(self, i : int = 1, j : int = 10):
        self.a = random.randint(i, j)
        self.b = random.randint(i, j)
        self.solution = self.a*self.b
        return
    
    def get_question(self):
        return(f"{self.a} * {self.b} = ")
    
    def is_correct(self, guess: int):
        return guess == self.solution

class Division(Math):
    pass


# asking 3 times if the answer was wrong
# richtige Antwort: +1 Leben
# falsche Antwort: -1 Leben gewonnen
# bei 0 Leben verloren, bei 10 
class Game:
    def __init__(self, math, writer):
        self.math = math
        self.writer = writer

        self.people = []
        self.addPerson()

        self.play = True
        while self.play:
            self.loop_start()

    def addPerson(self):
        name =  self.writer.get_input("Wie heißt Du?")
        new_person = Person(name)
        self.people.append(new_person)

    def print_header(self):
        subprocess.call('cls' if os.name == 'nt' else 'clear')
        self.writer.write_on(f"\n1x1-Übungen    -  Schluss mit 'zzz', 'ppp' ist neuer Spieler")
        for p in self.people:
            line = "".join([">" if p is self.active_player else " ", p.get_name(), "\t", "O"*p.get_lives()])
            self.writer.write_on(line)
        self.writer.write_on(f"================")
        return
    
    def loop_start(self):
        for p in self.people:
            self.active_player = p
            self.print_header()
            self.math.new_task()
            for i in range(3):
                try:
                    q = int(self.writer.get_input(self.math.get_question()))
                except ValueError as e:
                    if e == "zzz": self.play = False
                    elif e == "ppp": self.addPerson()
                    else: raise
                # if right answer, get a life
                if self.math.is_correct(q):
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
    writer = OnTerminal()
    g = Game(mult, writer)
