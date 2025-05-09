from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный метод,
    который является родительским для класса Product."""

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


class MixinLog:
    """Класс миксин, который при создании объекта
    печатает в консоль информацию о том,
    от какого класса и с какими параметрами был создан объект."""

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"


class Product(BaseProduct, MixinLog):
    """Класс продукты."""

    name: str
    description: str
    price: float
    quantity: float

    def __init__(self, name, description, price, quantity):
        if quantity <= 0:  # Если количество равно 0
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

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
        # Метод для создания экзэпляра класса Прдукты,
        # параметры получает в виде словаря:
        # {'название атрибута': 'значение'}.
        new_product = cls(**product_params)
        return new_product

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        # Метод для сложенния экземпляров класса Продукты и его подклассов.
        if type(other) is self.__class__:
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError


class Category:
    """Класс категории."""

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
    def add_product(self, product):
        # Метод для добавления продукта в список продуктов категории.
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

    def middle_price(self):
        """подсчитывает средний ценник всех товаров"""
        price_sum = sum(x.price for x in self.__products)
        quantity_sum = sum(x.quantity for x in self.__products)
        try:
            result = int(price_sum / quantity_sum)
        except ZeroDivisionError:
            result = 0
        return result


if __name__ == "__main__":
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством"
        )
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())
