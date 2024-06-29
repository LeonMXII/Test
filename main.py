# Квадратное уравнение
def discriminant(a, b, c):
    return b**2 - 4*a*c

def solution(a, b, c):
    if discriminant(a,b,c) < 0:
        return "корней нет"
    elif discriminant(a,b,c) ==0:
        x = (-b)/(2*a)
        return x
    else:
        discriminant(a, b, c) > 0
        x_1 = (-b + discriminant(a,b,c)** 0.5)/(2 * a)
        x_2 = (-b - discriminant(a,b,c)** 0.5)/(2 * a)
        return x_1, x_2


# Кто дальше
hare_distances = [8, 5, 3, 2, 0, 1, 1]
turtle_distances = [3, 3, 3, 3, 3, 3, 3]
def solve(hare_distances: list, turtle_distances: list):
    hare_all = 0
    for a in hare_distances:
        hare_all += a
    turtle_all = 0
    for b in turtle_distances:
         turtle_all += b
    if hare_all < turtle_all:
        resul = "черепаха"
    elif hare_all > turtle_all:
        resul = "заяц"
    else:
        resul = "одинаково"
    return resul


# Проверка возраста
def check_age(age: int):

    if age >= 18: # Введите условие для проверки возраста
        result = 'Доступ разрешён'
    else:
        result = 'Доступ запрещён'

    return result


if __name__ == "__main__":
    # Квадратное уравнение
    solution(1, 8, 15)
    solution(1, -13, 12)
    solution(-4, 28, -49)
    solution(1, 1, 1)

    # Кто дальше
    result = solve([8, 5, 3, 2, 0, 1, 1], [3, 3, 3, 3, 3, 3, 3])
    assert result == "черепаха", f"Победитель определен неверно: {result}"
    print(f"Победитель: {result}")
    result = solve([8, 5, 3, 2, 2, 1, 1], [3, 3, 3, 3, 3, 3, 3])
    assert result == "заяц", f"Победитель определен неверно: {result}"
    print(f"Победитель: {result}")
    result = solve([8, 5, 3, 2, 1, 1, 1], [3, 3, 3, 3, 3, 3, 3])
    assert result == "одинаково", f"Победитель определен неверно: {result}"
    print(f"Победитель: {result}")

    # Проверка возраста
    auth = check_age(10)
    assert auth == 'Доступ запрещён', f'Получен неверный ответ: {auth}'
    print('Возраст 10:', auth)

    auth = check_age(20)
    assert auth == 'Доступ разрешён', f'Получен неверный ответ: {auth}'
    print('Возраст 20:', auth)
