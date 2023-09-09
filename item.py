from message import MessageHandler


class Item:
    def __init__(self, name, function1=None, function2=None, function3=None):
        self.message = MessageHandler().set_message(name)
        self.name = name
        self.page_found = False

    def read_message(self):
        return self.message

    def get_name(self):
        return self.name

    def has_page(self):
        return self.page_found

    def take_page(self):
        self.page_found = True