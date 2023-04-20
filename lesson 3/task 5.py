products = 'Молоко', 'Хлеб', 'Ещё одно молоко', 'И ещё одно молоко (почему нет)', 'сыр', 'мёд'
for product in products:
    if len(product) % 2 == 0:
        print(product)