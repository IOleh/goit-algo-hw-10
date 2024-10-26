from pulp import LpMaximize, LpProblem, LpVariable, value

# 1. Створюємо задачу лінійного програмування
model = LpProblem("Maximize_Drink_Production", LpMaximize)

# 2. Визначаємо змінні
x1 = LpVariable("Lemonade", lowBound=0, cat="Integer")  # кількість "Лимонаду"
x2 = LpVariable("Fruit_Juice", lowBound=0, cat="Integer")  # кількість "Фруктового соку"

# 3. Додаємо цільову функцію
model += x1 + x2, "Total_Products"

# 4. Додаємо обмеження на ресурси
model += 2 * x1 + 1 * x2 <= 100, "Water_Constraint"
model += 1 * x1 <= 50, "Sugar_Constraint"
model += 1 * x1 <= 30, "Lemon_Juice_Constraint"
model += 2 * x2 <= 40, "Fruit_Puree_Constraint"

# 5. Розв'язуємо задачу
model.solve()

# 6. Виводимо результати
print(f"Optimal amount of Lemonade: {x1.varValue}")
print(f"Optimal amount of Fruit Juice: {x2.varValue}")
print(f"Total Products Produced: {value(model.objective)}")
