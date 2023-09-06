from room import Room

class House:
    def __init__(self):
        self.outside = None
        self.top_R = None
        self.ghost_room = None
        self.bottom_R = None
        self.gallery = None
        self.middle = None
        self.library = None
        self.top_L = None
        self.candle_room = None
        self.bottom_L = None
        self.porch = None


    def build_house(self):
        self.porch = Room("porch",self.bottom_L, self.bottom_R, self.outside, self.mirror)
        self.bottom_L = Room("bottom_L",self.candle_room, self.porch, self.top_L, None)
        self.candle_room = Room("candle_room",None, None, self.candle, self.bottom_L)
        self.top_L = Room("top_L",None, self.middle, self.library, self.bottom_L)
        self.library = Room("library",self.book1, self.book2, None, self.top_L)
        self.middle = Room("middle",self.top_L, self.top_R, self.chandelier,None)
        self.top_R = Room("top_R",self.middle, self.vent, self.ghost_room, self.bottom_R)
        self.ghost_room = Room("ghost_room",None, None, self.balcony, self.top_R)
        self.bottom_R = Room("bottom_R",self.porch, self.gallery, self.top_R, None)
        self.gallery = Room("gallery",self.portrait1, self.portrait2, None, self.bottom_R)
        self.outside = Room("outside",None, None, self.porch, None)

# left, right, forward, back, entrance, object1, object2=None