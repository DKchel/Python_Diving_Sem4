"""
Напишите функцию для транспонирования матрицы
"""

def transp_matrix(matrix: list[list]) -> list[list]:
    rows =  len(matrix[0])
    colums =  len(matrix)
    res_matrix = [[0] * colums for i in range(rows)]      
    for i in range(rows):
        for j in range(colums):
            res_matrix[i][j] = matrix[j][i]
    return res_matrix
 
            
def print_matrix(matrix: list[list]) -> list[list]:
    rows =  len(matrix[0])
    colums =  len(matrix)
    for i in range(colums):
        for j in range(rows):
            #print(matrix[i][j], end=' ')
            print(str(matrix[i][j]).rjust(4), end='')
        print()


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

    print_matrix(matrix)
    print()
    print_matrix(transp_matrix(matrix))
    