from sympy import symbols, diff, sympify
import math
import numpy as np

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

def sympy_2ndorderderivatives(myformula):
    x = symbols('x')
    y = symbols('y')
    a = sympy_gradient(myformula=myformula)
    h11 = diff(a[0], x)

    #h12 = diff(a[1], x)
    #h21 = diff(a[0], y)
    h12 = diff(a[0], y)
    h21 = diff(a[1], x)

    h22 = diff(a[1], y)
    return h11, h12, h21, h22

def newton_step(xv, yv):
    x = symbols('x')
    y = symbols('y')
    (g1, g2) = sympy_gradient(myformula=myformula)
    h11, h12, h21, h22 = sympy_2ndorderderivatives(myformula=myformula)
    g1_v = float(g1.subs({x: xv, y: yv}).evalf())
    g2_v = float(g2.subs({x: xv, y: yv}).evalf())
    h11_v = float(h11.subs({x: xv, y: yv}).evalf())
    h12_v = float(h12.subs({x: xv, y: yv}).evalf())
    h21_v = float(h21.subs({x: xv, y: yv}).evalf())
    h22_v = float(h22.subs({x: xv, y: yv}).evalf())

    # build numpy Hessian matrix (numeric floats)
    G = np.array([g1_v, g2_v], dtype=float)
    H = np.array([
        [h11_v, h12_v],
        [h21_v, h22_v]], dtype=float)

    try:
        step = np.linalg.solve(H, G)
    except np.linalg.LinAlgError:
        step = np.linalg.pinv(H).dot(G)

    x_new = xv - step[0]
    y_new = yv - step[1]

    print(f"({xv},{yv}) - ({step[0]},{step[1]}) = ({x_new},{y_new})")
    print("------------")

    return x_new, y_new


#myformula = '85 - (1 / 90) * x**2 * (x - 6) * y ** 2 * (y - 6)'
myformula = '(x - 3)**2 + (y - 4)**2'
iterations = 0
xv = 2
yv = 2
xv_new, yv_new = newton_step(xv, yv)
while math.isclose(xv, xv_new) == False or math.isclose(yv, yv_new) == False:
    iterations += 1
    xv = xv_new
    yv = yv_new
    xv_new, yv_new = newton_step(xv, yv)
