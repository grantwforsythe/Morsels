
matrix1 = [[1, 1], [1, 1]]
matrix2 = [[2, 2], [2, 2]]
matrix3 = [[]]

def add(*args):
    matrix_shape = {
        tuple(len(r) for r in matrix)
        for matrix in args
    }
 
    if len(matrix_shape) > 1:
        raise ValueError("Given matrices are not the same size.")

    return [
        [sum(values) for values in zip(*rows)]
        for rows in zip(*args)
    ]

if __name__ == '__main__':
    print(add(matrix1, matrix2))

    names = 'bob julian grant sara'.split()
    ages = '11 22 33 44'.split()
    print(dict(zip(names, ages)))
    # print(dict(*names, *ages))
