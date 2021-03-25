# Python script to calculate determinant of matrix with numpy

from numpy import array, linalg, vdot
from numpy.linalg import solve, det, norm

firstArray = [ 1, 2, 3 ]
secondArray = [ 4, 5, 6 ]
coefficients = array ( [ [ - 9, 6, 0 ], [ 6, - 8, 0 ], [ 3, - 2 , - 1 ] ] )
constants = array ( [ - 50, 0, 0] )

solVector = solve ( coefficients, constants )
print ( "Solutions:  ", solVector )
#print ( "Determinant:", det ( coefficients ) )
#print ( "Dot product:", vdot ( firstArray, secondArray ) )
#print ( "Norm:", norm ( constants ) )
