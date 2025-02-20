# Напишите программу, которая считывает данные из
# CSV-файла sales.csv, где содержатся данные о продажах
# (например, дата, товар, количество, цена).
# Программа должна вывести:
# - Общую сумму продаж.
# - Товар с наибольшим числом продаж.
import csv


SALES_FIELDNAMES = ["date", "product","quantity", "price"]


def get_csv_data(filename: str):
    result = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, fieldnames=SALES_FIELDNAMES)
        for row in reader:
            if list(row.values()) == SALES_FIELDNAMES:
                continue
            result.append(row)
    return result


def get_total_sales_sum(filename: str):
    total_sum = 0
    for row in get_csv_data(filename):
        total_sum += int(row["quantity"]) * float(row["price"])
    return total_sum


def get_most_frequent_product(filename: str):
    frequencies = {}
    for row in get_csv_data(filename):
        quantity = int(row["quantity"])
        product = row["product"]
        frequencies[product] = frequencies.get(product, 0) + quantity
    return max(frequencies, key=frequencies.get)


if __name__ == "__main__":
    print(get_most_frequent_product("C:\\Users\\dmitrii.korobov\\PycharmProjects\\magic_course_homework5\\task_3\\sales.csv"))
    print(get_total_sales_sum("C:\\Users\\dmitrii.korobov\\PycharmProjects\\magic_course_homework5\\task_3\\sales.csv"))

