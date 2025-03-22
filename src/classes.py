class Product:
    """Класс продукты"""

    name: str
    description: str
    price: float
    quantity: float

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс категории"""

    amount_categories = 0

    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        self.amount_products = len(products)
        Category.amount_categories += 1


