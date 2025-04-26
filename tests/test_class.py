from src.classes import Category, Product
from src.products import LawnGrass, Smartphone


def test_class_product(product_apple):
    assert product_apple.name == "apple"
    assert product_apple.description == "fruit"
    assert product_apple.price == 101.10
    assert product_apple.quantity == 150


def test_class_category(category_test, category_test_2):
    assert category_test.name == "Название"
    assert category_test.description == "Описание"
    assert category_test_2.name == "Название 2"
    assert category_test_2.description == "Описание 2"
    assert Category.category_count == 2
    assert Category.product_count == 3


def test_add_product(smartphone_1, smartphone_2, lawn_grass_1):
    Category.product_count = 0
    category_1 = Category(
        "Название категории",
        "Описание категории",
        [
            smartphone_2,
        ],
    )
    category_1.add_product(smartphone_1)
    assert category_1.product_count == 2
    assert category_1.products[1] == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    try:
        category_1.add_product(lawn_grass_1)
    except Exception:
        assert TypeError


def test_new_product(product_apple):
    product_test = Product.new_product(
        {
            "name": "Тест",
            "description": "Описание теста",
            "price": 23.89,
            "quantity": 2,
        }
    )
    assert product_test.name == "Тест"
    assert product_test.description == "Описание теста"
    assert product_test.price == 23.89
    assert product_test.quantity == 2


def test_add_price(product_apple):
    product_apple.price = 250
    assert product_apple.price == 250


def test_str_produsct(product_apple, product_banana):
    assert str(product_apple) == "apple, 101.1 руб. Остаток: 150 шт."
    assert str(product_banana) == "banana, 250 руб. Остаток: 50 шт."


def test_add_produscts_error(product_apple, product_banana):
    try:
        product_apple + product_banana
    except Exception:
        assert TypeError


def test_str_category(category_test):
    assert str(category_test) == "Название, количество продуктов: 200 шт."


def test_mixin_log1(smartphone_1):
    assert repr(smartphone_1) == "Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"


def test_mixin_log2(lawn_grass_1):
    assert repr(lawn_grass_1) == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"


def test_mixin_log3(product_apple):
    assert repr(product_apple) == "Product(apple, fruit, 101.1, 150)"


def test_base_product():
    assert (
        str(Product.__mro__)
        == "(<class 'src.classes.Product'>, <class 'src.classes.BaseProduct'>, <class 'abc.ABC'>, <class 'src.classes.MixinLog'>, <class 'object'>)"
    )
    assert (
        str(Smartphone.__mro__)
        == "(<class 'src.products.Smartphone'>, <class 'src.classes.Product'>, <class 'src.classes.BaseProduct'>, <class 'abc.ABC'>, <class 'src.classes.MixinLog'>, <class 'object'>)"
    )
    assert (
        str(LawnGrass.__mro__)
        == "(<class 'src.products.LawnGrass'>, <class 'src.classes.Product'>, <class 'src.classes.BaseProduct'>, <class 'abc.ABC'>, <class 'src.classes.MixinLog'>, <class 'object'>)"
    )


def test_mro():
    assert str(Product.__mro__[1]) == "<class 'src.classes.BaseProduct'>"
