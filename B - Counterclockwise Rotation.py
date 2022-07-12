from math import radians, e

a, b, d = map(int, input().split())
d = radians(d)

c = complex(a, b)
c_dash = c * e ** (1j * d)
print(c_dash.real, c_dash.imag)
