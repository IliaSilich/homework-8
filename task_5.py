import json


def compare_json_files(file1, file2):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    keys_set1 = set(data1.keys())
    keys_set2 = set(data2.keys())

    common_keys = keys_set1.intersection(keys_set2)
    different_keys1 = keys_set1 - keys_set2
    different_keys2 = keys_set2 - keys_set1

    differences = []

    for key in common_keys:
        if data1[key] != data2[key]:
            differences.append(f"Значение для ключа {key} разные")

    for key in different_keys1:
        differences.append(f"Ключ {key} отсутствует во втором файле")

    for key in different_keys2:
        differences.append(f"Ключ {key} отсутствует в первом файле")

    return differences


file1 = 'file1.json'
file2 = 'file2.json'

differences = compare_json_files(file1, file2)

if differences:
    print("Обнаружены различия:")
    for diff in differences:
        print(diff)
    else:
        print("Файлы идентичны.")
