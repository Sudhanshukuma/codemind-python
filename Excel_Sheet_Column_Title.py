n=int(input())
t='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'
while(n):
    r=n%26
    if r==0:
        t+='Z'
    else:
        t+=chr(64+r)
    n/=26
    n=int(n)
print(t[::-1])