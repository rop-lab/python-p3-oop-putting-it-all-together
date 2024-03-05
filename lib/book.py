class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = None  # Private variable for page_count
        self.page_count = page_count  # Using the setter method to set the initial page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


# Example usage:
book1 = Book("And Then There Were None", 272)
print(book1.title)         # Output: And Then There Were None
print(book1.page_count)    # Output: 272
