# Завдання 1. Оптимізація виробництва

## Опис завдання

Компанія виробляє два види напоїв: **"Лимонад"** і **"Фруктовий сік"**. Для їх виготовлення використовуються різні інгредієнти, але кількість ресурсів є обмеженою. Завдання полягає в тому, щоб максимізувати загальну кількість вироблених напоїв з наявними ресурсами.

### Умови:

1. **"Лимонад"** виготовляється з:
   - Вода – 2 од.  
   - Цукор – 1 од.  
   - Лимонний сік – 1 од.  

2. **"Фруктовий сік"** виготовляється з:
   - Фруктове пюре – 2 од.  
   - Вода – 1 од.  

3. **Ресурси**:
   - Вода – 100 од.  
   - Цукор – 50 од.  
   - Лимонний сік – 30 од.  
   - Фруктове пюре – 40 од.  

4. Потрібно визначити **оптимальну кількість** напоїв, яку можна виробити з наявних ресурсів, щоб максимізувати загальну кількість продукції.

---

## Кроки розв’язання

1. **Формалізуємо змінні**:
   - \(x_1\) — кількість "Лимонаду".
   - \(x_2\) — кількість "Фруктового соку".

2. **Цільова функція**:
   - Максимізувати загальну кількість напоїв:  
     \[ \text{Maximize} \quad x_1 + x_2 \]  
   Це означає, що ми прагнемо виробити якомога більше "Лимонаду" та "Фруктового соку" разом.

3. **Обмеження на ресурси**:
   - Використання води: \(2x_1 + 1x_2 \leq 100\)
   - Використання цукру: \(1x_1 \leq 50\)
   - Використання лимонного соку: \(1x_1 \leq 30\)
   - Використання фруктового пюре: \(2x_2 \leq 40\)

4. **Невід’ємність змінних**:
   - \(x_1 \geq 0\), \(x_2 \geq 0\)

5. **Використання PuLP**:  
   Ми використовуємо бібліотеку `PuLP` для розв’язання задачі лінійного програмування. Вона дозволяє знайти оптимальні значення змінних та максимізувати кількість напоїв, враховуючи обмеження.



## Висновок

Ця модель дозволяє знайти оптимальну кількість "Лимонаду" та "Фруктового соку", яку можна виробити з наявних ресурсів. У наведеному прикладі оптимальним рішенням є виготовлення 30 одиниць "Лимонаду" та 20 одиниць "Фруктового соку", що дозволяє використати ресурси максимально ефективно.


# Завдання 2. Обчислення визначеного інтеграла методом Монте-Карло

### Умова задачі
Необхідно обчислити визначений інтеграл функції методом Монте-Карло та порівняти отриманий результат з аналітичним розв’язанням, використовуючи функцію `quad` із бібліотеки `scipy`. 

Функція для інтегрування:  
\[ f(x) = x^2 \]  
Інтервал інтегрування:  
\[ [0, 2] \]  

### Розв'язання

1. **Інтеграл методом Монте-Карло**:
   - Створюємо випадкові точки на інтервалі \([0, 2]\) для оцінки площі під кривою.
   - Обчислюємо відсоток точок, які потрапляють під графік функції, що дає наближення до інтегралу.
   
2. **Аналітичне розв’язання (функція `quad`)**:
   - Використовуємо функцію `scipy.integrate.quad` для точного чисельного інтегрування.


### Результат

- **Інтеграл методом Монте-Карло**:  
  ```
  Інтеграл методом Монте-Карло: 2.6804
  ```
  
- **Аналітичне розв'язання за допомогою scipy.quad**:  
  ```
  Інтеграл з scipy.quad: 2.666666666666667 (похибка: 2.960594732333751e-14)
  ```

### Пояснення результату

1. **Метод Монте-Карло**:
   - Це статистичний метод, який оцінює площу під графіком функції за допомогою випадкових точок. Через випадковий характер результат може містити похибку. У нашому випадку результат 2.6804 близький до точного, що свідчить про коректність реалізації.

2. **Точне значення за допомогою `scipy.quad`**:
   - Інтеграл функції \( f(x) = x^2 \) на інтервалі \([0, 2]\) дорівнює:
     \[ \int_0^2 x^2 \, dx = \frac{2^3}{3} = \frac{8}{3} \approx 2.6667 \]
   - Похибка чисельного розв’язання дуже мала (близька до нуля), що підтверджує високу точність методу.

3. **Порівняння**:
   - Метод Монте-Карло дав результат 2.6804, що дуже близько до точного значення 2.6667.
   - Збільшення кількості випадкових точок може ще більше зменшити похибку Монте-Карло.

### Висновок

Метод Монте-Карло є ефективним способом наближеного обчислення інтегралів, проте він завжди містить випадкову похибку. Для дуже точних розрахунків краще використовувати чисельні методи, як `scipy.quad`. У цьому завданні результати обох підходів продемонстрували, що метод Монте-Карло може давати прийнятні результати навіть із відносно невеликою кількістю точок.
```

---

