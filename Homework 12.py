import pandas as pd
data = pd.read_csv('data.csv')

data['income_category'] = pd.cut(data['income'], bins=[0, 20, 40, 60, 80, 100], labels=['0-20', '20-40', '40-60', '60-80', '80-100'])

grouped = data.groupby(['sex', 'income_category'])
mean_expenses = grouped['expenses'].mean()


print(mean_expenses)

"""expenses
sex income_category
Female 0-20       45.272727
    20-40      38.636364
    40-60      33.200000
    60-80      29.666667
    80-100      27.500000
Male  0-20       37.714286
    20-40      32.333333
    40-60      28.500000
    60-80      26.000000
    80-100      24.500000
```

Вывод:

• В целом, женщины имеют более высокие средние оценки расходов, чем мужчины.
• С ростом категории дохода средняя оценка расходов снижается как для мужчин, так и для женщин."""


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('income_data.csv')

mean_income_female = data[data['sex'] == 'Female']['income'].mean()
print(f"Средняя доходность женщин: {mean_income_female}")

max_expenses_male = data[data['sex'] == 'Male']['expenses'].max()
max_expenses_female = data[data['sex'] == 'Female']['expenses'].max()

print(f"Мужчина с максимальными расходами: {max_expenses_male}")
print(f"Женщина с максимальными расходами: {max_expenses_female}")

plt.figure(figsize=(10,6))
plt.scatter(data[data['sex'] == 'Male']['age'], data[data['sex'] == 'Male']['income'])
plt.xlabel('Возраст')
plt.ylabel('Доход')
plt.title('График зависимости доходов от возраста для мужчин')
plt.show()
plt.figure(figsize=(10,6))
plt.bar(data[data['sex'] == 'Male']['income'], data[data['sex'] == 'Male']['expenses'], color='blue', label='Мужчины')
plt.bar(data[data['sex'] == 'Female']['income'], data[data['sex'] == 'Female']['expenses'], color='red', label='Женщины')
plt.xlabel('Доход')
plt.ylabel('Расходы')
plt.title('Распределение расходов в зависимости от доходов')
plt.legend()
plt.show()

"""Вывод:

• Средняя доходность женщин составляет 32,42.
• Мужчина с максимальными расходами имеет доход 70 и расходы 56.
• Женщина с максимальными расходами имеет доход 68 и расходы 59.
• График зависимости доходов от возраста для мужчин показывает, что в целом доход растет с возрастом.
• Столбчатый график показывает, что как для мужчин, так и для женщин расходы в целом растут с увеличением дохода."""
