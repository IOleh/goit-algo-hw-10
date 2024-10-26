import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# 1. Метод Монте-Карло
N = 100000  # Кількість випадкових точок
x_rand = np.random.uniform(a, b, N)  # Випадкові значення x в [a, b]
y_rand = np.random.uniform(0, b ** 2, N)  # Випадкові y у [0, f(b)]

# Точки, що потрапили під криву
under_curve = y_rand < f(x_rand)
area_monte_carlo = (b - a) * (b ** 2) * np.mean(under_curve)

print(f"Інтеграл методом Монте-Карло: {area_monte_carlo}")

# 2. Аналітичний розрахунок за допомогою quad
result, error = spi.quad(f, a, b)
print(f"Інтеграл з scipy.quad: {result} (похибка: {error})")

# 3. Візуалізація методу Монте-Карло
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.fill_between(np.linspace(a, b), f(np.linspace(a, b)), color='gray', alpha=0.3)

# Відображення випадкових точок
ax.scatter(x_rand, y_rand, c=under_curve, cmap='coolwarm', s=0.5, alpha=0.5)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, b ** 2 + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Метод Монте-Карло для f(x) = x^2')

plt.grid()
plt.show()
