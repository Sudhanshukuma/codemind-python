n=int(input())
d=0
p=1
while(n):
    i=n%10
    d+=i
    p*=i
    n=n//10
if(d==p):
    print("Spy Number")
else:
    print("Not Spy Number")