from room import Room
from item import Item
from pageholder import PageHolder
from door import Door
from vent import Vent
from portrait import Portrait

class House:
    def __init__(self):
        self.mirror = Item("mirror")
        self.candle = Item("candle")
        self.book1 = PageHolder("book 1")
        self.book2 = Item("book2")
        self.chandelier = PageHolder("chandelier")
        self.vent = Vent("vent")
        self.balcony = PageHolder("balcony")
        self.portrait1 = PageHolder("portrait1")
        self.portrait2 = Portrait("portrait2")
        self.outside = Room("outside")
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
        self.middle.set_position(self.top_L, self.top_R, None, self.chandelier)
        self.top_R.set_position(self.middle, self.vent, self.ghost_room, self.bottom_R)
        self.ghost_room.set_position(None, None, self.balcony, self.top_R)
        self.bottom_R.set_position(self.porch, self.gallery, self.top_R, None)
        self.gallery.set_position(self.portrait1, self.portrait2, None, self.bottom_R)
        self.outside.set_position(None, None, self.porch, None)
        self.lock_all_doors()

    def check_candlelight(self):
        if self.library.check_open():
            return "green"
        elif self.ghost_room.check_open():
            return "blue"
        elif self.gallery.check_open():
            return "purple"
        else:
            return "white"

    def lock_all_doors(self):
        self.library.lock_door()
        self.gallery.lock_door()
        self.ghost_room.lock_door()

    def check_vent(self):
        return self.vent.has_key()

# left, right, forward, back, entrance, object1, object2=None