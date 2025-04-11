import pytest

from src.classes import Category, Product


@pytest.fixture
def product_apple():
    return Product("apple", "fruit", 101.10, 150)


@pytest.fixture
def product_banana():
    return Product("banana", "fruit", 250, 50)


@pytest.fixture
def category_test(product_apple, product_banana):
    return Category("Название", "Описание", [product_apple, product_banana])


@pytest.fixture
def category_test_2():
    return Category("Название 2", "Описание 2", ["Продукт 1.2"])
