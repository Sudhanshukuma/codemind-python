n=int(input())
if(n<=0):
    n=(-n)
    n=str(n)
    n=n[::-1]
    n=int(n)
    print(-n)
else:
    n=str(n)
    n=n[::-1]
    n=int(n)
    print(n)
    