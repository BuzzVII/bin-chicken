import sympy
import math

# integratate the area bound by the intersection of a unit circle and
# verticle lines from the circumfrance at theta = pi/6 to 2*pi/6

theta_1 = math.pi/6
theta_2 = math.pi/3
x1 = math.cos(theta_1)
x2 = math.cos(theta_2)


# integrate in rectangle coordinates, take the upper quadrant of the
# circle and integrate form x2 to x1. y = sqrt(r**2 - x**2)

x = sympy.Symbol('x')
r = 6
int_x = (sympy.integrate(sympy.sqrt(r**2 - x**2), x))
# x*sqrt(1 - x**2)/2 + asin(x)/2
theta_1 = sympy.pi/6
theta_2 = sympy.pi/3
x1 = r*math.cos(theta_1)
x2 = r*math.cos(theta_2)
area = int_x.subs({"x":x1}) - int_x.subs({"x":x2})

print(area)

area = sympy.integrate(sympy.sqrt(r**2 - x**2), (x, x2, x1))
print(area)

print(3 * math.pi)


# Double integral in polar coordinates. Integrate from 0 to theta_1 and
# subtract 0 to theta_2 and the vertical line to r along the radius.
# The vertical line can be written as r = c/(sin(theta)) where c is the x
# value for the vertical line.
# since r bounds is a function of theta, it is preformed first:
# Int(Int(1)dr)dTheta

theta = sympy.Symbol('theta')
c = sympy.Symbol('c')

# Int(1)dr = r
int_r = 1 - c/(sympy.sin(theta))

# Int(int_r)dTheta
int_theta = sympy.integrate(int_r, theta)
# -c*(log(cos(theta) - 1)/2 - log(cos(theta) + 1)/2) + theta

