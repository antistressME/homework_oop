import pytest

from src.classes import Category, Product
from src.products import LawnGrass, Smartphone


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


@pytest.fixture
def smartphone_1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphone_2():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")


@pytest.fixture
def lawn_grass_1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawn_grass_2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
