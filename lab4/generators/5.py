a = int(input())
def tozero(n):
    g = a
    for _ in range(n):
        while(g >= 0):
             yield g
             g = g - 1
        
print(list(tozero(a)))