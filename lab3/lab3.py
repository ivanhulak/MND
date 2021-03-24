import random
import math


# Лабораторна робота №3
# Виконав Гулак Іван Володимирович  Варіант - 304
# Вхідні дані
x1_min = 15
x1_max = 45
x2_min = 30
x2_max = 80
x3_min = 15
x3_max = 45

gt = 0.7679
m = 3
N = 4
Tf = 2.306
Ft = 4.5

y_max = 200 + (x1_max + x2_max + x3_max) / 3
y_min = 200 + (x1_min + x2_min + x3_min) / 3

# Заповнимо матрицю планування для m = 3.
x1 = [random.randint(x1_min, x1_max + 1) for i in range(4)]
x2 = [random.randint(x2_min, x2_max + 1) for i in range(4)]
x3 = [random.randint(x3_min, x3_max + 1) for i in range(4)]
y1 = [random.randint(int(y_min), int(y_max) + 1) for i in range(4)]
y2 = [random.randint(int(y_min), int(y_max) + 1) for i in range(4)]
y3 = [random.randint(int(y_min), int(y_max) + 1) for i in range(4)]

plan_matrix = [[1, 1, 1, 1],
               [-1, -1, 1, 1],
               [-1, 1, -1, 1],
               [-1, 1, 1, -1]]

# 4) Знайдемо середні значення функції відгуку за рядками:
averageY = [0, 0, 0, 0]
for i in range(0, len(x1)):
    averageY[i] = (y1[i] + y2[i] + y3[i]) / 3
print(f"average_Y: {averageY}")


# Функції для обчислення mx1, mx2, mx3, my, a1, a2, a3, a11, a22, a33, a12 = a21, a13 = a31, a23 = a32
def func_mx(arr, main_arr):
    main_arr.append(sum(arr) / len(arr))


def func_a(arr, main_arr):
    main_arr.append((arr[0] * averageY[0] + arr[1] * averageY[1] + arr[2] * averageY[2] + arr[3] * averageY[3])/len(arr))


def func_aii(arr, main_arr):
    main_arr.append((arr[0]**2 + arr[1]**2 + arr[2]**2 + arr[3]**2) / len(arr))


def func_aij(arr1, arr2, main_arr):
    main_arr.append((arr1[0] * arr2[0] + arr1[1] * arr2[1] + arr1[2] * arr2[2] + arr1[3] * arr2[3])/len(arr1))


mx = []
func_mx(x1, mx)
func_mx(x2, mx)
func_mx(x3, mx)
print(f"MX: {mx}")

my = (averageY[0] + averageY[1] + averageY[2] + averageY[3]) / len(averageY)
print(f"MY: {my}")

a = []
func_a(x1, a)
func_a(x2, a)
func_a(x3, a)
print(f"A: {a}")

a11 = []
func_aii(x1, a11)
print(f"A11: {a11}")

a22 = []
func_aii(x2, a22)
print(f"A22: {a22}")

a33 = []
func_aii(x3, a33)
print(f"A33: {a33}")

a12 = a21 = []
func_aij(x1, x2, a12)
print(f"A12 = A21: {a12}")

a13 = a31 = []
func_aij(x1, x3, a13)
print(f"A13 = A31: {a13}")

a23 = a32 = []
func_aij(x2, x3, a23)
print(f"A23 = A32: {a23}")

r01 = [1, mx[0], mx[1], mx[2]]
r02 = [mx[0], a11[0], a12[0], a13[0]]
r03 = [mx[1], a12[0], a22[0], a32[0]]
r04 = [mx[2], a13[0], a23[0], a33[0]]
temp0 = [r01, r02, r03, r04]
determ = 1*a11[0]*a22[0]*a33[0] + mx[0]*a12[0]*a32[0]*mx[2] + mx[1]*a13[0]*mx[1]*a13[0] + mx[2]*mx[0]*a12[0]*a23[0] - \
         (mx[2]*a12[0]*a12[0]*mx[2] + a13[0]*a22[0]*a13[0]*1 + a23[0]*a32[0]*mx[0]*mx[0] + a33[0]*mx[1]*a11[0]*mx[1])


r11 = [my, mx[0], mx[1], mx[2]]
r12 = [a[0], a11[0], a12[0], a13[0]]
r13 = [a[1], a12[0], a22[0], a32[0]]
r14 = [a[2], a13[0], a23[0], a33[0]]
temp1 = [r11, r12[0], r13[0], r14[0]]
determ1 = my*a11[0]*a22[0]*a33[0] + a[0]*a12[0]*a32[0]*mx[2] + a[1]*a13[0]*mx[1]*a13[0] + a[2]*mx[0]*a12[0]*a23[0] - \
          (a[2]*a12[0]*a12[0]*mx[2] + a13[0]*a22[0]*a13[0]*my + a23[0]*a32[0]*a[0]*mx[0] + a33[0]*a[1]*a11[0]*mx[1])


r21 = [1, my, mx[1], mx[2]]
r22 = [mx[0], a[0], a12[0], a13[0]]
r23 = [mx[1], a[1], a22[0], a32[0]]
r24 = [mx[2], a[2], a23[0], a33[0]]
temp2 = [r21, r22, r23, r24]
determ2 = 1*a[0]*a22[0]*a33[0] + my*a12[0]*a32[0]*mx[2] + mx[1]*a13[0]*mx[1]*a[2] + mx[2]*mx[0]*a[1]*a23[0] - \
          (mx[2]*a[1]*a12[0]*mx[2] + a[2]*a22[0]*a13[0]*1 + a23[0]*a32[0]*my*mx[0] + a33[0]*mx[1]*a[0]*mx[1])


