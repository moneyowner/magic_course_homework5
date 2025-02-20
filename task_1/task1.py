# Напишите программу, которая сравнивает два JSON-файла
# (file1.json и file2.json) и выводит различия между ними.
# Программа должна определить, какие ключи или значения отличаются.
# Сравнивать только ключи и значения первого уровня.

import json


def json_diff(file1, file2):
    result = {}

    with (open(file1, 'r', encoding='utf-8') as first,
          open(file2, 'r', encoding='utf-8') as second):

        data1, data2 = json.load(first), json.load(second)

    keys1 = set(data1.keys())
    keys2 = set(data2.keys())

    keys_only_in_first_file1 = keys1 - keys2
    keys_only_in_first_file2 = keys2 - keys1

    result["keys_only_in_file1"] = keys_only_in_first_file1
    result["keys_only_in_file2"] = keys_only_in_first_file2

    common_keys = keys1 & keys2
    values_diffs = {}
    for key in common_keys:
        if data1[key] != data2[key]:
            values_diffs[key] = (data1[key], data2[key])
    result["values_diffs"] = values_diffs

    return result


if __name__ == "__main__":
    print(json_diff("C:\\Users\\dmitrii.korobov\\PycharmProjects\\magic_course_homework5\\task_1\\file1.json", "C:\\Users\\dmitrii.korobov\\PycharmProjects\\magic_course_homework5\\task_1\\file2.json"))
