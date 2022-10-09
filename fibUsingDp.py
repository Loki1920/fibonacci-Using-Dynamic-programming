# fibonacci series


def fib(n):
    a = []
    for i in range(n):
        a.append(-1)

    a[0]=0
    a[1]=1
    for i in range(2,n):
        a[i] = a[i-1]+a[i-2]
        
    return a[n-1]

n = int(input("enter n:"))
print(fib(n))
