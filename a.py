a=int(input())
b=int(input())
def sum_int(a,b):
    sum1=0
    for i in range(a,b+1):
        sum1 += i
    return sum1
print(sum_int(a,b))