products = {"хлеб": 60, "молоко": 80, "сыр": 150}
print("Доступные товары")
for product, price in products.items():
    print(f"{product}: {price}.руб")

product_name = input("Введите название товара")
if product_name in products:
    price = products[product_name]
    print(f"\nНазвание продукта: {product_name}")
    print(f"\nСтоимость: {price}.руб")
else:
    print("Такого товара нет")


