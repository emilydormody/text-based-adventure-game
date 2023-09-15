from item import Item

class Portrait(Item):
    def __init__(self, name):
        super().__init__(name)
        self.fallen = False

    def check_fallen(self):
        return self.fallen
    
    def fall_down(self):
        self.fallen = True