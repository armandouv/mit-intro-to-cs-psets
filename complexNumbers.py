import math
import cmath

z1 = complex(3, -2)
z2 = complex(2*math.sqrt(3), 2)
z3 = complex(-2,0)
sqr = math.sqrt(3)

res = ((8*z1*z2)+(12*z2*z2)+(2*z3))/z1

print(res)
print(cmath.polar(res))

inv = (((res * z1) - (2 * z3))/(4*z2) - (3*z2))/2
print(inv)

a = complex(6+6*sqr,2)
b = complex(8*sqr, 8)
c = a*b
d = c-4
x = d/z1
print(cmath.polar(x))
tot = x**(2/3)
print(cmath.polar(tot))