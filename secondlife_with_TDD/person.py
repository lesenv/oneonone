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
