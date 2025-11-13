from sys import stdin
import sys

sys.set_int_max_str_digits(100000)

class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, matrix):
        self.matrix = []
        for row in matrix:
            new_row = []
            for item in row:
                new_row.append(item)
            self.matrix.append(new_row)

    def __str__(self):
        rows = []
        for row in self.matrix:
            rows.append("\t".join(map(str, row)))
        return "\n".join(rows)

    def size(self):
        return len(self.matrix), len(self.matrix[0])

    def __add__(self, other):
        if self.size() != other.size():
            raise MatrixError(self, other)

        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[i])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)

        return Matrix(result)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = []
            for row in self.matrix:
                new_row = [item * other for item in row]
                result.append(new_row)
            return Matrix(result)
        elif isinstance(other, Matrix):
            rows_self, cols_self = self.size()
            rows_other, cols_other = other.size()

            if cols_self != rows_other:
                raise MatrixError(self, other)

            result = []
            for i in range(rows_self):
                row = []
                for j in range(cols_other):
                    total = 0
                    for k in range(cols_self):
                        total += self.matrix[i][k] * other.matrix[k][j]
                    row.append(total)
                result.append(row)

            return Matrix(result)

    __rmul__ = __mul__

    def transpose(self):
        rows, cols = self.size()
        transposed = []
        for j in range(cols):
            new_row = []
            for i in range(rows):
                new_row.append(self.matrix[i][j])
            transposed.append(new_row)

        self.matrix = transposed
        return self

    @staticmethod
    def transposed(matrix):
        rows, cols = matrix.size()
        transposed = []
        for j in range(cols):
            new_row = []
            for i in range(rows):
                new_row.append(matrix.matrix[i][j])
            transposed.append(new_row)

        return Matrix(transposed)

    def solve(self, vector):
        rows, cols = self.size()

        A = [row[:] for row in self.matrix]
        b = vector[:]

        for i in range(rows):
            max_row = i
            for k in range(i + 1, rows):
                if abs(A[k][i]) > abs(A[max_row][i]):
                    max_row = k

            A[i], A[max_row] = A[max_row], A[i]
            b[i], b[max_row] = b[max_row], b[i]

            for k in range(i + 1, rows):
                factor = A[k][i] / A[i][i]
                b[k] -= factor * b[i]
                for j in range(i, rows):
                    A[k][j] -= factor * A[i][j]

        x = [0] * rows
        for i in range(rows - 1, -1, -1):
            x[i] = b[i]
            for j in range(i + 1, rows):
                x[i] -= A[i][j] * x[j]
            x[i] /= A[i][i]

        return x


class SquareMatrix(Matrix):
    def __init__(self, matrix):
        super().__init__(matrix)
        rows, cols = self.size()

    def __pow__(self, power):
        if power == 0:
            n = self.size()[0]
            identity = []
            for i in range(n):
                row = []
                for j in range(n):
                    if i == j:
                        row.append(1)
                    else:
                        row.append(0)
                identity.append(row)
            return SquareMatrix(identity)

        result = None
        base = self
        while power > 0:
            if power % 2 == 1:
                if result is None:
                    result = base
                else:
                    result = result * base
            base = base * base
            power //= 2

        return result

exec(stdin.read())