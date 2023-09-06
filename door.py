

class Door:
    def __init__(self):
        self._unlocked = False

    def unlock(self):
        self._unlocked = True

    def is_unlocked(self):
        return self._unlocked