import pickle
import numpy as np

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

with open("matrix.pkl", "wb") as file:
    pickle.dump(matrix, file)

with open("matrix.pkl", "rb") as file:
    loaded_matrix = pickle.load(file)

print(loaded_matrix)


def calculate_determinant(matrix):
    np_matrix = np.array(matrix)

    if np_matrix.shape[0] != np_matrix.shape[1]:
        raise ValueError("Матрица не является квадратной")

    determinant = np.linalg.det(np_matrix)
    return determinant


with open("matrix.pkl", "rb") as file:
    matrix = pickle.load(file)

determinant = calculate_determinant(matrix)
print(f"Определитель матрицы:\n{determinant}")
