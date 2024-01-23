def find_min_max_temp(file_path):
    max_temp_city = None
    min_temp_city = None
    max_temp = float('-inf')
    min_temp = float('inf')

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data = line.strip().split(',')
            city = data[0]
            temperature = float(data[1])

            if temperature > max_temp:
                max_temp = temperature
                max_temp_city = city

            if temperature < min_temp:
                min_temp = temperature
                min_temp_city = city

    return max_temp_city, min_temp_city


file_path = "weather_data.txt"

try:
    max_temp_city, min_temp_city = find_min_max_temp(file_path)
    print(f"Город с самой высокой температурой: {max_temp_city}")
    print(f"Город с самой низкой температурой: {min_temp_city}")
except FileNotFoundError:
    print(f"Файл {file_path} не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
