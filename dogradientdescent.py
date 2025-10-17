from sympy import symbols, diff, sympify
import math

def values_are_equal(xv, yv, xv_new, yv_new):
    if math.isclose(xv, xv_new, rel_tol=1e-4, abs_tol=1e-4) == False:
        return False
    if math.isclose(yv, yv_new, rel_tol=1e-4, abs_tol=1e-4) == False:
        return False
    return True

def sympy_function(myformula):
    x = symbols('x')
    y = symbols('y')
    expr = sympify(myformula)
    return expr

def sympy_gradient(myformula):
    x = symbols('x')
    y = symbols('y')
    expr = sympify(myformula)
    return (diff(expr, x), diff(expr, y))

def gradient_descent_step(xv, yv):
    x = symbols('x')
    y = symbols('y')
    f1 = sympy_function(myformula=myformula)
    (f2, f3) = sympy_gradient(myformula=myformula)
    a4 = f1.subs({x: xv, y: yv}).evalf()
    a5 = f2.subs({x: xv, y: yv}).evalf()
    a6 = f3.subs({x: xv, y: yv}).evalf()
    #print(f"{iterations}. x {xv} y {yv} f {a4} --> ({a5},{a6})")
    print(f"{iterations}. x {xv} y {yv} --> ({a5},{a6})")
    x_new = xv - a5 * myalpha
    y_new = yv - a6 * myalpha
    return x_new, y_new

myformula = '85 - (1 / 90) * x**2 * (x - 6) * y ** 2 * (y - 6)'
myalpha = 0.01
iterations = 0
xv = 3.2
yv = 3.2
xv_new, yv_new = gradient_descent_step(xv, yv)
while values_are_equal(xv, yv, xv_new, yv_new) == False:
    iterations += 1
    xv = xv_new
    yv = yv_new
    xv_new, yv_new = gradient_descent_step(xv, yv)
