def countdown(x):
    if (x==0):
        return 1
    print(x)
    countdown(x-1)

def countup(x,y):
    if(x>y):
        return y
    print(x)
    countup(x+1,y)
def fib(a):
    if a == 1 or a == 2:
        return 1
    return fib(a - 2) + fib(a - 1)


def exp(x,y):
    if y==0:
        return 1
    return exp(x, y-1)*x

print(exp(5,2))