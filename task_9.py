def process_logs(file_path):
    # Словарь для хранения статистики
    statistics = {
        'success': {'GET': 0, 'POST': 0, 'PUT': 0, 'DELETE': 0},
        'failure': {'GET': 0, 'POST': 0, 'PUT': 0, 'DELETE': 0}
    }

    # Словарь для хранения статистики по ресурсам
    resource_stats = {
        '/index.html': {'success': 0, 'failure': 0},
        '/login.php': {'success': 0, 'failure': 0},
        '/upload.php': {'success': 0, 'failure': 0}
    }

    # Открытие файла для чтения
    with open(file_path, 'r') as file:
        for line in file:
            # Разделение строки на компоненты
            components = line.strip().split(' ')

            # Проверка на правильное количество компонентов
            if len(components) >= 7:
                date, time, ip_address, method, resource, status_code, response_size = components[0], components[1], components[2], components[3], components[4], components[5], components[6]

                # Проверка, относится ли запрос к мониторируемым ресурсам
                if resource in resource_stats:
                    # Подсчет успешных и неуспешных запросов
                    if status_code.startswith('2') or status_code.startswith('3'):
                        statistics['success'][method] += 1
                        resource_stats[resource]['success'] += 1
                    elif status_code.startswith('4') or status_code.startswith('5'):
                        statistics['failure'][method] += 1
                        resource_stats[resource]['failure'] += 1

    return statistics, resource_stats


file_path = "logs.txt"  # Замените на фактический путь к вашему файлу

try:
    stats, resource_stats = process_logs(file_path)

    print("Статистика успешных запросов:")
    for method, count in stats['success'].items():
            print(f"{method}: {count}")

    print("\nСтатистика неуспешных запросов:")
    for method, count in stats['failure'].items():
            print(f"{method}: {count}")

    print("\nСтатистика по ресурсам:")
    for resource, counts in resource_stats.items():
           print(f"{resource}: Успешные - {counts['success']}, Неуспешные - {counts['failure']}")

except FileNotFoundError:
    print(f"Файл {file_path} не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")