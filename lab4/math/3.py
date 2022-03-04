from math import tan, pi
n = int(input())
a = int(input())
s = n * (a ** 2) / (4 * tan(pi / n))
print(s)