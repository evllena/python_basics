class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join([str(num) for num in line]) for line in self.matrix)

    def __add__(self, other):
        try:
            res = [[int(self.matrix[line][num]) + int(other.matrix[line][num]) for  num in range(len(self.matrix[line]))]
                for line in range(len(self.matrix))]
            return Matrix(res)
        except IndexError:
            return f"Ошибка! Матрицы должны быть одинакового размера"


matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print(f"This is how matrix1 looks like:\n{matrix1}", end='\n\n')
print(f"This is how matrix2 looks like:\n{matrix2}", end='\n\n')
print(f"This is how matrix1 + matrix2 looks like:\n{matrix1 + matrix2}")