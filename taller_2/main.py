import numpy as np

if __name__ == '__main__':
    a = np.array([[1, 3, 5, 8], [2, 6, 5, 3], [4, 1, 9, 7], [1, 8, 0 ,2]])
    b = np.array([[1, 9, 5, 8], [12, 5, 5, 9], [4, 2, 9, 74], [0, 6, 0 ,3]])
    c = np.array([[1, 9], [10, 2]])
    print("Matrix a", a)
    print("Matrix b", b)
    print("Matrix c", c)

    print("Matrix 3*a", 3*a)
    print("Matrix a-7", a-7)
    print("Transposed matrix (a*b)", (a.dot(b)).transpose())
    print("Inverse matrix a", np.linalg.inv(a))
    print("Inverse matrix b", np.linalg.inv(b))