# Завдання 2. Обчислення визначеного інтеграла
# Ваше друге завдання полягає в обчисленні значення інтеграла функції методом Монте-Карло

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi
import random

# Визначення функції та меж інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Метод Монте-Карло для обчислення інтегралу
num_points = 10000  # Кількість точок
points_under_curve = 0

y_max = f(b)  # Максимальне значення функції на відрізку [a, b]

for _ in range(num_points):
    x_rand = random.uniform(a, b)
    y_rand = random.uniform(0, y_max)
    if y_rand <= f(x_rand):
        points_under_curve += 1

monte_carlo_result = (points_under_curve / num_points) * (b - a) * y_max
print(f"Обчислене значення інтегралу методом Монте-Карло: {monte_carlo_result}")

# Аналітичне обчислення інтегралу за допомогою функції quad
result, error = spi.quad(f, a, b)
print("Інтеграл (аналітичне значення):", result, "Оцінка абсолютної помилки:", error)

# Висновок
print(f"Різниця між Монте-Карло та аналітичним значенням: {abs(monte_carlo_result - result)}")

# Створення графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
