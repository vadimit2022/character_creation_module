from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Мы вычислили квадратный корень из введённого вами."""
    root = 0
    if your_number <= 0:
        root = calculate_square_root(your_number)
        return
    print(root)


print(message)
calc(25.5)
