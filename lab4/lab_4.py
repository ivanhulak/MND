# Гулак Іван ІВ-93 Варіант - 304
import random
import copy
import math
from tabulate import tabulate
from scipy.stats import f, t


def make_experiment(m=3):
    def dispersion(y_list, avg_y_list, m):
        Sy = []
        elem = 0
        for i in range(N):
            for j in range(m):
                elem += (y_list[i][j] - avg_y_list[i]) ** 2
            Sy.append(elem / m)
            elem = 0
        kar = [round(i, 2) for i in Sy]
        print(kar)
        return kar

    def r(floatNumber):
        return round(floatNumber, 2)

    def str_y():
        return 'y = {} + ({}) * x1 + ({}) * x2 + ({}) * x3 + ({}) * x1x2 + ({}) * x1x3 + ({}) * x2x3 + ({}) * x1x2x3'

    def cochrane_criterion(Sy):
        print("\n=================Cochren test=================\n")
        Gp = max(Sy) / sum(Sy)
        q = 0.05
        q_ = q / f2
        chr = f.ppf(q=1 - q_, dfn=f1, dfd=(f2 - 1) * f1)
        Gt = chr / (chr + f2 - 1)
        print("Cochren test: Gr = " + str(round(Gp, 3)))
        if Gp < Gt:
            print("Dispersions are homogeneous with a probability of 95%.")
            pass
        else:
            print("\nDispersions are homogeneous.\nConduct an experiment for m+=1\n")
            make_experiment(4)

    def student_criterion(Sy, d):
        print("\n=================Student's test=================\n")
        bettaList = [sum([Sy[i] * x0[0] for i in range(N)]) / N,
                     sum([Sy[i] * x1i[i] for i in range(N)]) / N,
                     sum([Sy[i] * x2i[i] for i in range(N)]) / N,
                     sum([Sy[i] * x3i[i] for i in range(N)]) / N,
                     sum([Sy[i] * xFactors12Norm[i] for i in range(N)]) / N,
                     sum([Sy[i] * xFactors13Norm[i] for i in range(N)]) / N,
                     sum([Sy[i] * xFactors23Norm[i] for i in range(N)]) / N,
                     sum([Sy[i] * xFactors123Norm[i] for i in range(N)]) / N]
        bettaList = [round(i, 2) for i in bettaList]

        tList = [bettaList[i] * S for i in range(N)]

        for i in range(N):
            if tList[i] < t.ppf(q=0.975, df=f3):
                bList[i] = 0
                d -= 1
                print('Exclude from the equation the coefficient b' + str(i))
        print("\n=================The resulting equation=================")
        print(str_y().format(r(bList[0]), r(bList[1]), r(bList[2]), r(bList[3]), r(bList[4]), r(bList[5]), r(bList[6]),
                             r(bList[7])))

    def fisher_criterion(d):
        print("\n=================Fisher's criterion=================")
        f4 = N - d
        S_ad = (m * sum(
            [(bList[0] + bList[1] * x1i[i] + bList[2] * x2i[i] + bList[3] * x3i[i] + bList[4] * xFactors12Norm[i] +
              bList[5] * xFactors13Norm[i] + bList[6] * xFactors23Norm[i] + bList[7] * xFactors123Norm[i]
              - avgYList[i]) ** 2 for i in range(N)]) / f4)
        Fp = S_ad / Sb

        if Fp > f.ppf(q=0.95, dfn=f4, dfd=f3):  # перевірка за критерієм Фішера з використанням scipy
            print('The regression equation is inadequate to the original at the significance level 0.05.\n Repeat experiment for'
                      'm+1')
            make_experiment(4)
        else:
            print('The regression equation is adequate to the original at the level of significance 0.05')

    def print_matrix():
        print("\n" + "-_-_" * 9 + "Матриця ПФЕ" + "-_-_" * 9 + "\n",
              tabulate([tableHeader,
                        x0 + [xFactors[0][0]] + [xFactors[0][1]] + [xFactors[0][2]] + xFactors12[0] + xFactors13[0] +
                        xFactors23[0] + xFactors123[0] + yList[0] + [avgYList[0]] + [Sy[0]],
                        x0 + [xFactors[1][0]] + [xFactors[1][1]] + [xFactors[1][2]] + xFactors12[1] + xFactors13[1] +
                        xFactors23[1] + xFactors123[1] + yList[1] + [avgYList[1]] + [Sy[1]],
                        x0 + [xFactors[2][0]] + [xFactors[2][1]] + [xFactors[2][2]] + xFactors12[2] + xFactors13[2] +
                        xFactors23[2] + xFactors123[2] + yList[2] + [avgYList[2]] + [Sy[2]],
                        x0 + [xFactors[3][0]] + [xFactors[3][1]] + [xFactors[3][2]] + xFactors12[3] + xFactors13[3] +
                        xFactors23[3] + xFactors123[3] + yList[3] + [avgYList[3]] + [Sy[3]],
                        x0 + [xFactors[4][0]] + [xFactors[4][1]] + [xFactors[4][2]] + xFactors12[4] + xFactors13[4] +
                        xFactors23[4] + xFactors123[4] + yList[4] + [avgYList[4]] + [Sy[4]],
                        x0 + [xFactors[5][0]] + [xFactors[5][1]] + [xFactors[5][2]] + xFactors12[5] + xFactors13[5] +
                        xFactors23[5] + xFactors123[5] + yList[5] + [avgYList[5]] + [Sy[5]],
                        x0 + [xFactors[6][0]] + [xFactors[6][1]] + [xFactors[6][2]] + xFactors12[6] + xFactors13[6] +
                        xFactors23[6] + xFactors123[6] + yList[6] + [avgYList[6]] + [Sy[6]],
                        x0 + [xFactors[7][0]] + [xFactors[7][1]] + [xFactors[7][2]] + xFactors12[7] + xFactors13[7] +
                        xFactors23[7] + xFactors123[7] + yList[7] + [avgYList[7]] + [Sy[7]],
                        ], headers="firstrow", tablefmt="pretty"))

        print("\n" + "-_-_" * 7 + "Нормалізована матриця ПФЕ" + "-_-_" * 7 + "\n",
              tabulate([tableHeader,
                        x0 + [xFactorsNorm[0][0]] + [xFactorsNorm[0][1]] + [xFactorsNorm[0][2]] + [xFactors12Norm[0]] +
                        [xFactors13Norm[0]] + [xFactors23Norm[0]] + [xFactors123Norm[0]] + yList[0] + [avgYList[0]] + [
                            Sy[0]],
                        x0 + [xFactorsNorm[1][0]] + [xFactorsNorm[1][1]] + [xFactorsNorm[1][2]] + [xFactors12Norm[1]] +
                        [xFactors13Norm[1]] + [xFactors23Norm[1]] + [xFactors123Norm[1]] + yList[1] + [avgYList[1]] + [
                            Sy[1]],
                        x0 + [xFactorsNorm[2][0]] + [xFactorsNorm[2][1]] + [xFactorsNorm[2][2]] + [xFactors12Norm[2]] +
                        [xFactors13Norm[2]] + [xFactors23Norm[2]] + [xFactors123Norm[2]] + yList[2] + [avgYList[2]] + [
                            Sy[2]],
                        x0 + [xFactorsNorm[3][0]] + [xFactorsNorm[3][1]] + [xFactorsNorm[3][2]] + [xFactors12Norm[3]] +
                        [xFactors13Norm[3]] + [xFactors23Norm[3]] + [xFactors123Norm[3]] + yList[3] + [avgYList[3]] + [
                            Sy[3]],
                        x0 + [xFactorsNorm[4][0]] + [xFactorsNorm[4][1]] + [xFactorsNorm[4][2]] + [xFactors12Norm[4]] +
                        [xFactors13Norm[4]] + [xFactors23Norm[4]] + [xFactors123Norm[4]] + yList[4] + [avgYList[4]] + [
                            Sy[4]],
                        x0 + [xFactorsNorm[5][0]] + [xFactorsNorm[5][1]] + [xFactorsNorm[5][2]] + [xFactors12Norm[5]] +
                        [xFactors13Norm[5]] + [xFactors23Norm[5]] + [xFactors123Norm[5]] + yList[5] + [avgYList[5]] + [
                            Sy[5]],
                        x0 + [xFactorsNorm[6][0]] + [xFactorsNorm[6][1]] + [xFactorsNorm[6][2]] + [xFactors12Norm[6]] +
                        [xFactors13Norm[6]] + [xFactors23Norm[6]] + [xFactors123Norm[6]] + yList[6] + [avgYList[6]] + [
                            Sy[6]],
                        x0 + [xFactorsNorm[7][0]] + [xFactorsNorm[7][1]] + [xFactorsNorm[7][2]] + [xFactors12Norm[7]] +
                        [xFactors13Norm[7]] + [xFactors23Norm[7]] + [xFactors123Norm[7]] + yList[7] + [avgYList[7]] + [
                            Sy[7]],
                        ], headers="firstrow", tablefmt="pretty"))

    N = 8
    if m == 3:
        tableHeader = ["X0", "X1", "X2", "X3", "X12", "X13", "X23", "X123", "Y1", "Y2", "Y3", "avgY", "S^2"]
    elif m == 4:
        tableHeader = ["X0", "X1", "X2", "X3", "X12", "X13", "X23", "X123", "Y1", "Y2", "Y3", "Y4", "avgY", "S^2"]
    else:
        print("Unsuccessful experiment")

    xMinList = [-20, -20, -20]
    xMaxList = [30, 40, -10]

    avgXMin = sum(xMinList) / len(xMinList)
    avgXMax = sum(xMaxList) / len(xMaxList)

    yMin = 200 + avgXMin
    yMax = 200 + avgXMax

    yList = [[random.randint(int(yMin), int(yMax)) for yi in range(m)] for list_y in range(N)]
    avgYList = [round(sum(yList[i]) / len(yList[i]), 2) for i in range(len(yList))]

    Sy = dispersion(yList, avgYList, m)

    f1 = m - 1
    f2 = N
    f3 = f1 * f2
    d = 4

    Sb = sum(Sy) / N
    S = math.sqrt(Sb / (N * m))

    x0 = [1]
    xFactorsNorm = [[-1, -1, -1],
                    [-1, -1, 1],
                    [-1, 1, -1],
                    [-1, 1, 1],
                    [1, -1, -1],
                    [1, -1, 1],
                    [1, 1, -1],
                    [1, 1, 1]]

    xFactors12Norm = [xFactorsNorm[i][0] * xFactorsNorm[i][1] for i in range(len(xFactorsNorm))]
    xFactors13Norm = [xFactorsNorm[i][0] * xFactorsNorm[i][2] for i in range(len(xFactorsNorm))]
    xFactors23Norm = [xFactorsNorm[i][1] * xFactorsNorm[i][2] for i in range(len(xFactorsNorm))]
    xFactors123Norm = [xFactorsNorm[i][0] * xFactorsNorm[i][1] * xFactorsNorm[i][2] for i in range(len(xFactorsNorm))]

    xFactors = [[-10, -20, 50],
                [-10, -20, 55],
                [-10, 60, 50],
                [-10, 60, 55],
                [50, -20, 50],
                [50, -20, 55],
                [50, 60, 50],
                [50, 60, 55]]

    xFactors12 = [[xFactors[i][0] * xFactors[i][1]] for i in range(len(xFactors))]
    xFactors13 = [[xFactors[i][0] * xFactors[i][2]] for i in range(len(xFactors))]
    xFactors23 = [[xFactors[i][1] * xFactors[i][2]] for i in range(len(xFactors))]
    xFactors123 = [[xFactors[i][0] * xFactors[i][1] * xFactors[i][2]] for i in range(len(xFactors))]

    # Знаходження коефіцієнтів регресії для нормованих факторів ПФЕ
    x1i = [xFactorsNorm[i][0] for i in range(N)]
    x2i = [xFactorsNorm[i][1] for i in range(N)]
    x3i = [xFactorsNorm[i][2] for i in range(N)]

    bList = [0] * 8
    bList[0] = sum(avgYList) / N  # b0
    for i in range(N):
        bList[1] += (avgYList[i] * x1i[i]) / N  # b1
        bList[2] += (avgYList[i] * x2i[i]) / N  # b2
        bList[3] += (avgYList[i] * x3i[i]) / N  # b3
        bList[4] += (avgYList[i] * x1i[i] * x2i[i]) / N  # b12
        bList[5] += (avgYList[i] * x1i[i] * x3i[i]) / N  # b13
        bList[6] += (avgYList[i] * x2i[i] * x3i[i]) / N  # b23
        bList[7] += (avgYList[i] * x1i[i] * x2i[i] * x3i[i]) / N  # b123

    print_matrix()
    print("\n=================Equation=================\n")
    print(str_y().format(r(bList[0]), r(bList[1]), r(bList[2]), r(bList[3]), r(bList[4]), r(bList[5]), r(bList[6]),
                         r(bList[7])))
    cochrane_criterion(Sy)
    student_criterion(Sy, d)
    fisher_criterion(d)


make_experiment()
