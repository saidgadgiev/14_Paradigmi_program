import numpy as np


def pearson_correlation(x, y):
    correlation_matrix = np.corrcoef(x, y)
    correlation_coefficient = correlation_matrix[0, 1]
    return correlation_coefficient


# Пример данных
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

correlation = pearson_correlation(x, y)
print("Корреляция Пирсона:", correlation)
