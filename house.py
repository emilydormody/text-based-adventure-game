from room import Room
from item import Item
from door import Door

class House:
    def __init__(self):
        self.mirror = None
        self.candle = None
        self.book1 = None
        self.book2 = None
        self.chandelier = None
        self.vent = None
        self.balcony = None
        self.portrait1 = None
        self.portrait2 = None
        self.top_R = Room("top_R")
        self.ghost_room = Room("ghost_room")
        self.bottom_R = Room("bottom_R")
        self.gallery = Room("gallery")
        self.middle = Room("middle")
        self.library = Room("library")
        self.top_L = Room("top_L")
        self.candle_room = Room("candle_room")
        self.bottom_L = Room("bottom_L")
        self.porch = Room("porch")
        self.main_door = Door()
        self.build_house()


    def build_house(self):
        self.porch.set_position(self.bottom_L, self.bottom_R, None, self.mirror)
        self.bottom_L.set_position(self.candle_room, self.porch, self.top_L, None)
        self.candle_room.set_position(None, None, self.candle, self.bottom_L)
        self.top_L.set_position(None, self.middle, self.library, self.bottom_L)
        self.library.set_position(self.book1, self.book2, None, self.top_L)
        self.middle.set_position(self.top_L, self.top_R, self.chandelier,None)
        self.top_R.set_position(self.middle, self.vent, self.ghost_room, self.bottom_R)
        self.ghost_room.set_position(None, None, self.balcony, self.top_R)
        self.bottom_R.set_position(self.porch, self.gallery, self.top_R, None)
        self.gallery.set_position(self.portrait1, self.portrait2, None, self.bottom_R)
        self.mirror = Item("mirror")
        self.candle = Item("candle")
        self.book1 = Item("book 1")
        self.book2 = Item("book2")
        self.chandelier = Item("chandelier")
        self.vent = Item("vent")
        self.balcony = Item("balcony")
        self.portrait1 = Item("portrait1")
        self.portrait2 = Item("portrait2")

# left, right, forward, back, entrance, object1, object2=None