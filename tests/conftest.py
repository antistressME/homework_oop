import pytest

from src.classes import Category, Product


@pytest.fixture
def product_apple():
    return Product("apple", "fruit", 101.10, 1.5)


@pytest.fixture
def category_test():
    return Category("Название", "Описание", ["Продукт 1", "Продукт 2"])


@pytest.fixture
def category_test_2():
    return Category("Название 2", "Описание 2", ["Продукт 1.2"])
