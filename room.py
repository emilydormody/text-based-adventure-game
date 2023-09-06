from door import Door

class Room:
    def __init__(self, name, left, right, forward, back, object1=None, object2=None):
        self._name = name
        self._left = left
        self._right = right
        self._forward = forward
        self._back = back
        self._object1 = object1
        self._object2 = object2
        self._entrance = Door()
        self.enter_message = self._name

    def go_left(self):
        if self._left is not None:
            return self._left

    def go_right(self):
        if self._right is not None:
            return self._right

    def go_forward(self):
        if self._forward is not None:
            return self._forward

    def go_back(self):
        if self._back is not None:
            return self._back

    def check_open(self):
        return self._entrance.is_unlocked()

    def set_message(self, message):
        self.enter_message = message

    def read_message(self):
        return self.enter_message


