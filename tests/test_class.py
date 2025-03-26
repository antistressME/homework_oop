from src.classes import Category


def test_class_product(product_apple):
    assert product_apple.name == "apple"
    assert product_apple.description == "fruit"
    assert product_apple.price == 101.10
    assert product_apple.quantity == 1.5


def test_class_category(category_test, category_test_2):
    assert category_test.name == "Название"
    assert category_test.description == "Описание"
    assert category_test.products == ["Продукт 1", "Продукт 2"]
    assert category_test_2.name == "Название 2"
    assert category_test_2.description == "Описание 2"
    assert category_test_2.products == ["Продукт 1.2"]
    assert Category.category_count == 2
    assert Category.product_count == 3
