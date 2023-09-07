from door import Door

class Room:
    def __init__(self, name):
        self._name = name
        self._left = None
        self._right = None
        self._forward = None
        self._back = None
        #self._object1 = object1
        #self._object2 = object2
        self._entrance = Door()
        self.enter_message = self._name

    def go_left(self):
        if self._left is not None:
            return self._left

    def get_left(self):
        return self._left

    def go_right(self):
        if self._right is not None:
            return self._right

    def get_right(self):
        return self._right

    def go_forward(self):
        if self._forward is not None:
            return self._forward

    def get_forward(self):
        return self._forward

    def go_back(self):
        if self._back is not None:
            return self._back

    def get_back(self):
        return self._back

    def check_open(self):
        return self._entrance.is_unlocked()

    def set_message(self, message):
        self.enter_message = message

    def read_message(self):
        return self.enter_message

    def set_position(self,left, right, forward, back):
        self._left = left
        self._right = right
        self._forward = forward
        self._back = back
