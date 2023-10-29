import matplotlib.pyplot as plt
from math import factorial

def combinatorics(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k))) 

### Создание области отрисовки
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.set_axis_off()

formula = 'Задача 3. \n'
formula = formula + 'В ящике имеется 15 деталей, из которых 9 окрашены. \n'
formula = formula + 'Рабочий случайным образом извлекает 3 детали. \n'
formula = formula + 'Какова вероятность того, что все извлеченные детали окрашены? \n'
formula = formula + 'Необходиом использовать формулу сочетания комбинаторики \n'
formula = formula + '$\\ C^k_n = \\frac{n!}{k!\\left(n-k\\right)!}  $\n'
formula = formula + 'и классическую формулу вероятности. \n'
formula = formula + '$\\ P(A) = \\frac{m}{n} $\n'
formula = formula + 'm количество благоприятных исходов, извлечений 3-х окрашенных деталей из 9 \n'
formula = formula + '$\\ m : \\ C^k_n = С^{3}_{9} $ \n'
formula = formula + 'а n количество сочетаний 3-х деталей из 15. \n'
formula = formula + '$\\ n : \\ C^k_n = С^{3}_{15} $\n'
formula = formula + '\n'

# Вычислим  m
m = combinatorics(9, 3)
formula = formula + 'Вычислим  m:\n'
formula = formula + 'm=' + str(m) + '\n'

# Вычислим  n
n = combinatorics(15, 3)
formula = formula + 'Вычислим  n:\n'
formula = formula + 'n=' + str(n) + '\n'

# Вычислим  P
P = m / n
formula = formula + 'Вычислим  P:\n'
formula = formula + 'P=' + str(round(P,4)) + '\n'

# Ответ
result = P * 100
formula = formula + 'Вероятность того, что все извлеченные детали окрашены:\n'
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


