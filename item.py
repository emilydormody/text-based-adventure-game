from message import MessageHandler


class Item:
    def __init__(self, name, function1=None, function2=None, function3=None):
        self.message = MessageHandler().set_message(name)
        self.name = name

    def read_message(self):
        return self.message

    def get_name(self):
        return self.name