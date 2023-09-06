

class Item:
    def __init__(self, message, function1=None, function2=None, function3=None):
        self._function3 = function3
        self._function2 = function2
        self._function1 = function1
        self.message = message

    def read_message(self):
        return self.message
