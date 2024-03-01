class Shoe:
    def __init__(self, brand, size):
        self._brand = brand
        self._size = size

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise ValueError("size must be an integer")
        self._size = value

# Example usage:
if __name__ == "__main__":
    # Creating a new instance of Shoe
    my_shoe = Shoe(brand="Nike", size=10)

    # Accessing and printing the initial values
    print(f"Brand: {my_shoe.brand}, Size: {my_shoe.size}")

    # Modifying the values using the setters
    my_shoe.brand = "Adidas"

    try:
        my_shoe.size = "not an integer"
    except ValueError as e:
        print(f"Error: {e}")  # This will print "size must be an integer"

    # Accessing and printing the updated values
    print(f"Brand: {my_shoe.brand}, Size: {my_shoe.size}")
