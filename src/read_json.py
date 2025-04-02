import json

from src.classes import Category, Product


def read_json():
    """Получаем данные из json-файла."""
    with open("products.json", encoding="utf8") as file:
        data = json.load(file)
        return data


def get_classes(data):
    """Получаем объекты классов"""
    for point in data:
        category = Category(point["name"], point["description"], point["products"])
        # print(category.name)
        # print(category.description)
        # print(category.product_count)
        # print(category.category_count)
        for item in point["products"]:
            product = Product(item["name"], item["description"], item["price"], item["quantity"])
            # print(product.name)
            # print(product.description)
            # print(product.price)
            # print(product.quantity)


if __name__ == "__main__":
    data = read_json()
    get_classes(data)
