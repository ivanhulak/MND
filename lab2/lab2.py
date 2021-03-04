# Гулак Іван ІВ-93 Варіант - 304
import random
import math
# Вхідні дані
variant = 304
m = 6

y_max = (30 - variant) * 10
y_min = (20 - variant) * 10

x1_min = 15
x1_max = 45
x2_min = 30
x2_max = 80

xn = [[-1, -1], [1, -1], [-1, 1]]

y = [[random.randint(y_min, y_max) for i in range(6)] for j in range(3)]
print(f'Матриця планування при m = {m}')
for i in range(3):
    print(y[i])
print("-" * 50)


# -------------   Функції, використані для обчислень в програмі   -----------------
def average_y(arr):
    average_ny = []
    for i in arr:
        average_ny.append(round(sum(i)/len(i), 2))
    return average_ny


def dispersion(counting_list):
    d = []
    for i in range(len(counting_list)):
        sum_of_y = 0
        for k in counting_list[i]:
            sum_of_y += (k - average_y(counting_list)[i]) ** 2
        d.append(round(sum_of_y / len(counting_list[i]), 2))
    return d


def f_uv(u, v):
    if u >= v:
        return u / v
    else:
        return v / u


def determinant(x11, x12, x13, x21, x22, x23, x31, x32, x33):
    det = x11 * x22 * x33 + x12 * x23 * x31 + x32 * x21 * x13 - x13 * x22 * x31 - x32 * x23 * x11 - x12 * x21 * x33
    return det
# ----------------------------------------------------------------------------------------------------------------

# Перевіримо однорідність дисперсії за критерієм Романовського:
# 1) Знайдемо середнє значення функції відгуку в рядку:
avg_y = average_y(y)
print(f"Середнє значення функції відгуку в рядку (avg_y): {avg_y}")


# 2) Знайдемо дисперсії по рядках:
print("Дисперсії по рядках")
print(f"d(y1): {dispersion(y)[0]}")
print(f"d(y2): {dispersion(y)[1]}")
print(f"d(y3): {dispersion(y)[2]}")


# 3) Обчислимо основне відхилення:
sigma_tetta = round(math.sqrt((2 * (2 * m - 2)) / (m * (m - 4))), 2)
print(f"Основне відхилення (tetta): {sigma_tetta}")


# 4) Обчислимо Fuv:
fuv = []
fuv.append(f_uv(dispersion(y)[0], dispersion(y)[1]))
fuv.append(f_uv(dispersion(y)[2], dispersion(y)[0]))
fuv.append(f_uv(dispersion(y)[2], dispersion(y)[1]))
print(f"Fuv: {fuv}")


# 5) Обчислимо Tetta:
tetta = []
tetta.append(((m - 2) / m) * fuv[0])
tetta.append(((m - 2) / m) * fuv[1])
tetta.append(((m - 2) / m) * fuv[2])


# 6) Обчислимо Ruv:
ruv = []
ruv.append(abs(tetta[0] - 1) / sigma_tetta)
ruv.append(abs(tetta[1] - 1) / sigma_tetta)
ruv.append(abs(tetta[2] - 1) / sigma_tetta)

# 7) Перевіримо на однорідність дисперсію
r_kr = 2
for i in range(len(ruv)):
    if ruv[i] > r_kr:
        print("Неоднорідна дисперсія")


# 8) Розрахунок нормованих коефіцієнтів рівняння регресії
mx1 = (xn[0][0] + xn[1][0] + xn[2][0]) / 3
mx2 = (xn[0][1] + xn[1][1] + xn[2][1]) / 3
my = sum(avg_y) / 3

a1 = (xn[0][0] ** 2 + xn[1][0] ** 2 + xn[2][0] ** 2) / 3
a2 = (xn[0][0] * xn[0][1] + xn[1][0] * xn[1][1] + xn[2][0] * xn[2][1]) / 3
a3 = (xn[0][1] ** 2 + xn[1][1] ** 2 + xn[2][1] ** 2) / 3

a11 = (xn[0][0] * avg_y[0] + xn[1][0] * avg_y[1] + xn[2][0] * avg_y[2]) / 3
a22 = (xn[0][1] * avg_y[0] + xn[1][1] * avg_y[1] + xn[2][1] * avg_y[2]) / 3

b0 = determinant(my, mx1, mx2, a11, a1, a2, a22, a2, a3) / determinant(1, mx1, mx2, mx1, a1, a2, mx2, a2, a3)
b1 = determinant(1, my, mx2, mx1, a11, a2, mx2, a22, a3) / determinant(1, mx1, mx2, mx1, a1, a2, mx2, a2, a3)
b2 = determinant(1, mx1, my, mx1, a1, a11, mx2, a2, a22) / determinant(1, mx1, mx2, mx1, a1, a2, mx2, a2, a3)

print(f"b0: {b0}")
print(f"b1: {b1}")
print(f"b2: {b2}")


# Отже, нормовані рівняння регресії
y_pr1 = b0 + b1 * xn[0][0] + b2 * xn[0][1]
y_pr2 = b0 + b1 * xn[1][0] + b2 * xn[1][1]
y_pr3 = b0 + b1 * xn[2][0] + b2 * xn[2][1]


# Проведемо натуралізацію коефіцієнтів:
dx1 = abs(x1_max - x1_min) / 2
dx2 = abs(x2_max - x2_min) / 2
x10 = (x1_max + x1_min) / 2
x20 = (x2_max + x2_min) / 2

a_0 = b0 - (b1 * x10 / dx1) - (b2 * x20 / dx2)
a_1 = b1 / dx1
a_2 = b2 / dx2

# Запишемо натуралізоване рівняння регресії:
yP1 = a_0 + a_1 * x1_min + a_2 * x2_min
yP2 = a_0 + a_1 * x1_max + a_2 * x2_min
yP3 = a_0 + a_1 * x1_min + a_2 * x2_max


print('Експериментальні значення критерію Романовського:')
for i in range(3):
    print(ruv[i])

print('Натуралізовані коефіцієнти: \na0 =', round(a_0, 4), 'a1 =', round(a_1, 4), 'a2 =', round(a_2, 4))
print('У практичний: ', round(y_pr1, 4), round(y_pr2, 4), round(y_pr3, 4))
print('У середній:', round(avg_y[0], 4), round(avg_y[1], 4), round(avg_y[2], 4))
print('У практичний норм.', round(yP1, 4), round(yP2, 4), round(yP3, 4))
