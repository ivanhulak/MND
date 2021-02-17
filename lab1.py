# Гулак Іван
# Варіант - 304 ( Уэт<-- )
import random

# Задаю будь-які а
a0, a1, a2, a3 = 7, 11, 4, 2

x1, x2, x3 = [], [], []
xn1, xn2, xn3 = [], [], []
y = []

# Формую масиви х1, х2, х3
for i in range(8):
    x1.append(random.randint(0, 20))
    x2.append(random.randint(0, 20))
    x3.append(random.randint(0, 20))

print(f"x1 = {x1}")
print(f"x2 = {x2}")
print(f"x3 = {x3}\n")

# Вибираю мінімальне значення
x1_min = min(x1)
x2_min = min(x2)
x3_min = min(x3)

# Вибираю максимальне значення
x1_max = max(x1)
x2_max = max(x2)
x3_max = max(x3)

# Знаходжу х0
x01 = (x1_max + x1_min)/2
x02 = (x2_max + x2_min)/2
x03 = (x3_max + x3_min)/2

# обчислюю інтервал зміни фактора dx
dx1 = x1_max - x01
dx2 = x2_max - x02
dx3 = x3_max - x03

# Знаходжу нормоване значення Хн для кожного фактора
for i in range(len(x1)):
    xn1.append(round(((x1[i] - x01) / dx1), 3))
    xn2.append(round(((x2[i] - x02) / dx2), 3))
    xn3.append(round(((x3[i] - x03) / dx3), 3))

print(f"xn1 = {xn1}")
print(f"xn2 = {xn2}")
print(f"xn3 = {xn3}")

# Вивожу на екран всі значення
print(f"\na0 = {a0} \na1 = {a1} \na2 = {a2} \na3 = {a3}")
print(f"\nx01 = {x01} \nx02 = {x02} \nx03 = {x03}")
print(f"\ndx1 = {dx1} \ndx2 = {dx2} \ndx3 = {dx3}")

# Шукаю уі
for i in range(len(x1)):
    y.append(a0 + a1 * x1[i] + a2 * x2[i] + a3 * x3[i])
print(f"\ny = {y}\n")

# Шукаю у еталонне по формулі, яка дана в лабораторній роботі
y_etalon = a0 + a1 * x01 + a2 * x02 + a3 * x03
print(f"Еталонне значення: y_etalon = {y_etalon}")

# Шукаю у еталонне зверху ( Уэт<-- )
arr = []
for i in range(len(y)):
    arr.append(y[i] - y_etalon)
print(arr)
new_arr = []
for i in range(len(arr)):
    if arr[i] >= 0:
        new_arr.append(arr[i])
print(new_arr)
res = y_etalon + min(new_arr)
print(f"res ( Yэт<-- ) = {res}\n")

# Додаткове завдання ( --> Y`, де Y` - середнє Y )
print("-" * 30)
average_y = round(sum(y)/len(y))
print(f"Середнє значення: average_y = {average_y}")

# Шукаю у середнє 'знизу'
arr = []
for i in range(len(y)):
    arr.append(y[i] - average_y)

new_arr = []
for i in range(len(arr)):
    if arr[i] <= 0:
        new_arr.append(arr[i])

result = average_y + max(new_arr)
print(f"result ( --> Y`, де Y` - середнє Y ) = {result}")
