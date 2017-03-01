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
    if(len(m1[0]) == len(m2)):
        m3 = new_matrix(len(m2[0]), len(m1))
        for col in range( len( m2[0] ) ):
            for row in range( len( m2 ) ):
                sum = 0;
                for index in range( len( m1[row] ) ):
                    sum += m1[row][index] * m2[index][col];
                m3[row][col] = sum

    del m2[:]
    for i in range(len(m3)):
        m2.append(m3[i])
        


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
