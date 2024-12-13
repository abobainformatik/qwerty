import pandas as pd
import matplotlib.pyplot as plt

# Задача 1: Объединение DataFrames


df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})

df_vertical = pd.concat([df1, df2])
print("Вертикальная конкатенация:\n", df_vertical)


df3 = df1.copy()
df3.insert(1, 'C', [7, 8, 9])
df3.insert(3, 'D', [10, 11, 12])

df_horizontal = df3
print("Горизонтальное объединение:\n", df_horizontal)



# Задача 2: Построение графика зависимости одного столбца от другого


df = pd.DataFrame({'x': [1, 2, 3, 4, 5],
          'y1': [2, 4, 6, 8, 10],
          'y2': [3, 5, 7, 9, 11],
          'y3': [4, 6, 8, 10, 12]})


plt.figure(figsize=(10,6))
plt.plot(df['x'], df['y1'], label='y1')
plt.plot(df['x'], df['y2'], label='y2')
plt.plot(df['x'], df['y3'], label='y3')
plt.xlabel('x')
plt.ylabel('y')
plt.title('График зависимости y от x')
plt.legend()
plt.show()
