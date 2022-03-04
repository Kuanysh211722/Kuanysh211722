import math
a = int(input())
b = int(input())
def gener(a, b):
    c = a
    for _ in range(a, b):
        c = c + 1
        g =int(math.pow(c, 2))
        yield g
for item in gener(a, b):
    print(item)