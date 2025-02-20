# Система учета заказов

# У вас есть JSON-файл orders.json,
# содержащий данные о заказах интернет-магазина.
# Каждый заказ включает информацию о клиенте,
# заказанных товарах, количестве и цене.

# Напишите программу, которая:
# Выводит общую сумму каждого заказа.
# Находит клиента с наибольшей суммой заказа и выводит его имя и сумму.
import json

def load_json_data(filename: str):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_orders_summaries(filename: str):
    data = load_json_data(filename)
    summaries = {}
    for order in data["orders"]:
        order_summ = 0
        for item in order["items"]:
            order_summ += item["quantity"] * item["price"]
            summaries[order["order_id"]] = order_summ
    return summaries


def get_most_expensive_client(filename: str):
    most_expensive_client = None
    max_order_sum = 0

    data = load_json_data(filename)

    for order in data["orders"]:
        order_summ = 0
        for item in order["items"]:
            order_summ += item["quantity"] * item["price"]

        if order_summ > max_order_sum:
            max_order_sum = order_summ
            most_expensive_client = order["customer"]["name"]
    return most_expensive_client, max_order_sum


if __name__ == "__main__":
    print(get_orders_summaries("C:\\Users\\dmitrii.korobov\\PycharmProjects\\magic_course_homework5\\task_5\\orders.json"))
    print(get_most_expensive_client("C:\\Users\\dmitrii.korobov\\PycharmProjects\\magic_course_homework5\\task_5\\orders.json"))
