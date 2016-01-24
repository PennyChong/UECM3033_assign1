import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate((x**2 +7*x)/(1 +sy.sqrt(x))**4, (x,0, 1))
    return ans

def my_solution():
    A = np.array( [[2,6,20, 45, -5,-3,-8,-45,7,3], [8,23,-7,-32, 9,20,11,2, 9,8], [3,3,0,2,57,22,4,1,6,-4], [2,1,9,4,-3,5,-32,-3,-15,8], [7,3,8,21,9,4,2,-4,-8,10], [2,16,1,1,4,2,0,8,-4,2], [8,9,10,11,23,4,1,-4,-66,-3], [-6,3,-3,2,8,-6,-28,11,22,7], [-3,-5,3,6,4,9,6,23,3,-4], [12,-13,0,2,-2,8,-34,7,8,3]] )
    b = np.array([35,23,8,23,14,60,19,50,-23,30])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1201782
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
