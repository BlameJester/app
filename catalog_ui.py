class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

class ProductCatalog:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_all_products(self):
        return self.products

if __name__ == "__main__":
    # Проверка работы класса Product
    catalog = ProductCatalog()
    product1 = Product("Товар 1", 10.0, "Описание товара 1")
    catalog.add_product(product1)

    for prod in catalog.get_all_products():
        print(f"Название: {prod.name}, Цена: {prod.price}, Описание: {prod.description}")