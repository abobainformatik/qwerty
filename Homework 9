import numpy as np
import matplotlib.pyplot as plt

def f(x, alpha, beta):
    return alpha * x*2 + beta * x

x = np.linspace(-10, 10, 1000)

# Задача 1
fig, ax = plt.subplots(figsize=(10,6))

ax.plot (x, f(x, 1, 1), color='blue', label='alpha=1, 
beta=1')
ax.plot (x, f(x, 2, 1), color='green', label='alpha=2, 
beta=1')
ax.plot(x, f(x, 1, 2), color='red', label='alpha=1, 
beta=2')

ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Графики функции f(x) для разных значений 
alpha и 
beta')
ax.legend
ax.grid

plt.savefig('task1.svg', format='svg')

# Задача 2
fig, ax = plt.subplots(figsize=(10,6))

ax.plot(x, f(x, 1, 1), color='blue', label='alpha=1, 
beta=1')
ax.plot(x, f(x, 2, 1), color='green', label='alpha=2, 
beta=1')
ax.plot(x, f(x, 1, 2), color='red', label='alpha=1, 
beta=2')

ax2 = ax.twinx
ax2.plot(x[x>0], f(x[x>0], 1, 1), color='blue', linestyle='dashed')
ax2.plot(x[x>0], f(x[x>0], 2, 1), color='green', linestyle='dashed')
ax2.plot(x[x>0], f(x[x>0], 1, 2), color='red', linestyle='dashed')

ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax2.set_ylabel('f(x) для x>0')
ax.set_title('Графики функции f(x) для x>0')
ax.legend
ax2.legend
ax.grid

plt.savefig('task2.svg', format='svg')


# Задача 3
fig, ax = plt.subplots(figsize=(10,6))

ax.plot(x, f(x, 1, 1), color='blue', label='alpha=1, 
beta=1')
ax.plot(x, f(x, 2, 1), color='green', label='alpha=2, 
beta=1')
ax.plot(x, f(x, 1, 2), color='red', label='alpha=1, 
beta=2')

ax2 = ax.twinx
ax2.plot(x[x<0], f(x[x<0], 1, 1), color='blue', linestyle='dashed')
ax2.plot(x[x<0], f(x[x<0], 2, 1), color='green', linestyle='dashed')
ax2.plot(x[x<0], f(x[x<0], 1, 2), color='red', linestyle='dashed')
ax2.plot(x[x<0], np.zeros(len(x[x<0])), color='black', linestyle='dotted')

ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax2.set_ylabel('f(x) для x<0')
ax.set_title('Графики функции f(x) для x<0')
ax.legend
ax2.legend
ax.grid

plt.savefig('task3.svg', format='svg')


# Задача 4
fig, axs = plt.subplots(1, 3, figsize=(18,6), sharey=True)

# График 1
ax = axs[0]
ax.plot(x, f(x, 1, 0), color='blue', linestyle='dashed', label='alpha=1, 
beta=0')
ax.plot(x, f(x, 1, -1), color='red', linestyle='dashed', label='alpha=1, 
beta=-1')
ax.plot(x, f(x, 1, 0.5), color='green', label='alpha=1, 
beta=0.5')
ax.plot(x, f(x, 1, 0.8), color='purple', label='alpha=1, 
beta=0.8')
ax.legend

# График 2
ax = axs[1]
ax.plot(x, f(x, 1, 0), color='blue', linestyle='dashed', label='alpha=1, 
beta=0')
ax.plot(x, f(x, 1, -1), color='red', linestyle='dashed', label='alpha=1, 
beta=-1')
ax.plot(x, f(x, 1, -0.5), color='green', label='alpha=1, 
beta=-0.5')
ax.plot(x, f(x, 1, -0.8), color='purple', label='alpha=1, 
beta=-0.8')
ax.legend

# График 3
ax = axs[2]
ax.plot(x, f(x, 1, 0), color='blue', linestyle='dashed', label='alpha=1, 
beta=0')
ax.plot(x, f(x, 1, -1), color='red', linestyle='dashed', label='alpha=1, 
beta=-1')
ax.plot(x, f(x, 1, -1.5), color='green', label='alpha=1, 
beta=-1.5')
ax.plot(x, f(x, 1, -2.5), color='purple', label='alpha=1, 
beta=-2.5')
ax.legend

for ax in axs:
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.grid

plt.suptitle('Графики функции f(x) для разных значений 
alpha и 
beta')
plt.savefig('task4.svg', format='svg')


“
