from src.classes import Category, Product


def test_class_product(product_apple):
    assert product_apple.name == "apple"
    assert product_apple.description == "fruit"
    assert product_apple.price == 101.10
    assert product_apple.quantity == 1.5


def test_class_category(category_test, category_test_2):
    assert category_test.name == "Название"
    assert category_test.description == "Описание"
    assert category_test_2.name == "Название 2"
    assert category_test_2.description == "Описание 2"
    assert Category.category_count == 2
    assert Category.product_count == 3


def test_add_product():
    product_1 = Product("Название 1", "Описание 1", 100, 5)
    product_2 = Product("Название 2", "Описание 2", 200.50, 8)
    product_3 = Product("Название 3", "Описание 3", 310, 14)
    category_1 = Category("Название категории", "Описание категории", [product_1, product_2])
    category_1.add_product(product_3)
    assert category_1.product_count == 3
    assert category_1.products[2] == "Название 3, 310 руб. Остаток: 14 шт."


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
