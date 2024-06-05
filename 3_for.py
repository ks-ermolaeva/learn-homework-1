"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

stock = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]


def main():

    def total_sold(items):
        total = 0
        for item in items:
            total += item
        return total

    def avg_sold(items):
        items_sum = 0
        for item in items:
            items_sum += item
        return round(items_sum / len(items))

    stock_total = 0
    for one_product in stock:
        product_total_sold = total_sold(one_product['items_sold'])
        print(f'Суммарное кол-во продаж {one_product["product"]}: {product_total_sold}')
        stock_total += product_total_sold

    stock_avg_sum = 0
    for avg_product in stock:
        avg_product_sold = avg_sold(avg_product['items_sold'])
        print(f'Среднее кол-во продаж {avg_product["product"]}: {avg_product_sold}')
        stock_avg_sum += avg_product_sold

    print(f'Суммарное кол-во продаж всех товаров: {stock_total}')
    stock_avg = round(stock_avg_sum / len(stock))
    print(f'Среднее кол-во продаж всех товаров: {stock_avg}')

if __name__ == "__main__":
    main()
