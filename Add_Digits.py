def add(a):
    return (a-1)%9 + 1 if a>0 else 0
a=int(input())
print(add(a))