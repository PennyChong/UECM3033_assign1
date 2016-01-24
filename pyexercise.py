import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( (x**2 +7*x)/(1 +sy.sqrt(x))**4, (x,0, 1))
    return ans

def my_solution():
    A = np.array( [[2,6,20, 45, -5,-3,-8,-45,47,32], [8,23,-74,-32, 39,20,11,2, 9,58], [3,3,0,2,57,22,4,1,6,-4], [2,1,9,4,-3,5,-32,-30,-15,8], [7,3,8,21,9,4,2,-54,-8,10], [2,16,1,1,43,52,0,8,-4,2], [8,9,10,11,23,4,1,-4,-66,-3], [-6,3,-3,2,88,-64,-32,11,22,7], [-3,-5,3,6,4,9,66,23,83,-4], [12,-13,0,2,-2,8,-34,74,8,3]] )
    b = np.array([9,6,9,23,4,5,1,7,-23,-4])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1201782
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
