class Person:
    joined = 0

    def __init__(self, name):
        self.name = name
        self.lives = 5

        self.joined = Person.joined
        Person.joined += 1

    def change_life(self, plus: bool = True):
        self.lives += 1 if plus else -1