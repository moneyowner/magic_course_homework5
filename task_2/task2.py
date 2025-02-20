# В файле users.json хранится список пользователей с полями:
# имя, возраст, город и профессия. Напишите программу,
# которая считывает файл и выводит только тех пользователей,
# которые старше 30 лет и работают в указанной профессии.

import json


def filter_users(filename, profession, age_threshold=30):
    with open(filename, 'r', encoding='utf-8') as file:
        users = json.load(file)

    filtered_users = [
        user for user in users
        if user.get("age", 0) > age_threshold
        and user.get("profession") == profession
    ]

    return filtered_users

if __name__ == "__main__":
    res = filter_users("C:\\Users\\dmitrii.korobov\\PycharmProjects\\magic_course_homework5\\task_2\\users.json","программист", 30)
    print(res)