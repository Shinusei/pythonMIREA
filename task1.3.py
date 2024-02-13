def f(x):
    a=x
    x = x + x
    x = x + x
    x = x + x
    x = x -(a-x)
    return x

print(f(3))