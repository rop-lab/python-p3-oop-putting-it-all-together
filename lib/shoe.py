class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None  # Private variable for size
        self.size = size  # Using the setter method to set the initial size
        self.condition = "Used"  # Default condition is Used

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"  # Set the condition to New after repair
