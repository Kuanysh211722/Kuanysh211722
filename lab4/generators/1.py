def gensquares(N):
    for i in range(N): 
        yield i**2
N=int(input())
for x in gensquares(N):
    print(x)