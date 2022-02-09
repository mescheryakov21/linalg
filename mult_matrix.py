import numpy as np

def multi_matrix (matrix_a, matrix_b,d):
    k = 0
    mult_arr = []
    etap_1 = []
    for ii in matrix_a:
        eff = 0
        for jj in (matrix_b.T):
            if k < d:
                eff = eff + ii[k]*jj[k]
                k += 1
            etap_1.append(eff)
        mult_arr.append(etap_1)
    return mult_arr

matrix_a = np.array([[1,2,3],[4,5,6]])
matrix_b = np.array([[7,8,9],[1,1,1],[2,2,3]])
a = np.shape(matrix_a)
b = np.shape(matrix_b)
if a[1] == b[0]:
    print(multi_matrix(matrix_a, matrix_b, a[1]))
else:
    print("Такая операция не возможна")

