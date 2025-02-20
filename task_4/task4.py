#   В файле employees.csv содержится список сотрудников
# с полями: имя, возраст, должность, зарплата.
# Напишите программу, которая считывает данные
# и выводит только тех сотрудников,
# у которых зарплата больше 50,000.
import csv


EMPLOYE_FIELDNAMES = ["name", "age", "position", "salary"]


def get_csv_data(filename: str):
    result = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, fieldnames=EMPLOYE_FIELDNAMES)
        for row in reader:
            if list(row.values()) == EMPLOYE_FIELDNAMES:
                continue
            result.append(row)
    return result


def filter_employees_by_salary(filename, salary_treshhold=50_000):
    return [row for row in get_csv_data(filename)
            if int(row["salary"]) >= salary_treshhold]


if __name__ == "__main__":
    print(filter_employees_by_salary("C:\\Users\\dmitrii.korobov\\PycharmProjects\\magic_course_homework5\\task_4\\employees.csv"))
