def sum_of_squares(number):
    if isinstance(number, int) and number > 0:
        return sum(x**2 for x in range(0, number+1))
    else:
        raise ValueError("должно быть представлено положительным целым числом большим нуля")


tests = [1, 5, -1, 0, '10', 5.5]
for n in tests:
    try:
        result = sum_of_squares(n)
        print(f"Сумма квадратов чисел от 1 до {n}: {result}")
    except ValueError as e:
        print(f"Ошибка: {e}")
