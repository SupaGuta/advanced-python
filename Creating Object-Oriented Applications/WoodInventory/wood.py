"""This module maintains the inventory and specifications of wood products."""

class Wood:
    """This class retrieves and displays wood product data."""
    
    def __init__(self, product, form, price, inventory):
        """Construct class instance with wood product attributes."""
        self.__product = product
        self.__form = form
        self.__price = price
        self.__inventory = inventory

    # Define properties for wood products.    
    @property
    def product(self):
        return self.__product

    @property
    def form(self):
        return self.__form

    @property
    def price(self):
        return self.__price

    @property
    def inventory(self):
        return self.__inventory
    
    @product.setter
    def product(self, product):
        self.__product = product
        
    @form.setter
    def form(self, form):
        self.__form = form
        
    @price.setter
    def price(self, price):
        self.__price = price
        
    @inventory.setter
    def inventory(self, inventory):
        self.__inventory = inventory

    def display(self):
        """Display the attributes of a wood product."""
        print(f"{self.product} ({self.form}) | "
              f"Price: {self.price:.2f}, Inventory: {self.inventory}")

    def sell_wood(self, quantity):
        """Sell a specified number of a wood product."""
        self.__inventory = self.__inventory - quantity
        print(f"\nSold {quantity} pieces of {self.product}.\n")

class Plywood(Wood):
    """This class retrieves and displays plywood data."""

    def __init__(self, product, form, price, inventory, width, length):
        """Construct class instance with plywood attributes."""
        super().__init__(product, form, price, inventory)
        self.__width = width
        self.__length = length

    # Define properties for plywood products.    
    @property
    def width(self):
        return self.__width
    
    @property
    def length(self):
        return self.__length
    
    @width.setter
    def width(self, width):
        self.__width = width
    
    @length.setter
    def length(self, length):
        self.__length = length

    def display(self):
        """Display the attributes of a plywood product."""
        print(f"This plywood is {self.width} inches wide"
              f" and {self.length} inches long.")