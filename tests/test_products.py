import pytest

from src.products import LawnGrass, Smartphone


def test_smartphone1(smartphone_1):
    smartphone1 = smartphone_1
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_smartphone2(smartphone_2):
    smartphone2 = smartphone_2
    assert smartphone2.name == "Xiaomi Redmi Note 11"
    assert smartphone2.description == "1024GB, Синий"
    assert smartphone2.price == 31000.0
    assert smartphone2.quantity == 14
    assert smartphone2.efficiency == 90.3
    assert smartphone2.model == "Note 11"
    assert smartphone2.memory == 1024
    assert smartphone2.color == "Синий"


def test_lawn_grass1(lawn_grass_1):
    lawn_grass1 = lawn_grass_1
    assert lawn_grass1.name == "Газонная трава"
    assert lawn_grass1.description == "Элитная трава для газона"
    assert lawn_grass1.price == 500.0
    assert lawn_grass1.quantity == 20
    assert lawn_grass1.country == "Россия"
    assert lawn_grass1.germination_period == "7 дней"
    assert lawn_grass1.color == "Зеленый"


def test_lawn_grass2(lawn_grass_2):
    lawn_grass2 = lawn_grass_2
    assert lawn_grass2.name == "Газонная трава 2"
    assert lawn_grass2.description == "Выносливая трава"
    assert lawn_grass2.price == 450.0
    assert lawn_grass2.quantity == 15
    assert lawn_grass2.country == "США"
    assert lawn_grass2.germination_period == "5 дней"
    assert lawn_grass2.color == "Темно-зеленый"


def test_add_smartphone(smartphone_1, smartphone_2):
    total = smartphone_1 + smartphone_2  # 180000.0 * 5 + 31000.0 * 14 = 1334000.0
    assert total == 1334000


def test_add_lawn_grass(lawn_grass_1, lawn_grass_2):
    total = lawn_grass_1 + lawn_grass_2  # 500.0 * 20 + 450.0 * 15 = 16750
    assert total == 16750


def test_add_dif_classes(smartphone_1, lawn_grass_1):
    try:
        smartphone_1 + lawn_grass_1
    except Exception:
        assert TypeError
