from display import *
from random import randint
from draw import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]


matrix = new_matrix()
print("initial empty matrix \n")
print_matrix(matrix)

print("Identity Matrix Test #1\n")
identMatrix = new_matrix()
ident(identMatrix)
print_matrix(identMatrix)


print("\nAdding points to a new matrix [1, 1, 0], [5, 5, 0]\n")
testMatrix = new_matrix(0,4)
add_point(testMatrix, 1, 1, 0)
add_point(testMatrix, 5, 5, 0)
print_matrix(testMatrix)

print("\nAdding edges to the new matrix [10, 10, 0], [20, 20, 0]\n")
add_edge(testMatrix, 10, 10, 0, 15, 15, 0)
print_matrix(testMatrix)


print("\nTesting scalar multiplication, multiplying by 3")
scalar_mult(testMatrix,3)
print_matrix(testMatrix)


print("\nTesting scalar_mult using the new matrix and [[1,2],[3,4],[5,6],[7,8]]")
print("\nCorrect output should be [513, 606], [513, 606],[0,0],[48,48]")
multMatrix = [[1,2],[3,4],[5,6],[7,8]]
matrix_mult(testMatrix,multMatrix)
print_matrix(multMatrix)


for i in range(1, 100,2):
    add_edge( matrix, int(i*math.cos(i*60)), int(i*math.sin(i*60)), 0, 500, int(250 + i*math.cos(i*60)), 0 )

        
draw_lines( matrix, screen, color )
display(screen)
