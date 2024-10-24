# Завдання 1. Оптимізація виробництва
# Компанія виробляє два види напоїв: "Лимонад" і "Фруктовий сік". Для виробництва цих напоїв використовуються різні інгредієнти та обмежена кількість обладнання. 
# Задача полягає у максимізації виробництва, враховуючи обмежені ресурси.

# Умови завдання:
# 1. "Лимонад" виготовляється з "Води", "Цукру" та "Лимонного соку".
# 2. "Фруктовий сік" виготовляється з "Фруктового пюре" та "Води".
# 3. Обмеження ресурсів: 100 од. "Води", 50 од. "Цукру", 30 од. "Лимонного соку" та 40 од. "Фруктового пюре".
# 4. Виробництво одиниці "Лимонаду" вимагає 2 од. "Води", 1 од. "Цукру" та 1 од. "Лимонного соку".
# 5. Виробництво одиниці "Фруктового соку" вимагає 2 од. "Фруктового пюре" та 1 од. "Води".
# Використовуючи PuLP, створіть модель, яка визначає, скільки "Лимонаду" та "Фруктового соку" потрібно виробити для максимізації загальної кількості продуктів, 
# дотримуючись обмежень на ресурси. Напишіть програму, код якої максимізує загальну кількість вироблених продуктів "Лимонад" та "Фруктовий сік", 
# враховуючи обмеження на кількість ресурсів.

import pulp

# Створення моделі лінійного програмування
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні
lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat='Continuous')

# Функція мети: максимізувати виробництво напоїв
model += lemonade + fruit_juice, "Total_Production"

# Обмеження на ресурси
model += 2 * lemonade + fruit_juice <= 100, "Water_Constraint"
model += 1 * lemonade <= 50, "Sugar_Constraint"
model += 1 * lemonade <= 30, "Lemon_Juice_Constraint"
model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

# Розв'язання задачі
model.solve()

# Результати
print(f"Статус: {pulp.LpStatus[model.status]}")
print(f"Кількість Лимонаду для виробництва: {lemonade.varValue}")
print(f"Кількість Фруктового соку для виробництва: {fruit_juice.varValue}")
print(f"Загальна кількість вироблених продуктів: {lemonade.varValue + fruit_juice.varValue}")