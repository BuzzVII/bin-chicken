import sympy
from sympy import solvers

# How high does a roller coaster cart need to be so that it cn do a
# loop or radius R?

R = sympy.Symbol('R')


# Assuming no friction we need to find the force requited to counter
# gravity when the cart is at the top of the loop, the minimum velocity
# to maintain this force and the heigh required for the kinetic energy
# of this velocity.

# Centripetal force is F = mv**2/R
# Gravitational force at the top of the loop: F = mg
# mg = mv**2/R, v = sqrt(Rg)

g = sympy.Symbol('g')
v = sympy.Symbol('v')
m = sympy.Symbol('m')
v_min = solvers.solve(m * g - m * v**2/R, v)

print(v_min)

# To maintain the speed at the top of the loop the cart needs enough
# energy for the minimum velocity, KE = 1/2 mv**2, plus the potential
# energy at the top of the loop H=2R, PE = 2Rmg. E_min = KE + PE.

E_min = m*g*2*R + 1/2 * m * v**2

# The height required for enough energy to complete the loop is when the
# potential energy is equal to this minimum energy
# PE = mgh = E_min.

h = sympy.Symbol('h')
h_min = solvers.solve(m*g*h - E_min, h)
print(h_min[0].subs({v:v_min[1]}))
