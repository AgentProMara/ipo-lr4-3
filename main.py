# Запрашиваем у пользователя ввод числа и преобразуем его в целое число
number = int(input("Введите число: "))

# Инициализируем переменную для хранения факториала и счетчик
factorial = 1
i = 1

# Используем цикл while для вычисления факториала
while i <= number:
    factorial *= i  # Умножаем текущий факториал на значение счетчика
    i += 1          # Увеличиваем счетчик на 1

# Выводим результат на экран
print(f"Факториал числа {number} равен {factorial}")
