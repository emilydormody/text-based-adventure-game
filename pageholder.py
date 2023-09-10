from item import Item


class PageHolder(Item):
    def __init__(self, name):
        super().__init__(name)
        self.page_found = False

    def has_page(self):
        return self.page_found

    def take_page(self):
        self.page_found = True
