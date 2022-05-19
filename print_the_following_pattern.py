n=int(input())
for i in range(1,n+1):
    print(' '*(n-i),end='')
    print(10**(2*i-1)//9*i)