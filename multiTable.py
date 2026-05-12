# 1x1 program
import random

# mit 5 Leben starten
class Person:
    def __init__(self):
        self.lives = 5

    def set_name(self):
        self.name = input("Wie heißt Du?")
        
        
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
        # people = [], addPerson()
        person1 = Person()
        person1.set_name()

        self.play = True

        while self.play:
            self.loop_start()

    def new_task(self):
        a = random.randint(1,10)
        b = random.randint(1,10)
        return [a, b]

    def print_header(self):
        print("\n1x1-Übungen    -  Schluss mit 'zzz'")
        print("===========")
        return
    
    def print_task(self, args):
        a, b = args
        c = input(f"{a} * {b} = ")
        try:
            d = int(c)
        except ValueError:
            if c == "zzz": self.play = False
            return False
        return d == a*b
    
    def loop_start(self):
        self.print_header()
        new = self.new_task()
        for _ in range(3):
            q = self.print_task(new)
            if q or not self.play:
                break


if __name__ == "__main__":
    g = Game()