r31 = [1, mx[0], my, mx[2]]
r32 = [mx[0], a11[0], a[0], a13[0]]
r33 = [mx[1], a12[0], a[1], a32[0]]
r34 = [mx[2], a13[0], a[2], a33[0]]
temp3 = [r31, r32, r33, r34]
determ3 = 1*a11[0]*a[1]*a33[0] + mx[0]*a[0]*a32[0]*mx[2] + my*a13[0]*mx[1]*a13[0] + mx[2]*mx[0]*a12[0]*a[2] - \
          (mx[2]*a12[0]*a[0]*mx[2] + a13[0]*a[1]*a13[0]*1 + a[2]*a32[0]*mx[0]*mx[0] + a33[0]*mx[1]*a11[0]*my)


r41 = [1, mx[0], mx[1], my]
r42 = [mx[0], a11[0], a12[0], a[0]]
r43 = [mx[1], a12[0], a22[0], a[1]]
r44 = [mx[2], a13[0], a23[0], a[2]]
temp4 = [r41, r42, r43, r44]
determ4 = 1*a11[0]*a22[0]*a[2] + mx[0]*a12[0]*a[1]*mx[2] + mx[1]*a[0]*mx[1]*a13[0] + my*mx[0]*a12[0]*a23[0] - \
          (mx[2]*a12[0]*a12[0]*my + a13[0]*a22[0]*a[0]*1 + a23[0]*a[1]*mx[0]*mx[0] + a[2]*mx[1]*a11[0]*mx[1])


b = [0, 0, 0, 0]
b[0] = determ1/determ
b[1] = determ2/determ
b[2] = determ3/determ
b[3] = determ4/determ

print("-" * 50)
for i in range(4):
    print(f"b{i}: {b[i]}")
print("-" * 50)

# Запишемо отримане рівняння регресії:
y = []
for i in range(len(x1)):
    y.append(b[0] + b[1] * x1[i] + b[2] * x2[i] + b[3] * x3[i])
    print(f"Y{i+1}: {y[i]}")


dispersiya = [0, 0, 0, 0]
for i in range(0, len(dispersiya)):
    dispersiya[i] = ((y1[i] - averageY[i])**2 + (y2[i] - averageY[i])**2 + (y3[i] - averageY[i])**2)/3
print(f"Dispersiya: {dispersiya}")

print("-" * 80)
print('Перевірка однорідності дисперсії за критерієм Кохрена:')
gp = max(dispersiya) / sum(dispersiya)
if gp < gt:
    print("Дисперсія однорідна")
else:
    print('Дсперсія не однорідна. Потрібно збільшити m')


# Далі оцінимо значимість коефіцієнтів регресії згідно критерію Стьюдента
sb = sum(dispersiya) / len(dispersiya)
sb2_odnoridna = sb / (N * m)
sb_odnoridna = math.sqrt(sb2_odnoridna)

beta = [0, 0, 0, 0]
beta[0] = (averageY[0] * 1 + averageY[1] * 1 + averageY[2] * 1 + averageY[3] * 1) / N
beta[1] = (averageY[0] * (-1) + averageY[1] * (-1) + averageY[2] * 1 + averageY[3] * 1) / N
beta[2] = (averageY[0] * (-1) + averageY[1] * 1 + averageY[2] * (-1) + averageY[3] * 1) / N
beta[3] = (averageY[0] * (-1) + averageY[1] * 1 + averageY[2] * 1 + averageY[3] * (-1)) / N
print(f"Beta: {beta}")

t = []
for i in range(len(beta)):
    t.append(abs(beta[i]) / sb_odnoridna)
print(f"t0: {t}")

print("-" * 80)
print('\nОцінка значимості коефіцієнтів регресії згідно критерію Стьюдента:')
d = 0   # кількість значимих коефіцієнтів
temp = [0, 0, 0, 0]
N = 4
Tf = 2.306

znach_kef = []
ne_znach_kef = []
for i in range(0, N):
    if t[i] <= Tf:
        # print(f"t[{i}] = {t[i]} <= Tf = {Tf} >= b[{i}] = {b[i]} - не значний коефіцієнт")
        ne_znach_kef.append(b[i])
        temp[i] = 0
    else:
        # print(f"t[{i}] = {t[i]} > Tf = {Tf} >= b[{i}] = {b[i]} - значний коефіцієнт")
        znach_kef.append(b[i])
        temp[i] = b[i]
        d += 1

# Додаткове завдання:
# виведіть в консоль які (по номеру) коефіцієнти значимі
# Я виділяю 217 та 218 стрічки, натискаю правою кнопкою миші та вибираю "Execute selection in Python Console"
print(f"значний коефіцієнт: {znach_kef}")
print(f"не значний коефіцієнт: {ne_znach_kef}")

y_2 = []
for i in range(0, N):
    y_2.append(temp[0] + temp[1] * x1[i] + temp[2] * x2[i] + temp[3] * x3[i])
print(f"y_2: {y_2}")


# Критерій Фішера
print("-" * 80)
print("Критерій Фішера")
s_ad = []
tmp = []
kof = m / (N - d)
for i in range(len(y_2)):
    tmp.append((y_2[i] - averageY[i])**2)
s_ad.append(kof * sum(tmp))
print(f"S_ad: {s_ad}")

fp = s_ad[0] / sb2_odnoridna
print(f"Fp: {fp}")
if fp > Ft:
    print("рівняння регресії неадекватно оригіналу при рівні значимості 0.05")
else:
    print("рівняння регресії адекватно оригіналу при рівні значимості 0.05")

print(f"y = {b[0]} + {b[1]} * x1 + {b[2]} * x2 + {b[3]} * x3")
