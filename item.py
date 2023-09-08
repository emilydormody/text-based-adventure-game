

class Item:
    def __init__(self, message, function1=None, function2=None, function3=None):
        self.message = message

    def read_message(self):
        return self.message
