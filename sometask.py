def sum_digits(num: int):
    split = [*str(num)]
    res = sum(map(int, split))
    return res


def func1(n_customers: int):
    """
    Функция, которая подсчитывает число покупателей, попадающих в каждую группу,
    если нумерация ID сквозная и начинается с 0.
    На вход функция получает целое число n_customers (количество клиентов).
    :param n_customers: количество клиентов
    """

    return func2(n_customers, 0)


def func2(n_customers: int, n_first_id: int):
    """
    Функция, аналогичная первой, если ID начинается с произвольного числа.
    :param n_customers: количество клиентов
    :param n_first_id: первый ID в последовательности
    :return:
    """
    num_classes = sum([9] * len(str(n_customers)))
    classes = [0] * num_classes
    for client_id in range(n_first_id, n_customers):
        c = sum_digits(client_id)
        classes[c] += 1

    return classes


if __name__ == "__main__":
    distribution = func2(19999, 0)
    for i, n in enumerate(distribution):
        print(f"В группе №{i} находится {n} пользователей")
    print(distribution)
