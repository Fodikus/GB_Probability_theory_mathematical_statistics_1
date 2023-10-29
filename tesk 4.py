import matplotlib.pyplot as plt
from math import factorial

def combinatorics(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k))) 

### Создание области отрисовки
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.set_axis_off()

formula = 'Задача 4. \n'
formula = formula + 'В лотерее 100 билетов. \n'
formula = formula + 'Из них 2 выигрышных. \n'
formula = formula + 'Какова вероятность того, что 2 приобретенных билета окажутся выигрышными? \n'
formula = formula + 'Необходиом использовать формулу сочетания комбинаторики \n'
formula = formula + '$\\ C^k_n = \\frac{n!}{k!\\left(n-k\\right)!}  $\n'
formula = formula + 'и классическую формулу вероятности. \n'
formula = formula + '$\\ P(A) = \\frac{m}{n} $\n'
formula = formula + 'Из-за того, что билет достаются одновременно, порядок не важен  \n'
formula = formula + 'm количество благоприятных исходов равна 1, выйгрышному билету \n'
formula = formula + '$\\ m : \\ {1} $ \n'
formula = formula + 'а n количество сочетаний 2-х билетов из 100. \n'
formula = formula + '$\\ n : \\ C^k_n = С^{2}_{100} $\n'
formula = formula + '\n'

# Вычислим  m
m = combinatorics(1, 1)
formula = formula + 'Вычислим  m:\n'
formula = formula + 'm=' + str(m) + '\n'

# Вычислим  n
n = combinatorics(100, 2)
formula = formula + 'Вычислим  n:\n'
formula = formula + 'n=' + str(n) + '\n'

# Вычислим  P
P = m / n
formula = formula + 'Вычислим  P:\n'
formula = formula + 'P=' + str(round(P,4)) + '\n'

# Ответ
result = P * 100
formula = formula + 'Вероятность того, что оба приобретенных билета окажутся выигрышными:\n'
formula = formula + 'P=' + str(round(result,2)) + '%'

### Отрисовка формулы
t = ax.text(0.5, 0.5, formula,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=20, color='black')
  
### Определение размеров формулы
ax.figure.canvas.draw()
bbox = t.get_window_extent()
bbox.width, bbox.height

# Установка размеров области отрисовки dpi=80
fig.set_size_inches(bbox.width/80,bbox.height/80)

### Отрисовка или сохранение формулы в файл
plt.show()


