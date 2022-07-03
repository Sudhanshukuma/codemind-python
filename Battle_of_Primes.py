def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
a=int(input())
b=int(input())
c=1
while(True):
    if prime(a+b+c):
        print(c)
        break
    c+=1