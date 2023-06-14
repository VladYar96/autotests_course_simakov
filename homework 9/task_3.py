# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
with open('test_file/task_3.txt', mode='r',  encoding='utf-8') as file:
    amount_purchases = []
    sum_price = 0
    all_purchases = file.readlines()
    for price in all_purchases:
        price = ''.join([num for num in price if num.isdigit])
        if price == '\n':
            amount_purchases.append(sum_price)
            sum_price = 0
        else:
            sum_price += int(price)

three_most_expensive_purchases = sum(sorted(amount_purchases)[-3:])
print(three_most_expensive_purchases)

assert three_most_expensive_purchases == 202346
