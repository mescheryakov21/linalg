import numpy as np

def multi_matrix (matrix_a, matrix_b,d):
    """
    Функция для произведения матриц
    Принимает: две матрицы и количество столбцов первой матрицы
    Возвращает матрица скалярного произведения
    """
    mult_arr = []
    for ii in matrix_a:  # берем строки одной матрицы
        etap_1 = []
        for jj in (matrix_b.T):  # берем столбцы второй матрицы, для этого транспонируем
            eff = 0
            k = 0
            while k < d:
                eff = eff + ii[k]*jj[k]
                k += 1
            etap_1.append(eff)    # соединение суммы произведений по элементно в вектор
        mult_arr.append(etap_1)   # соединение векторов в матрицу
    return mult_arr

matrix_a = np.array([[1,2,3],[4,5,6]])
matrix_b = np.array([[7,8,9],[1,1,1],[2,2,3]])
a = np.shape(matrix_a)  # определяем размерность матриц для возможности произведения
b = np.shape(matrix_b)
if a[1] == b[0]:
    print(multi_matrix(matrix_a, matrix_b, a[1]))
else:
    print("Такая операция не возможна")

