class Shoe:
    def __init__(self, brand, size, color, material, condition="Used"):
        self.brand = brand
        self.size = size  # Validated via the property setter
        self.color = color
        self.material = material
        self.condition = condition

    @property
    def size(self):
        """The size property"""
        return self._size

    @size.setter
    def size(self, size):
        """Validate that size is an integer"""
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")

    def cobble(self):
        """Repair the shoe and set its condition to 'New'"""
        self.condition = "New"
        print("Your shoe is as good as new!")