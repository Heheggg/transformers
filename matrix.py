import math


def print_matrix(matrix):
    output = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            output += (str)(matrix[i][j]) + "\t"
        output += "\n"
    print(output)


def ident(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0


def scalar_mult(matrix, s):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = matrix[i][j]*s


#m1 * m2 -> m2
def matrix_mult(m1, m2):
    if(len(m1) == len(m2[0])):
        m3 = new_matrix(len(m1), len(m2[0]))
        for row in range(len(m1)):
            for col in range(len(m2[0])):
                temp = 0
                for row2 in range(len(m2)):
                    temp += m1[row][row2] * m2[row2][col]
                m3[row][col] = temp

        for i in range(len(m2)):
            for j in range(len(m1[i])):
                m2[i][j] = m3[i][j]



def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
