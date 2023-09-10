from item import Item
from random import randint


class Vent(Item):
    def __init__(self, name):
        super().__init__(name)
        self.bats_out = False
        self.key = True

    def bats(self):
        if self.bats_out and self.key:
            return False
        else:
            if randint(0,2) == 0:
                if not self.bats_out:
                    self.bats_out = True
                return True
            return False

    def has_key(self):
        return self.key

    def take_key(self):
        self.key = False
