def print_error_operation():
    print("The operation cannot be performed.")


def get_matrix_from_input(matrix_size: []):
    print('Enter matrix:')
    matrix = []
    rows, cols = matrix_size
    for _ in range(rows):
        row = [float(x) for x in input().split()]
        matrix.append(row)
    return Matrix(matrix)


class Matrix:

    def __init__(self, matrix=None):
        if matrix is None:
            matrix = []
        self.matrix = matrix
        if len(matrix) != 0:
            self.rows, self.cols = len(matrix), len(matrix[0])
        else:
            self.rows, self.cols = 0, 0

    def matrix_add(self, second_matrix):
        result_matrix = []
        if self.check_matrix_add(second_matrix):
            for i in range(self.rows):
                result_row = [self.matrix[i][x] + second_matrix.matrix[i][x] for x in range(self.cols)]
                result_matrix.append(result_row)
            result_matrix = Matrix(result_matrix)
        else:
            print_error_operation()
        return result_matrix

    def check_matrix_add(self, matrix_to_add):
        return self.rows == matrix_to_add.rows and self.cols == matrix_to_add.cols

    def check_matrix_multiplication(self, matrix_to_multiplication):
        return self.cols == matrix_to_multiplication.rows

    def multiplication_by_number(self, number):
        result_matrix = []
        for i in range(self.rows):
            row = [x * number for x in self.matrix[i]]
            result_matrix.append(row)
        return Matrix(result_matrix)

    def multiplication_by_matrix(self, matrix):
        result_matrix = []
        if self.check_matrix_multiplication(matrix):
            for i in range(self.rows):
                row = []
                for j in range(matrix.cols):
                    row.append(sum(list(map(multiplication, zip(self.matrix[i], [x[j] for x in matrix.matrix])))))
                result_matrix.append(row)
            result_matrix = Matrix(result_matrix)
        else:
            print_error_operation()
        return result_matrix

    def print_matrix(self):
        print('The result is:')
        [print(*[x for x in row]) for row in self.matrix]
        # print([round(x, 2) for row in self.matrix for x in row])

    def perform_transpose(self, type_='', type_int=0):
        result_matrix = Matrix()
        if type_ == 'main' or type_int == 1:
            result_matrix = self.main_transpose()
        elif type_ == 'side' or type_int == 2:
            result_matrix = self.side_transpose()
        elif type_ == 'vertical' or type_int == 3:
            result_matrix = self.vertical_transpose()
        elif type_ == 'horizontal' or type_int == 4:
            result_matrix = self.horizontal_transpose()
        return result_matrix

    def main_transpose(self):
        return Matrix([list(x) for x in zip(*self.matrix)])

    def side_transpose(self):
        matrix = self.matrix
        matrix.reverse()
        matrix = [list(x) for x in zip(*matrix)]
        matrix.reverse()
        return Matrix(matrix)

    def vertical_transpose(self):
        matrix = self.matrix
        for row in matrix:
            row.reverse()
        return Matrix(matrix)

    def horizontal_transpose(self):
        matrix = self.matrix
        matrix.reverse()
        return Matrix(matrix)

    def get_co_matrix(self):
        matrix = self.matrix
        co_matrix = []
        for row in range(self.rows):
            co_matrix_row = []
            for col in range(self.cols):
                co_matrix_row.append(pow(-1, row + col) * get_determinant(get_submatrix(matrix, row, col)))
            co_matrix.append(co_matrix_row)
        return Matrix(co_matrix).perform_transpose('main')


def get_submatrix(matrix, row, col):
    result_matrix = []
    rows, cols = len(matrix), len(matrix[0])
    for index_row in range(rows):
        if row != index_row:
            matrix_result_row = []
            for index_col in range(cols):
                if col != index_col:
                    matrix_result_row.append(matrix[index_row][index_col])
            result_matrix.append(matrix_result_row)
    return result_matrix


def get_determinant(matrix: [[]]):
    # wrong case
    if not matrix or len(matrix) != len(matrix[0]):
        print("The matrix must be quadratic!")
        return False
    determinant = 0
    # The only element
    if len(matrix) == 1:
        return matrix[0][0]
    # base statement
    if len(matrix) == 2:
        determinant = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    # recursive statement
    else:
        for col in range(len(matrix[0])):
            determinant += matrix[0][col] * pow(-1, col + 2) * get_determinant(get_submatrix(matrix, 0, col))
    return determinant


def multiplication(numbers):
    result = 1
    for x in numbers:
        result *= x
    return result


def print_menu():
    print('1. Add matrices\n' +
          '2. Multiply matrix by a constant\n' +
          '3. Multiply matrices\n' +
          '4. Transpose matrix\n' +
          '5. Calculate a determinant\n' +
          '6. Inverse matrix\n' +
          '0. Exit\n')


def print_transpose_menu():
    print('1. Main diagonal\n' +
          '2. Side diagonal\n' +
          '3. Vertical line\n' +
          '4. Horizontal line\n')


def get_matrix_size():
    return [int(x) for x in input('Enter size of matrix:').split()]


while True:
    print_menu()
    choice = int(input('Your choice: '))
    if choice == 0:
        exit('Bye!')
    elif choice == 1:
        size = get_matrix_size()
        matrix_add_1 = get_matrix_from_input(size)
        size = get_matrix_size()
        matrix_add_2 = get_matrix_from_input(size)
        matrix_sum = matrix_add_1.matrix_add(matrix_add_2)
        if matrix_sum:
            matrix_sum.print_matrix()
    elif choice == 2:
        size = get_matrix_size()
        matrix_to_perform = get_matrix_from_input(size)
        constant = int(input())
        matrix_to_perform.multiplication_by_number(constant).print_matrix()
    elif choice == 3:
        size = get_matrix_size()
        matrix_1 = get_matrix_from_input(size)
        size = get_matrix_size()
        matrix_2 = get_matrix_from_input(size)
        matrix_result = matrix_1.multiplication_by_matrix(matrix_2)
        if matrix_result:
            matrix_result.print_matrix()
    elif choice == 4:
        print_transpose_menu()
        type_transpose = int(input('Your choice: '))
        size = get_matrix_size()
        matrix_to_perform = get_matrix_from_input(size)
        matrix_to_perform.perform_transpose(type_int=type_transpose).print_matrix()
    elif choice == 5:
        size = get_matrix_size()
        matrix_to_perform = get_matrix_from_input(size)
        determinant = get_determinant(matrix_to_perform.matrix)
        if determinant:
            print(determinant)
    elif choice == 6:
        size = get_matrix_size()
        matrix_to_perform = get_matrix_from_input(size)
        matrix_to_perform \
            .get_co_matrix() \
            .multiplication_by_number(1 / get_determinant(matrix_to_perform.matrix)) \
            .print_matrix()
