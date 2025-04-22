from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный метод,
    который является родительским для класса Product"""

    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def new_product(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class Product(BaseProduct):
    """Класс продукты"""

    name: str
    description: str
    price: float
    quantity: float

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        if self.__price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            product_price = self.__price
            return product_price

    @price.setter
    def price(self, new_price):
        if new_price < self.__price:
            agree = input("Введите y, чтобы подтвердить понижени цены" "\nили n, чтобы отменить изменение цены")
            if agree == "y" and new_price > 0:
                self.__price = new_price
            else:
                print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_params: dict):
        new_product = cls(
            name=product_params["name"],
            description=product_params["description"],
            price=product_params["price"],
            quantity=product_params["quantity"],
        )
        return new_product

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is self.__class__:
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError


class Category:
    """Класс категории"""

    category_count = 0
    product_count = 0

    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.product_count += len(self.__products)
        Category.category_count += 1

    @property
    def products(self):
        list_of_products = []
        for product in self.__products:
            list_of_products.append(str(product))
        return list_of_products

    # @products.setter
    def add_product(self, product):  # метод для добавления продукта
        if product not in self.__products and issubclass(type(product), Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    def __str__(self):
        quantity_c = 0
        for prod in self.__products:
            quantity_c += prod.quantity
        return f"{self.name}, количество продуктов: {quantity_c} шт."


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.product_count)
    print(category1.products)
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_count)

    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)
    print(category1)
    print(product4 + product1)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)
