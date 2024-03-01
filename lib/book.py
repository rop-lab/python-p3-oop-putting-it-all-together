class Book:
    def __init__(self, title, page_count):
        self._title = title
        self._page_count = None  # Initialize page_count as None initially
        self.page_count = page_count  # Use the property setter

    @property
    def title(self):
        return self._title

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

# Example usage:
book = Book("And Then There Were None", 272)
book.page_count = "not an integer"  # This will print "page_count must be an integer"
book.turn_page()  # This will print "Flipping the page...wow, you read fast!"
